from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to="images/")

class Article(models.Model):
    image = models.ImageField(upload_to="images/",null=False, blank=True)
    description = models.TextField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    removed = models.BooleanField(null=False)
    quantite = models.IntegerField(default=1)
    def __str__(self):
        return "{0}\n{1}".format(self.image, self.description)

class Demandeur(models.Model):
    username = models.CharField(max_length=250, unique=True, null=False, verbose_name="Nom d'utilisateur")
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class Demande(models.Model):
    demandeur = models.ForeignKey('Demandeur', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    articles = models.ManyToManyField(Article)
    

"""
class Product(models.Model):
    image = models.ImageField()
    description = models.TextField()
    removed = models.BooleanField()

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")
    
    def __str__(self):
           return self.nom
"""