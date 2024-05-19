from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from ..models import Goal


class InegrationTest(APITestCase):
    def test_create_goal(self):
        url = reverse("goals")
        data = {
                    "name": "skola",
                    "description": "mit dobre znamky"
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Goal.objects.count, 1)
