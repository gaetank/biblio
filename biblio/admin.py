from django.contrib import admin
from biblio.models import Author, Subject, Book

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Subject)

