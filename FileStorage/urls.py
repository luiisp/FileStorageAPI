from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Storage.views import FileViewSet, FileDownloadAPIView,UsersViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'files', FileViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('download/<int:file_id>/', FileDownloadAPIView.as_view(), name='download_file'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)