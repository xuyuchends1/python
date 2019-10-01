"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from django.urls import resolve
#from django.views import home_page 

# TODO: Configure your database in settings.py and sync before running tests.

class HoePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve("/")
        self.assertEqual(found.func,home_page)

if __name__=='__main__':
    HoePageTest.test_root_url_resolve_to_home_page_view()