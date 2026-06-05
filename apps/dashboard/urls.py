from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard_view),
    path('portefeuille/', views.portefeuille_view),
]
