# Generated by Django 5.0.6 on 2024-06-27 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hard_skill_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorAnket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('patronymic', models.CharField(max_length=1024)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('soft_skills', models.TextField(blank=True)),
                ('other_info', models.TextField(blank=True)),
                ('profile_photo', models.ImageField(default='static/staticfiles/default_user.jpg', upload_to='static/staticfiles/%Y/%m/%d/')),
                ('job_position', models.CharField(max_length=1024)),
                ('hard_skills_id', models.ManyToManyField(related_name='mentor_anket_hard_skills_id', to='hard_skill_app.hardskill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAnket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('patronymic', models.CharField(max_length=1024)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('soft_skills', models.TextField(blank=True)),
                ('other_info', models.TextField(blank=True)),
                ('profile_photo', models.ImageField(default='static/staticfiles/default_user.jpg', upload_to='static/staticfiles/%Y/%m/%d/')),
                ('establishment', models.CharField(max_length=1024)),
                ('start_study_year', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)])),
                ('end_study_year', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)])),
                ('course', models.IntegerField()),
                ('hard_skills_id', models.ManyToManyField(related_name='student_anket_hard_skills_id', to='hard_skill_app.hardskill')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
