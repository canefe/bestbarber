from django import template

register = template.Library()

@register.filter
def star_range(value):
    value = int(value)
    if value is None or value <= 0:
        return range(5)
    elif value >= 5:
        return range(5)
    else:
        return range(5-value)
