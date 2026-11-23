from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    xp = models.PositiveIntegerField(default=0)
    streak = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=100, default='Code Novice')
    avatar_color = models.CharField(max_length=30, default='#00f2fe')

    def __str__(self):
        return f"{self.user.username} (Level {self.calculate_rank_tier()} - {self.xp} XP)"

    def calculate_rank_tier(self):
        # 1 rank per 200 XP
        return max(1, 1 + (self.xp // 200))

    def get_title(self):
        tier = self.calculate_rank_tier()
        if tier < 3:
            return "Byte Novice"
        elif tier < 6:
            return "Syntax Scout"
        elif tier < 10:
            return "Logic Warrior"
        elif tier < 15:
            return "Algorithm Sorcerer"
        else:
            return "Grandmaster Architect"

    def add_xp(self, points):
        self.xp += points
        self.title = self.get_title()
        self.save()


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()


class Course(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('upcoming', 'Upcoming'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    badge_label = models.CharField(max_length=50, default='30 Levels Available')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    icon_type = models.CharField(max_length=50, default='code') # c, java, python
    color_accent = models.CharField(max_length=30, default='#38bdf8')
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def is_available(self):
        return self.status == 'available'

    def get_user_progress_stats(self, user):
        if not user.is_authenticated:
            return {'completed_count': 0, 'percentage': 0, 'current_unlocked_level': 1}
        
        total_levels = self.modules.count() or 30
        completed_count = UserProgress.objects.filter(
            user=user,
            level_module__course=self,
            completed=True
        ).count()

        percentage = int((completed_count / total_levels) * 100) if total_levels else 0
        current_unlocked = min(total_levels, completed_count + 1)

        return {
            'completed_count': completed_count,
            'total_levels': total_levels,
            'percentage': percentage,
            'current_unlocked_level': current_unlocked,
        }


class LevelModule(models.Model):
    DIFFICULTY_CHOICES = (
        ('Novice', 'Novice'),
        ('Apprentice', 'Apprentice'),
        ('Adept', 'Adept'),
        ('Master', 'Master'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    level_number = models.PositiveIntegerField() # 1 to 30
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="Brief summary of what this module covers")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Novice')
    xp_reward = models.PositiveIntegerField(default=100)
    
    # Educational content
    concept_content = models.TextField(help_text="Detailed explanation of the topic")
    code_example = models.TextField(help_text="Demonstration code example")
    
    # Practical challenge / playground
    challenge_title = models.CharField(max_length=200, default="Module Code Quest")
    challenge_description = models.TextField(help_text="Task for the student")
    starter_code = models.TextField(blank=True, default="")
    expected_output = models.TextField(blank=True, default="")
    must_contain = models.JSONField(default=list, blank=True, help_text="Words the code must contain to pass the practice check")
    solution_code = models.TextField(blank=True, default="", help_text="Full solution shown when the student asks for it")
    is_project = models.BooleanField(default=False, help_text="True for Mini Project / Capstone levels")
    solution_hint = models.TextField(blank=True, default="")
    
    # Interactive knowledge check quiz
    quiz_question = models.TextField()
    quiz_options = models.JSONField(help_text="JSON list of 4 multiple-choice options")
    quiz_correct_index = models.PositiveIntegerField(help_text="0-indexed correct option")
    quiz_explanation = models.TextField(help_text="Why this option is correct")

    class Meta:
        ordering = ['course', 'level_number']
        unique_together = ('course', 'level_number')

    def __str__(self):
        return f"{self.course.name} - Level {self.level_number}: {self.title}"

    def is_unlocked_for(self, user):
        if not user.is_authenticated:
            return self.level_number == 1
        if self.level_number == 1:
            return True
        
        # Check if previous level is completed
        prev_level = LevelModule.objects.filter(
            course=self.course,
            level_number=self.level_number - 1
        ).first()
        if not prev_level:
            return False
            
        return UserProgress.objects.filter(
            user=user,
            level_module=prev_level,
            completed=True
        ).exists()

    def is_completed_for(self, user):
        if not user.is_authenticated:
            return False
        return UserProgress.objects.filter(
            user=user,
            level_module=self,
            completed=True
        ).exists()


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_records')
    level_module = models.ForeignKey(LevelModule, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.PositiveIntegerField(default=0)
    submitted_code = models.TextField(blank=True, default="")
    quiz_answered_correctly = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'level_module')

    def __str__(self):
        status = "Completed" if self.completed else "In Progress"
        return f"{self.user.username} -> {self.level_module.course.slug.upper()} Lvl {self.level_module.level_number} ({status})"
