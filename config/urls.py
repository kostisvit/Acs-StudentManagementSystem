from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # User Management
    path('', include('accounts.urls')),
    
    # Local apps
    path('', include('pages.urls')),
    path('', include('students.urls'))
]
