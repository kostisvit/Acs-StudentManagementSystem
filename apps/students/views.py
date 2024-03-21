from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView


class StudentsListView(ListView):
    model = Student
    template_name = 'app/students.html'
    context_object_name = 'your_model_objects'

    def get_queryset(self):
        # Filter data based on the logged-in user's associated company
        user_company = self.request.user.company
        queryset = Student.objects.filter(company=user_company)
        return queryset 
  
