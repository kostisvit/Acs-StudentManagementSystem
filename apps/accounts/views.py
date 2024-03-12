# views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import JsonResponse
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            company = form.cleaned_data['company']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.company == company:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                # Handle invalid login
                pass
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def get_user_companies(request):
    username = request.GET.get('username', None)
    companies = list(CustomUser.objects.filter(user__username=username).values('company'))
    return JsonResponse({'companies': companies})



def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('home') 