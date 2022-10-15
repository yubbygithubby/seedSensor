#this is the program used to connect to the esp32 and send the data to adafruit
import socket
import time

#bluetooth connection
#The address of the esp32
#establish connection
esp32Address = "10:97:BD:0A:29:EE"
port = 1
connection = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

def connectESP32():
    connection.connect((esp32Address, port))

def receiveData():
    data = connection.recv(115200)
    if data != '1':
        return 'OFF'
    return 'SENSED'

def testData():
    currentTime = int(time.time())
    if currentTime % 2 == 0:
        return 'SENSED'
    else:
        return 'OFF'


def disconnectESP32():
    connection.close()

