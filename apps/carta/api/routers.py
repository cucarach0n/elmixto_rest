from rest_framework.routers import DefaultRouter
from apps.carta.api.views.producto_views import *
from django.urls import path
router = DefaultRouter()

router.register(r'producto',ProductoViewSet, basename = 'Producto-view')

urlpatterns = router.urls 