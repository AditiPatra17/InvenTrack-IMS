from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .manager import UserManager 
from django.conf import settings
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
import utils 


# Create your models here.
    
class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, blank=True, upload_to=utils.user_directory_path)
    address = models.CharField(max_length=200)
    is_staff = models.BooleanField(('staff status'), default=False, help_text=('Determines if user can access the admin site'))
    is_active = models.BooleanField(('active'), default=True)
    is_superuser = models.BooleanField(('active'), default=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone','address']

class Profile(models.Model):
    staff = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    #phone = models.CharField(settings.AUTH_USER_MODEL,max_length=10)
    #address = models.CharField(settings.AUTH_USER_MODEL,max_length=200)
    #image = models.ImageField(null=True, blank=True, upload_to="profile_images/")

    def __str__(self):
        return f'{self.staff.username}-Profile'


