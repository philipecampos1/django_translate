from django.apps import AppConfig


class TraducoesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traducoes'

    def ready(self):
        import traducoes.signals
