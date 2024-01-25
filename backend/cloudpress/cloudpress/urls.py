from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cms.views import CategoryViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
