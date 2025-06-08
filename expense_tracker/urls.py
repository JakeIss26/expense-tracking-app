from django.urls import path, include
from . import views
from .views import ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, register, profile, edit_profile, StatsView
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter 
from .views import ExpenseViewSet
from django.conf.urls.i18n import set_language

router = DefaultRouter() 
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('about/', views.about, name='about'),
    path('', ExpenseListView.as_view(), name='expense-list'),
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('i18n/setlang/', set_language, name='set_language'),
]
