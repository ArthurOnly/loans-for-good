"""
This module has the tasks of the loans app.
"""

from celery import shared_task

from apps.loans.integrations import CreditApiFacade
from apps.loans.models import LoanRequest


@shared_task
def credit_analysis_task(questionary_id, data):
    """
    This task is responsible for sending the data to the credit analysis API
    and updating the status of the loan request.
    """
    questionary = LoanRequest.objects.get(id=questionary_id)
    approved = CreditApiFacade().verify_credit(data)
    if approved:
        questionary.status_external = LoanRequest.LoanStatusChoices.APPROVED
    else:
        questionary.status_external = LoanRequest.LoanStatusChoices.REJECTED
        questionary.status_internal = LoanRequest.LoanStatusChoices.REJECTED
    questionary.save()
    return questionary.status_external
