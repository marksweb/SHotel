from django.contrib import admin
from django.urls import path, include

from apps.management.urls import router as management_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(management_router.urls)),
]
