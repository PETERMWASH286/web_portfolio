from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.http import FileResponse
import os
from django.http import FileResponse, HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'index.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            f'Message from {name} email {email}',
            message,
            email,
            ['petrasmwash1@gmail.com'],  # Replace with your company email
            fail_silently=False,
        )

        # Redirect to a thank you page or home page after sending the email
        messages.success(request, 'Your message has been sent successfully!')
        return HttpResponseRedirect('/')  # Replace '/thank-you/' with your thank you page URL

    return render(request, 'index.html')  # Replace 'contact.html' with your contact page template


def download_resume(request):
    resume_path = 'C:\\Users\\pincho\\Desktop\\desktop projects\\python projects\\Django projects\\projects\\working projects\\Portfolio websites\\web_portfolio\\portfolio\\media\\resume.pdf'
    if os.path.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type='application/pdf')
            return response
    else:
        # Handle case where resume file does not exist
        return HttpResponse("Resume not found", status=404)
