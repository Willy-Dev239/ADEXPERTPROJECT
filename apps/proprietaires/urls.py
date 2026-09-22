# apps/proprietaires/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # =============================================================
    # ⚡ Routes GÉO — AVANT les routes avec <int:pk>
    # =============================================================
    path("geo/continents/", views.geo_continents),
    path("geo/pays/",       views.geo_pays),
    path("geo/provinces/", views.geo_provinces),
    path("geo/communes/",  views.geo_communes),
    path("geo/quartiers/", views.geo_quartiers),

    # =============================================================
    # CRUD Propriétaires
    # =============================================================
    path("",             views.ProprietaireListCreate.as_view()),
    path("<int:pk>/",    views.ProprietaireDetail.as_view()),
]