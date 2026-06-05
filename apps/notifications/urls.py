from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationList.as_view()),
    path('<int:pk>/lire/', views.marquer_lu),
    path('avertissement/', views.envoyer_avertissement),
]
