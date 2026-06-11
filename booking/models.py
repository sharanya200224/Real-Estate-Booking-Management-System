from django.db import models
from django.contrib.auth.models import User
from properties.models import allproperties
import uuid
from django.db.models.deletion import CASCADE

# Create your models here.

class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    property=models.ForeignKey(allproperties,on_delete=models.CASCADE)
    
    rentamount=models.IntegerField()  
    advance_amount=models.IntegerField()  
    token=models.IntegerField()
    status = models.BooleanField(default=False)

    
    def __str__(self):
        return self.user.username
    



class BookingModel(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    booking_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    booking_date = models.DateField(
        auto_now_add=True
    )

    booking_time = models.TimeField(
        auto_now_add=True
    )

    property_detail = models.ForeignKey(
        allproperties,
        on_delete=models.CASCADE
    )

    owner_name = models.CharField(max_length=100)

    property_name = models.CharField(max_length=100)

    area = models.CharField(max_length=100)

    rent = models.IntegerField()

    advance = models.IntegerField()

    token = models.IntegerField()

    def __str__(self):
        return str(self.booking_id)



class Agreement(models.Model):
    stamp=(
    (20,20),
    
    (50,50),
    (100,100),
    (200,200),
    (300,300)
    )

    property_detail=models.ForeignKey(allproperties,on_delete=CASCADE)
    first_party_name=models.CharField(max_length=100)
    owner_phone=models.BigIntegerField()   
    email=models.EmailField()  
    address=models.TextField() 
    stamp_papper_price=models.IntegerField(choices=stamp)


    secondary_party_name=models.CharField(max_length=100)
    secondary_phone=models.BigIntegerField()  
    secondart_email=models.EmailField()   
    secondary_address=models.TextField()
    advance_amount=models.IntegerField()
