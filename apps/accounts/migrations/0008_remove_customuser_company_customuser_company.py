# Generated by Django 4.2 on 2024-03-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customusercompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company',
        ),
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.ManyToManyField(through='accounts.CustomUserCompany', to='accounts.company'),
        ),
    ]
