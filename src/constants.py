import threading
import socket
import time

PORT = 8000
SERVER = 'localhost'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'