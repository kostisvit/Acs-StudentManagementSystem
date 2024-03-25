from django.urls import path
from .views import login_view,logout_view

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Add other URLs for your project as needed
]
