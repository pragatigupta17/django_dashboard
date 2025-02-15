from django.shortcuts import render
from .models import User

# Create your views here.
def signin(request):
    return render(request, 'signin.html')
    print (request.method)
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
    
        if username == 'admin' and password == 'admin':
            x = "Welcome to Admin panel"
            return render(request,'admindashboard.html',{'msg': x})
        else:
                username:User.object.filter(user_name=name)
                password:User.object.filter(password=password)
                print(user)

    
        
    
        if username:
            data = User.objects.get(user_name=name)
            user_data={
                'name':data.name,
                'password':data.password
             }
            print(user_data)
            pass1 = data.password
            if pass1 == password:
                return render(request,'admindashboard.html',{'name':data.name,'password':data.password,'data':user_data,})
            else:
                msg = "username and password not match"
                return render(request, 'signin.html',{'msg':msg})
        else:
            msg = "password not exist"
            return render(request,'signin.html',{'msg':msg})
    else:
        return render(request, 'signin.html')





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