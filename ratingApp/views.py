from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
# Create your views here.


class home(View):
    def get(self,request):
        return render(request,'home/home.html')