from django.views.generic import TemplateView,ListView
from students.models import Student

class HomePageView(ListView):
  template_name = 'home.html'
  model = Student
  context_object_name = 'online_students'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_company = self.request.user.company
        context['online_students_count'] = self.get_queryset().filter(is_online=True,company=user_company).count()
        context['offline_students_count'] = self.get_queryset().filter(is_online=False,company=user_company).count()
        return context

  def get_queryset(self):
      return super().get_queryset()
  