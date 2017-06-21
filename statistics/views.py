import json
from django.http import HttpResponse, QueryDict
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LineChartSerializers, SittingHistorySerializers, DataHistorySerializers
from .models import MinuteStatistics, HourStatistics, SittingHistory
# Create your views here.


class LineChartAPIView(APIView):
    def get(self, request):
        minuteStatisticsData = MinuteStatistics.objects.order_by('updateTime')[0:1]
        lineChartSerializers = LineChartSerializers(minuteStatisticsData, many=True)
        return HttpResponse(json.dumps(lineChartSerializers.data))


class SittingHistoryAPIView(APIView):
    def get(self, request):
        numPage = request.GET['numPage']
        sittingHistory = SittingHistory.objects.all()
        paginator = Paginator(sittingHistory, 10)
        sittingHistorySerializers = SittingHistorySerializers(paginator.page(numPage).object_list, many=True)
        centent = QueryDict(mutable=True)
        centent['sittingDataList'] = sittingHistorySerializers.data
        centent['pageNumber'] = paginator.num_pages
        return HttpResponse(json.dumps(centent.dict()))


class DataHistoryAPIView(APIView):
    def get(self, request):
        date = request.GET['date']
        print date
        hourStatistics = HourStatistics.objects.filter(data=date).all()
        print hourStatistics
        dataHistorySerializers = DataHistorySerializers(hourStatistics, many=True)
        return HttpResponse(json.dumps(dataHistorySerializers.data))
        # return HttpResponse("OK")