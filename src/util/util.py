# Common utility functions
import copy, collections, unicodedata

defaultChartData = {
      "chart": {
        "type": ""
      },
      "xAxis": {
        "categories": ""
      },
      "legend": {
        "enabled": True
      },
      "yAxis": {
        "title": {
          "text": ""
        },
        "labels": {
          "format": "{value}"
        },
        "min": 0,
        "stackLabels": {
            "enabled": True,
            "format": "{stack}"
        }
      },
      "credits": {
        "enabled": False
      },
      "tooltip": {
        "pointFormat": '{series.name}: <b>{point.y}</b>',
        "enabled": True
      },
      "title": {
        "text": ''
      },
      "plotOptions": {
        "pie": {
            "allowPointSelect": True,
            "cursor": 'pointer',
            "dataLabels": {
                "enabled": True,
                "format": '<b>{point.name}</b>: ${point.y}'
            }
        },
        "series": {
            "stacking": ""
        }
      },
      "series": []
    }

def getPieData(data):
    chartData = copy.deepcopy(defaultChartData)
    chartData["chart"]["type"] = "pie"
    seriesData = []

    for datum in data:
        dataPoint = []
        service = unicodedata.normalize('NFKD', datum.service)\
        .encode('ascii','ignore')
        dataPoint.append(service)
        dataPoint.append(datum.value)
        seriesData.append(dataPoint)

    # construct one series
    series = {}
    series["data"] = seriesData

    chartData["series"].append(series)

    return chartData

def getColumnData(data):
    chartData = copy.deepcopy(defaultChartData)
    chartData["chart"]["type"] = "column"
    category = defaultCategory = "default"
    seriesData = collections.OrderedDict()
    seriesArr = []
    xCategs = []

    for datum in data:
        formattedYear = unicodedata.normalize('NFKD', datum.formattedYear)\
        .encode('ascii','ignore')

        if hasattr(datum, 'category'):
            category = datum.category

        if category not in seriesData:
            seriesData[category] = []

        if formattedYear not in xCategs:
            xCategs.append(formattedYear)

        datapoint = {}
        datapoint['y'] = datum.value
        seriesData[category].append(datapoint)


    for category in seriesData:
        series = {}
        if category != defaultCategory:
            series['name'] = category
        series["data"] = seriesData[category]
        seriesArr.append(series)

    chartData["series"] = seriesArr
    chartData["xAxis"]["categories"] = xCategs

    return chartData

def getBarData(data):
    chartData = getColumnData(data)
    chartData["chart"]["type"] = "bar"

    return chartData

def getLineData(data):
    chartData = getColumnData(data)
    chartData["chart"]["type"] = "line"

    return chartData

def getStackedColumnData(data):
    chartData = getColumnData(data)
    chartData["plotOptions"]["series"]["stacking"] = "normal"

    return chartData

def getStackedBarData(data):
    chartData = getColumnData(data)
    chartData["plotOptions"]["series"]["stacking"] = "normal"
    chartData["chart"]["type"] = "bar"

    return chartData


funcMap = {
    "pie": getPieData,
    "column": getColumnData,
    "bar": getBarData,
    "line": getLineData,
    "stackedBar": getStackedBarData,
    "stackedColumn": getStackedColumnData
}

def getChartData(type, data):
    return funcMap[type](data)
