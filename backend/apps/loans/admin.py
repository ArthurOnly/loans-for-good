from apps.loans.models import LoanRequest, Question, QuestionOption
from django.contrib import admin


# Register your models here.
class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 0


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
