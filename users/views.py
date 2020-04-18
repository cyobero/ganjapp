from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    return render(request, 'login.html')


def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
