from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Demandeur, Demande, Article
from .forms import LoginForm, SignInForm
import json
    
def home(request):
    articles = Article.objects.filter(removed = False)
    return render(request, 'principal/index.html', {"articles" : enumerate(articles)})

def validation(request):
    post = request.GET['list_article']
    list_article = json.loads(post)
    for i in list_article:
        article = Article.objects.get(image=i)
        article.removed = True
        article.save()
        print(article)
    #print(list_article)   
    return HttpResponse(json.dumps({"HTTPRESPONSE":"ok"}))

def saveuser(request):
    if request.method == "POST":
        print(request)
    return render(request, 'index.html', {"products" : []})

def login(request):
    return HttpResponse('Login')

def signin(request):
    
    sauvegarde = True
    form = SignInForm(request.POST or None, request.FILES)
    if form.is_valid():
        demandeur = Demandeur()
        demandeur.username = form.cleaned_data["username"]
        demandeur.password = form.cleaned_data["password"]
        demandeur.save()
        sauvegarde = True

    return render(request, 'signin.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })
    