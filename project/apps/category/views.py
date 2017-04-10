# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.utils.encoding import force_bytes

"""
Created on 06.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from .models import Category
from django.core.cache import cache
from django.conf import settings
from django.template import Context, Template


def index(request):
    category_list = Category.objects.all()
    return render_to_response("index.html", {'nodes': category_list})


def category_page(request, category_id):
    current_category = get_object_or_404(Category, id=category_id)
    root_category_id = current_category.get_root().id
    category_list = get_list_or_404(Category)
    return render_to_response("list.html", {
        'nodes': category_list,
        'current_category': current_category,
        'root_category_id': root_category_id})






