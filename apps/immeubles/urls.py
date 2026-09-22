# apps/immeubles/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ImmeubleActeursView, ImmeubleViewSet


router = DefaultRouter()
router.register(r"", ImmeubleViewSet, basename="immeuble")


urlpatterns = [

    path("geo/continents/", views.geo_continents),   
    path("geo/pays/",       views.geo_pays),         
    path("geo/provinces/",  views.geo_provinces),
    path("geo/communes/",   views.geo_communes),
    path("geo/quartiers/",  views.geo_quartiers),
    path("geo/complet/",    views.geo_complet),

    # =============================================================
    # Routes existantes
    # =============================================================
    path("provinces-communes/",            views.provinces_communes_view),
    path("list/",                          views.ImmeubleListCreate.as_view()),
    path("list/<int:pk>/",                 views.ImmeubleDetail.as_view()),
    path("<int:immeuble_id>/acteurs/",     ImmeubleActeursView.as_view()),
    path("par-proprietaire/",              views.get_immeubles_by_proprietaire),

    # =============================================================
    # Router — TOUJOURS EN DERNIER
    # =============================================================
    path("", include(router.urls)),
]