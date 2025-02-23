from django.shortcuts import render
from .models import Admin
from .models import User
from .models import Registration
# Create your views here.
def signin(request):
    print(request.method)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
    
        if email == 'admin@gmail.com' and password == 'admin':
            x = "Welcome to Admin panel"
            return render(request,'admindashboard.html',{'msg': x})
        else:
            #  x="Admin not match"
            #  return render(request,'signin.html', {'mag':x})
            user=User.objects.get(email=email)  
            if User:
                    user=User.objects.get(email=email)
                    print(user)
                    email=user.email
                    password1=user.password
                    if(password==password1):
                        return render(request,'base.html')
                    else:        
                        return render (request,'signin.html')
    else:
        return render (request,'signin.html')

def admindashboard(request):
    return render(request, 'admindashboard.html')

def fee_details(request):
    return render(request,'fee_details.html')

def student_details(request):
    return render(request,'student_details.html')

def fee_status(request):
    return render(request,'fee_status.html')

def registration(request):
    return render(request,'registration.html')
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        image=request.POST.get('image')
        f_name=request.POST.get('f_name')
        m_name=request.POST.get('m_name')
        dob=request.POST.get('dob')
        blood_grp=request.POST.get('blood_grp')
        specialisation=request.POST.get('specialisation')
        course=request.POST.get('course')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        session=request.POST.get('session')
        roll_no=request.POST.get('roll_no')
        address=request.POST.get('address')    
        print(__all__)
        user = Student.objects.filter(email=email)
    

def login(request):
    return render(request,'login.html')