from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.db.models.deletion import ProtectedError
from django.test import TestCase

from .admin import ModalidadeAdmin, TurmaAdmin
from .models import Modalidade, Turma


class AcademiaPagesTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.musculacao = Modalidade.objects.create(
			nome='Musculação',
			descricao='Treino com pesos, acompanhamento individual',
		)
		cls.pilates = Modalidade.objects.create(
			nome='Pilates', descricao='Solo e aparelhos, turmas pequenas'
		)
		cls.funcional = Modalidade.objects.create(
			nome='Funcional', descricao='Circuito de alta intensidade'
		)
		cls.natacao = Modalidade.objects.create(
			nome='Natação', descricao='Piscina aquecida (em reforma)', ativa=False
		)
		Turma.objects.bulk_create([
			Turma(modalidade=cls.pilates, dia_semana='SEGUNDA', horario='07:30', instrutor='Rafael', vagas=8),
			Turma(modalidade=cls.musculacao, dia_semana='SEGUNDA', horario='19:00', instrutor='Carla', vagas=15),
			Turma(modalidade=cls.funcional, dia_semana='TERCA', horario='06:30', instrutor='Diego', vagas=12),
			Turma(modalidade=cls.musculacao, dia_semana='TERCA', horario='18:00', instrutor='Carla', vagas=15),
			Turma(modalidade=cls.pilates, dia_semana='QUARTA', horario='07:30', instrutor='Rafael', vagas=8),
			Turma(modalidade=cls.funcional, dia_semana='SABADO', horario='09:00', instrutor='Diego', vagas=20),
		])

	def test_home_shows_active_modalities_and_contact_placeholders(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Musculação')
		self.assertContains(response, 'Pilates')
		self.assertContains(response, 'Funcional')
		self.assertNotContains(response, 'Natação')
		self.assertContains(response, 'Endereço da academia')
		self.assertContains(response, 'Telefone da academia')
		self.assertContains(response, '/turmas/')

	def test_schedule_is_available_and_in_weekday_order(self):
		response = self.client.get('/turmas/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['turmas'].count(), 6)
		actual = [
			(turma.dia_semana, turma.horario.strftime('%H:%M'))
			for turma in response.context['turmas']
		]
		self.assertEqual(actual, [
			('SEGUNDA', '07:30'),
			('SEGUNDA', '19:00'),
			('TERCA', '06:30'),
			('TERCA', '18:00'),
			('QUARTA', '07:30'),
			('SABADO', '09:00'),
		])
		self.assertContains(response, 'Início')

	def test_modality_with_classes_cannot_be_deleted(self):
		with self.assertRaises(ProtectedError):
			Modalidade.objects.filter(pk=self.musculacao.pk).delete()


class AdminConfigurationTests(TestCase):
	def test_admin_lists_and_filters_match_requirements(self):
		modalidade_admin = ModalidadeAdmin(Modalidade, AdminSite())
		turma_admin = TurmaAdmin(Turma, AdminSite())

		self.assertEqual(modalidade_admin.list_display, ('nome', 'ativa'))
		self.assertEqual(modalidade_admin.list_filter, ('ativa',))
		self.assertEqual(
			turma_admin.list_display,
			('modalidade', 'dia_semana', 'horario', 'instrutor', 'vagas'),
		)
		self.assertEqual(turma_admin.list_filter, ('modalidade', 'dia_semana'))
		self.assertEqual(turma_admin.search_fields, ('instrutor',))

	def test_admin_search_and_filters_find_expected_classes(self):
		modalidades = {
			nome: Modalidade.objects.create(nome=nome)
			for nome in ('Pilates', 'Musculação', 'Funcional')
		}
		Turma.objects.bulk_create([
			Turma(modalidade=modalidades['Pilates'], dia_semana='SEGUNDA', horario='07:30', instrutor='Rafael', vagas=8),
			Turma(modalidade=modalidades['Musculação'], dia_semana='SEGUNDA', horario='19:00', instrutor='Carla', vagas=15),
			Turma(modalidade=modalidades['Funcional'], dia_semana='TERCA', horario='06:30', instrutor='Diego', vagas=12),
			Turma(modalidade=modalidades['Musculação'], dia_semana='TERCA', horario='18:00', instrutor='Carla', vagas=15),
		])
		user = get_user_model().objects.create_superuser(
			username='admin', email='admin@example.com', password='test-password'
		)
		self.client.force_login(user)

		search_response = self.client.get('/admin/academia/turma/', {'q': 'Carla'})
		self.assertEqual(search_response.status_code, 200)
		self.assertEqual(search_response.context['cl'].result_count, 2)

		filtered_response = self.client.get(
			'/admin/academia/turma/',
			{
				'modalidade__id__exact': modalidades['Musculação'].pk,
				'dia_semana__exact': 'TERCA',
			},
		)
		self.assertEqual(filtered_response.status_code, 200)
		self.assertEqual(filtered_response.context['cl'].result_count, 1)
