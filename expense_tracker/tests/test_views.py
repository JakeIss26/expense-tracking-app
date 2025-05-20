from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Category, Expense
from datetime import date


class ExpenseViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass12345')
        self.client.login(username='testuser', password='pass12345')

        self.cat = Category.objects.create(name='Food')
        self.expense = Expense.objects.create(
            name='Lunch',
            amount=100,
            category=self.cat,
            date=date.today(),
            type='expense',
            user=self.user  # ДОБАВЬ ЭТО!
        )

    def test_expense_list_view(self):
        resp = self.client.get(reverse('expense-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Lunch')

    def test_expense_create_view_get(self):
        resp = self.client.get(reverse('expense-create'))
        self.assertEqual(resp.status_code, 200)

    def test_expense_create_view_post(self):
        data = {
            'name': 'Dinner',
            'amount': 200,
            'category': self.cat.id,
            'date': date.today(),
            'type': 'expense'
        }
        resp = self.client.post(reverse('expense-create'), data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Expense.objects.filter(name='Dinner', user=self.user).exists())

    def test_expense_update_view(self):
        url = reverse('expense-update', args=[self.expense.id])
        data = {
            'name': 'Breakfast',
            'amount': 50,
            'category': self.cat.id,
            'date': date.today(),
            'type': 'expense'
        }
        resp = self.client.post(url, data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.expense.refresh_from_db()
        self.assertEqual(self.expense.name, 'Breakfast')

    def test_expense_delete_view(self):
        url = reverse('expense-delete', args=[self.expense.id])
        resp = self.client.post(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Expense.objects.filter(id=self.expense.id).exists())