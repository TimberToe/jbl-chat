from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class UserApiTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.malin = User.objects.create(username="Malin")
        cls.fredrika = User.objects.create(username="Fredrika")
        cls.client = APIClient()
        cls.user_url = reverse("user-list")

    def test_lists_all_users_except_self(self):
        self.client.force_authenticate(user=self.malin)

        response = self.client.get(self.user_url)

        self.assertNotContains(
            response, text=self.malin.username, status_code=status.HTTP_200_OK
        )
        self.assertContains(
            response, text=self.fredrika.username, status_code=status.HTTP_200_OK
        )
