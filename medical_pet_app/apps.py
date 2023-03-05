from django.apps import AppConfig


class MedicalPetAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medical_pet_app'
    def ready(self):
        import medical_pet_app.signals