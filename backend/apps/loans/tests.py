from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.loans.models import LoanRequest, LoanRequestQuestionResponse, Question


class QuestionViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client
        self.question = Question.objects.create(label="Test Question", active=True)

    def test_get_questions(self):
        url = reverse("questions-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_question_detail(self):
        url = reverse("questions-detail", kwargs={"pk": self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LoanRequestViewSetTestCase(TestCase):
    def setUp(self):
        usermodel = get_user_model()
        self.client = APIClient()
        self.admin_user = usermodel.objects.create_superuser(username="admin", password="admin123")
        self.client.force_authenticate(user=self.admin_user)
        self.loan_request = LoanRequest.objects.create()
        LoanRequestQuestionResponse.objects.create(
            loan_request=self.loan_request,
            question_label="Test Question",
            question_key="test_key",
            value="Test Value",
        )

    def test_get_loan_requests(self):
        url = reverse("loan-requests-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_loan_request_detail(self):
        url = reverse("loan-requests-detail", kwargs={"pk": self.loan_request.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_loan_request(self):
        url = reverse("loan-requests-list")
        data = {
            "response.0.question_label": "Test Question",
            "response.0.question_key": "test_key",
            "response.0.value": "Test Value",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_loan_request_unauthenticated(self):
        url = reverse("loan-requests-list")
        self.client.force_authenticate(user=None)
        data = {
            "response.0.question_label": "Test Question 2",
            "response.0.question_key": "test_key 2",
            "response.0.value": "Test Value 2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Should add more tests
