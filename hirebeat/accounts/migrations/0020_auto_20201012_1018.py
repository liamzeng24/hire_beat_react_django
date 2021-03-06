# Generated by Django 3.0.7 on 2020-10-12 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200810_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='save_resume_limit',
            field=models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='saved_resume_count',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
