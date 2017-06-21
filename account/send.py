# **coding: utf-8**
import socket
import CRC16
import struct

host = '192.168.1.103'
port = 40000

def control(code):
    code = CRC16.crc(code)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Strange error creating socket: %s" % e
    try:
        s.connect((host, port))
        s.send(code)
        s.close()
    except:
        print "error"

control("01 05 00 01 00 00")