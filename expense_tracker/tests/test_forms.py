from django.test import TestCase
from ..forms import ExpenseForm, RegisterForm
from ..models import Category
from datetime import date

class ExpenseFormTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='Other')

    def test_expense_form_valid(self):
        form = ExpenseForm(data={
            'name': 'TestExpense',
            'amount': 100,
            'category': self.cat.id,
            'date': date.today(),
            'type': 'expense'
        })
        self.assertTrue(form.is_valid())

class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form = RegisterForm(data={
            'username': 'user2',
            'email': 'user2@example.com',
            'password1': 'strong_password1',
            'password2': 'strong_password1',
        })
        self.assertTrue(form.is_valid())
