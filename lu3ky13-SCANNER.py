import requests
import threading
from colorama import Fore, Back, Style
import sys
from time import sleep
from threading import Timer
import time

print(
        Fore.YELLOW +
         """


          \\\|///     
        \\  - -  //   
         (  @ @  )    
  -----oOOo-(_)-oOOo-------------
 |                               |
 |   Cyber Shield                |
 |                               |
 |                               |
  -------------------------------




 [ https://twitter.com/lu3ky13 ]

        """ + Fore.RESET)
time.sleep(5)
print()
print()
file = open('url.txt','r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)
        else :
            print(Fore.RED+'XSS NOT Found: '+url)
            
            
    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
