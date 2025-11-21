from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def blogs(request):
    return render(request, 'blogs.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        full_message = f"From: {name} <{email}>\n\n{message}"
        
        send_mail(
            subject=f"New Contact Message from {name}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL, 
            recipient_list=[settings.CONTACT_EMAIL], 
        )
        
        messages.success(request, "Thank you! Your message has been sent.")
        return redirect('index')  
    return render(request, 'index.html')

