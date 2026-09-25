from django.urls import path

from . import views

urlpatterns = [
    # Public
    path("public/",                     views.AnnoncePubliqueList.as_view()),
    path("photos/<int:pk>/",            views.annonce_photo, name="annonce_photo"),

    # Gestion
    path("photos/<int:pk>/supprimer/",  views.supprimer_photo),
    path("",                            views.AnnonceListCreate.as_view()),
    path("<int:pk>/",                   views.AnnonceDetail.as_view()),
    path("<int:pk>/photos/",            views.ajouter_photos),
    path("<int:pk>/marquer-louee/",     views.marquer_louee),
    path("<int:pk>/retirer/",           views.retirer),
    path("<int:pk>/republier/",         views.republier),
]