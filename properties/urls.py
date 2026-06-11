from django.urls import path
from properties import views


urlpatterns = [
    path('<int:id>',views.property_detail,name="property_details"),
    path('dashboard',views.dashboard_details,name="dashboard"),
    path('add_property',views.add_new_property,name="add_property"),
    path('property_edit/<int:id>',views.propertyEdit,name='property_edit'),
    path('calculator/<int:id>/',views.book_property,name='calculator'),
    path('allproperties', views.AllProperties,name='allproperties'),
    path('visit/<int:id>/',views.visit_property,name='visit'),
    path('bookadvance/<int:id>/',views.book_advance,name='bookadvance'),
    
]