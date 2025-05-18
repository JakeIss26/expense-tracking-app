from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass12345')
        self.client = Client()

    def test_login(self):
        resp = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'pass12345'}, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        self.client.login(username='testuser', password='pass12345')
        resp = self.client.post(reverse('logout'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='testuser', password='pass12345')
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)
