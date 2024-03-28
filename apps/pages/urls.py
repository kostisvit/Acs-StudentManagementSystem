from django.urls import path
from .views import  CompanyListView,CompanyInfoListView

urlpatterns = [
  #path('', HomePageView.as_view(),name='home'),
  path('companies/', CompanyListView.as_view(), name='home'),
  path('company/<int:company_id>/info', CompanyInfoListView.as_view(), name='company-info' )
]