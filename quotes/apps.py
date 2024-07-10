from django.apps import AppConfig
import utils.add_quotes_to_mongo


class QuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotes'
