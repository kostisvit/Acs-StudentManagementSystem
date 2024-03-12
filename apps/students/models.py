import uuid
from django.db import models
from .utils import create_new_stu_id


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, default="Male")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=50,null=True,blank=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    stu_id = models.CharField(max_length=50, unique=True,editable=False,default=create_new_stu_id)

    def __str__(self):
        return self.full_name