# views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import EmailLoginForm


def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('home')
            else:
                # Handle invalid login
                error_message = "Invalid email or password."
    else:
        form = EmailLoginForm()
        error_message = None
    return render(request, 'account/login.html', {'form': form, 'error_message': error_message})





def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('home') 