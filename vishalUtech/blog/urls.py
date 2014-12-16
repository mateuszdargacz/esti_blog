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

urlpatterns = patterns("",
                       url("^%sfeeds/(?P<format>.*)%s$" % _slashes,
                           "mezzanine.blog.views.blog_post_feed", name="blog_post_feed"),
                       url("^%stag/(?P<tag>.*)/feeds/(?P<format>.*)%s$" % _slashes,
                           "mezzanine.blog.views.blog_post_feed", name="blog_post_feed_tag"),
                       url("^%stag/(?P<tag>.*)%s$" % _slashes, "blog_post_list",
                           name="blog_post_list_tag"),
                       url("^%scategory/(?P<category>.*)/feeds/(?P<format>.*)%s$" % _slashes,
                           "mezzanine.blog.views.blog_post_feed", name="blog_post_feed_category"),

                       # local urls
                       url("^%scategory/(?P<category>.*)%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_list", name="blog_post_list_category"),
                       url("^%sauthor/(?P<username>.*)/feeds/(?P<format>.*)%s$" % _slashes,
                           "mezzanine.blog.views.blog_post_feed", name="blog_post_feed_author"),
                       url("^%sauthor/(?P<username>.*)%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_list", name="blog_post_list_author"),
                       url("^%sarchive/(?P<year>\d{4})/(?P<month>\d{1,2})%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_list", name="blog_post_list_month"),
                       url("^%sarchive/(?P<year>\d{4})%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_list", name="blog_post_list_year"),
                       url("^%s(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/"
                           "(?P<slug>.*)%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_detail", name="blog_post_detail_day"),
                       url("^%s(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>.*)%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_detail", name="blog_post_detail_month"),
                       url("^%s(?P<year>\d{4})/(?P<slug>.*)%s$" % _slashes,
                           "vishalUtech.blog.views.blog_post_detail", name="blog_post_detail_year"),
                       url("^%s(?P<slug>.*)%s$" % _slashes, "vishalUtech.blog.views.blog_post_detail",
                           name="blog_post_detail")
)