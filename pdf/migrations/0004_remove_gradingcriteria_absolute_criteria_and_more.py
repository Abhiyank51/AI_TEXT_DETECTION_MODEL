# Generated by Django 5.0.2 on 2024-05-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_gradingcriteria_absolute_criteria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradingcriteria',
            name='absolute_criteria',
        ),
        migrations.RemoveField(
            model_name='gradingcriteria',
            name='relative_criteria',
        ),
        migrations.RemoveField(
            model_name='gradingcriteria',
            name='word_range',
        ),
        migrations.AddField(
            model_name='gradingcriteria',
            name='max_words',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradingcriteria',
            name='min_words',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gradingcriteria',
            name='grading_type',
            field=models.CharField(choices=[('relative', 'Relative'), ('absolute', 'Absolute'), ('manual', 'Manual')], default='manual', max_length=10),
        ),
        migrations.AlterField(
            model_name='gradingcriteria',
            name='manual_criteria',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
