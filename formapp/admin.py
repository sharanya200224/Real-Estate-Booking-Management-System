from django.contrib import admin
from formapp.models import Realtors, UserData, Enquiry

# Register your models here.
admin.site.register(UserData)
admin.site.register(Realtors)
admin.site.register(Enquiry)

