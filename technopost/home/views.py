from django.shortcuts import render
from .models import datas


# Create your views here.
def home(request):
    post= {
        'datas':datas.objects.all()
    }
    return render(request,"home/home.html",post)

def about(request):
    return render(request,"home/about.html",{'title':'ABOUT'})