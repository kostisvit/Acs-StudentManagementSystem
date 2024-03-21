from django import template
from students.models import Student

register = template.Library()

@register.simple_tag
def online_student_count():
    """
    Returns the count of online students.
    """
    return Student.objects.filter(is_online=True).count()


@register.simple_tag
def offline_student_count():
    
    """
    Returns the count of offline students.
    """
    return Student.objects.filter(is_online=False).count()