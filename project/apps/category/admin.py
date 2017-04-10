# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 06.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from mptt.admin import DraggableMPTTAdmin
from .models import *

admin.site.unregister(Group)
admin.site.register(Category, DraggableMPTTAdmin,
    list_display=('tree_actions', 'indented_title', 'title'),
)
