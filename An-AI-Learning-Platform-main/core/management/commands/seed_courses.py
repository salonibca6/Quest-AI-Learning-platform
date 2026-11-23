from django.core.management.base import BaseCommand
from core.models import Course, LevelModule, UserProgress
from core.curriculum import get_levels


class Command(BaseCommand):
    help = "Loads the C and Java courses with 30 beginner-friendly levels each (7 are mini projects)."

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset-progress', action='store_true',
            help='Also delete all students\' saved progress (use this once after switching from the old 20 levels).',
        )

    def handle(self, *args, **options):
        self.stdout.write("Starting course seeding...")

        if options['reset_progress']:
            deleted, _ = UserProgress.objects.all().delete()
            self.stdout.write(f"Cleared {deleted} old progress records.")

        courses = {
            'c': dict(
                name='C Programming',
                tagline='Learn the language behind phones, games and operating systems, step by step.',
                description='C is the grandfather of many languages. In 30 small levels you will go from printing "Hello" to building a calculator, a report card, an ATM and a to-do list. Every idea is explained in simple words with examples.',
                icon_type='c', color_accent='#00f2fe', order=1),
            'java': dict(
                name='Java Programming',
                tagline='Learn the language of Android apps, games and big companies, step by step.',
                description='Java is used to build Android apps, Minecraft and banking systems. In 30 small levels you will learn variables, loops, classes and objects, and build real mini projects like a calculator, a bank account and a to-do list manager.',
                icon_type='java', color_accent='#f59e0b', order=2),
        }

        for slug, info in courses.items():
            course, _ = Course.objects.update_or_create(
                slug=slug,
                defaults=dict(info, badge_label='30 Levels Available', status='available'),
            )
            levels = get_levels(slug)
            for data in levels:
                LevelModule.objects.update_or_create(
                    course=course,
                    level_number=data['level_number'],
                    defaults={k: v for k, v in data.items() if k != 'level_number'},
                )
            # remove any leftover levels beyond the new list
            LevelModule.objects.filter(course=course, level_number__gt=len(levels)).delete()
            projects = sum(1 for d in levels if d['is_project'])
            self.stdout.write(f"  {course.name}: {len(levels)} levels ({projects} mini projects)")

        Course.objects.update_or_create(
            slug='python',
            defaults=dict(
                name='Python Programming',
                tagline='The language of AI, data and automation.',
                description='Python is coming soon! It is friendly, powerful and perfect for AI and data projects.',
                badge_label='Upcoming Track', status='upcoming',
                icon_type='python', color_accent='#10b981', order=3),
        )

        self.stdout.write(self.style.SUCCESS(
            f"Done! {Course.objects.count()} courses and {LevelModule.objects.count()} levels in the database."))
