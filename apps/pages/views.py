from django.views.generic import ListView
from students.models import Student
from accounts.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin



class CompanyListView(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    model = Company
    context_object_name = 'online_companys'
    
    def get_queryset(self):
        # Retrieve the user
        user = self.request.user
        # Retrieve all companies associated with the user
        companies = Company.objects.filter(usercompanyrelation__user=user)
        return companies



class CompanyInfoListView(ListView):
    template_name = 'app/company.html'
    model = Student
    context_object_name = 'company_info'
    
    
    def get_queryset(self):
        company_id = self.kwargs['company_id']  # Assuming you pass the company as a URL parameter
        return Student.objects.filter(company_id=company_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs['company_id']
        context['online_students_count'] = self.get_queryset().filter(is_online=True,company=company_id).count()
        context['offline_students_count'] = self.get_queryset().filter(is_online=False,company=company_id).count()
        return context
    
    def get_queryset(self):
      return super().get_queryset()