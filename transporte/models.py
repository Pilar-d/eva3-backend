from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Cliente(models.Model):
    TIPO_CLIENTE = (
        ('NATURAL', 'Persona Natural'),
        ('JURIDICO', 'Persona Jurídica'),
    )
    
    codigo = models.CharField(max_length=30, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre o Razón Social')
    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CLIENTE, default='NATURAL', verbose_name='Tipo de Cliente')
    direccion = models.TextField(blank=True, verbose_name='Dirección')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo Electrónico')
    ruc_o_dni = models.CharField(max_length=20, blank=True, verbose_name='RUC o DNI')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Carga(models.Model):
    TIPO_CARGA = (
        ('GENERAL', 'Carga General'),
        ('PELIGROSA', 'Carga Peligrosa'),
        ('REFRIGERADA', 'Carga Refrigerada'),
        ('FRAGIL', 'Carga Frágil'),
        ('VIVA', 'Carga Viva'),
        ('PERECEDERA', 'Carga Perecedera'),
    )
    
    codigo = models.CharField(max_length=30, unique=True, verbose_name='Código')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')
    tipo_carga = models.CharField(max_length=15, choices=TIPO_CARGA, default='GENERAL', verbose_name='Tipo de Carga')
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Peso (kg)')
    volumen_m3 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Volumen (m³)')
    valor_declarado = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='Valor Declarado')
    instrucciones_especiales = models.TextField(blank=True, verbose_name='Instrucciones Especiales')
    requiere_refrigeracion = models.BooleanField(default=False, verbose_name='Requiere Refrigeración')
    temperatura_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Temperatura Mínima (°C)')
    temperatura_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Temperatura Máxima (°C)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Carga'
        verbose_name_plural = 'Cargas'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

class Vehiculo(models.Model):
    TIPO_VEHICULO = (
        ('CAMION', 'Camión'),
        ('FURGON', 'Furgón'),
        ('CAMIONETA', 'Camioneta'),
        ('TRACTOR', 'Tractor'),
        ('REMOLQUE', 'Remolque'),
    )
    
    ESTADO_VEHICULO = (
        ('DISPONIBLE', 'Disponible'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
        ('REPARACION', 'En Reparación'),
        ('INACTIVO', 'Inactivo'),
    )

    placa = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    año = models.IntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(2030)
        ],
        verbose_name='Año'
    )
    color = models.CharField(max_length=30, blank=True, verbose_name='Color')
    tipo_vehiculo = models.CharField(max_length=15, choices=TIPO_VEHICULO, default='CAMION', verbose_name='Tipo de Vehículo')
    capacidad_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Capacidad (kg)')
    capacidad_volumen_m3 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Capacidad Volumen (m³)')
    estado = models.CharField(max_length=15, choices=ESTADO_VEHICULO, default='DISPONIBLE', verbose_name='Estado')
    kilometraje_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Kilometraje Actual')
    ultimo_mantenimiento = models.DateField(null=True, blank=True, verbose_name='Último Mantenimiento')
    proximo_mantenimiento = models.DateField(null=True, blank=True, verbose_name='Próximo Mantenimiento')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"

