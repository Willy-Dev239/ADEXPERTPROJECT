from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProprietaireListCreate.as_view()),
    path('<int:pk>/', views.ProprietaireDetail.as_view()),
]
