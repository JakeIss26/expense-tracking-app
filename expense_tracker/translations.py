from modeltranslation.translator import register, TranslationOptions
from .models import Category, Expense

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Expense)
class ExpenseTranslationOptions(TranslationOptions):
    fields = ('name', 'type',)