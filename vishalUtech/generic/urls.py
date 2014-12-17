from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns("",
    url("^admin_keywords_submit/$", "mezzanine.generic.views.admin_keywords_submit",
        name="admin_keywords_submit"),
    url("^rating/$", "mezzanine.generic.views.rating", name="rating"),
    url("^comment/$", "vishalUtech.generic.views.comment", name="comment"),
)
