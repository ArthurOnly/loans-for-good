from django.contrib import admin
from django.http.request import HttpRequest

from apps.loans.models import (
    LoanRequest,
    LoanRequestQuestionResponse,
    Question,
    QuestionOption,
)


# Register your models here.
class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 0


class LoanRequestQuestionResponseInline(admin.TabularInline):
    model = LoanRequestQuestionResponse
    extra = 0
    readonly_fields = ("question_label", "value", "file")
    can_delete = False
    exclude = ("question_key",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("label", "type", "required", "active", "ordering")
    list_filter = ("type", "required", "active")
    search_fields = ("label",)
    inlines = [QuestionOptionInline]


@admin.register(LoanRequest)
class LoanRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "status_external", "status_internal", "created_at")
    list_filter = ("status_external", "status_internal")
    search_fields = ("id",)
    readonly_fields = ("status_external", "created_at")
    inlines = [LoanRequestQuestionResponseInline]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
