from django.shortcuts import render
from .models import Advertisement

def index(request):
    data = Advertisement.objects.all()
    context = {"data":data}
    return render(request, 'index.html', context)

def home(request):
    return render(request, 'index.html')  

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(req):
    return render(req, 'advertisement-post.html')

def register(rq):
    return render(rq, 'register.html')

def login(rq):
    return render(rq, 'login.html')

def profile(rq):
    return render(rq, 'profile.html')
