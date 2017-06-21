# **coding: utf-8**
import socket
from account import CRC16


# 温度和湿度 有小数点
# 光照强度和二氧化碳浓度没有小数点

host = '192.168.1.103'
port = 40000


def control(code, type):
    code = CRC16.crc(code)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Strange error creating socket: %s" % e
    try:
        s.connect((host, port))
        s.send(code)
        data = s.recv(2048)
        data = data.encode('hex')[6:10]
        if "Temperature" == type or "Humidity" == type:
            data = int(str(int(data, 16))[0:2]) + int(str(int(data, 16))[2:3]) * 0.1
        elif "illumination" == type:
            data = int(str(int(data, 16))[2:5])
        else:
            data = int(data, 16)
        s.close()
        return data
    except:
        print "error"
