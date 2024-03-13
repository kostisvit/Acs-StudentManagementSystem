# views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import JsonResponse
from .models import CustomUser,Company,CustomUserCompany


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            company = form.cleaned_data.get('company')
            user = authenticate(request, username=username, password=password, company=company)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         company_id = form.cleaned_data['company'].id
    #         user = authenticate(request, username=username, password=password, company=company_id)
    #         if user is not None:
    #             if user.company_id == company_id:
    #                 login(request, user)
    #             return redirect('home')  # Replace 'home' with your desired redirect URL
    #         else:
    #             # Handle invalid login
    #             pass
    # else:
    #     form = LoginForm()
    # return render(request, 'account/login.html', {'form': form})


def filter_companies(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.GET.get('username')
        if username:
            user = CustomUser.objects.filter(username=username).first()
            if user:
                companies = Company.objects.filter(id=user.id)
                data = [{'id': company.id, 'name': company.company_name} for company in companies]
                return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)



# def filter_companies(request):
#     if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         username = request.GET.get('username')
#         if username:
#             user = CustomUser.objects.filter(username=username).first()
#             if user:
#                 companies = Company.objects.filter(id=user.company.id)
#                 data = [{'id': company.id, 'name': company.company_name} for company in companies]
#                 return JsonResponse(data, safe=False)
#     return JsonResponse({'error': 'Invalid request'}, status=400)



def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('home') 