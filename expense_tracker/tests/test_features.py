from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Expense
from django.contrib.auth.models import User
from datetime import date

class ExpenseFeatureTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.category = Category.objects.create(name='Transport')
        self.expense = Expense.objects.create(
            name='Bus Ticket',
            amount=100,
            category=self.category,
            date=date(2024, 5, 17),
            type=Expense.EXPENSE
        )

    def test_expense_list_accessible(self):
        self.client.force_login(self.user)
        url = reverse('expense-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Bus Ticket')

    def test_create_expense(self):
        self.client.force_login(self.user)
        url = reverse('expense-create')
        data = {
            'name': 'Metro',
            'amount': 80,
            'category': self.category.id,
            'date': '2024-05-18',
            'type': Expense.EXPENSE
        }
        resp = self.client.post(url, data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Expense.objects.filter(name='Metro').exists())

    def test_update_expense(self):
        self.client.force_login(self.user)
        url = reverse('expense-update', args=[self.expense.id])
        data = {
            'name': 'Bus Ticket',
            'amount': 150,
            'category': self.category.id,
            'date': '2024-05-17',
            'type': Expense.EXPENSE
        }
        resp = self.client.post(url, data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.expense.refresh_from_db()
        self.assertEqual(self.expense.amount, 150)

    def test_delete_expense(self):
        self.client.force_login(self.user)
        url = reverse('expense-delete', args=[self.expense.id])
        resp = self.client.post(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Expense.objects.filter(id=self.expense.id).exists())

    def test_stats_page_shows_charts(self):
        self.client.force_login(self.user)
        url = reverse('stats')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Analytics Charts')
        self.assertContains(resp, 'canvas')
