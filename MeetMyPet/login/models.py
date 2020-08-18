from django.db import models
from django.core.files.storage import FileSystemStorage
from datetime import date
import re
import bcrypt

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def get_all_by_email(self):
        return self.order_by('email')

    def register(self, form_data):
        my_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        #Creates a new user based on given input
        return self.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = my_hash,
            confirm = form_data['confirm'],
        )

    def authenticate(self, email, password):
        same_email = self.filter(email=email)
        if not same_email:
            return False
        user = same_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
    
    def validate(self, form_data):
        
        errors = {}
        #First/Last Name < 2
        if len(form_data['first_name']) < 2 or len(form_data['last_name']) < 2:
            errors['first_name'] = 'First/Last Name must be at least 3 characters.'
        
            
        #Email must be valid
        if not EMAIL_MATCH.match(form_data['email']):
            errors['email'] = 'Must be a valid email address.'

        #Email must be unique
        same_email = self.filter(email=form_data['email'])
        if same_email:
            errors['email'] = 'Email already in use'

        #Password must be at least 8 characters.
        if len(form_data['password']) < 7:
            errors['password'] = 'Password must be at least 8 characters.'

        #Password and confirm must match
        if form_data['password'] != form_data['confirm']:
            errors['password'] = 'Password does not match.'
        
        return errors
    
    
    # VALIDATES THE USER UPDATE FORM ALSO ADDS PROFILE PICTURE
    def profile_validator(self, form_data, file_data):
        errors = {}
   
        if len(form_data['first_name']) < 1:
            errors['first_name'] = 'First Name field is required.'

        if len(form_data['last_name']) < 1:
            errors['last_name'] = 'Last Name field is required.'

        if len(form_data['email']) < 1:
            errors['email'] = 'Email field is required.'
            
        if len(form_data['pet']) < 1:
            errors['pet'] = 'pet field is required.'
            
        if len(form_data['bio']) < 1:
            errors['bio'] = 'Bio field is required.'
        
        # LOOKING FOR KEY VALUE STRING "PICTURE" IN FILE DATA
        # IF THERE IS A PHOTO THEN NO ERROR MESSAGE

        if "picture" in file_data:
            print("there is a photo")
        else:
            errors['picture'] = 'Picture field is required.'
            
            
        
            
        return errors
    

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_pic = models.CharField(max_length=255, null=True)
    bio = models.CharField(max_length=255, null=True)
    pet = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()