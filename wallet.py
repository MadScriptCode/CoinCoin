import hashlib
import json
import os
import socket
import datetime

def getIp():
    ip = os.popen('curl -s ifconfig.me').readline()
    return ip

def createTransaction(startAddress, amount, fee, endAddress, utcTime, queue):
    with open("queue.json", "r") as outfile:
        queue = json.loads(queue, outfile)
    transaction = {
                "startAddress":str(startAddress),
                "amount":float(amount),
                "fee":float(fee),
                "endAddress":str(endAddress),
                "utcTime":datetime.datetime.utcnow()
                }

    with open("queue.json", "w") as outfile:
        json.dump(queue, outfile)
    return transaction
