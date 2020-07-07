from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method== 'POST':
        email = request.POST['email']
        passw = request.POST['pswd']
        user = auth.authenticate(username = email, password = passw)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.error(request,'invalid credentials')
            return redirect('')
    else:
        return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['fullname']
        passw = request.POST['pswd']
        cpass = request.POST['cnfpswd']
        if User.objects.filter(email=email).first():
            messages.error(request, 'User exists')
            return render(request,'index.html')
        else:
            if passw == cpass:
                user = User.objects.create_user(
                    username=email, email=email, password=passw)
                return render(request, 'index.html')
                
            else:
                messages.error(request, 'Passwords not matching')
                return render(request, 'index.html')


@login_required
def contact(request):
    return render(request, 'contactus.html')


@login_required
def menu(request):
    return render(request, 'menu.html')


def logout(request):
    auth.logout(request)
    return render(request,'index.html')