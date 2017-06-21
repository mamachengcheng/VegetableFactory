from django.test import TestCase
from django.http import QueryDict
import send
# Create your tests here.


# 读开关状态 01 01 00 01 00 04
# state = str(bin(int(data[6:8], 16)))[2:6]
# 第一个是紫光
# 第二个是蓝光
# 第三个是绿光
# 第四个是红光

# 读开关程度 01 03 00 00 00 04
# data = data.encode('hex')[6:22]
# 红光 int(data[0:4], 16)
# 蓝光 int(data[4:8], 16)
# 绿光 int(data[8:12], 16)
# 紫光 int(data[12:16], 16)

# conent =
State = "01 01 00 01 00 04"
Value = "01 03 00 00 00 04"
state = send.control(State, "state")
value = send.control(Value, "value")
if 1 == len(state):
    # conent['RedState'] = int(str(bin(int(state, 16)))[2:6][0])
    # conent['BlueState'] = 0
    # conent['GreenState'] = 0
    # conent['PurpleState'] = 0
    print int(str(bin(int(state, 16)))[2:6][0])
    print 0
    print 0
    print 0
if 2 == len(state):
    # conent['RedState'] = int(str(bin(int(state, 16)))[2:6][0])
    # conent['BlueState'] = int(str(bin(int(state, 16)))[2:6][1])
    # conent['GreenState'] = 0
    # conent['PurpleState'] = 0
    print int(str(bin(int(state, 16)))[2:6][0])
    print int(str(bin(int(state, 16)))[2:6][1])
    print 0
    print 0
if 3 == len(state):
    # conent['RedState'] = int(str(bin(int(state, 16)))[2:6][0])
    # conent['BlueState'] = int(str(bin(int(state, 16)))[2:6][1])
    # conent['GreenState'] = int(str(bin(int(state, 16)))[2:6][2])
    # conent['PurpleState'] = 0
    print int(str(bin(int(state, 16)))[2:6][0])
    print int(str(bin(int(state, 16)))[2:6][1])
    print int(str(bin(int(state, 16)))[2:6][2])
    print 0
if 4 == len(state):
    # conent['RedState'] = int(str(bin(int(state, 16)))[2:6][0])
    # conent['BlueState'] = int(str(bin(int(state, 16)))[2:6][1])
    # conent['GreenState'] = int(str(bin(int(state, 16)))[2:6][2])
    # conent['PurpleState'] = int(str(bin(int(state, 16)))[2:6][3])
    print int(str(bin(int(state, 16)))[2:6][0])
    print int(str(bin(int(state, 16)))[2:6][1])
    print int(str(bin(int(state, 16)))[2:6][2])
    print int(str(bin(int(state, 16)))[2:6][3])
print int(value[0:4], 16)
print int(value[4:8], 16)
print int(value[8:12], 16)
print int(value[12:16], 16)

# conent['RedValue'] = int(value[0:4], 16)
# conent['BlueValue'] = int(value[4:8], 16)
# conent['GreenValue'] = int(value[8:12], 16)
# conent['PurpleValue'] = int(value[12:16], 16)
# print conent['RedValue']
# print conent['BlueValue']
# print conent['GreenValue']
# print conent['PurpleValue']
# print conent