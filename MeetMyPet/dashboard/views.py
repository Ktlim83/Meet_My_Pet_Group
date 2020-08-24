from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from login.models import *
from dashboard.models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# LOADS BASE LANDING PAGE 
def base(request):
    context = {
            'curr_user': User.objects.get(id=request.session['user_id']),
            "others" : User.objects.all(),
        }
    return render(request, "base.html", context) 
 
#  LOADS PROFILE PAGE
def profile(request, id):
    if 'user_id' not in request.session:
        return redirect ('/')
    else:
        context = {
            'curr_user': User.objects.get(id=request.session['user_id']),
            'user': User.objects.get(id=id),
            "others" : User.objects.all(),
        }
        return render(request, "profile.html", context)
    
    
# EDITS THE USER PROFILE  
def edit_profile(request, id):
    # REMEMBER TO ADD ANOTHER PARAMETER FOR THE FILES DIRECTORY WITH POST
    errors = User.objects.profile_validator(request.POST,request.FILES)
    if errors:
        for field, value in errors.items():
            messages.error(request, value, extra_tags='edit_not_approved')
        return redirect(f'/woof/profile/{id}')
    else:
        curr_user = User.objects.get(id=id)
        curr_user.bio = request.POST['bio']
        curr_user.first_name = request.POST['first_name']
        curr_user.last_name = request.POST['last_name']
        curr_user.pet = request.POST['pet']
        curr_user.pet_age = request.POST['pet_age']
        curr_user.pet_temperament = request.POST['pet_temperament']
        curr_user.email = request.POST['email']
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        user_picture = fs.save(picture.name, picture)
        url = fs.url(user_picture)
        curr_user.profile_pic = url
        curr_user.save()
        print('congrats something worked!')
        messages.success(request, "You have successfully updated! Please sign in!", extra_tags='edit_approved')

        return redirect(f'/woof/profile/{id}')
    
#  LOADS MESSAGEBOARD PAGE
def messageboard(request):
    context = {
        'curr_user': User.objects.get(id=request.session['user_id']),
        'posts' : Post.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request, "messageboard.html", context)  

# CREATES A POST
def createPost(request):
    errors = Post.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/woof/messageboard')
    new_post = Post.objects.create(title=request.POST['title'], content=request.POST['content'], author=User.objects.get(id=request.session['user_id']))
    return redirect('/woof/messageboard')

# DELETE A POST
def deletePost(request, post_id):
    to_delete = Post.objects.get(id=post_id)
    if to_delete.author_id == request.session['user_id']:
        to_delete.delete()
    return redirect('/woof/messageboard')

# LIKE A POST
def likePost(request, post_id):
    message = Post.objects.get(id=post_id)
    message.likes.add(User.objects.get(id=request.session['user_id']))
    return redirect('/woof/messageboard')

# CREATE A COMMENT
def createComm(request, post_id):
    new_comm = Comment.objects.create(content=request.POST['content'], author=User.objects.get(id=request.session['user_id']), message=Post.objects.get(id=post_id))
    return redirect('/woof/messageboard')

# DELETE A COMMENT
def deleteComm(request, comment_id):
    to_delete = Comment.objects.get(id=comment_id)
    if to_delete.author_id == request.session['user_id']:
        to_delete.delete()
    return redirect('/woof/messageboard')














# LOGS OUT THE USER 
def logout(request):
    request.session.clear()
    return redirect('/')