from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
   user = models.ForeignKey(User,on_delete = models.CASCADE)
   uploadingdate = models.CharField(max_length=30)
   branch = models.CharField(max_length=30)
   subject = models.CharField(max_length=30)
   notefile = models.FileField(null=True)
   description = models.CharField(max_length=200, null=True)
   status = models.CharField(max_length=15)

   def __str__(self):
            return str(self.user)

class Signup(models.Model):
   user =  models.ForeignKey(User,on_delete = models.CASCADE)
   email = models.CharField(max_length=30)
   contact =  models.CharField(max_length=30)
   branch = models.CharField(max_length=30)

   def __str__(self):
        return self.user.username
   
   


   

    
