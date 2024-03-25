from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import json

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_successful(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('token', content)
        self.assertIn('expiration_time', content)
        self.assertIn('user', content)

    def test_invalid_credentials(self):
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertIn('error', content)
