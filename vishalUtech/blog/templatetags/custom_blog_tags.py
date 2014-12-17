# -*- coding: utf-8 -*-
from django.conf import settings

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
    main_categories = BlogCategory.objects.filter(is_children__isnull=True).distinct().annotate(
        post_count=Count("blogposts")).prefetch_related('parent')

    for main_category in main_categories:
        data = {
            'category': main_category,
            'children': main_category.parent.first().children.all() if main_category.parent.first() else []
        }
        categories.append(data)
    return categories


@register.assignment_tag
def most_popular():
    return BlogPost.trends.last_days()

@register.assignment_tag
def popular_this_week():
    print BlogPost.trends.last_days(settings.TOP_POST_DAYS)
    return BlogPost.trends.last_days(settings.TOP_POST_DAYS)

