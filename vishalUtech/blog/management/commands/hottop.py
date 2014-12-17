import random
from mezzanine.blog.models import BlogPost

__author__ = 'opel'

from django.core.management.base import BaseCommand


## CRON EXAMPLE (every 5 min)
## */5 * * * * python manage.py hottop

class Command(BaseCommand):
    help = "Updates views counter"

    def handle(self, *apps, **options):
        blog_posts = BlogPost.objects.all()
        for bp in blog_posts:
            current = bp.views_count
            old = bp.views_count_delta
            bp.views_count_delta = current
            bp.save()
        self.stdout.write("\nSuccess.\n")




