from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users

# Create your views here.

def index(request):

    return render(request,'gallery/index.html')

def home_view(request):
    return render(request,'gallery/home.html')

def new_view(request):
    return render(request,'gallery/new.html')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['ClassicUser'])
def my_view(request):
    return render(request,'gallery/my_view.html')


class SignUpView(SuccessMessageMixin,CreateView):
    form_class = CreateUserForm
    success_url= reverse_lazy('login')
    template_name = 'gallery/signup.html'

    success_message = "%(username)s account was created successfully!"
    
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        #REDIRECT NEXT LOGIC
        #DEPLOY USING LINODE
        if user is not None:
            login(request,user)
        else:
            messages.warning(request,'Username or password is incorrect!')

      
    context = {}
    return render(request,'accounts/login.html', context)

def logged_outPage(request):
    
    logout(request)

    return render(request,'accounts/logged_out.html')