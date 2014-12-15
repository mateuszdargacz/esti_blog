# -*- coding: utf-8 -*-
from mezzanine.blog.models import BlogCategory

__author__ = 'mateusz'
__date__ = '14.12.14 / 17:01'
__git__ = 'https://github.com/mateuszdargacz'
from mezzanine import template


register = template.Library()

@register.as_tag
def get_categories(parent=None):
    if parent:
        pass
    return BlogCategory.objects.all()
