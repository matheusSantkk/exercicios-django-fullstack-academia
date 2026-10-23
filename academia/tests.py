from django.test import TestCase

from .models import Aluno


class HomeViewTests(TestCase):
	def test_get_displays_registration_form(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertIn('form', response.context)
		self.assertFalse(response.context['form'].is_bound)

	def test_invalid_post_keeps_form_errors(self):
		response = self.client.post('/', {'nome': '', 'email': 'invalido'})

		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.context['form'].is_bound)
		self.assertIn('nome', response.context['form'].errors)
		self.assertIn('email', response.context['form'].errors)

	def test_valid_post_registers_student_and_redirects(self):
		response = self.client.post(
			'/',
			{
				'nome': 'Ana Silva',
				'email': 'ana@example.com',
				'telefone': '11999999999',
				'data_nascimento': '2000-01-01',
			},
		)

		self.assertRedirects(response, '/')
		self.assertTrue(Aluno.objects.filter(email='ana@example.com').exists())
