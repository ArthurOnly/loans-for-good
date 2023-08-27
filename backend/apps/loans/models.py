from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    class QuestionTypeChoices(models.TextChoices):
        TEXT = "text", _("Text")
        NUMBER = "number", _("Number")
        SELECT = "select", _("Select")
        DATE = "date", _("Date")
        FILE = "file", _("File")
        BOOLEAN = "boolean", _("Boolean")

    label = models.CharField(_("Label"), max_length=255)
    key = models.CharField(_("Key"), max_length=255)
    required = models.BooleanField(_("Required"), default=False)
    type = models.CharField(_("Type"), max_length=255, choices=QuestionTypeChoices.choices)
    active = models.BooleanField(_("Active"), default=True)
    ordering = models.IntegerField(_("Ordering"), default=0)

    class Meta:
        ordering = ["ordering"]
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        indexes = [
            models.Index(fields=["ordering"]),
        ]

    def __str__(self):
        return self.label

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(_("Label"), max_length=255)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Question Option")
        verbose_name_plural = _("Question Options")

    def __str__(self):
        return self.label

    @property
    def key(self):
        return self.label.lower().replace(" ", "_")

class LoanRequestQuestionResponse(models.Model):
    question_label = models.CharField(_("Question Label"), max_length=255)
    question_key = models.CharField(_("Question Key"), max_length=255)
    value = models.CharField(_("Value"), max_length=255)
    file = models.FileField(_("File"), upload_to="apps/loans/storage/loan_request_question_response", null=True, blank=True)
    loan_request = models.ForeignKey("LoanRequest", on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Loan Request Question Response")
        verbose_name_plural = _("Loan Request Question Responses")

    def __str__(self):
        return _("{question_label}: {value}").format(
            question_label=self.question_label, value=self.value
        )
    
    # @property
    # def file_link(self):
    #     if self.file:
    #         return format_html("<a href='%s'>download</a>" % (self.file.url,))
    #     else:
    #         return "No attachment"

class LoanRequest(models.Model):
    class LoanStatusChoices(models.TextChoices):
        PENDING = "pending", _("Pending")
        APPROVED = "approved", _("Approved")
        REJECTED = "rejected", _("Rejected")

    status_external = models.CharField(
        _("External Status"), max_length=255, choices=LoanStatusChoices.choices, default=LoanStatusChoices.PENDING
    )
    status_internal = models.CharField(
        _("Internal Status"), max_length=255, choices=LoanStatusChoices.choices, default=LoanStatusChoices.PENDING
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Loan Request")
        verbose_name_plural = _("Loan Requests")

    def __str__(self):
        return str(self.id)
