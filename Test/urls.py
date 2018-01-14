"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from project_models.api import urls as proj_model_urls
from rest_framework.authtoken import views
from project_models.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),

    url(r'^api/', include(proj_model_urls, namespace='proj_models')),

    # api auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]