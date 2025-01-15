from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'whatsapp']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu WhatsApp'}),
        }
