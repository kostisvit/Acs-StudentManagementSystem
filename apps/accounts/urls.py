from django.urls import path
from .views import login_view,logout_view,filter_companies

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('filter-companies/', filter_companies, name='filter_companies'),
    # Add other URLs for your project as needed
]
