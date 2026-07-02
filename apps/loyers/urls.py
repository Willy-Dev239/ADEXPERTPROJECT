from django.urls import path
from . import views
urlpatterns = [
    path('', views.LoyerListCreate.as_view()),
    path('<int:pk>/', views.LoyerDetail.as_view()),
    path('<int:pk>/enregistrer-paiement/', views.enregistrer_paiement),
    path('<int:pk>/quittance/', views.quittance_html),
    path('en-retard/', views.loyers_en_retard),
    path('impayes/', views.loyers_impayes),
    path('rapport-mensuel/', views.rapport_mensuel_loyers),
    path('paiements/rapport-journalier/', views.rapport_journalier),
    path('bordereaux/', views.bordereau_list),
    path('bordereaux/<int:pk>/valider/', views.valider_bordereau),
]
