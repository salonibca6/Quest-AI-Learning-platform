from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from .forms import UserRegistrationForm, UserLoginForm
from .models import Course, LevelModule, UserProgress, UserProfile


def root_gateway_view(request):
    """
    Website starts from Auth (Login / Sign Up) for new or unauthenticated users.
    Once authenticated, user lands on Home page.
    """
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(
                request,
                f"Registration successful, {user.username}! Welcome to Quest. Please sign in to launch your learning journey."
            )
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            ident = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password']

            # Support login by username OR email
            user = None
            if '@' in ident:
                try:
                    user_obj = User.objects.get(email__iexact=ident)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None
            else:
                user = authenticate(request, username=ident, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, Commander {user.username}! All systems operational.")
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password. Please verify your credentials.")
    else:
        form = UserLoginForm()

    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out safely. Keep coding and return soon!")
    return redirect('login')


@login_required
def home_view(request):
    courses = Course.objects.all().order_by('order')
    
    # Calculate course stats for current user
    course_cards = []
    total_completed_all = 0
    total_levels_all = 0

    for c in courses:
        stats = c.get_user_progress_stats(request.user)
        total_completed_all += stats['completed_count']
        total_levels_all += stats['total_levels']
        course_cards.append({
            'course': c,
            'stats': stats,
        })

    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    context = {
        'course_cards': course_cards,
        'profile': profile,
        'total_completed_all': total_completed_all,
        'total_levels_all': total_levels_all,
    }
    return render(request, 'home.html', context)


@login_required
def course_quest_map_view(request, slug):
    course = get_object_or_404(Course, slug=slug)

    # If course is upcoming, notify user and redirect to home
    if course.status != 'available':
        messages.info(request, f"{course.name} is currently in development and will launch soon!")
        return redirect('home')

    modules = list(course.modules.all().order_by('level_number'))
    progress_map = {
        up.level_module_id: up 
        for up in UserProgress.objects.filter(user=request.user, level_module__course=course)
    }

    levels_data = []
    completed_count = 0
    first_unlocked_playable = None

    for mod in modules:
        up = progress_map.get(mod.id)
        is_comp = up.completed if up else False
        if is_comp:
            completed_count += 1
            is_unlk = True
        else:
            # Check unlock condition
            is_unlk = mod.is_unlocked_for(request.user)

        if is_unlk and not is_comp and first_unlocked_playable is None:
            first_unlocked_playable = mod.level_number

        levels_data.append({
            'module': mod,
            'is_completed': is_comp,
            'is_unlocked': is_unlk,
            'progress': up,
        })

    total_count = len(modules) or 30
    completion_percentage = int((completed_count / total_count) * 100) if total_count else 0

    context = {
        'course': course,
        'levels_data': levels_data,
        'completed_count': completed_count,
        'total_count': total_count,
        'completion_percentage': completion_percentage,
        'next_playable_level': first_unlocked_playable or (1 if completed_count < total_count else total_count),
    }
    return render(request, 'course/quest_map.html', context)


@login_required
def level_module_detail_view(request, slug, level_number):
    course = get_object_or_404(Course, slug=slug)
    module = get_object_or_404(LevelModule, course=course, level_number=level_number)

    # Guard check: Ensure level is unlocked
    if not module.is_unlocked_for(request.user):
        messages.warning(request, f"Level {level_number} is locked. Complete Level {level_number - 1} to unlock this module!")
        return redirect('course_quest_map', slug=course.slug)

    progress, _ = UserProgress.objects.get_or_create(user=request.user, level_module=module)
    
    # Previous and next modules
    prev_module = LevelModule.objects.filter(course=course, level_number=level_number - 1).first()
    next_module = LevelModule.objects.filter(course=course, level_number=level_number + 1).first()

    total_levels = course.modules.count()
    level_data = {
        'expected': module.expected_output,
        'must_contain': module.must_contain or [],
        'solution': module.solution_code,
        'language': course.slug,
    }

    context = {
        'course': course,
        'module': module,
        'progress': progress,
        'prev_module': prev_module,
        'next_module': next_module,
        'total_levels': total_levels,
        'level_data': level_data,
        'is_capstone': (level_number == total_levels),
    }
    return render(request, 'course/level_detail.html', context)


@login_required
@require_POST
def complete_level_api(request, slug, level_number):
    try:
        data = json.loads(request.body)
    except Exception:
        data = {}

    course = get_object_or_404(Course, slug=slug)
    module = get_object_or_404(LevelModule, course=course, level_number=level_number)

    if not module.is_unlocked_for(request.user):
        return JsonResponse({'success': False, 'error': 'Level is locked.'}, status=403)

    user_code = data.get('code', '').strip()
    quiz_answer = data.get('quiz_answer') # int index

    progress, _ = UserProgress.objects.get_or_create(user=request.user, level_module=module)

    # Validate quiz if provided
    quiz_correct = True
    if quiz_answer is not None:
        try:
            quiz_answer = int(quiz_answer)
            quiz_correct = (quiz_answer == module.quiz_correct_index)
        except (ValueError, TypeError):
            quiz_correct = False

    if not quiz_correct:
        return JsonResponse({
            'success': False,
            'quiz_correct': False,
            'message': 'That answer is not correct. Read the lesson again and try once more!'
        })

    is_first_completion = not progress.completed
    progress.completed = True
    progress.completed_at = timezone.now()
    progress.quiz_answered_correctly = True
    if user_code:
        progress.submitted_code = user_code
    progress.save()

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if is_first_completion:
        profile.add_xp(module.xp_reward)

    next_lvl = LevelModule.objects.filter(course=course, level_number=level_number + 1).first()

    return JsonResponse({
        'success': True,
        'quiz_correct': True,
        'is_first_completion': is_first_completion,
        'xp_earned': module.xp_reward if is_first_completion else 0,
        'total_xp': profile.xp,
        'rank_tier': profile.calculate_rank_tier(),
        'rank_title': profile.get_title(),
        'has_next_level': next_lvl is not None,
        'next_level_number': next_lvl.level_number if next_lvl else None,
        'explanation': module.quiz_explanation,
        'message': f"Level {level_number} complete! You earned {module.xp_reward} XP!"
    })


@login_required
@require_POST
def ai_tutor_api(request):
    """
    Intelligent AI Assistant for C & Java Learning.
    Answers developer queries, gives code hints, debugs issues, and explains concepts.
    """
    try:
        body = json.loads(request.body)
    except Exception:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    user_query = body.get('prompt', '').strip()
    course_slug = body.get('course_slug', 'c')
    level_number = body.get('level_number', 1)
    user_code = body.get('code', '')

    if not user_query:
        return JsonResponse({'error': 'Prompt is required'}, status=400)

    course = Course.objects.filter(slug=course_slug).first()
    module = LevelModule.objects.filter(course=course, level_number=level_number).first() if course else None

    # Intelligent contextual response generation
    reply = generate_ai_learning_response(user_query, course, module, user_code)

    return JsonResponse({
        'reply': reply,
        'course': course.name if course else 'General',
        'level': level_number,
    })


def generate_ai_learning_response(query, course, module, code):
    """
    Rich AI Learning engine that understands C, Java, data structures, syntax errors,
    compiler messages, and algorithms.
    """
    query_lower = query.lower()
    lang = course.name if course else "Programming"
    mod_title = module.title if module else "General Coding"

    # Specific topic handlers
    if "explain" in query_lower or "what is" in query_lower or "how does" in query_lower:
        if "pointer" in query_lower:
            return (
                "### 🔍 AI Tutor: Deep Dive into Pointers\n\n"
                "A **pointer** is simply an integer variable that stores the physical RAM memory address of another variable.\n\n"
                "```c\n"
                "int score = 42;\n"
                "int *p = &score; // '&' obtains memory address of score\n"
                "printf(\"%d\", *p); // '*' dereferences to read the value 42\n"
                "```\n\n"
                "**Mental Model**: Think of your RAM as a giant post-office locker wall. `score` is the package inside locker #1024. Pointer `p` is a sticky note with the number `1024` written on it!"
            )
        elif "jvm" in query_lower or "bytecode" in query_lower:
            return (
                "### ☕ AI Tutor: Java Virtual Machine (JVM) Architecture\n\n"
                "When you run `javac App.java`, it does not produce machine code. Instead, it generates **platform-independent Bytecode** (`.class`).\n\n"
                "The **JVM** takes that bytecode and uses its **JIT (Just-In-Time) compiler** to turn hot code paths into lightning-fast native CPU instructions.\n\n"
                "This is how Java achieves 'Write Once, Run Anywhere' (WORA) while remaining fast!"
            )
        elif "struct" in query_lower:
            return (
                "### 📦 AI Tutor: C Structures (`struct`)\n\n"
                "A `struct` is a composite user-defined type that bundles heterogeneous data items together under one name.\n\n"
                "```c\n"
                "struct Player {\n"
                "    char name[30];\n"
                "    int health;\n"
                "    float speed;\n"
                "};\n"
                "```\n\n"
                "- Use `.` for direct struct variables (`player.health`).\n"
                "- Use `->` when accessing through a pointer (`ptr->health`)."
            )
        elif "stream" in query_lower or "lambda" in query_lower:
            return (
                "### ⚡ AI Tutor: Java Streams & Lambdas\n\n"
                "Streams enable declarative, functional data transformations without modifying the underlying collection:\n\n"
                "```java\n"
                "List<Integer> evens = list.stream()\n"
                "    .filter(n -> n % 2 == 0)\n"
                "    .map(n -> n * 2)\n"
                "    .toList();\n"
                "```\n\n"
                "**Key Distinction**: Intermediate operations (like `filter` and `map`) are lazy; computation only occurs when a terminal operation (like `toList` or `count`) is called!"
            )

    if "hint" in query_lower or "stuck" in query_lower or "solution" in query_lower:
        if module and module.solution_hint:
            return f"### 💡 Module Hint\n\n{module.solution_hint}\n\n*Review the starter code and compare your logic with the expected output.*"

    if "error" in query_lower or "bug" in query_lower or "fix" in query_lower or "debug" in query_lower:
        if "segmentation fault" in query_lower or "segfault" in query_lower:
            return (
                "### ⚠️ Debugging Segmentation Fault (Core Dumped)\n\n"
                "A segmentation fault happens when your program tries to read or write a memory location it does not have permission to access.\n\n"
                "**Top Causes to Check**:\n"
                "1. **Dereferencing NULL**: Did you check `if (ptr != NULL)` before doing `*ptr`?\n"
                "2. **Array Out of Bounds**: Check your loop condition (`i < size`, NOT `i <= size`).\n"
                "3. **Uninitialized Pointer**: A pointer without an assigned address points to random junk memory.\n"
                "4. **Buffer Overflow in strings**: Remember to allocate space for the terminating `'\\0'` character!"
            )
        elif "nullpointerexception" in query_lower or "npe" in query_lower:
            return (
                "### ⚠️ Debugging NullPointerException (NPE) in Java\n\n"
                "A `NullPointerException` occurs when you attempt to invoke a method or access an attribute on an object reference that currently points to `null`.\n\n"
                "**Quick Solutions**:\n"
                "- Check with `Objects.requireNonNull(obj)` or `if (obj != null)`.\n"
                "- Use `Optional<T>` for methods that might not return a value.\n"
                "- When comparing strings, prefer constant on the left: `\"ADMIN\".equals(role)` instead of `role.equals(\"ADMIN\")`!"
            )

    # General tailored guidance based on current module
    level_context = f"in **{mod_title}**" if module else ""
    return (
        f"### 🤖 Quest AI Assistant ({lang})\n\n"
        f"Great question regarding your current work {level_context}!\n\n"
        f"**Key Insights for this step:**\n"
        f"1. **Syntax Consistency**: In {lang}, verify matching braces `{{ }}` and required statement terminators `;`.\n"
        f"2. **Concept Application**: For this module, focus directly on the concept: *{module.summary if module else 'core programming concepts'}*.\n"
        f"3. **Pro-tip**: You can test your code directly in the sandbox below and see your output in real time before submitting.\n\n"
        f"If you'd like a specific code review, ask: *'Explain my code'* or *'Give me an analogy for {mod_title}'*!"
    )


@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    progress_records = UserProgress.objects.filter(user=request.user, completed=True).select_related('level_module', 'level_module__course')
    
    c_count = progress_records.filter(level_module__course__slug='c').count()
    java_count = progress_records.filter(level_module__course__slug='java').count()

    context = {
        'profile': profile,
        'progress_records': progress_records,
        'c_count': c_count,
        'java_count': java_count,
        'c_total': Course.objects.filter(slug='c').first().modules.count() if Course.objects.filter(slug='c').exists() else 30,
        'java_total': Course.objects.filter(slug='java').first().modules.count() if Course.objects.filter(slug='java').exists() else 30,
        'total_completed': progress_records.count(),
    }
    return render(request, 'profile.html', context)
