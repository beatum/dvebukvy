# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction

"""
Created on 06.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

import os, io, json
from project.settings import BASE_DIR
from datetime import datetime
from django.core.management.base import BaseCommand
from project.apps.category.models import Category

f = os.path.join(BASE_DIR, 'items.json')

"""
Plan:
a = Category.objects.create(category_title="4") count=100
b = Category.objects.create(category_title="4.1", parent=a) count=100
c = Category.objects.create(category_title="4.1", parent=b) count=500
d = Category.objects.create(category_title="4.1", parent=c) count=300
"""


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        self.make_category()

    def make_category(self):
        start = datetime.now()
        print("Star: %s" % start)
        try:
            with io.open(f) as json_data:
                data = json.load(json_data)
                for index, item in enumerate(data):
                    if index <= 100:
                        print('L1', index, '>= 100')
                        with transaction.atomic():
                            Category.objects.create(
                                category_title=str(index),
                                title=item['title'][0],
                                description=item['text'][0])
                    elif index >= 100 and index <= 200:
                        print('L2', '>= 100', index, '<= 200')
                        parent = Category.objects.get(category_title='0')
                        with transaction.atomic():
                            Category.objects.create(
                                parent=parent,
                                category_title=index,
                                title=item['title'][0],
                                description=item['text'][0])
                    elif index >= 200 and index <= 500:
                        print('L3', '>= 200', index, '<= 500')
                        parent = Category.objects.get(category_title='101')
                        with transaction.atomic():
                            Category.objects.create(
                                parent=parent,
                                category_title=index,
                                title=item['title'][0],
                                description=item['text'][0])
                    elif index >= 500 and index <= 1000:
                        print('L4', '>= 500', index, '<= 1000')
                        parent = Category.objects.get(category_title='301')
                        with transaction.atomic():
                            Category.objects.create(
                                parent=parent,
                                category_title=index,
                                title=item['title'][0],
                                description=item['text'][0])
                    else:
                        break
                json_data.close()
                print("End: %s" % (datetime.now()))
        except Exception as e:
            print(e)



