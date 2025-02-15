from django.shortcuts import render
from .models import User

# Create your views here.
def signin(request):
    return render(request, 'signin.html')
    print (request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            return render(request,'admindashboard.html',{})
        else:
                username:User.object.filter(stu_name=name)
def admindashboard(request):
    return render(request, 'admindashboard.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')