from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def add_breadcrumb(context, title, url_name, *args, **kwargs):
    crumbs = context.setdefault('breadcrumbs', [])
    crumbs.append({'title': title, 'url': reverse(url_name, args=args, kwargs=kwargs)})
    return ''

@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def render_breadcrumbs(context):
    return {'breadcrumbs': context.get('breadcrumbs', [])}

