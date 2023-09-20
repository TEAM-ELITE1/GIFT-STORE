import pyotp,requests,re,os,sys
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as tdp
os.system("clear")
def tfa(c):
    try:
        e=re.search("c_user=(\d){15}",c).group().replace("c_user=","")
        url="https://m.facebook.com/security/2fac/setup/intro"
        s=requests.Session()
        
        #1st sub options
        #print("\u001b[1;32mSTEP 1:\u001b[0m")
        
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
        print(f"Link:{u2}")
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
        if "https://m.facebook.com" in x:
            mode =1
        else:
            mode=2
        
        def m1():
            nonlocal c,s,a,x,r2,e
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
                l2="https://m.facebook.com"+l2
                hd = {
                    'Host': 'm.facebook.com',
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
        
            
            lx="https://m.facebook.com"+x
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
                
            print(f"\u001b[1;32mThe Key:{key}")
            
            open("/sdcard/2fk.txt","a").write(e+"\n"+key+"\n")
            
            
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
            l3="https://m.facebook.com"+a["action"]
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
            print(f"\u001b[1;32m{e}")
            return(r4)
        
        #####Recovery Codes
        #open("/sdcard/k4.html","r").read()
        def getRcodes(cc):
            print("\u001b[1;32mGETTING RECOVERY CODES:\u001b[0m")
            sp2=bs(cc,"html.parser")
            #
            
            a=sp2.find_all("form")[1]
            l5="https://m.facebook.com"+a["action"]
            
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
                        u2="https://m.facebook.com"+l
                        
            r6=s.get(u2,cookies={'cookie':c}).text
            open("/sdcard/k6.html","w").write(str(r6))
            
            
            sp2=bs(r6,"html.parser")
            a=sp2.find_all("form")[1]
            inps=a.find_all("input")
            l6="https://m.facebook.com"+a["action"]
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
                
                #tf+=1
                print("\u001b[1;32mRecovery Codes:")
                for i in frc:
                    rcode=i.string
                    print(rcode)
                    open("/sdcard/2fk.txt","a").write("\n"+rcode+"\n")
                print("\u001b[0m")
            except Exception as exp:
                print(exp)
    except Exception as exp:
        print(exp)


c=input("Cookie:")
tfa(c)
