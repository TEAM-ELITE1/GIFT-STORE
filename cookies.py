import os,random 
try:
    import bs4
except:
    os.system("pip install bs4")
    import bs4
try:
    import requests
except: 
    os.system("pip install requests")
    import requests 
import re
from bs4 import BeautifulSoup as bunny
rq= requests.Session()
limi=[]
#Mathod 1
test=bunny(rq.get("https://www.facebook.com/100091887965586/posts/129952413411024/?mibextid=kgD8tqJhEpGAe4Sj").text,"html.parser")
heron=re.findall('"text":"(.*?)"',str(test))
#mathod 2
logo=("""
\033[1;97m88""Yb 88   88 88b 88 88b 88 \033[1;91mYb  dP 
\033[1;97m88__dP 88   88 88Yb88 88Yb88  \033[1;91mYbdP  
\033[1;97m88""Yb Y8   8P 88 Y88 88 Y88  \033[1;91m 8P   
\033[1;97m88oodP `YbodP' 88  Y8 88  Y8  \033[1;91mdP    
\033[1;90m———————————————————————————————————
 \033[1;97m[\033[47m\033[1;92m>)\x1b[0m\033[1;97m OWNER       : Bunny(ᗒᗣᗕ)՞
 \033[1;97m[\033[47m\033[1;92m>)\x1b[0m \033[1;97mFACEBOOK    : Md Banny 
 \033[1;97m[\033[47m\033[1;92m>)\x1b[0m \033[1;97mGITHUB      : \033[1;92mBUNNY-143
\033[1;90m———————————————————————————————————""")
data=[]
def main():
    os.system("clear")
    print(logo)
    if len(limi) <4:
        for xxx in heron:
            if 'c_user' in xxx:
                data.append(xxx)
    print("\n\033[47m\033[1;91mCOOKIES\x1b[0m:\033[1;92m "+random.choice(data))
    fuck=input("\n\n\033[1;97m[)————————\033[1;93mPress Enter")
    main()
main()



