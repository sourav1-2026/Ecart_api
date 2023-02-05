
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls.static import static
from django.conf import settings

from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('categoryapi', views.CategoryView, basename='category')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accounts.urls')),
    path('api/', include(router.urls)),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)