#!/bin/usr/python3.8.x
# coding:utf-8
# Zodiac simple programs

"""
Apa apa apa
Serahludah
"""

import os,sys,json
from time import sleep
try:
	import requests
except:
	exit("error : not installed 'requests' module, install it first")

banner = """
\033[1;90m
||=================================||
   ______          _ _
  |___  /         | (_)
     / /  ___   __| |_  __ _  ___
    / /  / _ \ / _` | |/ _` |/ __|
  ./ /__| (_) | (_| | | (_| | (__
  \_____/\___/ \__,_|_|\__,_|\___|
||=================================||
 \033[47;1;91m     [•] Coded by : LeON [•]      \033[0m
"""
class Main:
	def __init__(self):
		self.leon()
		
	def leon(self):
		try:
			os.system('clear')
			print(banner)
			print("\033[1;91m•\033[1;92m For Birthday ex..: 21 08 1999")
			print()
			name=input("\033[1;97m{\033[1;92m•\033[1;97m}\033[1;97m Enter your Name :\033[1;96m ")
			sleep(1)
			date=input("\033[1;97m{\033[1;92m•\033[1;97m} Enter your Birthday :\033[1;96m ").replace(' ','-')
			url=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama='+name,'&tanggal='+date)
			a=json.loads(url.text)
			r=a['data']
			print("")
			print("""
      |----------------------------------|
	[+] Name     : %s
	[+] Birthday : %s
	[+] Age      : %s
	[+] Zodiac   : %s
      |----------------------------------|
			"""%(r['nama'], r['lahir'], r['usia'], r['zodiak']))
		except Exception as f:
			exit("err : %s"%(f))
			
Main()