from django.urls import path
from . import views
from .views import ChangePasswordView
from .api_views import RegisterView, VerifyEmailView, ResendCodeView

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

    # Inscription avec code de vérification (nouvelles vues)
    path('register/', RegisterView.as_view()),
    path('verify-email/', VerifyEmailView.as_view()),
    path('resend-code/', ResendCodeView.as_view()),
]