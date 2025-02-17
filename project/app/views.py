from django.shortcuts import render
from .models import Admin
from .models import User

# Create your views here.
def signin(request):
    print(request.method)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        if email == 'admin@gmail.com' and password == 'admin':
            x = "Welcome to Admin panel"
            return render(request,'admindashboard.html',{'msg': x})
        else:
            admin=signin.objects.filter(email=email)
            if(data):
                user=signin.objects.get(email=email)
                print(user)
                password=user.email
                if(password==password):
                    return render(request,'base.html')
                else:        
                    return render (request,'signin.html')
    else:
        return render (request,'signin.html')



        
    
       



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