from django.db import models

# Create your models here.
class account(models.Model):
    
    Username= models.CharField(max_length=100, unique=True)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=8)
    Repassword=models.CharField(max_length=8)

class UserRegistration(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    
