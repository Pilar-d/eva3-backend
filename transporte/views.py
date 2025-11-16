from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from .models import *

class IndexView(TemplateView):
    template_name = 'transporte/index.html'

class DashboardView(TemplateView):
    template_name = 'transporte/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_clientes'] = Cliente.objects.filter(activo=True).count()
        context['total_despachos'] = Despacho.objects.count()
        context['despachos_pendientes'] = Despacho.objects.filter(estado='PENDIENTE').count()
        context['despachos_en_ruta'] = Despacho.objects.filter(estado='EN_RUTA').count()
        context['ultimos_despachos'] = Despacho.objects.select_related('cliente', 'ruta').order_by('-created_at')[:5]
        return context

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'transporte/cliente/list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    
    def get_queryset(self):
        return Cliente.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes_activos'] = Cliente.objects.filter(activo=True).count()
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'transporte/cliente/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:cliente_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente creado exitosamente.')
        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'transporte/cliente/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:cliente_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente actualizado exitosamente.')
        return super().form_valid(form)

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'transporte/cliente/detail.html'
    context_object_name = 'cliente'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'transporte/cliente/confirm_delete.html'
    success_url = reverse_lazy('transporte:cliente_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Cliente eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Carga
class CargaListView(ListView):
    model = Carga
    template_name = 'transporte/carga/list.html'
    context_object_name = 'cargas'
    paginate_by = 10
    
    def get_queryset(self):
        return Carga.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargas_peligrosas'] = Carga.objects.filter(tipo_carga='PELIGROSA').count()
        context['cargas_refrigeradas'] = Carga.objects.filter(requiere_refrigeracion=True).count()
        context['peso_total'] = Carga.objects.aggregate(Sum('peso_kg'))['peso_kg__sum'] or 0
        return context

class CargaCreateView(CreateView):
    model = Carga
    template_name = 'transporte/carga/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:carga_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Carga creada exitosamente.')
        return super().form_valid(form)

class CargaUpdateView(UpdateView):
    model = Carga
    template_name = 'transporte/carga/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:carga_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Carga actualizada exitosamente.')
        return super().form_valid(form)

class CargaDetailView(DetailView):
    model = Carga
    template_name = 'transporte/carga/detail.html'
    context_object_name = 'carga'

class CargaDeleteView(DeleteView):
    model = Carga
    template_name = 'transporte/carga/confirm_delete.html'
    success_url = reverse_lazy('transporte:carga_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Carga eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Vehiculo
class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'transporte/vehiculo/list.html'
    context_object_name = 'vehiculos'
    paginate_by = 10
    
    def get_queryset(self):
        return Vehiculo.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_vehiculos'] = Vehiculo.objects.count()
        context['vehiculos_disponibles'] = Vehiculo.objects.filter(estado='DISPONIBLE').count()
        context['vehiculos_mantenimiento'] = Vehiculo.objects.filter(estado='MANTENIMIENTO').count()
        
        # Vehículos con mantenimiento urgente (próximos 7 días)
        fecha_limite = timezone.now().date() + timedelta(days=7)
        context['mantenimientos_urgentes'] = Vehiculo.objects.filter(
            proximo_mantenimiento__lte=fecha_limite,
            activo=True
        ).count()
        return context

class VehiculoCreateView(CreateView):
    model = Vehiculo
    template_name = 'transporte/vehiculo/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:vehiculo_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Vehículo creado exitosamente.')
        return super().form_valid(form)

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    template_name = 'transporte/vehiculo/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:vehiculo_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Vehículo actualizado exitosamente.')
        return super().form_valid(form)

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'transporte/vehiculo/detail.html'
    context_object_name = 'vehiculo'

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'transporte/vehiculo/confirm_delete.html'
    success_url = reverse_lazy('transporte:vehiculo_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Vehículo eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Aeronave
class AeronaveListView(ListView):
    model = Aeronave
    template_name = 'transporte/aeronave/list.html'
    context_object_name = 'aeronaves'
    paginate_by = 10
    
    def get_queryset(self):
        return Aeronave.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_aeronaves'] = Aeronave.objects.count()
        context['aeronaves_disponibles'] = Aeronave.objects.filter(estado='DISPONIBLE').count()
        context['aeronaves_vuelo'] = Aeronave.objects.filter(estado='VUELO').count()
        context['total_horas_vuelo'] = Aeronave.objects.aggregate(
            Sum('horas_vuelo_totales')
        )['horas_vuelo_totales__sum'] or 0
        return context

class AeronaveCreateView(CreateView):
    model = Aeronave
    template_name = 'transporte/aeronave/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:aeronave_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Aeronave creada exitosamente.')
        return super().form_valid(form)

