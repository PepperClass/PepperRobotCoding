# coding: utf-8

import requests

def stt(self, URL, header, body):
    respData = requests.post(URL,data=body,headers=header)
    return respData.content
    
