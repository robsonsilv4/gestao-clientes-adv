from django import template

register = template.Library()

@register.filter
def concatena(data):
    return data + '- Texto concatenado'


@register.filter
def arredonda(value, casas):
    return round(value, casas)
