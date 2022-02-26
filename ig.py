import requests
import json
import random
from tkinter import *
from tkinter import messagebox
import sys


fray = 0
king = Tk()

def login():
	global fray
	global king
	global text1
	global insert
	params = { 
	'username: e1.get(),'
	'password': e2.get(),
	}

#sesh ID lol

a = requests.session()

url1 = "https://www.instagram.com/accounts/login/"
r1 = s.get(url1)
csrf1 = r1.cookies.get_dict()['csrftoken']
url2 = 'https://www.instagram.com/accounts/login/ajax/'

#login form

username = params['username']
password = params['password']
#headers of the page 
headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'x-csrftoken': csrf1,
        'x-instagram-ajax': '1',
        'x-requested-with': 'XMLHttpRequest'
    }

#in

r2 = s.post(url2, headers=h2, data=data2)

if r2.json()['authenticated'] == False:
        messagebox.showinfo("Uh oh", "Invalid Account Info Or Accept Sus Request On Instagram")
        print("$Failed")
        
else:
     csrf = r2.cookies.get_dict()['csrftoken']
print('$Authenticated')
		

hx = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/edit/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'x-csrftoken': csrf,
            'x-instagram-ajax': '1',
            'x-requested-with': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }
#editing

fr = {
            'first_name': 'Sy',
            'email': '{}xxx@outlook.com'.format(str(random.randint(11111111, 99999999))),
            'username': '',
            'phone_number':'',
            'gender': '3',
            'biography':'',
            'external_url':'',
            'chaining_enabled': 'on'
        }
urlf = "https://www.instagram.com/accounts/edit/"
master.update()
res = None
s.headers.update(hf)
	
