from mezzanine.blog.models import BlogPost
from mezzanine.core.managers import DisplayableManager, CurrentSiteManager
from mezzanine.utils.sites import current_site_id

__author__ = 'opel'

from datetime import datetime, timedelta


class BlogPostManager(DisplayableManager):
    def last_days(self, mdays):
        # return BlogPost.objects.filter(publish_date__gte=datetime.now()-timedelta(days=mdays)).order_by('ratio')
        #Sorted QuerySet by ratio propety from last [settings.TOP_POST_DAYS] days.:
        return sorted(BlogPost.objects.filter(publish_date__gte=datetime.now() - timedelta(days=mdays)),
                      key=lambda a: a.ratio)

    def top_viewed(self):
        return sorted(BlogPost.objects.all(), key=lambda a: a.topviewed)


class BlogPostExtend:
    objects = DisplayableManager()
    trends = BlogPostManager()

    @property
    def ratio(self):
        """
        Returns views amount per day for post
        """
        diff = (datetime.now().date() - self.publish_date.date()).days
        return int(self.views_count) / int(diff)

    @property
    def topviewed(self):
        """
        Returns top viewed post
        """
        return int(self.views_count)-int(self.views_count_delta)


BlogPost.__bases__ += (BlogPostExtend,)