
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

def login_page(response):
    pass

def login_user(response):
    username = response.POST.get('username')
    password = response.POST.get('password')
    user = authenticate(response, username=username, password=password)

    if user is not None:
        # display success message
        success_msg = 'Login Successful !'
        login(response, user)
        
    else:
        error_msg = 'Username or password not found'


# Register for account here

def register(response):

        username = response.POST.get('username')
        password = response.POST.get('password')
    

        if not username:
            error_msg = "Username is required"
            print(error_msg)
            return {'msg': error_msg}

        elif User.objects.filter(username=username).exists():
            error_msg = "Username already exists"
            print(error_msg)
            return {'msg': error_msg}
        
        elif not password:
            error_msg = "Password is required"
            print(error_msg)
            return {'msg': error_msg}
        
        else:
            if response.user.is_authenticated:  # makes sure we won't log user in if they are already logged in
                error_msg = 'Please log out before creating new account !'
                print(error_msg)
                return {'msg': error_msg}
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                authenticate(response, username=username, password=password)
                login(response, user)  # login here
                success_msg = 'User registered and logged in ! '
                return {'success_msg': success_msg}

    


# Confirm with user that they want to log out
def logout_user(response):
    logout(response)
            

# Page for managing accounts ex: change pwd
def accounts(response):
    return render(response, 'accounts.html', {})
