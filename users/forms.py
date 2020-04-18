from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import Profile

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', ]

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
