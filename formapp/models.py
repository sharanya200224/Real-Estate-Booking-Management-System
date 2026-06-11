from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields
    phone=models.BigIntegerField()
    house_no=models.IntegerField()
    street=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    userpic=models.ImageField(upload_to='userpic/',blank=True,null=True)
# Create your models here.

# Create your models here.
class Realtors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.BigIntegerField()   
    address=models.CharField(max_length=100)
    lic_no=models.IntegerField()   
    lic_img= models.ImageField(upload_to='realtorpic/',blank=True,null=True)
    is_approved= models.BooleanField(default=False)
    photo=models.ImageField(blank=True,null=True)

    

class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()  
    email=models.EmailField()  
    address=models.CharField()   
    description=models.TextField() 