# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 06.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.db import models
from django.core.cache import cache
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    category_title = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['category_title']

    def __str__(self):
        return self.category_title

    def __unicode__(self):
        return u'%s' % self.category_title

    def delete(self, *args, **kwargs):
        # simple way...
        cache.clear()
        super(MPTTModel, self).delete(*args, **kwargs)

