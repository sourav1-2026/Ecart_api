
from .views import UserRegister
from django.urls import path,include

urlpatterns = [
   
    path('register/',UserRegister.as_view())
]
