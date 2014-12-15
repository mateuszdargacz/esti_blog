# -*- coding: utf-8 -*-
from mezzanine.conf import settings
from django.conf.urls import patterns, url

__author__ = 'mateusz'
__date__ = '15.12.14 / 14:14'
__git__ = 'https://github.com/mateuszdargacz'

_slashes = (
    "/" if settings.BLOG_SLUG else "",
    "/" if settings.APPEND_SLASH else "",
)

urlpatterns = patterns("vishalUtech.blog.views",
                       url("^%s(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/"
                           "(?P<slug>.*)%s$" % _slashes,
                           "blog_post_detail", name="blog_post_detail_day"),
                       url("^%s(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>.*)%s$" % _slashes,
                           "blog_post_detail", name="blog_post_detail_month"),
                       url("^%s(?P<year>\d{4})/(?P<slug>.*)%s$" % _slashes,
                           "blog_post_detail", name="blog_post_detail_year"),
                       url("^%s(?P<slug>.*)%s$" % _slashes, "blog_post_detail",
                           name="blog_post_detail")
)