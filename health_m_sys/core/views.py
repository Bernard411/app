from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'landing.html')


from .models import *
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    # Redirect to a success page or home page.
    return redirect('login.html')  # Replace 'home' with the name of your home URL pattern.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:  # Check if both username and password are provided
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            
                return redirect('homepage')  # Assuming you have a 'success' URL name defined in your urls.py
            else:
               
                messages.error(request, 'Invalid username or password.')
        else:
            # Return an error message if either username or password is missing
            messages.error(request, 'Please provide both username and password.')
    return render(request, 'login.html')  # Assuming you have a login.html template in your templates directory

from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            # Authenticate the user
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)  # Log in the user
                return redirect('login')  # Redirect to the home page after successful registration
            
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

