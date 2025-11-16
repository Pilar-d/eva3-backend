from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Permite acciones de escritura solo a usuarios staff (is_staff).
    Lectura permitida a usuarios autenticados (o se puede cambiar a AllowAny según política).
    """

    def has_permission(self, request, view):
        # Safe methods allowed to authenticated users (change to AllowAny if public read)
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # escritura solo staff
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsCreatorOrStaff(permissions.BasePermission):
    """
    Permite editar/eliminar solo al creador del objeto o personal staff.
    Asume que el objeto tiene atributo 'creado_por'.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # staff puede todo
        if request.user and request.user.is_staff:
            return True
        # el creador puede modificar
        return hasattr(obj, 'creado_por') and obj.creado_por == request.user
