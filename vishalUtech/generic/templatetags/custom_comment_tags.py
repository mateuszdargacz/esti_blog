__author__ = 'opel'
from django.core.urlresolvers import reverse

from vishalUtech.generic.forms import ThreadedCommentForm
from mezzanine import template

register = template.Library()

### Own template tag
@register.inclusion_tag("generic/includes/comments.html", takes_context=True)
def custom_comments_for(context, obj):
    """
    Overwritten template tag, based at comments_for (genertic.templatetags)
    Provides a generic context variable name for the object that
    comments are being rendered for.
    """
    print 'tes fdsfsdfs'
    form = ThreadedCommentForm(context["request"], obj)
    try:
        context["posted_comment_form"]
    except KeyError:
        context["posted_comment_form"] = form
    context["unposted_comment_form"] = form
    context["comment_url"] = reverse("comment")
    context["object_for_comments"] = obj
    return context
