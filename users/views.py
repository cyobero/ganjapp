from django.shortcuts import render
from django.contrib.auth import login, authenticate
from users.forms import LoginForm, SignupForm

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
