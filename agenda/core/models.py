from django.db import models

class Agenda(models.Model):
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    observacao = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.nome_completo} - {self.email}"
