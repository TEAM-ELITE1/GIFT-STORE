import os


def logo():
	os.system("clear")
	print("SUBSCRIBE YOUTUBE PUTRA-XD!")
	print(f"1. download dis3\n2. download file decompile\n3. my telegram\n4. download string decompile")
	dee = input("input : ")
	if dee in [" ",""]:
		print("wrong input!")
	elif dee in ["01","1"]:
		os.system("termux-open https://shrinke.me/dis3filesp")
	elif dee in ["02","2"]:
		os.system("termux-open https://shrinke.me/decom")
	elif dee in ["03","3"]:
		os.system("termux-open https://shrinke.me/putraxd")
	elif dee in ["04","4"]:
		print("check my youtube ")
		os.system("termux-open https://youtube.com/@putra-xd4465")

logo()


