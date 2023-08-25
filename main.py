import socket
from flask import Flask

app = Flask(__name__)

def GetIP():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return IP

@app.route('/')
def PrintIP():
    ip = GetIP()
    message = "Your Computer IP Address is:" + ip
    return message

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GetIP()

