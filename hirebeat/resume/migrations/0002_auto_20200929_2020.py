# Generated by Django 3.0.7 on 2020-09-29 20:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='avoid_words_bool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='data_formating_bool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education_match_bool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='file_type_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='file_type_list_bool',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(default=False), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hard_skill_jd_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=0, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hard_skill_resume_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=0, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hard_skill_skills_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hard_skill_variations_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_level_text_bool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='measureable_results_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='measureable_results_list_bool',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(default=False), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='other_skill_jd_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=0, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='other_skill_resume_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=0, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='other_skill_skills_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='section_headings_bool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills_keywords_bool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='soft_skill_jd_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=0, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='soft_skill_resume_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=0, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='soft_skill_skills_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='soft_skill_variations_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='word_count_bool',
            field=models.BooleanField(default=False, null=True),
        ),
    ]