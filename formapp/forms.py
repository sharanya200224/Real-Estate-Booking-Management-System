from django import forms
from django.contrib.auth.models import User 
from formapp.models import UserData
from formapp.models import Realtors , Enquiry
from django_recaptcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        # fields="_all_"
        fields=['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserData
        fields = ['phone', 'house_no', 'street', 'landmark', 'city', 'state', 'zipcode', 'userpic']
    
    captcha=ReCaptchaField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
        
class UserProfileFormUpdateForm(forms.ModelForm):
    class Meta:
        model=UserData
        fields=['phone','house_no','street','landmark','city','state','zipcode','userpic']


class RealtorForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class RealtorProfileForm(forms.ModelForm):
    class Meta:
        model=Realtors
        fields=['phone','address','lic_no','lic_img','photo']

class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields = '__all__'
        
class RealtorUpdateForm(forms.ModelForm):
    class Meta:
        model = Realtors
        fields = [
            'phone',
            'address',
            'lic_no',
            'lic_img',
            'photo'
        ]