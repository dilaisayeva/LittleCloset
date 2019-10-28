from django.urls import path
from .views import *

app_name = 'register'
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('index/',index)

]
