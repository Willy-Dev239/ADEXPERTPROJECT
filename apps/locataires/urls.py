from django.urls import path
from . import views
urlpatterns = [
    path('', views.LocataireListCreate.as_view()),
    path('<int:pk>/', views.LocataireDetail.as_view()),
    path('<int:pk>/historique/', views.locataire_historique),
    path('<int:pk>/bordereaux/', views.list_bordereaux),
    path('<int:pk>/upload-bordereau/', views.upload_bordereau),
    path('<int:pk>/historique-pdf/', views.locataire_historique_pdf),
]
