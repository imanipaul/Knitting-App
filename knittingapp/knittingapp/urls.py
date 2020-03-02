"""knittingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from app.views import UserViewSet, YarnViewSet, NoteViewSet, PatternViewSet, NeedleViewSet, ProjectViewSet
from rest_framework.routers import DefaultRouter

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)

router.register(r'api/users', UserViewSet, basename='user')
router.register(r'api/yarns', YarnViewSet, basename='yarn')
router.register(r'api/notes', NoteViewSet, basename='note')
router.register(r'api/patterns', PatternViewSet, basename='pattern')
router.register(r'api/needles', NeedleViewSet, basename='needle')
router.register(r'api/projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth')
]
