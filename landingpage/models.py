from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    whatsapp = models.CharField(max_length=15, verbose_name="Número do WhatsApp")

    def __str__(self):
        return self.nome
