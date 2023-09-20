#SHELL FINDER V1
#Change Or Edit Author COPYRIGHT Never Make You Coder, Don't Be A Bastard Dude!
#Coded By Wissem Mahfoud
#I Accept All Responsibility For Any illegal Usage.
#Owner-TN
import threading
from multiprocessing.dummy import Pool
import os,sys,time
from bs4 import BeautifulSoup
from platform import system
import random
import datetime
import cookielib
import os
import re
from colorama import Fore								
from colorama import Style								
from colorama import init												
import requests, re, os, base64;
import urllib, httplib, urllib2
from multiprocessing.dummy import Pool as ThreadPool
try:
    os.system('title SHELL FINDER V1')
except:
    pass
if system() == 'Windows':
    os.system('cls')
elif system() == 'Linux':
    os.system('clear')
else:
    pass
########### COLOR ############ 
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										
##############################  
print ('''{}{}
              ________
            /'        /|
           /         / |_
          /         /  //|
         /_________/  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
       / // // /// | /   8//|      SHELL FINDER V1                                       
      / // // ///__|/    8//|      CODED BY WISSEM MAHFOUD
     /.(_)// /// |       8///|     THINK TWICE, CODE ONCE
    (_)' `(_)//| |       8////|___________ 
   (_) /_\ (_)'| |        8///////////////
   (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
      `(_)'  d'  H`b
            d'   `b`b
           d'     H `b
          d'      `b `b
         d'           `b
        d'             `b  
        
''').format(fr,sb)
now = datetime.datetime.now()
print('\n\033[92m                        STARTED AT: ' + str(now))
################################
def backdoor(url):
    try:

        url = url.strip()
        paths = ['wso.php','css/1/jou.php','FARES.php','COPYRIGHT.php','fares.php','WSO.php','dz.php','w.php','wp-content/plugins/akismet/akismet.php','images/stories/w.php','w.php','shell.php','cpanel.php','cpn.php','sql.php','mysql.php','config.php','configuration.php','madspot.php','Cgishell.pl','killer.php','changeall.php','2.php','Sh3ll.php','dz0.php','dam.php','user.php','dom.php','whmcs.php','r00t.php','1.php','a.php','r0k.php','abc.php','egy.php','syrian_shell.php','xxx.php','settings.php','tmp.php','cyber.php','c99.php','r57.php','404.php','gaza.php','1.php','d4rk.php','index1.php','nkr.php','xd.php','M4r0c.php','Dz.php','sniper.php','ksa.php','v4team.php','offline.php','priv8.php','911.php','madspotshell.php','c100.php','sym.php','cp.php','tmp/cpn.php','tmp/w.php','tmp/r57.php','tmp/king.php','tmp/sok.php','tmp/ss.php','tmp/as.php','tmp/dz.php','tmp/r1z.php','tmp/whmcs.php','tmp/root.php','tmp/r00t.php','templates/beez/index.php','templates/beez/beez.php','templates/rhuk_milkyway/index.php','tmp/uploads.php','tmp/upload.php','tmp/sa.php','sa.php','readme.php','tmp/readme.php','wp.zip','wp-content/plugins/disqus-comment-system/disqus.php',
                  'd0mains.php','wp-content/plugins/akismet/akismet.php','madspotshell.php','info.php','egyshell.php','Sym.php','c22.php','c100.php','olux.php',
                  'wp-content/plugins/akismet/admin.php#','configuration.php','g.php','wp-content/plugins/google-sitemap-generator/sitemap-core.php#','/wp-content/plugins/ubh/za3imccc.php',
                  'wp-content/plugins/akismet/widget.php#','xx.pl','ls.php','Cpanel.php','k.php','zone-h.php','tmp/user.php','tmp/Sym.php','cp.php','lucifer.php',
                  'tmp/madspotshell.php','tmp/root.php','tmp/whmcs.php','tmp/index.php','tmp/2.php','tmp/dz.php','tmp/cpn.php','images/vuln.php','wp-content/vuln.php','/za3imccc.php','/download.php',
                  'tmp/changeall.php','tmp/Cgishell.pl','tmp/sql.php','0day.php','tmp/admin.php','cliente/downloads/h4xor.php','bypass.php',
                  'whmcs/downloads/dz.php','L3b.php','d.php','tmp/d.php','tmp/L3b.php','wp-content/plugins/akismet/admin.php',
                  'templates/rhuk_milkyway/index.php','templates/beez/index.php','sado.php','admin1.php','upload.php','up.php','vb.zip','vb.rar',
                  'admin2.asp','uploads.php','sa.php','sysadmins/','admin1/','sniper.php','administration/Sym.php','images/Sym.php',
                  '/r57.php','/wp-content/plugins/disqus-comment-system/disqus.php','gzaa_spysl','sql-new.php','/shell.php','/sa.php','/admin.php',
                  '/sa2.php','/2.php','/gaza.php','/up.php','/upload.php','/uploads.php','/templates/beez/index.php','shell.php','/amad.php',
                  '/t00.php','/dz.php','/site.rar','/Black.php','/site.tar.gz','/home.zip','/home.rar','/home.tar','/home.tar.gz',
                  '/forum.zip','/forum.rar','/forum.tar','/forum.tar.gz','/test.txt','/ftp.txt','/user.txt','/site.txt','/error_log','/error',
                  '/cpanel','/awstats','/site.sql','/vb.sql','/forum.sql','r00t-s3c.php','c.php','/backup.sql','/back.sql','/data.sql','wp.rar/',
                  'wp-content/plugins/disqus-comment-system/disqus.php','asp.aspx','/templates/beez/index.php','tmp/vaga.php',
                  'tmp/killer.php','whmcs.php','abuhlail.php','tmp/killer.php','tmp/domaine.pl','tmp/domaine.php','useradmin/',
                  'tmp/d0maine.php','d0maine.php','tmp/sql.php','X.php','123.php','m.php','b.php','up.php','tmp/dz1.php','dz1.php','forum.zip','Symlink.php','Symlink.pl',
                  'forum.rar','joomla.zip','joomla.rar','wp.php','buck.sql','sysadmin.php','images/c99.php', 'xd.php', 'c100.php',
                  'spy.aspx','xd.php','tmp/xd.php','sym/root/home/','billing/killer.php','tmp/upload.php','tmp/admin.php',
                  'Server.php','tmp/uploads.php','tmp/up.php','Server/','wp-admin/c99.php','tmp/priv8.php','priv8.php','cgi.pl/','/sites/default/files/vuln.php','/sites/default/files/up.php',
                  'tmp/cgi.pl','downloads/dom.php','templates/ja-helio-farsi/index.php','webadmin.html','admins.php',
                  '/wp-content/plugins/count-per-day/js/yc/d00.php','bluff.php','king.jeen','admins/','admins.asp','admins.php','wp.zip','/wp-content/plugins/disqus-comment-system/WSO.php']
        for directory in paths:
            try:
                opensite = urllib2.urlopen(url + "/" + directory, timeout=15)
                k = opensite.read()
                if "-rw-r--r--" in k:
                    print(fc+"["+fc+">"+fc+"] "+fg+url+ "/" + directory +fw+" .... "+fg+" Found "+fw+"")
                    ope = open("Shells.txt", "a").write(url + "/" + directory + "\n")
                    break
                else:
                    print(fc+"["+fc+">"+fc+"] "+fr+url+fw+" .... "+fr+" Not Found "+fw+""+fw)
            except:
                print(fc+"["+fc+">"+fc+"] "+fr+url+fw+" .... "+fr+" Not Found "+fw+""+fw)
                pass
    except:
        pass
################################
def main():
    for i in lucifer:
        try:
            i = i.strip()
            data = backdoor(i)
        except:
            pass
################################
lucifer = raw_input("\n\033[92m[!]\033[91m WELCOME TO HELL ENTER LIST OF WEBSITES : ")
fast = raw_input("\033[92m[!]\033[91m ENTER THREAD NUMBER : ")
################################
try:
    with open(lucifer, 'r') as f:
        kiwi = f.read().splitlines()
except IOError:
    pass
################################
kiwi = list((kiwi))
pool = ThreadPool(int(fast))
pool.map(backdoor, kiwi)
pool.close()
pool.join()
################################
if __name__ == '__main__':
    print("\n\t\033[95m Lucifer Finish Press Enter To Exit ")
############# Owner TN #########
