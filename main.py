import socket
from flask import Flask
import requests

app = Flask(__name__)

def GetIP():
    import requests

    IP = requests.get('https://api.ipify.org').text
    return IP

@app.route('/')
def PrintIP():
    ip = GetIP()
    message = "Your Computer IP Address is: " + ip
    return message

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

