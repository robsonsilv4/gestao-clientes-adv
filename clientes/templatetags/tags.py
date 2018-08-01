from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag(takes_context=True)
def data_atual(context):
    return timezone.now()
