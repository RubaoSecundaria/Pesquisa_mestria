from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'recomendacao', 'data_criacao')
    list_filter = ('recomendacao',)
    search_fields = ('nome', 'comentarios')
    readonly_fields = ('data_criacao',)
    date_hierarchy = 'data_criacao'
