from django.shortcuts import render, redirect
from home_view.forms import ContactForm
from django.contrib import messages
import threading
from django.core.mail import EmailMessage


# Create your views here.
class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def solution(request):
    return render(request, 'solution.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            form.save()
            messages.success(request, 'Thanks for contact us')
            from_email = 'koracodeafrica@gmail.com'
            message_client= f"hello I am {full_name} and my email {email} and my phone is {phone} my subject is {subject} \n  {message}"
            data = {'email_subject': subject, 'email_body': message_client, 'to_email': 'byiringoroscar@gmail.com'}
            msg = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
            EmailThread(msg).start()
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
