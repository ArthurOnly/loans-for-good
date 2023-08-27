from apps.loans.models import LoanRequest, LoanRequestQuestionResponse
from apps.loans.tasks import credit_analysis_task
from django.db import transaction


def create_loan_request(data):
    questions = data.get("response")

    with transaction.atomic():
        loan_request = LoanRequest.objects.create()

        question_responses = [
            LoanRequestQuestionResponse(loan_request=loan_request, **question_data)
            for question_data in questions
        ]
        LoanRequestQuestionResponse.objects.bulk_create(question_responses)

        responses_dict = {question.question_key: question.value for question in question_responses}

        credit_analysis_task.delay(loan_request.id, responses_dict)

    return loan_request
