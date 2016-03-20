from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='retirement'),
  url(r'^rs-op-expenditure$', views.rsOpExpenditure, name='rs-op-expenditure'),
  url(r'^rs-auth-positions$', views.rsAuthPositions, name='rs-auth-positions'),
  url(r'^rs-retiree-benefits$',
      views.rsRetireeBenefits,
      name='rs-retiree-benefits'),
  url(r'^rs-federated-funded$',
      views.rsFederatedFundedPercent,
      name='rs-federated-funded'),
  url(r'^rs-police-and-fire-funded$',
      views.rsPoliceAndFireFundedPercent,
      name='rs-police-and-fire-funded'),
]
