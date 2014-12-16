from django.conf import settings
from django.db import models
from django.db.models import ForeignKey
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.core.managers import DisplayableManager, CurrentSiteManager
from mezzanine.utils.sites import current_site_id

__author__ = 'opel'

from datetime import datetime, timedelta


class BlogPostManager(DisplayableManager):
    def last_days(self, mdays):
        # return BlogPost.objects.filter(publish_date__gte=datetime.now()-timedelta(days=mdays)).order_by('ratio')
        # Sorted QuerySet by ratio propety from last [settings.TOP_POST_DAYS] days.:
        return sorted(BlogPost.objects.filter(publish_date__gte=datetime.now() - timedelta(days=mdays))[
                      :settings.TOP_POST_DAYS_AMOUNT],
                      key=lambda a: -a.ratio)

    def top_viewed(self):
        return sorted(BlogPost.objects.all()[:settings.TOP_VIEWED_AMOUNT], key=lambda a: -a.topviewed)


class BlogPostExtend:
    objects = DisplayableManager()
    trends = BlogPostManager()

    @property
    def ratio(self):
        """
        Returns views amount per day for post
        """
        diff = (datetime.now().date() - self.publish_date.date()).days
        diff = 1 if diff == 0 else diff

        return int(self.views_count) / int(diff)

    @property
    def topviewed(self):
        """
        Returns top viewed post
        """
        return int(self.views_count) - int(self.views_count_delta)


BlogPost.__bases__ += (BlogPostExtend,)


class BlogCategoryExtend:
    # Foreign key added  here instead of settings.EXTRA_MODEL_FIELDS,
    # because of mezzine's bug with circular relation
    parent = models.ForeignKey('self', verbose_name='Parent category', blank=True, null=True)


BlogCategory.__bases__ += (BlogPostExtend,)


