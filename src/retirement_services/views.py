from django.shortcuts import render_to_response
from .models import (RSOpExpenditure,
                     RSAuthPosition,
                     RSRetireeBenefits,
                     RSFederatedFundedPercent,
                     RSPoliceAndFireFundedPercent)
from util import *
from django.http.response import HttpResponse
import json

def index(request):
    return render_to_response('retirement/index.html')

def rsOpExpenditure(request):
    data = RSOpExpenditure.objects.filter(active=True)
    if not data.count():
        return HttpResponse({}, content_type="application/json")

    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Retirement Services Operating Expenditures"
    chartData["title"]["text"] = "Retirement Services Operating Expenditures ($millions)"
    chartData["yAxis"]["labels"]["format"] = "${value}"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def rsAuthPositions(request):
    data = RSAuthPosition.objects.filter(active=True)
    if not data.count():
        return HttpResponse({}, content_type="application/json")
    chartData = getChartData("column", data)

    # set series parameters
    chartData["series"][0]["name"] = "Retirement Services Authorized Positions"
    chartData["title"]["text"] = "Retirement Services Authorized Positions"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def rsRetireeBenefits(request):
    data = RSRetireeBenefits.objects.filter(active=True)
    if not data.count():
        return HttpResponse({}, content_type="application/json")

    chartData = getChartData("line", data)
    chartData["title"]["text"] = ("Retirement Services"
                                  " Pension and Retiree Health"
                                  " and Dental Benefits ($millions)")
    chartData["yAxis"]["labels"]["format"] = "${value}"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def rsFederatedFundedPercent(request):
    data = RSFederatedFundedPercent.objects.filter(active=True)
    if not data.count():
        return HttpResponse({}, content_type="application/json")

    chartData = getChartData("line", data)
    chartData["title"]["text"] = ("Retirement Services"
                                  " Federated Funded Status")
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")

def rsPoliceAndFireFundedPercent(request):
    data = RSPoliceAndFireFundedPercent.objects.filter(active=True)
    if not data.count():
        return HttpResponse({}, content_type="application/json")

    chartData = getChartData("line", data)
    chartData["title"]["text"] = ("Retirement Services"
                                  " Police and Fire Funded Status")
    chartData["yAxis"]["labels"]["format"] = "{value}%"

    response = {}
    response['chartData'] = chartData
    responseData = json.dumps(response)

    return HttpResponse(responseData, content_type="application/json")
