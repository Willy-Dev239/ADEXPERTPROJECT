from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bordereaux-virement', views.BordereauVirementViewSet, basename='bordereau-virement')

urlpatterns = [
    path('', views.ContratListCreate.as_view()),
    path('<int:pk>/', views.ContratDetail.as_view()),
    path('<int:pk>/resilier/', views.resilier_contrat),
    path('<int:pk>/generer-loyers/', views.generer_loyers),
    path('societe/', views.ContratSocieteListCreate.as_view()),
    path('societe/<int:pk>/', views.ContratSocieteDetail.as_view()),
] + router.urls