from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('transportation.urls')),

    # transportation
    url(r'^transportation/', include('transportation.urls')),

    # retirement
    url(r'^retirement/', include('retirement_services.urls')),
]
