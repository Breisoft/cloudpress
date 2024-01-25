from django.test import TestCase

from rest_framework import status


from .models import Category

# Create your tests here.

from rest_framework.test import APIClient, APITestCase

import pprint


class CategoryViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')
        self.detail_url = '/api/categories/1/'  # Adjust the URL as per your routing
        self.list_url = '/api/categories/'

    def test_list_categories_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming 2 categories

        pp = pprint.PrettyPrinter(width=80)

        pp.pprint(response.data)

    def test_read_category_detail_unauthenticated(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Category 1')  # Check details
