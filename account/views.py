from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from control import Control
from .models import DeviceControl
from .CRC16 import calcString

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


def test(request):
    return render(request, "src/test.html")


# def t(request):
#     if request.method == 'GET':
#         t = request.GET['t']
#         return render(request, "src/test.html")

class controlAPIView(APIView):

    @csrf_exempt
    def post(self, request):
        # print request.POST
        # data = request.POST['light']
        # code = '01 05 0001 FF00'
        # control_light = Control().control()
        # print type(request.POST)
        # stream = BytesIO(request.POST)
        # data = JSONParser().parse(stream)
        # print type(data)
        # print stream
        # print type(request.)
        print request.POST.lists()
        print request.POST.get('redState')
        # print request.POST['light']
        # return type(request.POST.lists())
        # print request.POST['light']
        # print "\n"
        # print request.POST.dict
        return HttpResponse("hah")

    def get(self, request):
        diviceNum = request.GET["diviceNum"]
        # diviceType = request.GET["diviceType"]
        diviceState = request.GET["diviceState"]

        if diviceState == "true":
            diviceState = 1
        else:
            diviceState = 0

        controlObject = DeviceControl.objects.filter(control_num=diviceNum).filter(control_statue=diviceState)
        # controlWay = Control().control(controlObject[0].control_code)
        print(controlObject[0].control_code)
        print type(controlObject[0].control_code)
        print repr(controlObject[0].control_code)
        print type(repr(controlObject[0].control_code))

        INITIAL_MODBUS = 0xFFFF

        print len(repr(controlObject[0].control_code))
        print hex(calcString(repr(controlObject[0].control_code), INITIAL_MODBUS))
        # print diviceNum
        # print diviceState
        return HttpResponse('get')
