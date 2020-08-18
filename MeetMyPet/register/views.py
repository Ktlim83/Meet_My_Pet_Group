from django.shortcuts import render, redirect
from login.models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'register/index.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/register')

    new_user = User.objects.register(request.POST)
    request.session['user_id'] = new_user.id
    return redirect('/')