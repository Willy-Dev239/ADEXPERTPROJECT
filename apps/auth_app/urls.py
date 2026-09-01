from django.urls import path
from . import views
# urls.py
from .views import ChangePasswordView

    

urlpatterns = [
    path('csrf/', views.csrf_token_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('me/', views.me_view),
    path('users/<int:user_id>/lier-locataire/', views.lier_locataire),     
    path('users/<int:user_id>/lier-proprietaire/', views.lier_proprietaire),
    path('users/', views.UserListCreateView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('users/<int:user_id>/reset-password/', views.ResetUserPasswordView.as_view()),
    path('api/auth/change-password/', ChangePasswordView.as_view()),
    path('register/', views.register_view),
]