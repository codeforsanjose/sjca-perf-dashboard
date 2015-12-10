from django.shortcuts import render_to_response
from .models import OpExpByService, AuthPosition, OpExpenditure, \
ModeOfCommute, SignalActivity, RoadwayMarking, ParkingDowntown, \
ParkingCitation, StreetLandscape, SidewalkRepair, StormCall, \
DrainRequest, StreetSweeping, StreetRepair, PavementIndexArea, \
PavementIndexSJ, Pothole, RoadFunding
from django.http.response import HttpResponse
import json
from util import *

def index(request):
    return render_to_response('transportation/index.html')

def trafficMaintenance(request):
    return render_to_response('transportation/traffic-maintenance.html')

def streetMaintenance(request):
    return render_to_response('transportation/street-maintenance.html')

def parking(request):
    return render_to_response('transportation/parking.html')

def stormDrainage(request):
    return render_to_response('transportation/storm-drainage.html')

def pavementMaintenance(request):
    return render_to_response('transportation/pavement-maintenance.html')

def opExpBySerivce(request):
    data = OpExpByService.objects.filter(active=True)
    chartData = getChartData("pie", data)

    # set series parameters
    chartData["series"][0]["name"] = "Service expenditure"
    chartData["title"]["text"] = "Service expenditure"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def opExpenditure(request):
    data = OpExpenditure.objects.filter(active=True)
    chartData = getChartData("stackedColumn", data)

    # set series parameters
    chartData["series"][0]["name"] = "Non-personal/Equipment"
    chartData["series"][1]["name"] = "Personal services"
    chartData["title"]["text"] = "DOT Operating Expenditures ($millions)"
    chartData["yAxis"]["labels"]["format"] = "${value}"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def authPosition(request):
    data = AuthPosition.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Authorized Positions"
    chartData["title"]["text"] = "DOT Authorized Positions"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def modeOfCommute(request):
    data = ModeOfCommute.objects.filter(active=True)
    chartData = getChartData("bar", data)

    # set series parameters
    chartData["series"][0]["name"] = "Envision 2040 General Plan Target"
    chartData["series"][1]["name"] = "American Community Survey 2014"
    chartData["title"]["text"] = "San Jose Residents' Mode of Commuting to Work"
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

# traffic maintenance
def signalActivities(request):
    data = SignalActivity.objects.filter(active=True)
    chartData = getChartData("stackedColumn", data)

    # set series parameters
    chartData["series"][0]["name"] = "Preventive Maintenance"
    chartData["series"][1]["name"] = "Repairs"
    chartData["title"]["text"] = "Number of Traffic Signal Maintenance Activities"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def roadwayMarkings(request):
    data = RoadwayMarking.objects.filter(active=True)
    chartData = getChartData("line", data)

    # set series parameters
    chartData["series"][0]["name"] = "Roadway Markings"
    chartData["title"]["text"] = "Percent of Roadway Markings Meeting Visibility and Operational Guidelines"
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

#traffic-maintenance END

#parking START
def parkingDowntown(request):
    data = ParkingDowntown.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Parking Customers"
    chartData["title"]["text"] = "Parking Customers at the City's Downtown Facilities (millions) "

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def parkingCitations(request):
    data = ParkingCitation.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Parking Citations"
    chartData["title"]["text"] = "Parking Citations Issued (thousands)"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

# parking - END

# street maintenance - START
def streetLandscapes(request):
    data = StreetLandscape.objects.filter(active=True)
    chartData = getChartData("line", data)

    # set series parameters
    chartData["series"][0]["name"] = "Percent of Street Landscapes in Good Condition"
    chartData["title"]["text"] = "Percent of Street Landscapes in Good Condition"
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def sidewalkRepairs(request):
    data = SidewalkRepair.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Sidewalk Repairs"
    chartData["title"]["text"] = "Sidewalk Repairs"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

# street maintenance - END

# storm drainage - START
def streetSweeping(request):
    data = StreetSweeping.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Debris Collected (Thousand Tons)"
    chartData["series"][1]["name"] = "Curb Sweeping (Thousand Miles) [Right Axis]"
    chartData["series"][1]["type"] = "line"
    chartData["title"]["text"] = "Street Sweeping"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def stormCalls(request):
    data = StormCall.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Storm Calls"
    chartData["title"]["text"] = "Storm Calls"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def drainRequests(request):
    data = DrainRequest.objects.filter(active=True)
    chartData = getChartData("line", data)

    # set series parameters
    chartData["series"][0]["name"] = "Percentage of High Priority Storm Drain Requests"
    chartData["title"]["text"] = "Percentage of High Priority Storm Drain Requests Addressed Within 4 Hours"
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

# storm drainage - END

# pavement maintenance - START
def streetRepairs(request):
    data = StreetRepair.objects.filter(active=True)
    chartData = getChartData("line", data)

    # set series parameters
    chartData["series"][0]["name"] = "Roadway Markings"
    chartData["title"]["text"] = "% of San Jose residents rating street repair as 'excellent or 'good'"
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def pavementIndexArea(request):
    data = PavementIndexArea.objects.filter(active=True)
    chartData = getChartData("bar", data)

    # set series parameters
    chartData["series"][0]["name"] = "2014 Pavement Condition Index"
    chartData["title"]["text"] = "2014 Pavement Condition Index Selected Bay Area Comparisons*"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def pavementIndexSJ(request):
    data = PavementIndexSJ.objects.filter(active=True)
    chartData = getChartData("line", data)

    # set series parameters
    chartData["series"][0]["name"] = "2014 Pavement Condition Index"
    chartData["title"]["text"] = "2014 Pavement Condition Index San Jose"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def potholes(request):
    data = Pothole.objects.filter(active=True)
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Number of Potholes Filled"
    chartData["title"]["text"] = "Number of Potholes Filled (thousands)"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def roadFunding(request):
    data = RoadFunding.objects.filter(active=True)
    chartData = getChartData("stackedColumn", data)

    # set series parameters
    chartData["series"][0]["stack"] = "Today's Annual Funding"
    chartData["series"][1]["stack"] = "Today's one-time need"
    chartData["series"][2]["stack"] = "One-time need in 2020, if continuing current funding"
    chartData["series"][3]["stack"] = "One-time need in 2024, if continuing current funding"
    chartData["title"]["text"] = "Funding Needed to Fix Poor, Failed, and Overdue Roads (in millions)"
    chartData["legend"]["enabled"] = False
    chartData["tooltip"]["enabled"] = False

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

# pavement maintenance - END
