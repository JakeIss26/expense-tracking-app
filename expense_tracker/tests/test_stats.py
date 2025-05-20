from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Category, Expense
from datetime import date

class StatsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass12345')
        self.client.login(username='testuser', password='pass12345')

        cat = Category.objects.create(name='Misc')
        Expense.objects.create(
            name='TestExpense',
            amount=100,
            category=cat,
            date=date.today(),
            type='expense',
            user=self.user
        )
        Expense.objects.create(
            name='TestIncome',
            amount=400,
            category=cat,
            date=date.today(),
            type='income',
            user=self.user
        )

    def test_stats_view(self):
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('income_percent', response.context)
        self.assertIn('category_labels', response.context)
