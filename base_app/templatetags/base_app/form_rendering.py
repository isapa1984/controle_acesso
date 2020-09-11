from django import template

register = template.Library()

@register.inclusion_tag('tags/field.html')
def render_field(field):
    return {'field': field}

@register.inclusion_tag('tags/form.html')
def render_form(form):
    return form

