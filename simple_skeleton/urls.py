from django.conf.urls import include, path
from django.contrib import admin

from simple_skeleton.apps.core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('admin/', include(admin.site.urls)),
]
