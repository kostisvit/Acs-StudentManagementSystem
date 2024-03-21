from django import template
from accounts.models import Company

register = template.Library()

@register.simple_tag
def get_company_name():
    """
    Returns the name of the company.
    """
    company = Company.objects.first()
    return company.name if company else "Unknown Company"