# logistica/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Configuración Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="LogiTrack API",
        default_version='v1',
        description="Sistema de gestión logística para transporte terrestre y aéreo.",
        contact=openapi.Contact(email="soporte@logitrack.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),

    # Redirección raíz hacia la web de transporte (HTML)
    path('', RedirectView.as_view(url='/transporte/', permanent=False)),

    # Vistas de Django (HTML)
    path('transporte/', include('transporte.urls')),

    # API REST
    path('api/transporte/', include('transporte.urls')),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Documentación API
    path('swagger.<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Auth DRF para login/logout navegador
    path('api-auth/', include('rest_framework.urls')),
]
