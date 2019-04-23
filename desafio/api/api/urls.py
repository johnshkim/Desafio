
from django.contrib import admin
from django.urls import path, include
from core.views import CadastroViewSet
from rest_framework import routers
#definicao de rotas para acesso pelo navegador
router = routers.DefaultRouter()
router.register('cadastros', CadastroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
