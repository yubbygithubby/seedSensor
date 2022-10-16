from unittest import result

from numpy import recfromcsv
from connectSense import *
currentData = 'OFF'
try:
    connectESP32()
    print("connected")
except:
    print("can't connect")

count = 0

while(count<500):
    result = receiveData(currentData)
    print(result)
    count+=1

disconnectESP32()

