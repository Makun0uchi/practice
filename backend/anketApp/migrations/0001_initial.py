# Generated by Django 5.0.6 on 2024-06-21 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hardskillApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('surname', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('patronymic', models.CharField(max_length=1024)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('soft_skills', models.TextField(blank=True)),
                ('other_info', models.TextField(blank=True)),
                ('job_position', models.CharField(max_length=1024)),
                ('hard_skills_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hardskillApp.hardskill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('surname', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('patronymic', models.CharField(max_length=1024)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('soft_skills', models.TextField(blank=True)),
                ('other_info', models.TextField(blank=True)),
                ('establishment', models.CharField(max_length=1024)),
                ('start_study_date', models.DateField()),
                ('end_study_date', models.DateField()),
                ('course', models.IntegerField()),
                ('hard_skills_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hardskillApp.hardskill')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
