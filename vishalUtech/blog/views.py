from __future__ import unicode_literals
from calendar import month_name

from future.builtins import str
from future.builtins import int
from django.http import Http404
from django.shortcuts import get_object_or_404
from mezzanine.blog.models import BlogCategory, BlogPost
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate
from mezzanine.utils.models import get_user_model


User = get_user_model()

# from datetime import datetime, timedelta
# import operator

# def last_days(mdays):
#     posts = BlogPost.objects.filter(publish_date__gte=datetime.now()-timedelta(days=mdays))
#     for p in posts:
#         diff = (datetime.now().date()-p.publish_date.date()).days
#     posts = [(p,int(p.views_count)/int(diff),diff,p.views_count) for p in posts]
#     posts.sort(key=operator.itemgetter(1), reverse=True)
#     sorted_list = []
#     for p in posts:
#         sorted_list.append(p[0])
#     return sorted_list


def blog_post_list(request, tag=None, year=None, month=None, username=None,
                   category=None, template="blog/blog_post_list.html"):
    """
    Display a list of blog posts that are filtered by tag, year, month,
    author or category. Custom templates are checked for using the name
    ``blog/blog_post_list_XXX.html`` where ``XXX`` is either the
    category slug or author's username if given.
    """

    settings.use_editable()
    templates = []
    blog_posts = BlogPost.objects.published(for_user=request.user)

    if tag is not None:
        tag = get_object_or_404(Keyword, slug=tag)
        blog_posts = blog_posts.filter(keywords__keyword=tag)
    if year is not None:
        blog_posts = blog_posts.filter(publish_date__year=year)
        if month is not None:
            blog_posts = blog_posts.filter(publish_date__month=month)
            try:
                month = month_name[int(month)]
            except IndexError:
                raise Http404()
    if category is not None:
        category = get_object_or_404(BlogCategory, slug=category)
        blog_posts = blog_posts.filter(categories=category)
        templates.append(u"blog/blog_post_list_%s.html" %
                         str(category.slug))
    author = None
    if username is not None:
        author = get_object_or_404(User, username=username)
        blog_posts = blog_posts.filter(user=author)
        templates.append(u"blog/blog_post_list_%s.html" % username)

    prefetch = ("categories", "keywords__keyword")
    blog_posts = blog_posts.select_related("user").prefetch_related(*prefetch)
    ### Adding feature posts for main page, amount set in settings
    blog_posts_feature = blog_posts.order_by('?')[:settings.RANDOM_POST_AMOUNT]
    blog_posts_top_week= BlogPost.trends.last_days(settings.TOP_POST_DAYS)
    blog_posts_top_viewed = BlogPost.trends.top_viewed()
    blog_posts = paginate(blog_posts, request.GET.get("page", 1),
                          settings.BLOG_POST_PER_PAGE,
                          settings.MAX_PAGING_LINKS)

    context = ( {"blog_posts": blog_posts, "year": year, "month": month,
                 "tag": tag, "category": category, "author": author,
                 "blog_posts_feature": blog_posts_feature,
                 "blog_posts_top_week": blog_posts_top_week,
                 "blog_posts_top_viewed": blog_posts_top_viewed,

                 })

    templates.append(template)
    return render(request, templates, context)


def blog_post_detail(request, slug, year=None, month=None, day=None,
                     template="blog/blog_post_detail.html"):
    """. Custom templates are checked for using the name
    ``blog/blog_post_detail_XXX.html`` where ``XXX`` is the blog
    posts's slug.
    """
    blog_posts = BlogPost.objects.published(
        for_user=request.user).select_related()
    blog_post = get_object_or_404(blog_posts, slug=slug)
    context = {"blog_post": blog_post, "editable_obj": blog_post}
    templates = [u"blog/blog_post_detail_%s.html" % str(slug), template]
    ### Increase visit_counter
    blog_post.views_count += 1
    blog_post.save()
    return render(request, templates, context)



