from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import registrationForm, surveyform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth import authenticate
from django.contrib import messages         # to show flash messages
from django.views.generic import View
from .models import AddInstitute
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('homee')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request,' Username or Password is wrong.')
    context = {}
    return render(request,'registration/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('homee')
    else:
        form = registrationForm()

        if request.method == 'POST':
            form = registrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account is created for ' + user)
                return redirect('login')


    context = {'form':form}
    return render(request,'registration/signup.html',context)

@login_required(login_url='login')
# class dashboard(View):
def dashboard(request):
    forms = surveyform()
    if request.method == 'POST':
        forms = surveyform(request.POST)
        if forms.is_valid():
            f = forms.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request,"rating added update")
        else:
            messages.error(request,f"some error occurred {forms.errors}")
    context= {'form2':forms}
    return render(request,'registration/dashboard.html', context)
