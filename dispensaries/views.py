from django.shortcuts import render

# Create your views here.
def dispensaries(request):
    return render(request, 'dispensaries.html')
