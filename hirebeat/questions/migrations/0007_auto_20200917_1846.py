# Generated by Django 3.0.7 on 2020-09-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20200917_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Positive Attitude', 'Positive Attitude'), ('Work Commitment', 'Work Commitment'), ('Teamwork Skill', 'Teamwork Skill'), ('Leadership', 'Leadership'), ('Pressure Handling', 'Pressure Handling'), ('Proactive Skill', 'Proactive Skill'), ('Work Ethic', 'Work Ethic'), ('Creativity', 'Creativity'), ('Dependable & Reliable', 'Dependable & Reliable'), ('Reliability', 'Reliability'), ('Communication', 'Communication'), ('Problem Solving', 'Problem Solving')], default='Positive Attitude', max_length=50),
        ),
    ]
