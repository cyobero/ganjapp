from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from users.models import Profile

def index(request):
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        return render(request, 'index.html')
    return redirect(reverse('login'))


def contact(request):
    return render(request, 'contact.html')
