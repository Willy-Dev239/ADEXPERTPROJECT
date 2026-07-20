from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ImmeubleActeursView, ImmeubleViewSet

router = DefaultRouter()
router.register(r'', ImmeubleViewSet, basename='immeuble')

urlpatterns = [
    path('provinces-communes/', views.provinces_communes_view),
    path('list/', views.ImmeubleListCreate.as_view()),
    path('list/<int:pk>/', views.ImmeubleDetail.as_view()),
    path('<int:immeuble_id>/acteurs/', ImmeubleActeursView.as_view()),
    path('par-proprietaire/', views.get_immeubles_by_proprietaire),
    path('', include(router.urls)),
]
