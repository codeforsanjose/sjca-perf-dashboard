from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='retirement'),
  url(r'^rs-op-expenditure$', views.rsOpExpenditure, name='rs-op-expenditure'),
  url(r'^rs-auth-positions$', views.rsAuthPositions, name='rs-auth-positions')
]
