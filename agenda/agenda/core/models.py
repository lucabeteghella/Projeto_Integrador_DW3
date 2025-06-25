from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o admin dono do contato
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    observacao = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.nome_completo} - {self.email}"
