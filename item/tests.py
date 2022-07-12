"""
Test case for todos item
"""
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from . import views


class SmokeTest(TestCase):
    """

    """

    def test_root_url_resolves_to_home_view(self):
        """
        Test the root url goes to the home_view
        """
        found = resolve('/')
        self.assertEquals(found.func, views.index)

    def test_home_view_return_correct_html(self):
        """
        Test the home view load the right html content
        """
        #request = HttpRequest()
        #response = views.index(request)
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('<title>Todos</title>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'index.html')
