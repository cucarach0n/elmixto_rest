from django.db import models
class TipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key = True)
    nombreTipoProducto = models.CharField('Nombre del tipo de producto',max_length=150,null = False)
    horarioTipoProducto = models.CharField('Horario del producto',max_length=1, null=False)
    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipo de Productos'

    def __str__(self):
        return f'Tipo producto {self.nombreTipoProducto} con el id {self.idTipoProducto}'

class Producto(models.Model):
    idProducto = models.AutoField(primary_key = True)
    nombreProducto = models.CharField('Nombre del producto',max_length=250,null = False)
    precio = models.DecimalField("Precio del producto", null = True, blank = True, default=0,decimal_places=2,max_digits=4)
    imagenProducto = models.ImageField('Imagen del producto', upload_to='imagenProducto/', default="imagenProducto/defaultProducto.png", null=True, blank = True)
    tipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, null=False)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'Producto {self.nombreProducto} con el id {self.idProducto}'
