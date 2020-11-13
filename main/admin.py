from django.contrib import admin
from .models import Resume, Vacancy, Questions


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'position', 'contacts', 'money', 'experience', 'education', 'skills',
                    'info', 'portfolio_url', 'status')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'position', 'company_name', 'what_do', 'requirements', 'conditions', 'money',
                    'contacts', 'rubric', 'position2', 'status')


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'question', 'answer')
