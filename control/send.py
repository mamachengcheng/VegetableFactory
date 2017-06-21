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
        if "state" == type:
            state = data.encode('hex')[6:8]
            return state
        elif "value" == type:
            value = data.encode('hex')[6:22]
            return value
        s.close()
        return
    except:
        print "error"
