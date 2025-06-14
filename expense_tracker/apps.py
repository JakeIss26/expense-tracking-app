from django.apps import AppConfig


class ExpenseTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense_tracker'

    def ready(self):
        import expense_tracker.translations
