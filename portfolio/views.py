from django.shortcuts import render

# Create your views here.

from collections import defaultdict

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Education, Experience, Contact

def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})

def resume(request):
    education = Education.objects.all().order_by('-end_date')
    experience = Experience.objects.all().order_by('-end_date')
    projects = Project.objects.all().order_by('-date_created')
    
    # Organize skills by category
    skills = Skill.objects.all()
    skill_categories = defaultdict(list)
    for skill in skills:
        skill_categories[skill.get_category_display()].append(skill)
    
    return render(request, 'resume.html', {
        'education': education,
        'experience': experience,
        'skill_categories': dict(skill_categories),
        'projects': projects
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create a new Contact message
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html')