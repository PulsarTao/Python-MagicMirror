# -*- coding: utf-8 -*-
#集成测试
from Apilib.Rapi import Roobot
from VSerial import VSerial

if __name__=="__main__":
    try:
        print Roobot("hi")
        print VSerial.DeviceCheck()
    except Exception as e:
        print e
    finally:
        print "Done"
    