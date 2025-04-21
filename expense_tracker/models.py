from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Категории расходов (еда, транспорт, развлечения и т. д.)"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.id}. {self.name} ({self.category}) — {self.amount}₽ on date {self.date}"
