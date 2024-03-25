# Generated by Django 4.2 on 2024-03-25 14:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ManyToManyField(related_name='UserCompanyRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
