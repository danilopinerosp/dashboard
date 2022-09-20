"""Production dashboard app."""
from django.apps import AppConfig


class ProductionDashboardConfig(AppConfig):
    """Production Dashboard Config class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "production_dashboard"
