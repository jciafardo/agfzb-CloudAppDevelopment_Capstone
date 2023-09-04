from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from users.views import register, logout_user, login_user
from django.http import HttpResponseRedirect


# delete this comment 
# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def index(response):
        
    if response.method == 'POST':
        if 'username' in response.POST or 'password' in response.POST:

            

            if 'sign-up' in response.POST:    
                register(response)
                return HttpResponseRedirect('/djangoapp/register')
            if 'login' in response.POST:
                login_user(response)
                return HttpResponseRedirect('/djangoapp/login')

                

        if 'logout' in response.POST:
            logout_user(response)
            return HttpResponseRedirect('/djangoapp/logout')
    
    if response.user.is_authenticated:
        is_auth = True 
    else:
        is_auth = False 
    
    return render(response, 'djangoapp/index.html', {'is_auth': is_auth})
    

def static(request):
    return render(request, 'static.html', {})



# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html', {})

# def about(request):
# ...


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html', {})

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

