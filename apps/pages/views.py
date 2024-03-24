from django.views.generic import ListView
from students.models import Student
from accounts.models import Company


# class HomePageView(ListView):
#   template_name = 'home.html'
#   model = Company


#   def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_company = self.request.user.company
#         context['online_students_count'] = self.get_queryset().filter(is_online=True,company=user_company).count()
#         context['offline_students_count'] = self.get_queryset().filter(is_online=False,company=user_company).count()
#         return context

#   def get_queryset(self):
#       return super().get_queryset()



class CompanyListView(ListView):
    template_name = 'home.html'
    model = Company
    context_object_name = 'online_companys'
    
    def get_queryset(self):
        # Filter data based on the logged-in user's associated company
        user_company = self.request.user.company
        queryset = Company.objects.filter(name=user_company)
        return queryset 



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
        context['online_students_count'] = self.get_queryset().filter(is_online=True,company_id=company_id).count()
        context['offline_students_count'] = self.get_queryset().filter(is_online=False,company_id=company_id).count()
        return context
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         company_id = self.kwargs['company_id']  # Get the company ID from URL
#         context['company'] = Student.objects.filter(company_id=company_id).count() # Add company object to context
#         context['online_students_count'] = self.get_queryset().count()

#         return context
    
    
    def get_queryset(self):
      return super().get_queryset()