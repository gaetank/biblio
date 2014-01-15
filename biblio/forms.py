# -*- coding: utf-8 -*-

from django.forms import ModelForm, Form, CharField, PasswordInput
from biblio.models import Author, Book
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

class AuthorForm(ModelForm):
    class Meta:
        model = Author

class BookForm(ModelForm):
	class Meta:
		model = Book

class LoginForm(Form):
	username = CharField(max_length=100, label="Identifiant:")
	password = CharField(max_length=100, label="Mot de passe:", widget=PasswordInput)

class InscriptionForm(Form):
	pseudo = CharField(max_length=100, label="Pseudo")
	password = CharField(max_length=100, label="Mot de passe", widget=PasswordInput)
	mail = CharField(max_length=255, label="Mail")