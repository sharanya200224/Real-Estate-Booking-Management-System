from django.contrib import admin
from properties.models import allproperties, Rooms, Livingarea, kitchen, bathroom,balcony

# Register your models here.
admin.site.register(allproperties)
admin.site.register(Rooms)
admin.site.register(Livingarea)
admin.site.register(kitchen)
admin.site.register(bathroom)
admin.site.register(balcony)

