import os
from apps.carta.models import Producto
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from datetime import datetime
from django.utils.crypto import get_random_string
from django.conf import settings
from apps.usuario.authentication_mixings import Authentication
from django.http import FileResponse
from apps.carta.api.serializers.producto_serializers import ProductoCreateSerializer,ProductoSerializer

class ProductoViewSet(viewsets.GenericViewSet):
    serializer_class = ProductoCreateSerializer
    def get_queryset(self):
        return Producto.objects.all()
    def list(self,request):
        '''
        Listar productos

        parametros
        - no requiere parametros
        '''
        productoList = self.get_queryset()
        producto_serializer = ProductoSerializer(productoList,many = True)
        return Response(producto_serializer.data, status = status.HTTP_200_OK )
    def create(self,request):
        '''
        Crear producto

        parametros
        - nombreProducto varchar(255)
        - precio decimal(4,2) opcional
        - imagenProducto File Imagen opcional
        - tipoProducto varchar(1)
        '''
        producto_serializer = self.serializer_class(data = request.data)
        if producto_serializer.is_valid():
            productoCreado = producto_serializer.save()
            return Response(ProductoSerializer(productoCreado).data,status = status.HTTP_201_CREATED)

        else:
            return Response(producto_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        '''
        Actualizar producto

        parametros
        - nombreProducto varchar(255)
        - precio decimal(4,2) opcional
        - imagenProducto File Imagen opcional
        - tipoProducto varchar(1)
        '''
        productoObj = Producto.objects.filter(idProducto = pk).first()
        if productoObj:
            producto_serializer = self.serializer_class(productoObj,data = request.data)
            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response(producto_serializer.data,status = status.HTTP_200_OK)
            return Response(producto_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        return Response({"mensaje":"No existe el producto"},status = status.HTTP_404_NOT_FOUND)