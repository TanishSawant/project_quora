from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length = 15)
    email = models.EmailField()
    #profile_picture =  models.ImageField(default='default.png', upload_to='profile_pics')

    def authenticate(self, username, password):
        if self.user_name == username and self.password == password:
            return User.Objects.get(user_name = username)
        else:
            return None
