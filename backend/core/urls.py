from django.contrib import admin
from django.urls import path, include

from apps.management.urls import router as management_router
from apps.reservations.urls import router as reservations_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('management/', include(management_router.urls)),
        path('reservations/', include(reservations_router.urls)),
    ])),
]
