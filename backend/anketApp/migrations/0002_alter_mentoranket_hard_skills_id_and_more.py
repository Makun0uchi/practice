# Generated by Django 5.0.6 on 2024-06-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketApp', '0001_initial'),
        ('hardSkillApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentoranket',
            name='hard_skills_id',
            field=models.ManyToManyField(related_name='ma_hard_skills_id', to='hardSkillApp.hardskill'),
        ),
        migrations.AlterField(
            model_name='studentanket',
            name='hard_skills_id',
            field=models.ManyToManyField(related_name='sa_hard_skills_id', to='hardSkillApp.hardskill'),
        ),
    ]