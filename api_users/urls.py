from django.urls import include, path
from rest_framework import routers

from . import views

router_users = routers.DefaultRouter()

router_users.register(
    'users', views.UserViewSet, basename='user',
)

auth_urls = [
    path('token/', views.token_obtain, name='get_token'),
    path('email/', views.pre_reg, name='pre_reg'),
]

urlpatterns = [
    path('v1/', include(router_users.urls)),
    path('v1/auth/', include(auth_urls)),
]
