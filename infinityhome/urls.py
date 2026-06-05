from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.auth_app.urls')),
    path('api/proprietaires/', include('apps.proprietaires.urls')),
    path('api/immeubles/', include('apps.immeubles.urls')),
    path('api/locaux/', include('apps.locaux.urls')),
    path('api/locataires/', include('apps.locataires.urls')),
    path('api/contrats/', include('apps.contrats.urls')),
    path('api/loyers/', include('apps.loyers.urls')),
    path('api/charges/', include('apps.charges.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
    path('api/chat/', include('apps.chat.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('locataire/', TemplateView.as_view(template_name='locataire_dashboard.html')),
    path('proprietaire/', TemplateView.as_view(template_name='proprietaire_dashboard.html')),
    path('identifiants/', TemplateView.as_view(template_name='identifiants.html')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
