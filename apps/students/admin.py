from django.contrib import admin
from .models import *



class StudentsAdmin(admin.ModelAdmin):
  list_display = ('full_name','display_companies','is_online')
  
  def display_companies(self, obj):
    return ", ".join([company.name for company in obj.company.all()])


admin.site.register(Student,StudentsAdmin)
