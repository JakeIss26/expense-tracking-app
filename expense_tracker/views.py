from django.shortcuts import render, redirect
from .models import Category, Expense
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .forms import ExpenseForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, UpdateProfileForm
from rest_framework import viewsets
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all() 
    serializer_class = ExpenseSerializer

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense-list')

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense-list')

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'
    success_url = reverse_lazy('expense-list')

@login_required
def home(request):
    data = Expense.objects.all()
    return render(request, 'home.html', {'data': data})
    
def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expense-list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})
