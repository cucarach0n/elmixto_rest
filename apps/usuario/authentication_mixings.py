from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header
from apps.usuario.authentication import ExpiringTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.urls import resolve
from apps.usuario.models import User
class Authentication(object):
    user = None
    userFull = None
    
    def get_user(self,request):
        token = get_authorization_header(request).split()
        current_site = resolve(request.path_info).url_name
        #print(current_site)
        if token:
            print('Validando peticion de :')
            try:
                token = token[1].decode()
                print(token)
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            print('Autenticando token de :')
            try:

                user = token_expire.authenticate_credentials(token)
                print(user)
                if user != None:
                    self.user = user
                    self.userFull = User.objects.filter(correo = user.correo).first()
                    return user 
            except:
                return Response({'error':'Error en la validacion de las credenciales'},status = status.HTTP_403_FORBIDDEN) 
        return None
    def dispatch(self,request,*args,**kwargs):
        user = self.get_user(request)
        #se encontro un token en la peticion
        
        if user is not None:
            #print(self.userFull)
            if self.userFull.is_superuser:
                print('Administrador : '+ self.userFull.correo )
                print(request.path)
            #print('Despachando peticion al usuario ' + user.correo)
            '''
            if type(user) == str:
                response = Response({'error':user,'expired':self.user_token_expire},status = status.HTTP_400_BAD_REQUEST)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            if not self.user_token_expire:
                return super().dispatch(request,*args,**kwargs)
            '''
            return super().dispatch(request,*args,**kwargs)
        response = Response({'error':'Se requieren credenciales validas para esta peticion'},status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response