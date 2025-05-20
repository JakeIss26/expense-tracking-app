from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .forms import ExpenseForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from .forms import RegisterForm, UpdateProfileForm
from rest_framework import viewsets
from .serializers import ExpenseSerializer
from .tasks import send_welcome_email
from django.views import View
from django.db.models import Sum


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense-list')

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'
    success_url = reverse_lazy('expense-list')

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(f"Sending welcome email to: {user.email}")
            send_welcome_email.apply_async(args=[user.email])
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

@method_decorator(login_required, name='dispatch')
class StatsView(View):
    def get(self, request):
        income_total = Expense.objects.filter(user=request.user, type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense_total = Expense.objects.filter(user=request.user, type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        total = income_total + expense_total
        if total > 0:
            income_percent = round(income_total / total * 100, 2)
            expense_percent = round(expense_total / total * 100, 2)
        else:
            income_percent = expense_percent = 0

        expense_labels, expense_values = self.get_category_chart_data(request, 'expense')
        income_labels, income_values = self.get_category_chart_data(request, 'income')

        context = {
            'income_percent': income_percent,
            'expense_percent': expense_percent,
            'income_total': income_total,
            'expense_total': expense_total,
            'category_labels': expense_labels,
            'category_values': expense_values,
            'income_cat_labels': income_labels,
            'income_cat_values': income_values
        }
        return render(request, 'stats.html', context)

    def get_category_chart_data(self, request, type_):
        data = (
            Expense.objects
            .filter(user=request.user, type=type_)
            .values('category__name')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )
        labels = [item['category__name'] for item in data]
        values = [float(item['total'] or 0) for item in data]
        return labels, values