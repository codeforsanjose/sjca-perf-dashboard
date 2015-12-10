from django.contrib import admin
from .models import OpExpByService, AuthPosition, OpExpenditure, \
ModeOfCommute, SignalActivity, RoadwayMarking, ParkingDowntown, \
ParkingCitation, StreetLandscape, SidewalkRepair, StreetSweeping, \
StormCall, DrainRequest, StreetRepair, PavementIndexArea, \
PavementIndexSJ, Pothole, RoadFunding

admin.site.register(OpExpByService)
admin.site.register(AuthPosition)
admin.site.register(OpExpenditure)
admin.site.register(ModeOfCommute)
admin.site.register(SignalActivity)
admin.site.register(RoadwayMarking)
admin.site.register(ParkingDowntown)
admin.site.register(ParkingCitation)
admin.site.register(StreetLandscape)
admin.site.register(SidewalkRepair)
admin.site.register(StreetSweeping)
admin.site.register(StormCall)
admin.site.register(DrainRequest)
admin.site.register(StreetRepair)
admin.site.register(PavementIndexArea)
admin.site.register(PavementIndexSJ)
admin.site.register(Pothole)
admin.site.register(RoadFunding)
