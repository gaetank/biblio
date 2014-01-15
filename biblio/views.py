# Create your views here.

from biblio.models import *
from biblio.forms import *
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group


def show_main(request):
	return render(request, "biblio/main.html",{})

def show_authors(request):
	return render(request, "biblio/authors.html", {"authors": Author.objects.order_by("lastname")})

def show_books(request):
	return render(request, "biblio/books.html", {"books": Book.objects.order_by("title")})

def show_author(request, pk):
	return render(request, "biblio/author.html", {"author": Author.objects.get(pk=pk)})

#@permission_required("biblio.can_edit_database")
def ajouter_auteur(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = AuthorForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()     # on enregistre
            return render_to_response('biblio/confirmation_auteur.html', {})
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = AuthorForm()  # Nous créons un formulaire vide
    return render(request, 'biblio/ajouter_auteur.html', locals())
    
def ajouter_livre(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = BookForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()
            return render_to_response('biblio/confirmation_livre.html', {})
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = BookForm()  # Nous créons un formulaire vide
    return render(request, 'biblio/ajouter_livre.html', locals())

def login_page(request):
    context = {}
    context.update(csrf(request))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is None:
                context["errmsg"] = "Echec de l'authentification"
            elif user.is_active:
                 login(request, user)
                 url = request.GET.get("next", "/")
                 return HttpResponseRedirect(url)
            else:
                context["errmsg"] = "Compte désactivé"
        else:
            context["errmsg"] = "Paramètres non valides"
    else:
        form = LoginForm()
    context["form"] = form
    return render(request, "biblio/login.html", context)
