import hashlib
import json
import os

def getIp():
    ip = os.popen('curl -s ifconfig.me').readline()
    return ip

def addTransaction(message, queue):
    queue.digest(b"{0}".format(message))
    return queue

def createTransaction(startAddress, amount, fee, endAddress):
    transaction = {
                "startAddress":str(startAddress),
                "amount":float(amount),
                "fee":float(fee),
                "endAddress":str(endAddress)
                }
    return transaction
