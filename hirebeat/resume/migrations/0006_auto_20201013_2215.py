# Generated by Django 3.0.7 on 2020-10-14 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_merge_20201012_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='measureable_results_list_bool',
        ),
        migrations.AddField(
            model_name='resume',
            name='measureable_results_bool',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
