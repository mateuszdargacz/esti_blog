from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from mezzanine.generic.views import initial_validation

__author__ = 'opel'

from json import dumps

from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import ObjectDoesNotExist
from django.contrib.messages import error

from vishalUtech.generic.forms import ThreadedCommentForm

from mezzanine.utils.cache import add_cache_bypass
from mezzanine.utils.views import render, set_cookie, is_spam
from mezzanine.utils.models import get_model
from mezzanine.conf import settings


@login_required
def comment(request, template="generic/comments.html"):
    """
    Handle a ``ThreadedCommentForm`` submission and redirect back to its
    related object.
    """
    response = initial_validation(request, "comment")
    if isinstance(response, HttpResponse):
        return response
    obj, post_data = response
    form = ThreadedCommentForm(request, obj, post_data)
    if form.is_valid():
        url = obj.get_absolute_url()
        if is_spam(request, form, url):
            return redirect(url)
        comment = form.save(request)
        response = redirect(add_cache_bypass(comment.get_absolute_url()))
        # Store commenter's details in a cookie for 90 days.
        for field in ThreadedCommentForm.cookie_fields:
            cookie_name = ThreadedCommentForm.cookie_prefix + field
            cookie_value = post_data.get(field, "")
            print cookie_name, cookie_value
            set_cookie(response, cookie_name, cookie_value.encode('utf-8', 'replace'))
        return response
    elif request.is_ajax() and form.errors:
        return HttpResponse(dumps({"errors": form.errors}))
    # Show errors with stand-alone comment form.
    context = {"obj": obj, "posted_comment_form": form}
    response = render(request, template, context)

    return response
