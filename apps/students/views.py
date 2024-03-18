from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView


class StudentsListView(ListView):
  model = Student
  template_name = 'app/students.html'
  
  # def get_queryset(self):
  #   company_id = self.kwargs.get('company_id')
  #   return Student.objects.filter(company_id=company_id)
  
