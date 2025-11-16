from django.contrib import admin
from .models import (
    Cliente, Carga, Vehiculo, Aeronave,
    Conductor, Piloto, Ruta, Despacho
)

# --- 1. Clases ModelAdmin para tablas base ---

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'ruc_o_dni', 'email', 'telefono', 'tipo_cliente', 'activo')
    search_fields = ('codigo', 'nombre', 'ruc_o_dni', 'email')
    list_filter = ('tipo_cliente', 'activo', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'tipo_cliente', 'ruc_o_dni')
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono', 'email')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Carga)
class CargaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'tipo_carga', 'peso_kg', 'volumen_m3', 'requiere_refrigeracion')
    list_filter = ('tipo_carga', 'requiere_refrigeracion', 'created_at')
    search_fields = ('codigo', 'descripcion')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'descripcion', 'tipo_carga')
        }),
        ('Especificaciones', {
            'fields': ('peso_kg', 'volumen_m3', 'valor_declarado')
        }),
        ('Condiciones Especiales', {
            'fields': ('requiere_refrigeracion', 'temperatura_min', 'temperatura_max', 'instrucciones_especiales')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'tipo_vehiculo', 'capacidad_kg', 'estado', 'activo')
    list_filter = ('tipo_vehiculo', 'estado', 'activo', 'created_at')
    search_fields = ('placa', 'marca', 'modelo')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Básica', {
            'fields': ('placa', 'marca', 'modelo', 'año', 'color', 'tipo_vehiculo')
        }),
        ('Capacidades', {
            'fields': ('capacidad_kg', 'capacidad_volumen_m3')
        }),
        ('Estado y Mantenimiento', {
            'fields': ('estado', 'kilometraje_actual', 'ultimo_mantenimiento', 'proximo_mantenimiento', 'activo')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'modelo', 'tipo_aeronave', 'capacidad_kg', 'estado', 'activo')
    list_filter = ('tipo_aeronave', 'estado', 'activo', 'created_at')
    search_fields = ('matricula', 'modelo')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Básica', {
            'fields': ('matricula', 'modelo', 'tipo_aeronave')
        }),
        ('Capacidades y Especificaciones', {
            'fields': ('capacidad_kg', 'capacidad_volumen_m3', 'autonomia_horas')
        }),
        ('Estado y Mantenimiento', {
            'fields': ('estado', 'horas_vuelo_totales', 'ultimo_mantenimiento', 'proximo_mantenimiento', 'activo')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo_licencia', 'numero_licencia', 'telefono', 'activo')
    list_filter = ('tipo_licencia', 'activo', 'created_at')
    search_fields = ('codigo', 'nombre', 'numero_licencia')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Personal', {
            'fields': ('codigo', 'nombre', 'fecha_nacimiento')
        }),
        ('Licencia y Contacto', {
            'fields': ('tipo_licencia', 'numero_licencia', 'fecha_vencimiento_licencia', 'telefono', 'email')
        }),
        ('Dirección', {
            'fields': ('direccion',)
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo_licencia', 'numero_licencia', 'horas_vuelo_totales', 'activo')
    list_filter = ('tipo_licencia', 'activo', 'created_at')
    search_fields = ('codigo', 'nombre', 'numero_licencia')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Personal', {
            'fields': ('codigo', 'nombre', 'fecha_nacimiento')
        }),
        ('Licencia y Certificaciones', {
            'fields': ('tipo_licencia', 'numero_licencia', 'fecha_vencimiento_licencia', 'fecha_vencimiento_medico')
        }),
        ('Experiencia y Contacto', {
            'fields': ('horas_vuelo_totales', 'telefono', 'email')
        }),
        ('Dirección', {
            'fields': ('direccion',)
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'origen', 'destino', 'tipo_transporte', 'distancia_km', 'activo')
    list_filter = ('tipo_transporte', 'activo', 'created_at')
    search_fields = ('codigo', 'nombre', 'origen', 'destino')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'tipo_transporte')
        }),
        ('Origen y Destino', {
            'fields': ('origen', 'destino')
        }),
        ('Distancias y Tiempos', {
            'fields': ('distancia_km', 'tiempo_estimado_horas')
        }),
        ('Costos Estimados', {
            'fields': ('costo_combustible_estimado', 'peajes_estimados')
        }),
        ('Descripción y Estado', {
            'fields': ('descripcion', 'activo')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# --- 2. Clase ModelAdmin para Despacho (con mejoras) ---

@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = (
        'referencia', 
        'estado', 
        'cliente', 
        'ruta', 
        'fecha_programada', 
        'fecha_entrega',
        'peso_total_kg',
        'costo_transporte',
        'tipo_despacho_display', 
        'creado_por'
    )
    list_filter = (
        'estado', 
        'ruta__tipo_transporte', 
        'fecha_programada', 
        'fecha_entrega',
        'creado_por'
    )
    search_fields = ('referencia', 'cliente__nombre', 'ruta__nombre')
    ordering = ('-fecha_solicitud',)
    
    # Campos que se muestran como sólo lectura para la auditoría
    readonly_fields = ('creado_por', 'fecha_solicitud', 'created_at', 'updated_at')
    
    # Usa raw_id_fields para seleccionar FKeys por ID, mejorando el rendimiento
    raw_id_fields = (
        'ruta', 'vehiculo', 'aeronave', 'conductor', 
        'piloto', 'cliente', 'carga'
    )
    
    # Agrupación de campos para una mejor organización en el formulario de detalle
    fieldsets = (
        ('Información Básica', {
            'fields': ('referencia', 'estado', 'observaciones')
        }),
        ('Fechas', {
            'fields': ('fecha_programada', 'fecha_entrega')
        }),
        ('Detalle de la Carga', {
            'fields': ('cliente', 'carga', 'peso_total_kg', 'volumen_m3')
        }),
        ('Costos', {
            'fields': ('costo_transporte', 'seguro_carga')
        }),
        ('Asignación de Ruta', {
            'fields': ('ruta',)
        }),
        ('Recursos Terrestres', {
            'fields': ('vehiculo', 'conductor'),
            'classes': ('collapse',)
        }),
        ('Recursos Aéreos', {
            'fields': ('aeronave', 'piloto'),
            'classes': ('collapse',)
        }),
        ('Auditoría', {
            'fields': ('creado_por', 'fecha_solicitud', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Método para mostrar el tipo de transporte de la ruta en list_display
    def tipo_despacho_display(self, obj):
        return obj.ruta.get_tipo_transporte_display() if obj.ruta else '-'
    
    tipo_despacho_display.short_description = 'Tipo Transporte'
    tipo_despacho_display.admin_order_field = 'ruta__tipo_transporte'

    # Sobrescribir save_model para asignar automáticamente el usuario creador
    def save_model(self, request, obj, form, change):
        if not obj.creado_por:
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

    # Acciones personalizadas para Despacho
    actions = ['marcar_como_en_ruta', 'marcar_como_entregado']

    def marcar_como_en_ruta(self, request, queryset):
        updated = queryset.update(estado='EN_RUTA')
        self.message_user(request, f'{updated} despacho(s) marcado(s) como "En ruta"')
    
    marcar_como_en_ruta.short_description = "Marcar como En ruta"

    def marcar_como_entregado(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(estado='ENTREGADO', fecha_entrega=timezone.now())
        self.message_user(request, f'{updated} despacho(s) marcado(s) como "Entregado"')
    
    marcar_como_entregado.short_description = "Marcar como Entregado"