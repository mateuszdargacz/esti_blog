
__author__ = 'opel'

from copy import deepcopy
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost, BlogCategory

from django.contrib import admin
from django.conf import settings

from vishalUtech.blog.forms import NestedCategoryForm
from vishalUtech.blog.models import BlogCategoryParentRelation


blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"] += (u"views_count",)
blog_fieldsets[0][1]["fields"] += (u"views_count_delta",)


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets


class BlogCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for blog categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    form = NestedCategoryForm

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        Save related instance of
        """
        obj.save()
        parent_id = form.cleaned_data.get('parent')
        if parent_id:
            relation, _ = BlogCategoryParentRelation.objects.get_or_create(parent=parent_id)
            relation.children.add(obj)
            print 'CLEANED', relation.children


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)

admin.site.unregister(BlogCategory)
admin.site.register(BlogCategory, BlogCategoryAdmin)
