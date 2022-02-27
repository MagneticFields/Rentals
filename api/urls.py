from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as token_views

from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', token_views.obtain_auth_token)
]