class AeronaveUpdateView(UpdateView):
    model = Aeronave
    template_name = 'transporte/aeronave/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:aeronave_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Aeronave actualizada exitosamente.')
        return super().form_valid(form)

class AeronaveDetailView(DetailView):
    model = Aeronave
    template_name = 'transporte/aeronave/detail.html'
    context_object_name = 'aeronave'

class AeronaveDeleteView(DeleteView):
    model = Aeronave
    template_name = 'transporte/aeronave/confirm_delete.html'
    success_url = reverse_lazy('transporte:aeronave_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Aeronave eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Conductor
class ConductorListView(ListView):
    model = Conductor
    template_name = 'transporte/conductor/list.html'
    context_object_name = 'conductores'
    paginate_by = 10
    
    def get_queryset(self):
        return Conductor.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()
        treinta_dias = hoy + timedelta(days=30)
        
        context['total_conductores'] = Conductor.objects.count()
        context['conductores_activos'] = Conductor.objects.filter(activo=True).count()
        context['licencias_vencidas'] = Conductor.objects.filter(
            fecha_vencimiento_licencia__lt=hoy
        ).count()
        context['licencias_proximas'] = Conductor.objects.filter(
            fecha_vencimiento_licencia__range=[hoy, treinta_dias]
        ).count()
        return context

class ConductorCreateView(CreateView):
    model = Conductor
    template_name = 'transporte/conductor/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:conductor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Conductor creado exitosamente.')
        return super().form_valid(form)

class ConductorUpdateView(UpdateView):
    model = Conductor
    template_name = 'transporte/conductor/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:conductor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Conductor actualizado exitosamente.')
        return super().form_valid(form)

class ConductorDetailView(DetailView):
    model = Conductor
    template_name = 'transporte/conductor/detail.html'
    context_object_name = 'conductor'

class ConductorDeleteView(DeleteView):
    model = Conductor
    template_name = 'transporte/conductor/confirm_delete.html'
    success_url = reverse_lazy('transporte:conductor_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Conductor eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Piloto
class PilotoListView(ListView):
    model = Piloto
    template_name = 'transporte/piloto/list.html'
    context_object_name = 'pilotos'
    paginate_by = 10
    
    def get_queryset(self):
        return Piloto.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()
        
        context['total_pilotos'] = Piloto.objects.count()
        context['pilotos_activos'] = Piloto.objects.filter(activo=True).count()
        context['licencias_vencidas'] = Piloto.objects.filter(
            fecha_vencimiento_licencia__lt=hoy
        ).count()
        context['total_horas_vuelo'] = Piloto.objects.aggregate(
            Sum('horas_vuelo_totales')
        )['horas_vuelo_totales__sum'] or 0
        return context

class PilotoCreateView(CreateView):
    model = Piloto
    template_name = 'transporte/piloto/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:piloto_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Piloto creado exitosamente.')
        return super().form_valid(form)

class PilotoUpdateView(UpdateView):
    model = Piloto
    template_name = 'transporte/piloto/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:piloto_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Piloto actualizado exitosamente.')
        return super().form_valid(form)

class PilotoDetailView(DetailView):
    model = Piloto
    template_name = 'transporte/piloto/detail.html'
    context_object_name = 'piloto'

