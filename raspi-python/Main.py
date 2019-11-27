import os
import datetime
import glob
import time
import base64
import sys
import pymysql

#카메라 라이브러리
import picamera
import RPi.GPIO as GPIO

#통신 라이브러리
#import urllib.response
#import urllib.request
#import http.server
#import webiopi

#각 기능별 모듈 import
import temper
import relay
import cam
import events
import client


def runningTime(self):
    pass

def nowMin(self, nowTime):
    self.nowTime = nowTime
    min = nowTime.strftime('%M')
    return min
    
if __name__ == "__main__" :
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave' #temp_sensor

    image_folder = '/home/pi/Documents/test/'

    db = pymysql.connect(host='18.216.172.165', user='pi', passwd='pikey999', db='raspi_db', charset='utf8');
    cur = db.cursor();

    temper = temper
    cam = cam

    while True:
        err = 0
        toggle = 0
        nowTime = datetime.datetime.now()
        if(nowMin(nowTime)%10 == 0):
            temper.sendtmpDB(db)
            events.endevtDB(temper, err)
        elif(nowMin(nowTime)%23 == 0):
            cam.sendomgDb(db)
            events.endevtDB(cam, err)
        signal = client.datas
        if(signal == 0):
            relay.ctrl(toggle)
        elif(signal == 1):
            relay.ctrl(toggle)

        
        
    
