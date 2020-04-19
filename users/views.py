from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from users.forms import LoginForm, SignupForm
from users.models import Profile

from users.forms import LoginForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # first, validate form
        if form.is_valid():
            form = form.clean()
            email = form['email']
            password = form['password']

            query_user = User.objects.filter(email=email)

            # If the length of `query_user` is > 0, then a
            # user object exists.
            if len(query_user) > 0:
                user = query_user[0]
            else:
                form = LoginForm(request.POST)
                return render(request, 'login.html', {'form': form})
            user = authenticate(username=user.username, password=password)

            if user is not None:
                # verify if user is still active
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index'))
            else:
                form = LoginForm(request.POST)
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)

    # take user back to the login page
    return HttpResponseRedirect(reverse('login'))


@login_required
def profile_view(request, username):
    if request.user.is_authenticated:
        profile = Profile.objects.get(username=username)
        return render(request, 'profile.html', {'profile': profile })
    return render(request, 'profile.html')
