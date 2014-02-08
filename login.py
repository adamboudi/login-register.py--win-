#coded by adam boudi
import os
import getpass
home=input("Choose one \n[1]Login\n[2]register\nadam@windows:~$ ")
username=None
password=None
passone=None
passtwo=None
if home=="1":
	username=input("username: ")
	password=getpass.getpass("password: ")
	if os.path.isfile(username+".txt")==True:
		u=open(username+".txt","r")
		if password==u.read():
			os.system("cls")
			os.system("color a")
			print("welcome back "+username)
		else:
			os.system("cls")
			os.system("color c")
			print("wrong password!")
	else:
		os.system("cls")
		os.system("color c")
		print("No user")
elif home=="2":
	username=input("username: ")
	passone=getpass.getpass("password: ")
	passtwo=getpass.getpass("password: ")
	if passone==passtwo:
		u=open(username+".txt","w+")
		u.write(passone)
	else:
		os.system("cls")
		os.system("color c")
		print("pass don't match")
else:
	os.system("cls")
	os.system("color c")
	print("bad command !")
