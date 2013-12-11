from django.test import TestCase
from pages.models import Page

# Create your tests here.
class PageTests(TestCase):
    def test_page_creation(self):
        page1st = Page(name = '1st', header = 'First header')
        page2nd = Page(name = '2nd', header = 'Second header')
        self.assertEqual(page1st.name, '1st' )
        self.assertEqual(page2nd.name, '2nd')
