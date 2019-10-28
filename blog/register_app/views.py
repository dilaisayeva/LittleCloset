from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import FormView, RedirectView,View
 
from django.http import HttpResponse

from django.core.mail import send_mail

def index(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'isayev.adil.63@mail.ru',
    ['isayev.adil.63@mail.ru'],
    fail_silently=True,
)
    print(send_mail)
   
    return HttpResponse('Task is done!')


class UserRegistration(CreateView):
    model=User
    form_class=SignUpForm
    # my_group = Group.objects.get(name='person') 
    # my_group.user_set.add(model)
    # users = User.objects.all()
    # for u in users:
    #     my_group.user_set.add(u)
    template_name='registration.html'
    print('Clicked')
    success_url=reverse_lazy('register:login')
 
class LoginView(FormView):
   
    form_class = AuthenticationForm
    success_url =reverse_lazy('blog:index')
    template_name = 'login.html' 