import shodan
import sys
import subprocess
import os

try:
    def brr():
        #start adb
        os.system("adb start-server")
        count = 0
        for ip in ips:
            ip = ip.strip()
            count = count + 1
            print("Connecting to: "+ str(count) + ' Time for => ' + ip)
            os.system("adb connect "+ip+":5555")
            pass

except:
    print("Some error has occurred, please check your internet connection !!")

with open("ips.txt", "r") as ips:
    brr()
