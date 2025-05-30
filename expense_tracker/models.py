from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Категории расходов (еда, транспорт, развлечения и т. д.)"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, blank=False)

    def __str__(self):
        return f"{self.id}. {self.name} ({self.category}) — {self.amount}т on date {self.date} - Type: {self.get_type_display()}"
