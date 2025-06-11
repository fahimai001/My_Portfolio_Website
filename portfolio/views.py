from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.

from collections import defaultdict

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Education, Experience, Contact

def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})

def resume(request):
    current_experience = Experience.objects.filter(current=True).order_by('-start_date')
    previous_experience = Experience.objects.filter(current=False).order_by('-end_date')
    experience = list(current_experience) + list(previous_experience)
    
    education = Education.objects.all().order_by('-end_date')
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
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Format the email message
        email_message = f"""
You have received a new contact message from your portfolio website:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
        
        # Send the email
        try:
            # Create email message
            email_obj = EmailMessage(
                f'Portfolio Contact: {subject}',  # Subject
                email_message,  # Body
                'fahim.sabir011@gmail.com',  # From email
                ['fahim.sabir011@gmail.com'],  # To email 
                headers={'Reply-To': email}  # Set reply-to as the sender's email
            )
            
            # Send the email
            email_obj.send(fail_silently=False)
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
            print(f"Email error: {e}")  # For debugging
            
        return redirect('contact')
    
    return render(request, 'contact.html')