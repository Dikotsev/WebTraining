from django import template


register = template.Library()

@register.inclusion_tag()
def __():
    pass