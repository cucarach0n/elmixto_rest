
from dataclasses import field
from apps.carta.models import Producto
from rest_framework import serializers

class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = ('idProducto','fechaCreacion','fechaUpdate',)

class ProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = ('idProducto','fechaCreacion','fechaUpdate','tipoProducto',)

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

'''class InvitacionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitacionTeam
        fields = ['idInvitacionTeam','fechaCreacion','tipoInvitacion','cantidadInvitacion','fechaExpiracion','slugInvitacion','teamUsuario']
    def to_representation(self,instance):
        cantidadInvitados = InvitacionUsuario.objects.filter(invitacionTeam = instance).count()
        return {
        "idInvitacionTeam": instance.idInvitacionTeam,
        "fechaCreacion": instance.fechaCreacion,
        "tipoInvitacion": instance.tipoInvitacion,
        "cantidadInvitacion": instance.cantidadInvitacion,
        "cantidadInvitados": cantidadInvitados,
        "fechaExpiracion": instance.fechaExpiracion,
        "slugInvitacion": instance.slugInvitacion,
        "teamUsuario": TeamUsuarioDetailSerializer(instance.teamUsuario).data
    }'''