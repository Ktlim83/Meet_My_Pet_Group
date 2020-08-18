from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# LOADS LOGIN PAGE 
def index(request):
    context = {
        'user': User.objects.get_all_by_email()
    }
    return render(request, 'index.html', context)

# LOGS IN THE USER WITH CREDENTIALS 
def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, 'Invalid Email or Password')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/woof')
    return redirect('/')







def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)
