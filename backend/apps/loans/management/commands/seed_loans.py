from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.loans.models import Question, QuestionOption


class Command(BaseCommand):
    help = "Importa dados iniciais (dev only)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Importando dados iniciais...", ending="\r")

        with transaction.atomic():
            self._create_user()
            self._create_questions()

        self.stdout.write("Importação concluída!    ")

    def _create_user(self):
        usermodel = get_user_model()
        usermodel.objects.create_superuser(
            username="admin",
            email="admin@mail.com",
            password="admin",
        )

    def _create_questions(self):
        Question.objects.get_or_create(
            label="Nome",
            defaults={
                "key": "name",
                "required": True,
                "type": Question.QuestionTypeChoices.TEXT,
                "active": True,
                "ordering": 0,
            },
        )

        Question.objects.get_or_create(
            label="CPF",
            defaults={
                "key": "document",
                "required": True,
                "type": Question.QuestionTypeChoices.TEXT,
                "active": True,
                "ordering": 1,
            },
        )

        Question.objects.get_or_create(
            label="Foto da identidade",
            defaults={
                "key": "document_photo",
                "required": True,
                "type": Question.QuestionTypeChoices.FILE,
                "active": True,
                "ordering": 2,
            },
        )

        question, created = Question.objects.get_or_create(
            label="Como você conheceu a plataforma",
            defaults={
                "key": "how_did_you_meet_us",
                "required": True,
                "type": Question.QuestionTypeChoices.SELECT,
                "active": True,
                "ordering": 3,
            },
        )
        QuestionOption.objects.get_or_create(
            question=question,
            label="Google",
        )
        QuestionOption.objects.get_or_create(
            question=question,
            label="Facebook",
        )
        QuestionOption.objects.get_or_create(
            question=question,
            label="LinkedIn",
        )
