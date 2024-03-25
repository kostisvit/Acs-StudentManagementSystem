from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField('CustomUser', related_name="UserCompanyRelation")
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    username = None
    #company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees",default="1")
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserCompanyRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'company')