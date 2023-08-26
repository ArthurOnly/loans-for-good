from django.db import models


# Create your models here.
class Question(models.Model):
    class QuestionTypeChoices(models.TextChoices):
        TEXT = "text", "Text"
        NUMBER = "number", "Number"
        SELECT = "select", "Select"
        DATE = "date", "Date"
        FILE = "file", "File"
        BOOLEAN = "boolean", "Boolean"

    label = models.CharField(max_length=255)
    required = models.BooleanField(default=False)
    type = models.CharField(max_length=255, choices=QuestionTypeChoices.choices)
    active = models.BooleanField(default=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ["ordering"]
        indexes = [
            models.Index(fields=["ordering"]),
        ]

    def __str__(self):
        return self.label

    @property
    def key(self):
        return self.label.lower().replace(" ", "_")


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.label

    @property
    def key(self):
        return self.label.lower().replace(" ", "_")


class LoanRequest(models.Model):
    class LoanStatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    status_external = models.CharField(
        max_length=255, choices=LoanStatusChoices.choices, default=LoanStatusChoices.PENDING
    )
    status_internal = models.CharField(
        max_length=255, choices=LoanStatusChoices.choices, default=LoanStatusChoices.PENDING
    )
    response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
