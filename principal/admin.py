from django.contrib import admin

from .models import Article, Demandeur, Demande
"""
class DemandeAdmin(admin.ModelAdmin):
    list_filter = ('date', )
    search_fields = ('date', )
    date_hierarchy = 'date'
    ordering = ('date', )
"""
admin.site.register(Article)
admin.site.register(Demandeur)
#admin.site.register(Demande, DemandeAdmin)
admin.site.register(Demande)
