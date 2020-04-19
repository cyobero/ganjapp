from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from users.forms import LoginForm, SignupForm

from users.forms import LoginForm
# Create your views here.
def login_view(request):
    errors = []
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
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
                errors.append("Invalid email address provided. Please try again.")
                form = LoginForm(request.POST)
                return render(request, 'login.html', {'form': form, 'errors': errors})
            user = authenticate(username=user.username, password=password)

            if user is not None:
                # verify if user is still active
                if user.is_active:
                    login(request, user)
                    return redirect(user)
            else:
                errors.append("Whoops. Femmeputer does not femmepute.")
                form = LoginForm(request.POST)
                return render(request, 'login.html', {'form': form, 'errors':
                                                      errors})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)

    # take user back to the login page
    return HttpResponseRedirect(reverse('login'))
