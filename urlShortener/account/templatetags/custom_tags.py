from django import template

register = template.Library()


@register.simple_tag()
def call(func, *args, **kwargs):
    return func(*args, **kwargs)