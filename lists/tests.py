from django.test import TestCase
from django.test import TestCase
from .views import home_page
from django.urls import resolve
# Create your tests here.
class SmokeTest(TestCase):
    # def test_bad_maths(self):
    #     self.assertEqual(1+1,3)
        
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #maps django urls
        self.assertEqual(found.func,home_page)