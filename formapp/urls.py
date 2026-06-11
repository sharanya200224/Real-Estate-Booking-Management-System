from django.urls import path
from formapp import views


urlpatterns=[
    path('',views.registration, name="registration"),
    path('login', views.user_login, name="login"),
    path('home', views.home, name='home'),
    path('logout', views.user_logout, name="logout"),
    path('profile',views.profile, name='profile'),
    path('update', views.user_update, name='update'  ),
    path('realtorreg', views.realtor_reg, name='realtorreg'),
    path('realtordetail',views.realtor_detail, name='realtordetail'),
    path('dashboard', views.realtor_dashboard, name='dashboard'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('search',views.search,name='search'),
]