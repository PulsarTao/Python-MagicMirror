# -*- coding: utf-8 -*-
'''
获取串口通信数据
'''
import serial  
import serial.tools.list_ports  
import time

'''
读取串口数据
'''
def SoundCheck():
    ser=serial.Serial("COM4")
    #ser.open()
    data = ''
    #函数循环测试
    while True :
        ser.write(data)
        data = ser.read(1)
        time.sleep(1)
        if data != '':
            print data
'''
检测已连接的串口
'''
def DeviceCheck():
    port_list = list(serial.tools.list_ports.comports())  
    if len(port_list) <= 0:  
        return None  
    else:
        try:
            port_list_0 =list(port_list[0])  
            port_serial = port_list_0[0]
            ser = serial.Serial(port_serial,9600,timeout = 6)
            ser.close()
            return ser.name.encode("utf-8")
            ser.open()
            print ser.isOpen()
            ser.close
        except Exception as e:
            print "COM Error! \n %r " % e
            return None
        
#Union debug
if __name__=="__main__":
    print DeviceCheck()
    SoundCheck()