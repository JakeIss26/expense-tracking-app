from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ..models import Category, Expense
from datetime import date

class ExpenseAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apitester', password='pass456')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.cat = Category.objects.create(name='API Category')

        Expense.objects.create(
            name='API Expense',
            amount=50,
            category=self.cat,
            date=date.today(),
            type='expense',
            user=self.user  # ВАЖНО
        )

    def test_api_list(self):
        resp = self.client.get('/api/expenses/')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(isinstance(data, list))
        self.assertGreaterEqual(len(data), 1)
