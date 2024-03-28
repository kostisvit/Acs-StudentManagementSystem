from django.views.generic import ListView
from students.models import Student
from accounts.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin



class CompanyListView(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    model = Company
    context_object_name = 'online_companys'
    
    def get_queryset(self):
        # Assuming you have a ForeignKey relationship between User and Company
        # Adjust this filtering according to your actual model structure
        return Company.objects.filter(user=self.request.user)



class CompanyInfoListView(ListView):
    template_name = 'app/company.html'
    model = Student
    context_object_name = 'company_info'
    
    
    def get_queryset(self):
        # Assuming you have a ForeignKey relationship between User and Company
        # Adjust this filtering according to your actual model structure
        return Student.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs['company_id']
        context['online_students_count'] = self.get_queryset().filter(is_online=True,company=company_id).count()
        context['offline_students_count'] = self.get_queryset().filter(is_online=False,company=company_id).count()
        return context
    
    def get_queryset(self):
      return super().get_queryset()