from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import Course, LevelModule, UserProgress, UserProfile
import json


class QuestPlatformTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Seed test courses
        self.c_course = Course.objects.create(
            slug='c',
            name='C Programming',
            tagline='Master low-level systems',
            description='C description',
            status='available',
            order=1
        )
        self.java_course = Course.objects.create(
            slug='java',
            name='Java Programming',
            tagline='Enterprise standard',
            description='Java description',
            status='available',
            order=2
        )
        self.python_course = Course.objects.create(
            slug='python',
            name='Python Programming',
            tagline='AI & Data',
            description='Python description',
            status='upcoming',
            order=3
        )

        # Create 30 levels for C
        for i in range(1, 31):
            LevelModule.objects.create(
                course=self.c_course,
                level_number=i,
                title=f"C Module {i}",
                summary=f"Summary for C module {i}",
                difficulty="Novice" if i <= 5 else "Apprentice",
                xp_reward=100,
                concept_content=f"Detailed concepts for level {i}",
                code_example=f"// Example {i}",
                challenge_title=f"Challenge {i}",
                challenge_description=f"Task {i}",
                starter_code=f"// Starter {i}",
                expected_output="Success",
                solution_hint="Hint",
                quiz_question="What is C?",
                quiz_options=["A compiled language", "A script", "A database", "An OS"],
                quiz_correct_index=0,
                quiz_explanation="C is a compiled procedural language."
            )

        # Create 30 levels for Java
        for i in range(1, 31):
            LevelModule.objects.create(
                course=self.java_course,
                level_number=i,
                title=f"Java Module {i}",
                summary=f"Summary for Java module {i}",
                difficulty="Novice" if i <= 5 else "Apprentice",
                xp_reward=100,
                concept_content=f"Detailed concepts for level {i}",
                code_example=f"// Java Example {i}",
                challenge_title=f"Challenge {i}",
                challenge_description=f"Task {i}",
                starter_code=f"// Starter {i}",
                expected_output="Success",
                solution_hint="Hint",
                quiz_question="What is the JVM?",
                quiz_options=["Java Virtual Machine", "JavaScript Virtual Module", "Joint Vector Matrix", "None"],
                quiz_correct_index=0,
                quiz_explanation="JVM runs Java bytecode."
            )

    def test_unauthenticated_redirects_to_login(self):
        """Unauthenticated visitor hitting / should be redirected to /login/"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_user_registration_and_login_flow(self):
        """User registers, then logs in, then arrives at home page"""
        reg_response = self.client.post('/register/', {
            'username': 'neo_coder',
            'email': 'neo@quest.dev',
            'password': 'QuestSecretPassword123!',
            'confirm_password': 'QuestSecretPassword123!'
        })
        self.assertEqual(reg_response.status_code, 302)
        self.assertIn('/login/', reg_response.url)

        # Verify user exists
        user = User.objects.get(username='neo_coder')
        self.assertEqual(user.email, 'neo@quest.dev')
        self.assertTrue(hasattr(user, 'profile'))

        # Log in
        login_response = self.client.post('/login/', {
            'username': 'neo_coder',
            'password': 'QuestSecretPassword123!'
        })
        self.assertEqual(login_response.status_code, 302)
        self.assertIn('/home/', login_response.url)

    def test_home_page_elements(self):
        """Verify home page has Quest logo, About, Courses, C, Java, Python (upcoming), Let's start buttons"""
        user = User.objects.create_user(username='alice', password='password123')
        self.client.login(username='alice', password='password123')

        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')

        # Quest Logo and branding
        self.assertIn('Quest', content)
        self.assertIn('AI Learning Matrix', content)

        # About & Courses navigation
        self.assertIn('About', content)
        self.assertIn('Courses', content)

        # Courses sections
        self.assertIn('C Programming', content)
        self.assertIn('Java Programming', content)
        self.assertIn('Python Programming', content)
        self.assertIn('Upcoming', content)

        # "Let's start" button
        self.assertIn("Let's start", content)

        # Footer professional reason
        self.assertIn("Why Choose Quest to Learn Programming Languages?", content)

        # Animated developer canvas
        self.assertIn('developer-canvas', content)

    def test_gamification_30_levels_and_unlock_progression(self):
        """Verify 30 levels appear, level 1 is unlocked, level 2 is locked until level 1 is cleared"""
        user = User.objects.create_user(username='bob', password='password123')
        self.client.login(username='bob', password='password123')

        # Quest map view
        map_response = self.client.get('/course/c/')
        self.assertEqual(map_response.status_code, 200)
        self.assertEqual(len(map_response.context['levels_data']), 30)

        # Initially, Level 1 is unlocked, Level 2 is locked
        level_1 = map_response.context['levels_data'][0]
        level_2 = map_response.context['levels_data'][1]
        self.assertTrue(level_1['is_unlocked'])
        self.assertFalse(level_1['is_completed'])
        self.assertFalse(level_2['is_unlocked'])

        # Level 2 detail should be locked if directly accessed
        l2_response = self.client.get('/course/c/level/2/')
        self.assertEqual(l2_response.status_code, 302) # Redirects back with warning

        # Level 1 detail can be accessed
        l1_response = self.client.get('/course/c/level/1/')
        self.assertEqual(l1_response.status_code, 200)

        # Complete Level 1 via API
        complete_response = self.client.post(
            '/api/complete-level/c/1/',
            data=json.dumps({'quiz_answer': 0, 'code': 'printf("Quest C Activated\\n");'}),
            content_type='application/json'
        )
        self.assertEqual(complete_response.status_code, 200)
        data = complete_response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['xp_earned'], 100)

        # Now Level 2 must be unlocked!
        map_response_after = self.client.get('/course/c/')
        level_1_after = map_response_after.context['levels_data'][0]
        level_2_after = map_response_after.context['levels_data'][1]
        self.assertTrue(level_1_after['is_completed'])
        self.assertTrue(level_2_after['is_unlocked'])

        # User can now access Level 2 directly
        l2_after = self.client.get('/course/c/level/2/')
        self.assertEqual(l2_after.status_code, 200)

    def test_ai_tutor_api(self):
        """Test AI assistant endpoint"""
        user = User.objects.create_user(username='charlie', password='password123')
        self.client.login(username='charlie', password='password123')

        response = self.client.post(
            '/api/ai-tutor/',
            data=json.dumps({
                'prompt': 'Can you explain what is a pointer in C?',
                'course_slug': 'c',
                'level_number': 10
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('reply', data)
        self.assertIn('pointer', data['reply'].lower())


class CurriculumAndVoiceTests(TestCase):
    """Tests for the 30-level curriculum, mini projects, voice panel and lesson text."""

    def test_curriculum_has_30_levels_and_7_projects_per_course(self):
        from core.curriculum import get_levels
        for slug in ('c', 'java'):
            levels = get_levels(slug)
            self.assertEqual(len(levels), 30)
            self.assertEqual([l['level_number'] for l in levels], list(range(1, 31)))
            self.assertEqual(sum(1 for l in levels if l['is_project']), 7)
            for l in levels:
                self.assertEqual(len(l['quiz_options']), 4)
                self.assertTrue(0 <= l['quiz_correct_index'] < 4)
                self.assertTrue(l['solution_code'])
                self.assertTrue(l['must_contain'])

    def test_seed_command_loads_30_levels(self):
        from django.core.management import call_command
        call_command('seed_courses', verbosity=0)
        self.assertEqual(Course.objects.get(slug='c').modules.count(), 30)
        self.assertEqual(Course.objects.get(slug='java').modules.count(), 30)
        self.assertTrue(LevelModule.objects.get(course__slug='c', level_number=6).is_project)

    def test_level_page_has_voice_switch_and_project_badge(self):
        from django.core.management import call_command
        call_command('seed_courses', verbosity=0)
        User.objects.create_user(username='dana', password='password123')
        self.client.login(username='dana', password='password123')
        html = self.client.get('/course/c/level/1/').content.decode('utf-8')
        self.assertIn('id="voiceToggle"', html)
        self.assertIn('voice.js', html)
        self.assertIn('id="levelData"', html)
        # headings from the lesson are rendered as HTML, not raw ### marks
        self.assertNotIn('### ', html)

    def test_simple_md_filter_escapes_html_and_formats(self):
        from core.templatetags.quest_extras import simple_md
        out = simple_md('### Title\nSome **bold** and `code` <script>x</script>\n- a\n- b')
        self.assertIn('<h4', out)
        self.assertIn('<strong>bold</strong>', out)
        self.assertIn('<li>a</li>', out)
        self.assertNotIn('<script>', out)

    def test_complete_level_returns_explanation(self):
        from django.core.management import call_command
        call_command('seed_courses', verbosity=0)
        User.objects.create_user(username='eli', password='password123')
        self.client.login(username='eli', password='password123')
        mod = LevelModule.objects.get(course__slug='c', level_number=1)
        resp = self.client.post(
            '/api/complete-level/c/1/',
            data=json.dumps({'quiz_answer': mod.quiz_correct_index, 'code': 'x'}),
            content_type='application/json')
        self.assertTrue(resp.json()['success'])
        self.assertEqual(resp.json()['explanation'], mod.quiz_explanation)
