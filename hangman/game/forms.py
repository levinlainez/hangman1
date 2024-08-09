from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=150)
    contrasena = forms.CharField(widget=forms.PasswordInput)
