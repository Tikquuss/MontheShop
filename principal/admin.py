from django.contrib import admin

from .models import Image, Article, Demandeur, Demande
"""
class ArticleAdmin(admin.ModelAdmin):
    image = models.ImageField(upload_to="images/",null=False, blank=True)
    description = models.TextField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    removed = models.BooleanField(null=False)
    quantite = models.IntegerField(default=1)

    list_filter = ('date', )
    #Il devra être possible de rechercher des redirections depuis la longue URL via une barre de recherche
    search_fields = ('date', )
    #tous les champs devront être affichés dans une catégorie
    list_display = ('demandeur', 'date', 'article')
    #le tri par défaut sera fait selon la date de création du raccourci.
    date_hierarchy = 'date'
    ordering = ('date', )
"""
class DemandeAdmin(admin.ModelAdmin):
    list_filter = ('date', )
    #Il devra être possible de rechercher des redirections depuis la longue URL via une barre de recherche
    search_fields = ('date', )
    #tous les champs devront être affichés dans une catégorie
    #list_display = ('demandeur', 'date', 'article')
    #le tri par défaut sera fait selon la date de création du raccourci.
    date_hierarchy = 'date'
    ordering = ('date', )

admin.site.register(Image)
admin.site.register(Article)
admin.site.register(Demandeur)
admin.site.register(Demande, DemandeAdmin)
