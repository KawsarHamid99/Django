from django.apps import AppConfig


class FirstsignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "firstsignals"

    def ready(self):
        import firstsignals.signals
