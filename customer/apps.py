from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'


    # override ready() for signals
    def ready(self):
        import customer.signals
