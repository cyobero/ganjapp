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

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
