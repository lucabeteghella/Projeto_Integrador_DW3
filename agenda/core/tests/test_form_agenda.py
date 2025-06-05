from django.test import TestCase
from core.forms import AgendaForm

class AgendaFormTest(TestCase):

    def setUp(self):
        self.valid_data = {
            'nome_completo': 'Maria Souza',
            'email': 'maria.souza@example.com',
            'telefone': '(19) 98888-7777',
            'observacao': 'Cliente frequente.'
        }

    def test_form_fields(self):
        form = AgendaForm()
        expected_fields = ['nome_completo', 'email', 'telefone', 'observacao']
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_valid_form(self):
        form = AgendaForm(data=self.valid_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_nome_completo_required(self):
        data = self.valid_data.copy()
        data['nome_completo'] = ''
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome_completo', form.errors)

    def test_email_required(self):
        data = self.valid_data.copy()
        data['email'] = ''
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_telefone_required(self):
        data = self.valid_data.copy()
        data['telefone'] = ''
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('telefone', form.errors)

    def test_observacao_max_length(self):
        data = self.valid_data.copy()
        data['observacao'] = 'x' * 101
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('observacao', form.errors)
