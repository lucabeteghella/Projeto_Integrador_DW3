from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from core.models import Agenda
import re

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        labels = {
            'email': 'E-Mail:',
            'password': 'Senha:',
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu e-mail institucional'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }),
        }
        error_messages = {
            'email': {
                'required': "Informe o e-mail.",
            },
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@fatec.sp.gov.br'):
            raise ValidationError('Informe seu e-mail institucional.')
        return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise ValidationError("Usuário com esse e-mail não encontrado.")

            user = authenticate(username=user.username, password=password)
            if user is None:
                raise ValidationError("Senha incorreta para o e-mail informado.")

            self.user = user


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['nome_completo', 'email', 'telefone', 'observacao']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observação',
                'rows': 3,
                'style': 'resize: vertical; border-radius: 8px;',
            }),
        }

    def clean_nome_completo(self):
        nome = self.cleaned_data.get('nome_completo')
        if not nome:
            raise forms.ValidationError('Este campo é obrigatório.')
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome):
            raise forms.ValidationError('O nome deve conter apenas letras e espaços.')
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            numeros = re.sub(r'\D', '', telefone)
            if not numeros:
                raise forms.ValidationError("O telefone deve conter ao menos um número.")
            if len(numeros) < 8:
                raise forms.ValidationError("O telefone parece estar incompleto.")
            return numeros
        raise forms.ValidationError("Este campo é obrigatório.")
