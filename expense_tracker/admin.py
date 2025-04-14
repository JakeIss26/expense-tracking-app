from django.contrib import admin
from .models import Category
from .models import Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
list_display = ('name') # Поля, которые будут отображаться в списке
 
search_fields = ('name') # Поиск по названию задачи
list_filter = ('name') # Фильтр по дате создания

@admin.register(Expense)
class CategoryAdmin(admin.ModelAdmin):
list_display = ('name', 'amount', 'category', 'date') # Поля, которые будут отображаться в списке
 
search_fields = ('name', 'amount', 'category', 'date') # Поиск по названию задачи
list_filter = ('name', 'amount', 'category', 'date') # Фильтр по дате создания
