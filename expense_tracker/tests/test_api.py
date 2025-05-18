from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Category, Expense
from datetime import date

class ExpenseAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass12345')
        self.client = Client()
        self.client.login(username='testuser', password='pass12345')
        cat = Category.objects.create(name='ApiCat')
        Expense.objects.create(
            name='ApiTest',
            amount=333,
            category=cat,
            date=date.today(),
            type='expense'
        )

    def test_api_list(self):
        resp = self.client.get('/api/expenses/')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(isinstance(data, list))
        self.assertGreaterEqual(len(data), 1)