class PilotoDeleteView(DeleteView):
    model = Piloto
    template_name = 'transporte/piloto/confirm_delete.html'
    success_url = reverse_lazy('transporte:piloto_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Piloto eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Ruta
class RutaListView(ListView):
    model = Ruta
    template_name = 'transporte/ruta/list.html'
    context_object_name = 'rutas'
    paginate_by = 10
    
    def get_queryset(self):
        return Ruta.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_rutas'] = Ruta.objects.count()
        context['rutas_terrestres'] = Ruta.objects.filter(tipo_transporte='TERRESTRE').count()
        context['rutas_aereas'] = Ruta.objects.filter(tipo_transporte='AEREO').count()
        context['rutas_activas'] = Ruta.objects.filter(activo=True).count()
        return context

class RutaCreateView(CreateView):
    model = Ruta
    template_name = 'transporte/ruta/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:ruta_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Ruta creada exitosamente.')
        return super().form_valid(form)

class RutaUpdateView(UpdateView):
    model = Ruta
    template_name = 'transporte/ruta/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:ruta_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Ruta actualizada exitosamente.')
        return super().form_valid(form)

class RutaDetailView(DetailView):
    model = Ruta
    template_name = 'transporte/ruta/detail.html'
    context_object_name = 'ruta'

class RutaDeleteView(DeleteView):
    model = Ruta
    template_name = 'transporte/ruta/confirm_delete.html'
    success_url = reverse_lazy('transporte:ruta_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Ruta eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Despacho
class DespachoListView(ListView):
    model = Despacho
    template_name = 'transporte/despacho/list.html'
    context_object_name = 'despachos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Despacho.objects.select_related(
            'cliente', 'ruta', 'vehiculo', 'aeronave'
        ).order_by('-fecha_solicitud')
        
        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now()
        
        context['total_despachos'] = Despacho.objects.count()
        context['despachos_pendientes'] = Despacho.objects.filter(estado='PENDIENTE').count()
        context['despachos_en_ruta'] = Despacho.objects.filter(estado='EN_RUTA').count()
        context['despachos_entregados'] = Despacho.objects.filter(estado='ENTREGADO').count()
        context['despachos_cancelados'] = Despacho.objects.filter(estado='CANCELADO').count()
        
        # Despachos retrasados (pendientes o en ruta con fecha programada pasada)
        context['despachos_retrasados'] = Despacho.objects.filter(
            Q(estado='PENDIENTE') | Q(estado='EN_RUTA'),
            fecha_programada__lt=hoy
        ).count()
        
        # Por tipo de transporte
        context['despachos_terrestres'] = Despacho.objects.filter(
            ruta__tipo_transporte='TERRESTRE'
        ).count()
        context['despachos_aereos'] = Despacho.objects.filter(
            ruta__tipo_transporte='AEREO'
        ).count()
        
        # Totales de peso y volumen
        context['peso_total'] = Despacho.objects.aggregate(
            Sum('peso_total_kg')
        )['peso_total_kg__sum'] or 0
        context['volumen_total'] = Despacho.objects.aggregate(
            Sum('volumen_m3')
        )['volumen_m3__sum'] or 0
        
        return context

class DespachoCreateView(CreateView):
    model = Despacho
    template_name = 'transporte/despacho/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:despacho_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Despacho creado exitosamente.')
        return super().form_valid(form)

class DespachoUpdateView(UpdateView):
    model = Despacho
    template_name = 'transporte/despacho/form.html'
    fields = '__all__'
    success_url = reverse_lazy('transporte:despacho_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Despacho actualizado exitosamente.')
        return super().form_valid(form)

class DespachoDetailView(DetailView):
    model = Despacho
    template_name = 'transporte/despacho/detail.html'
    context_object_name = 'despacho'

class DespachoDeleteView(DeleteView):
    model = Despacho
    template_name = 'transporte/despacho/confirm_delete.html'
    success_url = reverse_lazy('transporte:despacho_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Despacho eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)