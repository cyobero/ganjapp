from django.shortcuts import render, redirect, reverse
from users.models import Profile
from django.contrib.auth.decorators import login_required

def index(request):
    # redirect to login page if user is not
    # logged in.
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
