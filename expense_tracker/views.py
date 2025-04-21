from django.shortcuts import render
from .models import Category, Expense

def home(request):
    data = Expense.objects.all()
    return render(request, 'home.html', {'data': data})
    
def about(request):
    return render(request, 'about.html')

