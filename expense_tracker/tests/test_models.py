from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Expense
from datetime import date

class CategoryModelTest(TestCase):
    def test_category_str(self):
        cat = Category.objects.create(name='Food')
        self.assertEqual(str(cat), 'Food')

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        self.cat = Category.objects.create(name='Sport')

    def test_expense_str(self):
        expense = Expense.objects.create(
            name='Football',
            amount=123,
            category=self.cat,
            date=date.today(),
            type='expense',
            user=self.user
        )
        s = str(expense)
        self.assertIn('Football', s)
        self.assertIn('Sport', s)
        self.assertIn('Expense', s)

    def test_expense_type_choices(self):
        expense = Expense.objects.create(
            name='Game',
            amount=100,
            category=self.cat,
            date=date.today(),
            type='income',
            user=self.user
        )
        self.assertIn(expense.type, dict(Expense.TYPE_CHOICES))
