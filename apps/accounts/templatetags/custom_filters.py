# custom_filters.py

from django import template

register = template.Library()

@register.filter(name='extract_username')
def extract_username(email):
    """
    Extracts the username part from the given email address.
    """
    return email.split('@')[0]
