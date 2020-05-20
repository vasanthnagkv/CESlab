import serial
from win10toast import ToastNotifier
import time
import os
import ctypes

toaster = ToastNotifier()
arduino = serial.Serial('COM5', 115200, timeout=.1)
warningNum=0

while True:
	data = arduino.readline()[:-2]  #the last bit gets rid of the new-line chars
	if data:
            lightValue = data.decode('utf-8')
            print(lightValue)
            if (int(lightValue) < 300):
                warningNum = 0
                

            if(int(lightValue) > 300 and (warningNum < 2)):
                print("Its DARK with " + lightValue)
                toaster.show_toast("its DARK",
                   icon_path=None,
                   duration=3)
                print("warning "+ str(warningNum))
                time.sleep(150)
                arduino.flushInput()
                warningNum = warningNum + 1
                             
            elif(warningNum == 2):
                toaster.show_toast("Logging off due to DARKNESS" + str(lightValue),
                   icon_path=None,
                   duration=3)
                ctypes.windll.user32.LockWorkStation()
                time.sleep(10)
                arduino.flushInput()
                