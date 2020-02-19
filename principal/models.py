from django.db import models

class Article(models.Model):
    #image = models.ForeignKey('Image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=False)
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    removed = models.BooleanField(null=False)
    #quantite = models.IntegerField(default=1)
    demande = models.ForeignKey('Demande', related_name = "Articles", blank=True, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return "{0}\n{1}".format(self.image, self.description)

class Demandeur(models.Model):
    username = models.CharField(max_length=250, unique=True, null=False, verbose_name="Nom d'utilisateur")
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class Demande(models.Model):
    demandeur = models.ForeignKey('Demandeur', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    #articles = models.ForeignKey('Article', related_name = "Articles", on_delete=models.CASCADE)
    def __str__(self):
        return  "{0}\n{1}".format(self.date, self.demandeur.__str__()) 
