from django.shortcuts import render, HttpResponse, redirect
from .models import *

# LOADS BASE LANDING PAGE 
def base(request):
    return render(request, "base.html") 
 
#  LOADS PROFILE PAGE
def profile(request):
    return render(request, "profile.html")  
















# LOGS OUT THE USER 
def logout(request):
    request.session.clear()
    return redirect('/')