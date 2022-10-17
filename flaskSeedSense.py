from operator import truediv
from flask import Flask, jsonify, render_template, request
from connectSense import *
import sys


app = Flask(__name__, template_folder="templates")

global ip
global connected

ip = "172.19.61.109"

connected = False

currentData = 'OFF'
@app.route('/_stuff', methods = ['GET'])
def stuff():
    #return jsonify(result = receiveData())
    global connected
    global currentData
    if connected:
        toReturn = receiveData(currentData)
        currentData = toReturn
        return jsonify(result = toReturn)
    return jsonify(result = testData())

@app.route('/')
def first_function():
   return render_template('index.html')

@app.route('/_connect', methods = ['GET'])

def connect():
    global connected
    print(f"before{connected}", file=sys.stdout)

    try:
        if connected == False:
            connected = True
            print(f"after{connected}", file = sys.stdout)
            return jsonify(isconnect = 'true')
        else:
            return jsonify(isconnect = 'true')

    except:
        return jsonify(isconnect = 'false')
        
@app.route('/test')
def returnTest():
    return jsonify(result = "hell")

@app.route('/displayData')
def displayData():
    try:
         connectESP32()
         connected = True
    except:
        pass

    return render_template('dataDisplay.html')


if __name__ == "__main__":

    #app.run(host=ip, debug=True)
    app.run(debug=True)