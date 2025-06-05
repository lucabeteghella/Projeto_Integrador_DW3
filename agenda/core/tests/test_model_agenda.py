from django.test import TestCase
from core.models import Agenda

class AgendaModelTest(TestCase):
    def setUp(self):
        self.agenda = Agenda.objects.create(
            nome_completo="João da Silva",
            telefone="(19) 99999-8888",
            email="joao.silva@example.com",
            observacao="Cliente importante, prefere contato por e-mail."
        )

    def test_agenda_criada_com_sucesso(self):
        self.assertEqual(self.agenda.nome_completo, "João da Silva")
        self.assertEqual(self.agenda.telefone, "(19) 99999-8888")
        self.assertEqual(self.agenda.email, "joao.silva@example.com")
        self.assertEqual(self.agenda.observacao, "Cliente importante, prefere contato por e-mail.")

    def test_str_retorna_nome_e_email(self):
        self.assertEqual(str(self.agenda), "João da Silva - joao.silva@example.com")

    def test_observacao_limite_caracteres(self):
        observacao_max = 'A' * 100
        agenda = Agenda.objects.create(
            nome_completo="Maria Teste",
            telefone="(11) 91234-5678",
            email="maria@example.com",
            observacao=observacao_max
        )
        self.assertEqual(len(agenda.observacao), 100)

