from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='transportation'),

  # index
  url(r'^op-exp-by-serivce$', views.opExpBySerivce, name='op-exp-by-serivce'),
  url(r'^op-expenditure$', views.opExpenditure, name='op-expenditure'),
  url(r'^auth-position$', views.authPosition, name='auth-position'),
  url(r'^mode-of-commute$', views.modeOfCommute, name='mode-of-commute'),

  # traffic-maintenance
  url(r'^traffic-maintenance$', views.trafficMaintenance, name='traffic-maintenance'),
  url(r'^signal-activities$', views.signalActivities, name='signal-activities'),
  url(r'^roadway-markings$', views.roadwayMarkings, name='roadway-markings'),

  # parking
  url(r'^parking$', views.parking, name='parking'),
  url(r'^parking-downtown$', views.parkingDowntown, name='parking-downtown'),
  url(r'^parking-citations$', views.parkingCitations, name='parking-citations'),

  # streetscapes maintenance
  url(r'^street-maintenance$', views.streetMaintenance, name='street-maintenance'),
  url(r'^street-landscapes$', views.streetLandscapes, name='street-landscape'),
  url(r'^sidewalk-repairs$', views.sidewalkRepairs, name='sidewalk-repairs'),

  # storm drainage
  url(r'^storm-drainage$', views.stormDrainage, name='storm-drainage'),
  url(r'^street-sweeping$', views.streetSweeping, name='street-sweeping'),
  url(r'^storm-calls$', views.stormCalls, name='storm-calls'),
  url(r'^drain-requests$', views.drainRequests, name='drain-requests'),

  # pavement maintenance
  url(r'^pavement-maintenance$', views.pavementMaintenance, name='pavement-maintenance'),
  url(r'^street-repairs$', views.streetRepairs, name='street-repairs'),
  url(r'^pavement-index-area$', views.pavementIndexArea, name='pavement-index-area'),
  url(r'^pavement-index-sj$', views.pavementIndexSJ, name='pavement-index-sj'),
  url(r'^potholes$', views.potholes, name='potholes'),
  url(r'^road-funding$', views.roadFunding, name='road-funding')
]
