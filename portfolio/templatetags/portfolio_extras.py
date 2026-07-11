from django import template

register = template.Library()


@register.filter
def split(value, separator=','):
    return [part.strip() for part in value.split(separator) if part.strip()]
