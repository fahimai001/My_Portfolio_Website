from django.db import models

# Create your models here.

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default='My Portfolio')
    contact_email = models.EmailField(default='your@email.com')
    phone_number = models.CharField(max_length=20, default='+1234567890')
    address = models.CharField(max_length=200, default='City, Country')
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

class UserProfile(models.Model):
    name = models.CharField(max_length=100, default='Your Name')
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    about_text = models.TextField(blank=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User Profile"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    date_created = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('AI/ML', 'Machine Learning & Data Analysis'),
        ('NLP', 'NLP & Generative AI'),
        ('MLOps', 'Data Engineering & Cloud Computing'),
        ("Backend Technologies", "Backend Frameworks")
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='AI/ML')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

    class Meta:
        ordering = ['-end_date', '-start_date']

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-end_date', '-start_date']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-date_sent']
