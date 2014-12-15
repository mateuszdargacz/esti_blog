import random
from mezzanine.blog.models import BlogPost

__author__ = 'opel'

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = ("Updates views counter"
            )
    def handle(self, *apps, **options):
        blog_posts = BlogPost.objects.all()
        for bp in blog_posts:
            current = bp.views_count
            delta = bp.views_count_delta
            if delta==0:
                delta = bp.views_count
            before = current - delta

            print current,delta,'(',before,')'

            bp.views_count_delta = current - before
            bp.save()
        self.stdout.write("\nDone.\n" )




