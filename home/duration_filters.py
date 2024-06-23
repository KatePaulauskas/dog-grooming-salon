from django import template

register = template.Library()

@register.filter
def hours(td):
    total_seconds = int(td.total_seconds())
    return total_seconds // 3600

@register.filter
def minutes(td):
    total_seconds = int(td.total_seconds())
    return (total_seconds // 60) % 60