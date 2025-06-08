from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    """Категории расходов (еда, транспорт, развлечения и т. д.)"""
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Category Name")) 

    def __str__(self):
        return self.name

class Expense(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    
    TYPE_CHOICES = [
        (INCOME, _("Income")), 
        (EXPENSE, _("Expense")),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("Category"))
    date = models.DateField(verbose_name=_("Date"))
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, blank=False, verbose_name=_("Type"))

    def __str__(self):
        return f"{self.id}. {self.name} ({self.category}) — {self.amount} тг on date {self.date} - Type: {self.get_type_display()}"
