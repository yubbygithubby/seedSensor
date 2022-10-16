from operator import truediv
from flask import Flask, jsonify, render_template, request
from connectSense import *

app = Flask(__name__, template_folder="templates")

connected = False

@app.route('/_stuff', methods = ['GET'])
def stuff():
    #return jsonify(result = receiveData())
    if connected:
        return jsonify(result = receiveData())
    return jsonify(result = testData())

@app.route('/')
def first_function():
   return render_template('index.html')

@app.route('/_connect', methods = ['GET'])
def connect():
    try:
        if connected == False:
            connectESP32()
            connected = True
            return jsonify(isConnected = 'true')
        else:
            return jsonify(isConnected = 'true')

        

    except:
        return jsonify(isConnected = 'false')
        
@app.route('/displayData')
def displayData():
    try:
         connectESP32()
         connected = True
    except:
        pass

    return render_template('dataDisplay.html')


if __name__ == "__main__":
  #app.run(host='192.168.0.163', debug=True)
  app.run(debug=True)