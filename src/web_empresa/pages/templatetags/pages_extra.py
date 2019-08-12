from django import template
from pages.models import Page

#registrar templatetags en libreria de templates
register = template.Library() 

@register.simple_tag
def get_pages_list():
    pages = Page.objects.all()
    return pages #devolver al template en forma de templatetags