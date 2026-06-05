from django.urls import path
from . import views
urlpatterns = [
    path('', views.LocalListCreate.as_view()),
    path('<int:pk>/', views.LocalDetail.as_view()),
]
