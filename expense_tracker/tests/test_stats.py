from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Category, Expense
from datetime import date

class StatsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass12345')
        self.client = Client()
        self.client.login(username='testuser', password='pass12345')
        cat = Category.objects.create(name='Misc')
        Expense.objects.create(
            name='TestExpense',
            amount=100,
            category=cat,
            date=date.today(),
            type='expense'
        )
        Expense.objects.create(
            name='TestIncome',
            amount=400,
            category=cat,
            date=date.today(),
            type='income'
        )

    def test_stats_view(self):
        resp = self.client.get(reverse('stats'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('income_percent', resp.context)
        self.assertIn('category_labels', resp.context)
