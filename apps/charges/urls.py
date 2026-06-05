from django.urls import path
from . import views
urlpatterns = [
    path('', views.ChargeListCreate.as_view()),
    path('<int:pk>/', views.ChargeDetail.as_view()),
    path('rapport-mensuel/', views.rapport_mensuel_charges),
]
