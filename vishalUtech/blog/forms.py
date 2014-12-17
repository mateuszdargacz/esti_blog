# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '17.12.14 / 10:25'
__git__ = 'https://github.com/mateuszdargacz'

from mezzanine.blog.models import BlogCategory

from django import forms


class NestedCategoryForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=BlogCategory.objects.filter(is_children__isnull=True), cache_choices=True,
                                    required=False, label="Parent category")
