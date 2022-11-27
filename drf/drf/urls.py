from django.contrib import admin
from api import views
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cake', views.CakeViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]