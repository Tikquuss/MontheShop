from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Demandeur, Demande, Article

import json
from django.db.models import Q
import operator
from functools import reduce

headers_links = {
    'facebook_link' : "https://recharge.orange.cm/",
    'twitter_link' : "https://recharge.orange.cm/",
    'linkedin_link' : "https://recharge.orange.cm/",
    'skype_link' : "https://recharge.orange.cm/",
    'dribbble_link' : "https://recharge.orange.cm/"
}

currentDemandeur = None
list_article = []

# marche
def home(request, articles__ = None, isinscrit=None, isconnect=None, homeMessage = 'Aucun produit disponnible', pannier = False):
    global currentDemandeur, headers_links
    articles = articles__
    if articles == None :
        articles = Article.objects.filter(removed = False)
    locals_data = headers_links
    locals_data["articles"] = enumerate(articles)
    locals_data["troplong"] = False if len(articles) <= 3 else True
    locals_data["message"] = None if len(articles) != 0 else homeMessage
    locals_data['currentDemandeur'] = currentDemandeur
    locals_data['pannier'] = pannier
    if isinscrit != None :
        locals_data['inscrit'] = isinscrit
    if isconnect != None :
        locals_data['connect'] = isconnect
    if isinscrit == None : 
        if currentDemandeur :
            locals_data['currentDemandeur'] = currentDemandeur
            locals_data['inscrit'] = True
    print('locals_data______________________________',locals_data)
    return render(request, 'principal/index.html', locals_data)

def log(request):
    global currentDemandeur
    post = request.POST
    print('post_______________________', post)
    username = post.get('username')
    password = post.get('password')
    print(username, password)
    #errorMessage = isCorrect(username, password)
    #if errorMessage :
    #    return modal(request, errorMessage)
    
    # todo : verifier si les infos sont correctes
    try :
        demandeur = Demandeur.objects.get(username=username)
        print(demandeur)
        if username != currentDemandeur.username :
            # l'utilisateur courant met à jour ses informations, mais les informations sont existantes
            # todo : faire en sorte qu'on reste sur le meme modal
            return modal(request, errorMessage = "Un utilisateur ayant le même nom existe, changez le nom d'utilisateur") 
    except :
        pass
    # informations inchangées / l'utilisateur courant met à jour ses informations avec les bonnes informations
    return saveDemande(request, username, password)

def validation(request):
    global list_article
    print(request.GET)
    post = request.GET['list_article']
    print(post)
    list_article = json.loads(post)
    """
    if len(post) != 0 :
        list_article = json.loads(post)
        import pickle
        pickle.dump(list_article, open( "save.p", "wb" ) )
    else :
        import pickle
        list_article =  pickle.load( open( "save.p", "rb" ))
        print(list_article)
    """
    print("list_article--------------------nb") 
    print(list_article)   
    return HttpResponse(json.dumps({"HTTPRESPONSE":"ok"}))

def modal(request, errorMessage):
    return singin(request, errorMessage=errorMessage)

def saveDemande(request, username, password):
    global currentDemandeur, list_article
    print("____________________saveDemande_________________")
    errorMessage = isCorrect(username, password)
    allDemande_currentDemandeur = []
    if errorMessage :
        return modal(request, errorMessage)
    if currentDemandeur :
        if currentDemandeur.username and currentDemandeur.password :
            a = Demandeur.objects.get(username = currentDemandeur.username)
            print("_____________current demandeur__________", a)
            allDemande_currentDemandeur = Demande.objects.filter(demandeur = a)
            print("_____________allDemande_currentDemandeur__________")  
            print(allDemande_currentDemandeur)
            a.delete()
            #currentDemandeur.delete()
            print("_____________delete current demandeur__________")        
    currentDemandeur = Demandeur()
    print("_____________init current demandeur__________")
    currentDemandeur.username = username
    currentDemandeur.password = password
    try :
        currentDemandeur.save()
    except :
        Demandeur.objects.get(username=username).delete()
        currentDemandeur.save()
    print("_____________save current demandeur__________")
    demande = Demande()
    demande.demandeur = currentDemandeur
    demande.save()
    for demande in allDemande_currentDemandeur :
        demande.demandeur = currentDemandeur
        demande.save()
    print("_____________save current demande__________")
    print("_____________liste des articles__________", list_article)
    articles = Article.objects.filter(id__in = list_article)
    for article in articles:
        article.removed = True
        article.demande = demande
        article.save()
        print("_____________article__________", '_______', article)
    #return redirect(home)
    return home(request, articles__ = None, isinscrit=True, isconnect=True)
   

def isCorrect(username, password):
    errorMessage = None
    if not(username) or not(password):
        errorMessage = 'Tout les champs sont réquis'
    return errorMessage

def singup(request, errorMessage=''):
    return render(request,"principal/modal.html", {'errorMessage':errorMessage,'inscrit':False, 'troplong':False})
    
def onsingup(request):
    global currentDemandeur
    post = request.POST
    username = post['username']
    password = post['password']
    errorMessage = isCorrect(username, password)
    if errorMessage :
        return singup(request, errorMessage = errorMessage)
    try :
        Demandeur.objects.get(username = username)
        return singup(request, errorMessage = 'utilisateur existant')
    except :
        currentDemandeur = Demandeur()
        currentDemandeur.username = username
        currentDemandeur.password = password
        currentDemandeur.save()
        return home(request, isinscrit=True, isconnect=True)

def singin(request, errorMessage=''):
    return render(request,"principal/modal.html",  {'errorMessage':errorMessage,'inscrit':True, 'troplong':False})

def onsingin(request):
    global currentDemandeur
    post = request.POST
    username = post['username']
    password = post['password']
    errorMessage = isCorrect(username, password)
    if errorMessage :
        return singin(request, errorMessage = errorMessage)
    try :
        demandeur = Demandeur.objects.get(username = username)
        if demandeur.password == password :
            currentDemandeur = demandeur
            return home(request, isconnect=True, isinscrit=True)
        else:
            return singin(request, errorMessage = 'mot de passe incorrect')
    except :
        return singin(request, errorMessage = 'utilisateur introuvable')

def contact(request):
    #return redirect("https://www.google.com/maps/place/Rond+Point+Damase+,Tradex/@3.8160716,11.4870556,17z/data=!3m1!4b1!4m12!1m6!3m5!1s0x108bd0305fb342ad:0xb2c73ae2d473b77d!2sRond+Point+Damase+,Tradex!8m2!3d3.8160663!4d11.4892443!3m4!1s0x108bd0305fb342ad:0xb2c73ae2d473b77d!8m2!3d3.8160663!4d11.4892443")
    return render(request, "principal/contact.html")


def logout(request):
    return home(request, isconnect=False, isinscrit=True)

def profil(request):
    pass

def monpannier(request):
    print("currentDemandeur", currentDemandeur)
    demandes = Demande.objects.filter(demandeur=currentDemandeur)
    print("demandes" ,demandes)
    articles = []
    for demande in demandes :
        #articles.extend([article for article in enumerate(demande.articles)])
        articles.extend(Article.objects.filter(demande = demande))
    print(articles)
    return home(request, articles__ = articles, isconnect=True, isinscrit=True, homeMessage = 'pannier vide', pannier = True)

@csrf_exempt
def error(request):
    post = request.POST
    username = post['origin']
    return modal(request, errorMessage = post['message']) 