from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    image_field = models.ImageField(default = 'default.jpg', upload_to = 'profile-pics')
    user = models.ForeignKey(User, unique = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'
