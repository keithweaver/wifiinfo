from wifiinfo.Connection import *

def about():
    return ('This library will help find the current wifi information based on your OS.')

# os - is the current operating system
# version - the current version of the system
def getWifi(os = 'osx', version = None):
    return Connection(os, version)
