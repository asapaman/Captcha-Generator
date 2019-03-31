import random
from random import randint

from tkinter import *
root=Tk()

List=[]
string=''
show_string=''
counter=0
var=StringVar()
#_________________________ function to generate random number _______________________
# this function genrates random number and appends it in list
def generate():
	i=0
	while i!=2:
		List.append(randint(0,9))
		List.append(randint(65,90))
		List.append(randint(97,122))
		i+=1
	random.shuffle(List)   # it shuffles the list so it Format changes randomly


#__________________________ Function to convert generated random number ___________
# This function converts number into string variable:
def convert():
	global show_string
	global string
	for i in List:
		if i >9:
			show_string+=chr(i)
			string+=chr(i)
		else:
			show_string+=str(i)
			string+=str(i)

		show_string+=' '


#___________________________ SECOND PAGE ________________________________
# function
def second():
	frame=Frame(root)
	frame.pack()
	label=Label(frame, text='TEXT BASED CAPTCHA\n', bd=5, font='Caladea 35 underline',
	justify=CENTER, padx=2, pady=2,)
	label.pack()
	label=Label(frame, text='\n*** ACCESS  GRANTED ***', bd=5, font='KacstOffice 25 bold',
	justify=CENTER, padx=2, pady=2,)
	label.pack()
	button1 = Button(frame, text ="Exit", command = root.destroy)
	button1.pack()


#___________________________ function to display Main Page _________________________
# this will display captcha on main page and other function like button etc.
def Main_page():
	global var
	frame=Frame(root)
	frame.pack()
	label=Label(frame, text='TEXT BASED CAPTCHA\n', bd=5, font='Caladea 35 underline',
	justify=CENTER, padx=2, pady=2,)
	label.pack()
	label=Label(frame, text=show_string, bd=5, font='cmmi10 25 bold',
	justify=CENTER, padx=9, pady=6,bg='white')
	label.pack()
	Label(frame, text='\n').pack()

	# -------------- internal function ---------------------------
	# this will work when Refresh button you will click on refresh button
	def Refresh():
		global string
		global show_string
		string=''
		show_string=''
		frame.destroy()
		srart()

	#------------------- internal function -----------------------
	def submit():
		global counter
		print(str(var.get()))
		if str(var.get())==string:
			frame.destroy()
			second()
		elif counter==1:
			pass
		else:
			label=Label(frame, text='!!! Wrong entery !!!\nTry again', bd=5, font='KacstOffice 18 ',
			justify=CENTER, pady=10)
			label.pack()
			counter+=1

	button1 = Button(frame, text ="Refresh", command = Refresh)
	button1.pack()
	entry=Entry(frame,textvariable=var,bg='white',font='Lato')
	entry.pack()
	button2 = Button(frame, text ="submit", command = submit)
	button2.pack()


# __________________________from here main function starts _________________________
def srart():
	global List
	List=[]
	generate()
	convert()
	print(List)
	print(string)
	print(show_string)
	Main_page()
srart()
root.mainloop()

