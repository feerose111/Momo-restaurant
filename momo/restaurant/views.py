from django.shortcuts import render, redirect
from .models import Customer
from datetime import datetime
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages




date  = datetime.now()
# Create your views here.
def index(request):
    return render(request, 'main/index.html',{'date':date})

def about(request):
    return render(request, 'main/about.html',{'date':date})

def  contact(request):
    if request.method =='POST':
         data = request.POST
         name = data['name']
         email = data['email']
         phone = data['phone']
         message = data['message']
         
         Customer.objects.create(name=name, email=email, phone = phone, message = message)
         return redirect("contact")
    return render(request, 'main/contact.html',{'date':date})

def menu(request):
    return render(request, 'main/menu.html',{'date':date})

def services(request):
    return render(request, 'main/services.html',{'date':date})

'''
authentication part
'''
class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
def register_user (request):
    if  request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request , ("User is registered succesfully !"))
            return redirect('menu')
    else:
        form = CustomRegistrationForm()
    
    return render(request,'auth/register.html', {'form' : form})


def login_user(request):
    if request.method  == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('menu')
        else:
                messages.success(request , ("There was error Logging In, Try Again!"))
                return redirect('login')          
    else:
        return render(request,'auth/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request , ("You were Logged Out!"))
    return redirect('index')
