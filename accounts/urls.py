
from .views import UserRegister,LoginView
from django.urls import path,include

urlpatterns = [
   
    path('register/',UserRegister.as_view()),
    path('login/',LoginView.as_view())
]
