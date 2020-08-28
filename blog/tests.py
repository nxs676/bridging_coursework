from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from blog.views import cv


class CVTest(TestCase):

    def test_cv_returns_correct_html(self):
        response = self.client.get('/cv.html')
        self.assertTemplateUsed(response, 'blog/cv.html')
