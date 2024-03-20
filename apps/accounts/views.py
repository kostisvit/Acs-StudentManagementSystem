# views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CustomUser,Company


def login_view(request):
    pass
    # if request.method == 'POST':
    #     form = LoginForm(request, data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             # Redirect to a success page.
    #             return redirect('home')
    # else:
    #     form = LoginForm()
    # return render(request, 'account/login.html', {'form': form})






def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('home') 