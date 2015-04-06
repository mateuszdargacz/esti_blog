# -*- coding: utf-8 -*-
from vishalUtech.blog.models import BlogCategoryParentRelation
from django.contrib.auth import get_user_model
from django.db.transaction import commit_on_success, atomic
from django.utils.encoding import smart_text
from mezzanine.blog.models import BlogPost, BlogCategory
from django.core.files.storage import default_storage

__author__ = 'mateusz'
__date__ = '16.12.14 / 09:36'
__git__ = 'https://github.com/mateuszdargacz'

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
import urllib
import random
from loremipsum import get_sentences, get_sentence


class Command(BaseCommand):
    help = 'Generates dummy blog posts, first arg is amount, deafault 100'
    image_url = 'http://lorempixel.com/664/374'
    users = get_user_model().objects.all()
    categories_amount = 4
    categories = []

    def generate_categories(self):
        categories = BlogCategory.objects.all()
        if categories.count() < self.categories_amount:
            for x in xrange(self.categories_amount - categories.count()):
                cat = BlogCategory.objects.create(title=''.join(get_sentences(1))[:15])
                cat.save()
                for x in xrange(random.randint(0, 6)):
                    nested = BlogCategory.objects.create(title=''.join(get_sentences(1))[:15])
                    relation, _ = BlogCategoryParentRelation.objects.get_or_create(parent=cat)
                    relation.children.add(nested)
        else:
            return categories
        return BlogCategory.objects.all()

    def get_category(self):
        if self.categories:
            return self.categories[random.randint(1, len(self.categories)-1)]

    def get_remote_image(self):
        result = urllib.urlretrieve(self.image_url)
        return File(open(result[0]))

    def get_user(self):
        return self.users[random.randint(0, len(self.users)-1)]

    @atomic
    def handle(self, *args, **options):
        amount = 1
        if len(args) > 0:
            try:
                amount = int(args[0])
            except TypeError:
                print 'Number of posts required'
        self.categories = self.generate_categories()

        for counter in xrange(amount):
            data = {
                'title': ''.join(get_sentences(1)),
                'content': ' '.join(get_sentences(random.randint(8, 16))).replace('.', ' ', 6),
                'user': self.get_user(),
            }
            post = BlogPost.objects.create(**data)
            filedata = self.get_remote_image()
            file_path = 'uploads/blog/%s.jpg' % filedata.name
            uploadedfile = default_storage.save(file_path, filedata)
            post.featured_image = file_path
            for x in xrange(random.randint(1, 3)):
                cat = self.get_category()
                if cat:
                    post.categories.add(cat)
            post.save()

