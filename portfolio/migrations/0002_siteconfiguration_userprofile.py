# Generated by Django 5.1.7 on 2025-04-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='My Portfolio', max_length=100)),
                ('contact_email', models.EmailField(default='your@email.com', max_length=254)),
                ('phone_number', models.CharField(default='+1234567890', max_length=20)),
                ('address', models.CharField(default='City, Country', max_length=200)),
                ('github_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('copyright_text', models.CharField(default='© {% now "Y" %} My Portfolio. All Rights Reserved.', max_length=200)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your Name', max_length=100)),
                ('job_title', models.CharField(default='Your Job Title', max_length=200)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile/')),
                ('about_text', models.TextField(blank=True)),
                ('resume_file', models.FileField(blank=True, upload_to='resumes/')),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]
