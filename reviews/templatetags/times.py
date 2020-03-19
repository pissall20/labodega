from django import template

register = template.Library()

@register.filter(name='times')
def times(n):
    return list(range(n))
