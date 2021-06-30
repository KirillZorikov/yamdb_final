from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path(f'{settings.PROJECT_NAME}/admin/', admin.site.urls),
    path(f'{settings.PROJECT_NAME}/api/', include('api.urls')),
    path(f'{settings.PROJECT_NAME}/api/', include('api_users.urls')),
    path(
        f'{settings.PROJECT_NAME}/redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc',
    ),
]
