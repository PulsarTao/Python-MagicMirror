# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import base64


'''
发送String类型消息给远程人工智能API接口
返回Srting类型的数据
'''
def SendMsg(Msg):
    url = "http://www.tuling123.com/openapi/api"
    data = {'key':'d5f3fdfaccb93969a630f4e46751fde9',
          'info':Msg,
          'userid':'123456'}
    Sjson = urllib.urlencode(data)
    request = urllib2.Request(url, Sjson)
    try:
        res = urllib2.urlopen(request)
        try:
            response = res.read()
            Jresponse = json.loads(response)
            return Jresponse
        except Exception as e:
            print 'Error Object can not be read \n %r' % e
    except Exception as e:
        print'Error URL can not be open \n %r' % e
        print request
        return None
    finally:
        try:
            res.close()
        except Exception as e:
            print 'Error no Object to close'
'''
获取百度TTS的API接口token
返回String类型的token
'''
def Token():
        url = "https://openapi.baidu.com/oauth/2.0/token"
        Tdata = {'grant_type':'client_credentials',
               'client_id':'72n3GYlVpc1n4du35GYOrT4X',
               'client_secret':'3b83be694855a70b46590f18d17aec41'}
        Sjson = urllib.urlencode(Tdata)
        request = urllib2.Request(url, Sjson)
        try:
            res = urllib2.urlopen(request)
            try:
                response = res.read().decode('utf-8', 'ignore')
                Jresponse = json.loads(response)
                return Jresponse['access_token']
            except Exception as e:
                print 'Error can not read json %r' % e
        except Exception as e:
            print 'Error can not open URL %r' % e
            return None
        finally:
            try:
                res.close()
            except Exception as e:
                print 'None Object to close'
'''
启动TTS翻译
返回mp3格式的文件
'''
def TTS(Text):
    tok = Token()
    url = "http://tsn.baidu.com/text2audio"
    Tdata = {'tex':Text,
           'lan':'zh',
           'tok':tok,
           'ctp':1,
           'cuid':7422218}
    Sjson = urllib.urlencode(Tdata)
    request = urllib2.Request(url, Sjson)
    try:
        res = urllib2.urlopen(request)
        try:
            response = res.read()
            return response
        except Exception as e:
                print 'Error can not read json %r' % e
    except Exception as e:
        print 'Error can not open URL %r' % e
        return None
    finally:
        try:
            res.close()
        except Exception as e:
            print 'None Object to close'
    
'''
远程人工智能应答集成模块
由获取的字符串调用方法返回base64格式的语音数据
'''
def Roobot(Msg):
    Msg=Msg.encode('utf-8')
    print Msg
    Text = SendMsg(Msg)
    Text = Text['text']
    Text = Text.encode('utf-8')
    print Text
    Vedio = TTS(Text)
    response = base64.b64encode(Vedio)
    return response

# Union Debug
if  __name__ == '__main__':
    print Roobot("你好")
    exit()
    
    
