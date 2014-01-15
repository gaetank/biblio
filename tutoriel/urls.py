from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutoriel.views.home', name='home'),
    # url(r'^tutoriel/', include('tutoriel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^/?$', "biblio.views.show_main"),
     url(r'^authors/?$', "biblio.views.show_authors"),
     url(r'^books/?$', "biblio.views.show_books"),
     url(r'^author/(\d+)$', "biblio.views.show_author"),
     url(r'^ajouter_auteur/$', "biblio.views.ajouter_auteur"),
     url(r'^ajouter_livre/$', "biblio.views.ajouter_livre"),
     url(r'^login/?$', "biblio.views.login_page"),
)
