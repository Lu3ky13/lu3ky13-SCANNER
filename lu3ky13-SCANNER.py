
from re import A, X
from urllib.error import URLError
import requests
import threading
import sys
from time import sleep
from threading import Timer
import time
import getpass

red = "\033[91m"
green = "\33[42m"
yellow = "\33[33m"
end = "\33[0m"


def domain(domain):
    #x=input(Fore.GREEN +'Enter your url:-')
    r = requests.get(f'http://web.archive.org/cdx/search/cdx?url=*.{domain}&output=text&fl=original&collapse=urlkey')
    with open('url.txt', 'a') as f:
        f.write('\n')
        f.writelines(str(r.text))
        f.write('\n')


def subdomain(subdomain):
    r = requests.get(f'http://web.archive.org/cdx/search/cdx?url={subdomain}&output=text&fl=original&collapse=urlkey')
    with open('url.txt', 'a') as f:
        f.write('\n')
        f.writelines(str(r.text))
        f.write('\n')


def Send_req(url,payload):
    
    file = open('url.txt','r',encoding='utf-8')
    payloads = open('payloads.txt','r',encoding='utf-8')
    try:
        url = url.replace("=",f"={payload}")
    

        res = requests.get(url)
        if payload in res.text:
           print(f"{green}-- XSS Found   -->  {url}  {end}")
           with open('Output.txt', 'a') as f:
            f.write('\n')
            f.writelines(url)
            f.write('\n')
        else :
            print(f"{red}XSS NOT Found: {url}{end}")
        
    except Exception as e:
        file = file.readlines()
        for payload in payloads:
            for url in file:
                url = url.strip('\n')
                payload = payload.strip('\n')
                threading.Thread(target=Send_req,args=(url,payload,)).start()
    except KeyboardInterrupt:
        input(f"\n{red}You Wanna Cancel Brute Force ? Press Any Key To Cancel:{end}")
        print(f"{yellow}Thanks For Using Tool, Have Nice Day :)")
        sys.exit(0)
        
def main():
    print(f"""
        {yellow}
         


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

       {end} """ )
    time.sleep(0.5)
    
    while True:
        try:
            print("""
Choose a Number, Attention Choose a True Number !:
1) Web Archive Domain
2) Web Archive Subdomain
3) Start XSS Brute Forcing
4) About Us
    """)
            option = input(f"{red}Lu3cky${getpass.getuser()}:{yellow} Choose A Number =>{end}")
            if option == "1":
                web = input(f"{red}Lu3cky${getpass.getuser()}:{yellow} Enter A Domain:{end}")
                domains = web
                domain(domains)
            elif option == "2":
                subweb = input(f"{red}Lu3cky${getpass.getuser()}:{yellow} Enter A Subdomain:{end}")
                subdomains = subweb
                subdomain(subdomains)
            elif option == "3":
                file = open('url.txt','r')
                payloads = open('payloads.txt','r')
                print(f"Brute Force Been Started !!")
                Send_req(file,payloads)
            elif option == "4":
                print("We Are Cyber Shield Kurdish Cyber Secruity Team \nWe work pentesting and benifit hacking tutorials\nIf you need contact us to one of admin thats all social medias:\nFacebook:https://www.facebook.com/cybershield.team\nInstagram:https://www.instagram.com/cyber_shield_team/\nYoutube:https://www.youtube.com/c/cybershieldteam")
            else:
                print("Wrong Number ! Try Again Later !")
        except KeyboardInterrupt:
            input(f"{red} You Wanna Cancel Process ? Press Any Key To Cancel:{end}")
            print(f"{red} Thanks For Using Tool, Have Nice Day :){end}")
            sys.exit(0)
            
    
if __name__ == '__main__':
    main()
