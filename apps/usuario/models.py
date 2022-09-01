from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, correo,nombres,apellidos,dni,genero,numeroTelefono,tipoCuenta,habilitado, password, is_superuser,**extra_fields):
        user = self.model(
            correo = correo,
            nombres = nombres,
            apellidos = apellidos,
            dni = dni,
            genero = genero,
            numeroTelefono = numeroTelefono,
            tipoCuenta = tipoCuenta,
            habilitado = habilitado,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,dni,genero,nombres,apellidos,numeroTelefono,tipoCuenta, correo,habilitado, password=None, **extra_fields):
        return self._create_user( correo,nombres,apellidos,dni,genero,numeroTelefono,tipoCuenta,habilitado, password,False, **extra_fields)

    def create_superuser(self, correo,nombres,apellidos,dni,genero,numeroTelefono,tipoCuenta,habilitado, password=None,**extra_fields):
        return self._create_user(correo,nombres,apellidos,dni,genero,numeroTelefono,tipoCuenta, habilitado, password,True,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    #nombreUsuario = models.CharField('Usuario',max_length = 255, unique = True)
    correo = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    nombres = models.CharField('Nombres',max_length = 255,null=False)
    apellidos = models.CharField('Apellidos',max_length = 255,null=False)
    dni = models.CharField('Dni',max_length=8, null=False, blank = False, unique = True)
    avatar = models.ImageField('Imagen de perfil', upload_to='avatars/', default="avatars/avataruni.png",max_length=255, null=True, blank = True)
    genero = models.CharField('Genero',max_length=1,null = False, blank = False)
    numeroTelefono = models.CharField('Numero Telefono',max_length=12,null = True, blank = True)
    tipoCuenta = models.CharField('Tipo de cuenta',max_length=1,null = True, blank = True,default='0')
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    habilitado = models.BooleanField(default = True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'correo'
    #REQUIRED_FIELDS = ['correo']

    def __str__(self):
        return f'Usuario {self.nombres} con el correo {self.correo}'

