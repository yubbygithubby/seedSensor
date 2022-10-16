from connectSense import *

try:
    connectESP32()
    print("connected")
except:
    print("can't connect")

count =0

while(count<500):
    print(receiveData())
    count+=1

disconnectESP32()

