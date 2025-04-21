from django.contrib import admin
from .models import Category
from .models import Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'category', 'date')
    search_fields = ('name', 'amount', 'category__name', 'date')
    list_filter = ('name', 'amount', 'category', 'date')