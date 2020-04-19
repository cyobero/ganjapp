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
                return render(request, 'login.html', {'form': form})
            user = authenticate(username=user.username, password=password)

            if user is not None:
                # verify if user is still active
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index'))
            else:
                errors.append("Whoops. Femmeputer does not femmepute.")
                form = LoginForm(request.POST)
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def profile_view(request):
    return render(request, 'profile.html')


def signup_view(request):
    errors = []

    if request.method == 'POST':
        form = SignupForm(request.POST)

        # Form validation
        if form.is_valid:
            form = form.clean()
            username = form['username']
            email = form['email']
            password = form['password']

            # Create `User` and `Profile` objects that automatically saves to
            # the database once instantiated. Redirect user to home page if
            # registration is successful. Return error message if unsuccessful.
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                # Create `Profile` model
                Profile(user_id=user.id).save()
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect(reverse('profile'))
            except IntegrityError:
                errors.append("The email address provided has already been registered.")
                form = SignupForm(request.POST)

                return render(request, 'signup.html', {'form': form, 'errors': errors})
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
