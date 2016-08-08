#-*- coding: utf-8 -*-
import Rapi
import urllib2
import urllib
import wave
import base64

'''
读取temp的wav文件
返回包含base64编码的语音和文件长度数组
'''
def ReadTemp():
    fp = wave.open('temp.wav', 'rb')  
    nf = fp.getnframes()  
    Vlen = nf * 2  
    Vdata = fp.readframes(nf)
    
'''
获取本地temp数据
发送识别数据到百度语音识别平台
由返回的识别数据json格式中获取识别信息
'''
def SendVdata():
    
    return 0 