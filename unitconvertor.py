#sorry previous button dose not works it was one of the frist tkinter project hope you like it
#DEEPJYOTI KARMAKAR TRIPURA INDIA
import tkinter as d
from datetime import datetime

from tkcalendar import Calendar
ob=d.Tk()
def  func4():
	la6.destroy()
	lab2.destroy()
	lab7.destroy()
	lab8.destroy()
	enfuni3.destroy()
	enfuni4.destroy()
	bu.destroy()
	delbu.destroy()
	bufornex.destroy()
	enfuni2.destroy()
	
	#for calender
	cDay = datetime.now().day
	cMonth = datetime.now().month
	cYear = datetime.now().year
	ob.geometry("400x400")
	# Add Calendar
	cal = Calendar(ob, selectmode = 'day',year=cYear, month = cMonth,day = cDay)
	cal.grid()
	labti=datetime.now().time()
	labtime=d.Label(ob,text=f"TIME::{labti}",bg="yellow",fg="black")
	labtime.grid()
	buforpre=d.Button(ob,text="previous",bg="red",fg="black")
	buforpre.grid()
	
	
def func():
	number=ennu.get()
	unitfornum=enunit.get()
	unitfor_cha=enunitch.get()
	if unitfornum=="cm":#CM
		if unitfor_cha=="m":
			num=number/100
		elif unitfor_cha=="mm":
			num=number*10
		elif unitfor_cha=="km":
			num=number/100000
		elif unitfor_cha=="feet":
			num=number/30.48
		elif unitfor_cha=="nm":
			num=number*10000000
		else:
			num="FUCK"
		
	elif unitfornum=="m":#M
		if unitfor_cha=="cm":
			num=number*100
		elif unitfor_cha=="mm":
			num=number*1000
		elif unitfor_cha=="km":
			num=number/1000
		elif unitfor_cha=="feet":
			num=number*3.28
		elif unitfor_cha=="nm":
			num=number*1000000000
		else:
			num="FUCK"
	elif unitfornum=="km":#km
		if unitfor_cha=="cm":
			num=number*100000
		elif unitfor_cha=="mm":
			num=number*1000000
		elif unitfor_cha=="m":
			num=number/1000
		elif unitfor_cha=="feet":
			num=number*3281
		elif unitfor_cha=="nm":
			num=number*1000000000000
		else:
			num="FUCK"
	elif unitfornum=="mm":#mm
		if unitfor_cha=="cm":
			num=number/10
		elif unitfor_cha=="m":
			num=number/1000
		elif unitfor_cha=="km":
			num=number/1000000
		elif unitfor_cha=="feet":
			num=number/305
		elif unitfor_cha=="nm":
			num=number*1000000
		else:
			num="FUCK"
			
	elif unitfornum=="nm":#NM
		if unitfor_cha=="cm":
			num=number/10000000
		elif unitfor_cha=="m":
			num=number/1000000000
		elif unitfor_cha=="km":
			num=number/1000000000000
		elif unitfor_cha=="feet":
			num=number/3.048000000009
		elif unitfor_cha=="mm":
			num=number/1000000
		else:
			num="FUCK"
	else:
		num="FUCK"
		
	
	
	la6.config(text=num)
	
def func2():
	enfuni2.delete("0","end")
	enfuni3.delete("0","end")
	enfuni4.delete("0","end")
la6=d.Label(ob,bg="green")
la6.grid(row=20,column=2)#for cm
lab2=d.Label(ob,text="       NUMBER         ",bd=7,bg="gray")
lab2.grid(row=0,column=1)
#vrioables
ennu=d.IntVar()
enunit=d.StringVar()
enunitch=d.StringVar()
enfuni2=d.Entry(ob,textvariable=ennu,bd=8)
enfuni2.grid(row=0,column=2)

lab7=d.Label(ob,text="   UNIT FOR NUM ",bd=4,bg="yellow")
lab7.grid(row=2,column=1)
enfuni3=d.Entry(ob,textvariable=enunit,bd=8)
enfuni3.grid(row=2,column=2)

lab8=d.Label(ob,text=" UNIT TO CHANGE",bd=4,bg="gray")
lab8.grid(row=4,column=1)
enfuni4=d.Entry(ob,textvariable=enunitch,bd=7)
enfuni4.grid(row=4,column=2)

bu=d.Button(ob,text="CHANGE",bg="black",fg="white",bd=9,command=func)
bu.grid(row=9,column=2)

delbu=d.Button(ob,text="DELETE",bg="red",fg="black",bd=9,command=func2)
delbu.grid(row=9,column=1)

#bu
bufornex=d.Button(ob,bg="gold",command=func4)
bufornex.grid(row=76,column=2)
bufornex.config(text="NEXT")
ob.mainloop()
