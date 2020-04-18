from django.shortcuts import render

# Create your views here.
def shop_home(request):
    return render(request, "shop.html")
