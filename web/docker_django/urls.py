"""UserGroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from UserGroup.views import GroupInfoView,GroupMemberView,test, url_test, docker_test

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Group API Swagger Docs")

urlpatterns = [
    path('', schema_view),
    path('test/', test),
    path('docker_test/', docker_test),
    path('cicd_test/', cicd_test),
    path('admin/', admin.site.urls),
    path('api/groups/', GroupInfoView.as_view()),
    path('api/groups/<group_name>/', GroupMemberView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
