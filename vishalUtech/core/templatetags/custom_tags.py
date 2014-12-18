# -*- coding: utf-8 -*-
from mezzanine.core.templatetags.mezzanine_tags import admin_app_list
from mezzanine.utils.sites import current_site_id

from django.contrib.sites.models import Site

__author__ = 'mateusz, opel'
__date__ = '14.12.14 / 17:07'
__git__ = 'https://github.com/mateuszdargacz'

from mezzanine import template


register = template.Library()

@register.inclusion_tag("admin/includes/dropdown_menu.html",
                        takes_context=True)
def own_admin_dropdown_menu(context):
    """
    OVERWRITES admin_dropdown_menu at mezzanine/core/templatetags/
    Renders the app list for the admin dropdown menu navigation.
    solves site permissions problem with /admin/ when you
    are logged in as twitter user for example
    """
    context["dropdown_menu_app_list"] = admin_app_list(context["request"])
    user = context["request"].user
    sites = None
    if user.is_superuser:
        sites = Site.objects.all()
    else:
        try:
            sites = user.sitepermissions.get().sites.all()
        except:
            context["dropdown_menu_sites"] = []
            context["dropdown_menu_selected_site_id"] = current_site_id()
            return context
    context["dropdown_menu_sites"] = list(sites)
    context["dropdown_menu_selected_site_id"] = current_site_id()
    return context
