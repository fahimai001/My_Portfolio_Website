# Generated by Django 5.1.7 on 2025-04-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_siteconfiguration_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.CharField(choices=[('AI/ML', 'AI & Machine Learning'), ('NLP', 'NLP & Generative AI'), ('MLOps', 'MLOps & Cloud'), ('Algorithms', 'Learning Algorithms')], default='AI/ML', max_length=50),
        ),
    ]
