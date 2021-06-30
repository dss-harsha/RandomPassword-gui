import random
import string
from tkinter import *
from tkinter.ttk import *

def password():
	letters = string.ascii_letters 
	symbols = string.punctuation 
	numbers = string.digits

	

	letters_no = a.get()     # enter required no of letters,digits,symbols
	symbols_no = b.get()
	numbers_no = c.get()




	pletters="".join(random.choice(letters) for x in range(0,letters_no))   # string.join(iterable)
	psymbols="".join(random.choice(symbols) for x in range(0,symbols_no))
	pnumbers="".join(random.choice(numbers) for x in range(0,numbers_no))
	password = pletters+psymbols+pnumbers
	l = list(password)
	random.shuffle(l)
	password = "".join(l)
	d.set(password)
	


def submit():
	password1 = password()
	show_password.insert()

root = Tk()


root.title("Random Password Generator")
root.geometry('1000x1000')

a = IntVar()
b = IntVar()
c = IntVar()
d = StringVar()



Letters= Label(root,text="Enter no of letters").place(x=40,y=160)
Symbols= Label(root,text="Enter no of symbols").place(x=40,y=260)
Numbers= Label(root,text="Enter no of Numbers").place(x=40,y=360)
submit = Button(root,text="Run",command=submit).place(x=400,y=760)

pword = Label(root,text="Password").place(x=40,y=460)


enter_letters= Entry(root,width=30,textvariable=a).place(x=500,y=160)
enter_symbols= Entry(root,width=30,textvariable=b).place(x=500,y=260)
enter_numbers= Entry(root,width=30,textvariable=c).place(x=500,y=360)
enter_location = Entry(root,width=30).place(x=500,y=460)
show_password = Entry(root,width=30,text="%s" %(d)).place(x=500,y=460)


root.mainloop()










