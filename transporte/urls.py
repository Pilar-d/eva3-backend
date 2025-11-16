from django.urls import path
from . import views

app_name = 'transporte'

urlpatterns = [
    # ==================== PÁGINAS PRINCIPALES ====================
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    
    # ==================== GESTIÓN DE CLIENTES ====================
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    
    # ==================== GESTIÓN DE CARGAS ====================
    path('cargas/', views.CargaListView.as_view(), name='carga_list'),
    path('cargas/nueva/', views.CargaCreateView.as_view(), name='carga_create'),
    path('cargas/<int:pk>/', views.CargaDetailView.as_view(), name='carga_detail'),
    path('cargas/<int:pk>/editar/', views.CargaUpdateView.as_view(), name='carga_update'),
    path('cargas/<int:pk>/eliminar/', views.CargaDeleteView.as_view(), name='carga_delete'),
    
    # ==================== GESTIÓN DE VEHÍCULOS ====================
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo_list'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculos/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo_delete'),
    
    # ==================== GESTIÓN DE AERONAVES ====================
    path('aeronaves/', views.AeronaveListView.as_view(), name='aeronave_list'),
    path('aeronaves/nueva/', views.AeronaveCreateView.as_view(), name='aeronave_create'),
    path('aeronaves/<int:pk>/', views.AeronaveDetailView.as_view(), name='aeronave_detail'),
    path('aeronaves/<int:pk>/editar/', views.AeronaveUpdateView.as_view(), name='aeronave_update'),
    path('aeronaves/<int:pk>/eliminar/', views.AeronaveDeleteView.as_view(), name='aeronave_delete'),
    
    # ==================== GESTIÓN DE CONDUCTORES ====================
    path('conductores/', views.ConductorListView.as_view(), name='conductor_list'),
    path('conductores/nuevo/', views.ConductorCreateView.as_view(), name='conductor_create'),
    path('conductores/<int:pk>/', views.ConductorDetailView.as_view(), name='conductor_detail'),
    path('conductores/<int:pk>/editar/', views.ConductorUpdateView.as_view(), name='conductor_update'),
    path('conductores/<int:pk>/eliminar/', views.ConductorDeleteView.as_view(), name='conductor_delete'),
    
    # ==================== GESTIÓN DE PILOTOS ====================
    path('pilotos/', views.PilotoListView.as_view(), name='piloto_list'),
    path('pilotos/nuevo/', views.PilotoCreateView.as_view(), name='piloto_create'),
    path('pilotos/<int:pk>/', views.PilotoDetailView.as_view(), name='piloto_detail'),
    path('pilotos/<int:pk>/editar/', views.PilotoUpdateView.as_view(), name='piloto_update'),
    path('pilotos/<int:pk>/eliminar/', views.PilotoDeleteView.as_view(), name='piloto_delete'),
    
    # ==================== GESTIÓN DE RUTAS ====================
    path('rutas/', views.RutaListView.as_view(), name='ruta_list'),
    path('rutas/nueva/', views.RutaCreateView.as_view(), name='ruta_create'),
    path('rutas/<int:pk>/', views.RutaDetailView.as_view(), name='ruta_detail'),
    path('rutas/<int:pk>/editar/', views.RutaUpdateView.as_view(), name='ruta_update'),
    path('rutas/<int:pk>/eliminar/', views.RutaDeleteView.as_view(), name='ruta_delete'),
    
    # ==================== GESTIÓN DE DESPACHOS ====================
    path('despachos/', views.DespachoListView.as_view(), name='despacho_list'),
    path('despachos/nuevo/', views.DespachoCreateView.as_view(), name='despacho_create'),
    path('despachos/<int:pk>/', views.DespachoDetailView.as_view(), name='despacho_detail'),
    path('despachos/<int:pk>/editar/', views.DespachoUpdateView.as_view(), name='despacho_update'),
    path('despachos/<int:pk>/eliminar/', views.DespachoDeleteView.as_view(), name='despacho_delete'),
]