class Aeronave(models.Model):
    TIPO_AERONAVE = (
        ('AVION_CARGA', 'Avión de Carga'),
        ('HELICOPTERO', 'Helicóptero'),
        ('AVION_COMBINADO', 'Avión Combinado'),
    )
    
    ESTADO_AERONAVE = (
        ('DISPONIBLE', 'Disponible'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
        ('VUELO', 'En Vuelo'),
        ('INACTIVO', 'Inactivo'),
    )

    matricula = models.CharField(max_length=10, unique=True, verbose_name='Matrícula')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    tipo_aeronave = models.CharField(max_length=20, choices=TIPO_AERONAVE, default='AVION_CARGA', verbose_name='Tipo de Aeronave')
    capacidad_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Capacidad (kg)')
    capacidad_volumen_m3 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Capacidad Volumen (m³)')
    autonomia_horas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Autonomía (horas)')
    estado = models.CharField(max_length=15, choices=ESTADO_AERONAVE, default='DISPONIBLE', verbose_name='Estado')
    horas_vuelo_totales = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Horas de Vuelo Totales')
    ultimo_mantenimiento = models.DateField(null=True, blank=True, verbose_name='Último Mantenimiento')
    proximo_mantenimiento = models.DateField(null=True, blank=True, verbose_name='Próximo Mantenimiento')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Aeronave'
        verbose_name_plural = 'Aeronaves'

    def __str__(self):
        return f"{self.matricula} - {self.modelo}"

class Conductor(models.Model):
    TIPO_LICENCIA = (
        ('A', 'Licencia A - Motocicletas'),
        ('B', 'Licencia B - Vehículos Livianos'),
        ('C', 'Licencia C - Vehículos Pesados'),
        ('D', 'Licencia D - Transporte Público'),
        ('E', 'Licencia E - Maquinaria Pesada'),
    )

    codigo = models.CharField(max_length=30, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre Completo')
    tipo_licencia = models.CharField(max_length=5, choices=TIPO_LICENCIA, default='C', verbose_name='Tipo de Licencia')
    numero_licencia = models.CharField(max_length=20, unique=True, verbose_name='Número de Licencia')
    fecha_vencimiento_licencia = models.DateField(verbose_name='Fecha de Vencimiento de Licencia')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo Electrónico')
    direccion = models.TextField(blank=True, verbose_name='Dirección')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Piloto(models.Model):
    TIPO_LICENCIA_PILOTO = (
        ('PPL', 'Licencia de Piloto Privado'),
        ('CPL', 'Licencia de Piloto Comercial'),
        ('ATPL', 'Licencia de Piloto de Transporte de Línea Aérea'),
    )

    codigo = models.CharField(max_length=30, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre Completo')
    tipo_licencia = models.CharField(max_length=5, choices=TIPO_LICENCIA_PILOTO, default='CPL', verbose_name='Tipo de Licencia')
    numero_licencia = models.CharField(max_length=20, unique=True, verbose_name='Número de Licencia')
    fecha_vencimiento_licencia = models.DateField(verbose_name='Fecha de Vencimiento de Licencia')
    fecha_vencimiento_medico = models.DateField(verbose_name='Fecha de Vencimiento Certificado Médico')
    horas_vuelo_totales = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Horas de Vuelo Totales')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo Electrónico')
    direccion = models.TextField(blank=True, verbose_name='Dirección')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Ruta(models.Model):
    TIPO_TRANSPORTE = (
        ('TERRESTRE', 'Terrestre'),
        ('AEREO', 'Aéreo'),
    )

    codigo = models.CharField(max_length=30, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    origen = models.CharField(max_length=150, verbose_name='Origen')
    destino = models.CharField(max_length=150, verbose_name='Destino')
    distancia_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Distancia (km)')
    tiempo_estimado_horas = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Tiempo Estimado (horas)')
    tipo_transporte = models.CharField(max_length=12, choices=TIPO_TRANSPORTE, default='TERRESTRE', verbose_name='Tipo de Transporte')
    costo_combustible_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Costo Combustible Estimado')
    peajes_estimados = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Peajes Estimados')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'

    def __str__(self):
        return f"{self.codigo} - {self.origen} → {self.destino}"

class Despacho(models.Model):
    ESTADO = (
        ('PENDIENTE', 'Pendiente'),
        ('EN_RUTA', 'En ruta'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
        ('RETRASADO', 'Retrasado'),
    )

    referencia = models.CharField(max_length=50, unique=True, verbose_name='Referencia')
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Solicitud')
    fecha_programada = models.DateTimeField(null=True, blank=True, verbose_name='Fecha Programada')
    fecha_entrega = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Entrega')

    # Relaciones
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name='despachos', verbose_name='Ruta')
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.SET_NULL, related_name='despachos', null=True, blank=True, verbose_name='Vehículo')
    aeronave = models.ForeignKey('Aeronave', on_delete=models.SET_NULL, related_name='despachos', null=True, blank=True, verbose_name='Aeronave')
    conductor = models.ForeignKey('Conductor', on_delete=models.SET_NULL, related_name='despachos', null=True, blank=True, verbose_name='Conductor')
    piloto = models.ForeignKey('Piloto', on_delete=models.SET_NULL, related_name='despachos', null=True, blank=True, verbose_name='Piloto')
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT, related_name='despachos', verbose_name='Cliente')
    carga = models.ForeignKey('Carga', on_delete=models.PROTECT, related_name='despachos', verbose_name='Carga')

    peso_total_kg = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Peso Total (kg)')
    volumen_m3 = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True, verbose_name='Volumen (m³)')
    costo_transporte = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='Costo de Transporte')
    seguro_carga = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='Seguro de Carga')

    estado = models.CharField(max_length=12, choices=ESTADO, default='PENDIENTE', verbose_name='Estado')
    observaciones = models.TextField(blank=True, verbose_name='Observaciones')
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachos_creados', verbose_name='Creado por')

    # auditoría
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        ordering = ['-fecha_solicitud']
        verbose_name = 'Despacho'
        verbose_name_plural = 'Despachos'
        indexes = [
            models.Index(fields=['referencia']),
            models.Index(fields=['estado']),
            models.Index(fields=['fecha_solicitud']),
        ]

    def __str__(self):
        return f"{self.referencia} ({self.estado})"

    @property
    def tipo_despacho(self):
        """Retorna el tipo de despacho basado en el tipo de transporte de la ruta"""
        return self.ruta.tipo_transporte if self.ruta else None

    @property
    def dias_retraso(self):
        """Calcula los días de retraso si la entrega está pendiente y pasó la fecha programada"""
        if self.estado in ['PENDIENTE', 'EN_RUTA'] and self.fecha_programada:
            from django.utils import timezone
            if timezone.now() > self.fecha_programada:
                diferencia = timezone.now() - self.fecha_programada
                return diferencia.days
        return 0