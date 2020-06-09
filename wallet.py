import hashlib
import json
import os
import socket
import datetime

def getIp():
    ip = os.popen('curl -s ifconfig.me').readline()
    return ip

def createTransaction(startAddress, amount, fee, endAddress, utcTime):
    with open("queue.json", "r") as outfile:
        queue = json.loads(queue, outfile)
    transaction = {
                "startAddress":str(startAddress),
                "amount":float(amount),
                "fee":float(fee),
                "endAddress":str(endAddress),
                "utcTime":datetime.datetime.utcnow(),
                "difficulty":0,
                "blockHeight":0
                }

    with open("queue.json", "w") as outfile:
        json.dump(queue, outfile)
    return transaction

def getBalance():
    pass

blockStatus = {
    "upToDate":False,
    "blockSource":False,
    "lastBlock":0
}

#block source to other wallets
source = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
source.bind((getIp(), 7777))

#main loop
while True:
    print("Balance, options")
    option = input("What would you like to do? (Enter the number) ")
