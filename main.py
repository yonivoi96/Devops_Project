import socket
from flask import Flask
import requests

app = Flask(__name__)

def GetIP():
    response = requests.get('https://httpbin.org/ip')
    data = response.json()
    IP = data['origin']
    return IP

@app.route('/')
def PrintIP():
    ip = GetIP()
    message = "Your Computer IP Address is: bla"
    return message

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

