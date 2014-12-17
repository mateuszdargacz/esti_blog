# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '14.12.14 / 17:01'
__git__ = 'https://github.com/mateuszdargacz'


from mezzanine import template
from mezzanine.blog.models import BlogPost, BlogCategory

from django.db.models import Count


register = template.Library()


@register.as_tag
def nested_blog_categories(*args):
    """
    Put a list of  nested categories for blog posts into the template context.
    """
    categories = []
    posts = BlogPost.objects.published()
    main_categories = BlogCategory.objects.filter(is_children__isnull=True).distinct().annotate(
        post_count=Count("blogposts")).prefetch_related('parent')

    for main_category in main_categories:
        data = {
            'category': main_category,
            'children': main_category.parent.first().children.all() if main_category.parent.first() else []
        }
        categories.append(data)
    print categories
    return categories
