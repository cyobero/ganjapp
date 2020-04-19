from django.shortcuts import render
from users.models import Profile

def index(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'index.html', {'user': user })
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
