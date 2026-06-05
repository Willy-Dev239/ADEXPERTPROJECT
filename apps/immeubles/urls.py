from django.urls import path
from . import views
from .views import ImmeubleActeursView 
urlpatterns = [
    path('', views.ImmeubleListCreate.as_view()),
    path('<int:pk>/', views.ImmeubleDetail.as_view()),
    path('provinces-communes/', views.provinces_communes_view),# urls.py  (ajouter)
     path('<int:immeuble_id>/acteurs/', ImmeubleActeursView.as_view()),
]
