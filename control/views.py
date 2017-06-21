from django.shortcuts import render
import send
from rest_framework.views import APIView
from django.http import QueryDict
from django.http import HttpResponse
import json
# Create your views here.

State = "01 01 00 01 00 04"
Value = "01 03 00 00 00 04"


class ControlStateAPIView(APIView):
    def get(self, request):
        conent = QueryDict(mutable=True)
        state = send.control(State, "state")
        state = bin(int(state, 16))[2:6]
        value = send.control(Value, "value")
        if 1 == len(state):
            conent['RedState'] = int(str(state)[-1])
            conent['BlueState'] = 0
            conent['GreenState'] = 0
            conent['PurpleState'] = 0
        if 2 == len(state):
            conent['RedState'] = int(str(state)[-1])
            conent['BlueState'] = int(str(state)[-2])
            conent['GreenState'] = 0
            conent['PurpleState'] = 0
        if 3 == len(state):
            conent['RedState'] = int(str(state)[-1])
            conent['BlueState'] = int(str(state)[-2])
            conent['GreenState'] = int(str(state)[3])
            conent['PurpleState'] = 0
        if 4 == len(state):
            conent['RedState'] = int(str(state)[-1])
            conent['BlueState'] = int(str(state)[-2])
            conent['GreenState'] = int(str(state)[-3])
            conent['PurpleState'] = int(str(state)[-4])
        conent['RedValue'] = int(value[0:4], 16)
        conent['GreenValue'] = int(value[4:8], 16)
        conent['BlueValue'] = int(value[8:12], 16)
        conent['PurpleValue'] = int(value[12:16], 16)
        return HttpResponse(json.dumps(conent.dict()))
