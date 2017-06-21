from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
import send
from .models import DeviceControl
from statistics.models import SittingHistory
import CRC16

# Create your views here.
def indexPage(request):
    return render(request, "src/index.html")


def adminPage(request):
    return render(request, "src/app/account/admin.html")


def signInPage(request):
    return render(request, "src/app/account/signin.html")


def signUpPage(request):
    return render(request, "src/app/account/signup.html")


def controlPage(request):
    return render(request, "src/app/account/control.html")

def historyDataPage(request):
    return render(request, "src/app/account/historydata.html")



# def t(request):
#     if request.method == 'GET':
#         t = request.GET['t']
#         return render(request, "src/test.html")

class controlAPIView(APIView):

    def get(self, request):
        diviceNum = request.GET["diviceNum"]
        controlType = request.GET["controlType"]
        diviceState = request.GET["diviceState"]
        controlObject = ""

        if controlType == '0':
            if diviceState == "true":
                diviceState = 1
            else:
                diviceState = 0

            controlObject = DeviceControl.objects.filter(control_num=diviceNum).filter(control_statue=diviceState).get()

            code = controlObject.control_code
        else:
            diviceState = int(str(diviceState))
            if diviceState >= 16 and diviceState <= 100:
                state_code = ' 00 ' + str(hex(diviceState))[2:4].upper()
                controlObject =DeviceControl.objects.filter(control_type=controlType).filter(control_num=diviceNum).get()
                code = controlObject.control_code + state_code

            elif diviceState >= 0 and diviceState < 16:
                state_code = ' 00 0' + str(hex(diviceState))[2:3].upper()
                controlObject =DeviceControl.objects.filter(control_type=controlType).filter(control_num=diviceNum).get()
                code = controlObject.control_code + state_code

        send.control(code)
        sittingHistory = SittingHistory()
        sittingHistory.deviceName = controlObject.control_deviceName
        sittingHistory.sittingContent = controlObject.control_name
        sittingHistory.save()
        print code
        return HttpResponse('get')

# class ajaxAPIView(APIView):
#
#     def get(self, request):
#         val = request.GET["val"]
#         print "ajax"+val
#         return HttpResponse("ajax"+val)
