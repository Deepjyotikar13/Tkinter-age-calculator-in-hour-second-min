from tkinter import *
from tkinter import ttk
import datetime
ob=Tk()

def func():
	if com.get()=="Houre":
		funcforhoure()
	elif com.get()=="Day":
		funcforday()
	elif com.get()=="Current day":
		current_day()
	else:
		pass
def current_day():
	pass
def funcfordayandhour():
	global calculated_day ,calculated_month,calculated_year ,given_year,label788
	#date of birth
	birth_day=var1dbd.get()
	birth_month=var2dbm.get()
	birth_year=var3dby.get()
	#current date is
	given_day=var4cd.get()
	given_month=var5cm.get()
	given_year=var6cy.get()
	month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if (birth_day > given_day):
		given_month = given_month - 1
		given_day = given_day + month[birth_month-1] 
	if (birth_month > given_month):
	   given_year = given_year - 1
	   given_month = given_month + 12
	calculated_day = given_day - birth_day
	calculated_month = given_month - birth_month
	calculated_year = given_year - birth_year
	#16,17,18
	label788=Label(ob,text=calculated_day,font=("lucida 6 bold")).grid(row=16,column=1)
	label78=Label(ob,text=calculated_month,font=("lucida 6 bold")).grid(row=17,column=1)
	label7=Label(ob,text=calculated_year,font=("lucida 6 bold")).grid(row=18,column=1)
	dayy=calculated_day
	monthh=calculated_month*30
	yearr=calculated_year*365
	if calculated_year >1:
		yeart=calculated_year//4
		lisyy=[]
		for op in range(1,yeart+1):
			lisyy.append(1)
	else:
		pass
	sulis=sum(lisyy)
	yearre=yearr+sulis

	#else:
		#gh=abs(yearr)
	#year365=gh*365
#	totalhoures=dayy+monthh+year365
	hh=dayy+monthh+yearre
	label3=Label(ob,text=hh,font=("lucida 6 bold")).grid(row=19,column=1)
	HOUres=hh*24
	label7800=Label(ob,text=HOUres,font=("arial 7 bold")).grid(row=20,column=1)
	Seconds=hh*3600
	label780=Label(ob,text=Seconds,font=("arial 7 bold")).grid(row=21,column=1)
	Week=hh/7
	label7=Label(ob,text=Week,font=("arial 7 bold")).grid(row=22,column=1)
	

ob.config(bg="red")
labelofdob=Label(ob,text="YOUR DATE OF BIRTH",font=("arial 7 bold"),bg="red",relief="raised").grid(row=0,column=1)
dateofb=Label(ob,text=" Date  ",bg="yellow",fg="black",font=("lucida 8 bold"),relief="raised",bd=8).grid(row=1)
monthofb=Label(ob,text="Month",bg="light green",fg="black",font=("lucida 8 bold"),relief="raised",bd=8).grid(row=2)
yearofb=Label(ob,text=" Year  ",bg="light blue",fg="black",font=("lucida 8 bold"),relief="raised",bd=8).grid(row=3)
#DATE OF BIRTH VALUES
var1dbd=IntVar()
var2dbm=IntVar()
var3dby=IntVar()
enfordate=Entry(ob,relief="raised",bd=6,textvariable=var1dbd).grid(row=1,column=1)
enformonth=Entry(ob,relief="raised",bd=6,textvariable=var2dbm).grid(row=2,column=1)
enforyear=Entry(ob,relief="raised",bd=6,textvariable=var3dby).grid(row=3,column=1)

labelofcy=Label(ob,text="CURRENT TIME ",font=("lucida 7 bold"),bg="red",relief="raised").grid(row=5,column=1)
date=Label(ob,text=" Date  ",bg="yellow",fg="black",font=("lucida 8 bold"),relief="raised",bd=8).grid(row=6)
month=Label(ob,text="Month",bg="light green",fg="black",font=("lucida 8 bold"),relief="raised",bd=8).grid(row=7)
year=Label(ob,text=" Year  ",bg="light blue",fg="black",font=("lucida 8 bold"),relief="raised",bd=8).grid(row=8)
#CURRENT DATE VALUES
var4cd=IntVar()
var5cm=IntVar()
var6cy=IntVar()
date_for_c=Entry(ob,relief="raised",bd=6,textvariable=var4cd).grid(row=6,column=1)
month_for_c=Entry(ob,relief="raised",bd=6,textvariable=var5cm).grid(row=7,column=1)
year_for_c=Entry(ob,relief="raised",bd=6,textvariable=var6cy).grid(row=8,column=1)

com=ttk.Combobox(ob,values=("Currentday"),state="readonly")
com.grid(row=10,column=1)
butt=Button(ob,text="Calculate",font=('calibri', 8, 'bold', 'underline'),bd=6,bg="orange",command=funcfordayandhour).grid(row=12,column=1)
lab5=Label(ob,text="  Day    ",font=("lucida 9 bold"),bg="light blue",relief="raised",bd=7)
lab5.grid(row=16)
lab6=Label(ob,text="Month ",font=("lucida 9 bold"),bg="light green",relief="raised",bd=7).grid(row=17)
lab7=Label(ob,text="  Year   ",font=("lucida 9 bold"),bg="gold",relief="raised",bd=7).grid(row=18)
label3=Label(ob,text="   Days   " ,font=("arial 8 bold"),bd=7,relief="raised").grid(row=19)
label3=Label(ob,text=" Houres  " ,font=("arial 8 bold"),bg="yellow",bd=7,relief="raised").grid(row=20)
label4=Label(ob,text="Seconds",font=("lucida 8 bold"),bd=8,relief="raised",bg="white").grid(row=21)
label6=Label(ob,text="  Weeks ",font=("lucida 8 bold"),bd=8,relief="raised",bg="green").grid(row=22)
bu788=Button(ob,text="Clear",font=("lucida 7 bold"),bg="black",fg="white",bd=7).grid(row=12,column=2)

ob.mainloop()