from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelmodule',
            name='must_contain',
            field=models.JSONField(blank=True, default=list, help_text='Words the code must contain to pass the practice check'),
        ),
        migrations.AddField(
            model_name='levelmodule',
            name='solution_code',
            field=models.TextField(blank=True, default='', help_text='Full solution shown when the student asks for it'),
        ),
        migrations.AddField(
            model_name='levelmodule',
            name='is_project',
            field=models.BooleanField(default=False, help_text='True for Mini Project / Capstone levels'),
        ),
        migrations.AlterField(
            model_name='course',
            name='badge_label',
            field=models.CharField(default='30 Levels Available', max_length=50),
        ),
    ]
