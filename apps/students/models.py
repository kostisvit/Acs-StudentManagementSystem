import uuid
from django.db import models
from .utils import create_new_stu_id

from accounts.models import Company

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default='1')
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=50,null=True,blank=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    stu_id = models.CharField(max_length=50, unique=True,editable=False,default=create_new_stu_id)

    def __str__(self):
        return self.full_name