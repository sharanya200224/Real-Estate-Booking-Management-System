from django.urls import path

from booking import views


urlpatterns=[  
    path('book/<int:id>/',views.booking_property,name="book"),
    path('success/',views.booking_success,name='success'),
    path('book_property/<int:id>/',views.book_property,name='book_property'),
    path('agreement/<int:id>/',views.agreement_detail,name='agreement'),
    path('agreementdetail/<int:id>/',views.agreement_creation,name='agreementdetail')
]