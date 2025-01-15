from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'whatsapp')  # Exibe esses campos no admin
    search_fields = ('nome', 'email')  # Permite buscar por nome ou e-mail
