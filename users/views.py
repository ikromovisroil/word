from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import auth
from .forms import *
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = Userloginform(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password,)
            if user and user.is_active:
                auth.login(request,user)
                return redirect(reverse('create_docx'))
    else:
        form = Userloginform()
    context = { 'form':form }
    return render(request, 'registration/login.html',context)



def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))