from django.shortcuts import render, redirect
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
    return render(request, 'contact.html')
