import math
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import font

w = tk.Tk()
w.geometry("1050x700+440+1")
w.title("Hotel Management")
w.config(bg='#E2FAFC')

# font for whole  *****************************************************
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=14)
Font_tuple = ("PMingLiU", 20, "bold")
font_entry = ("Kozuka Gothic Pr6N M", 12, "normal")
Font_tuple2 = ("Kozuka Gothic Pr6N M", 16, "bold")

# Parent Frame ********************************************************************
fr_parent = Frame(w , padx=50 , pady=50)
fr_parent.config(bg='#B5E2FA' )

# frame 1 Title *******************************************************
title = Frame(fr_parent , background="#B5E2FA")
Label(title , text="Hotel Shivhare", font=Font_tuple, background="#B5E2FA").pack(side=TOP)
Label(title , text="Management", font=Font_tuple2,background="#B5E2FA").pack(side=BOTTOM)
title.grid(row=1 , column= 1 , columnspan=2)

# List in Items
drink = 300
burger = 89
cherry = 199
nacho = 67
pizza = 299
biscuit = 10
roll = 10
tea = 10

# Order Number  - - - - -
ran = ["1","2","3","4","5","6","7","9","0" ]

random_num=""
def rand(ran):
    global random_num
    for i in range(0,5):
        r = random.choice(ran)
        random_num=random_num+r

rand(ran)



# frame 2 Product List *************************************************

prod_list_frame = LabelFrame(fr_parent, text="Product List" ,background="#FAF8F4", bd=0, font=4)
f_prod = Frame(prod_list_frame , background="#FAF8F4" , padx=5 , pady=5,)

# drink - - -
var_drink = IntVar()
l_drink = Label(f_prod , text="Drink : ",background="#FAF8F4")
e_drink = Entry(f_prod  ,font=font_entry ,width=15, textvariable=var_drink)
l_drink.grid(row=1 , column=1,sticky = W)
e_drink.grid(row=1 , column=2  ,ipady=5 , pady=5)

# burger King - - -
var_burger = IntVar()
l_burger = Label(f_prod , text="Burger King : ",background="#FAF8F4")
e_burger = Entry(f_prod ,font=font_entry ,width=15, textvariable=var_burger)
l_burger.grid(row=2 , column=1,sticky = W)
e_burger.grid(row=2 , column=2,ipady=5 ,pady=5 , padx=5)

# Cherry - - -
var_cherry = IntVar()
l_cherry = Label(f_prod , text="Cherry : ",background="#FAF8F4")
e_cherry = Entry(f_prod,font=font_entry ,width=15, textvariable=var_cherry)
l_cherry.grid(row=3 , column=1,sticky = W)
e_cherry.grid(row=3 , column=2,ipady=5,pady=5)

# Nacho Fries - - -
var_nacho = IntVar()
l_nacho = Label(f_prod , text="Nacho Fries : ",background="#FAF8F4")
e_nacho = Entry(f_prod,font=font_entry ,width=15, textvariable=var_nacho)
l_nacho.grid(row=4 , column=1,sticky = W)
e_nacho.grid(row=4 , column=2,ipady=5,pady=5)

# Pizza - - -
var_pizza = IntVar()
l_pizza = Label(f_prod , text="Pizza : ",background="#FAF8F4")
e_pizza = Entry(f_prod,font=font_entry ,width=15, textvariable=var_pizza)
l_pizza.grid(row=5 , column=1,sticky = W)
e_pizza.grid(row=5 , column=2,ipady=5,pady=5)

# Bicuits - - -
var_biscuit = IntVar()
l_biscuit = Label(f_prod , text="Biscuits : ",background="#FAF8F4")
e_biscuit = Entry(f_prod,font=font_entry ,width=15, textvariable=var_biscuit)
l_biscuit.grid(row=6 , column=1,sticky = W)
e_biscuit.grid(row=6 , column=2,ipady=5,pady=5)

# Roll - - -
var_roll = IntVar()
l_roll = Label(f_prod , text="Roll : ",background="#FAF8F4")
e_roll = Entry(f_prod,font=font_entry ,width=15, textvariable=var_roll)
l_roll.grid(row=7, column=1,sticky = W)
e_roll.grid(row=7, column=2,ipady=5,pady=5)

# Tea - - -
var_tea = IntVar()
l_tea = Label(f_prod , text="Tea : ",background="#FAF8F4")
e_tea = Entry(f_prod,font=font_entry ,width=15, textvariable=var_tea)
l_tea.grid(row=8, column=1, sticky=W)
e_tea.grid(row=8, column=2, ipady=5, pady=5)

f_prod.pack(fill=BOTH)
prod_list_frame.grid(row=2, column=1, rowspan=2, ipadx=5 , ipady=5, padx=5, pady=5 )

# frame 3 Bill ***************************************************

t_bill = Frame(fr_parent ,background="#FAF8F4" , pady=30)

Label(t_bill, text="Order Number : ", background="#FAF8F4", padx=5, pady=5).grid(row=1, column=1, sticky=W)
Label(t_bill, text="Cost : ", background="#FAF8F4", padx=5, pady=5).grid(row=2, column=1, sticky=W)
Label(t_bill, text="Service Cost : ", background="#FAF8F4", padx=5, pady=5).grid(row=3,column=1, sticky=W)
Label(t_bill, text="Tax : ", background="#FAF8F4", padx=5, pady=5).grid(row=4, column=1, sticky=W)
Label(t_bill, text="Sub Total : ", background="#FAF8F4", padx=5, pady=5).grid(row=5, column=1, sticky=W)
Label(t_bill, text="Total : ", background="#FAF8F4", padx=5, pady=5).grid(row=6, column=1, sticky=W)

# Print Output labels  - - - - - - - - - - - - -

# order number - - -
order = Label(t_bill, background="#FAF8F4", padx=5, pady=5, width=10)
order.grid(row=1, column=2, sticky=W)

# cost - - -
cost = Label(t_bill, background="#FAF8F4", padx=5, pady=5, width=10)
cost.grid(row=2, column=2, sticky=W)

# Service Cost - - -
service = Label(t_bill, background="#FAF8F4", padx=5, pady=5, width=10)
service.grid(row=3, column=2, sticky=W)

# Tax - - -
tax = Label(t_bill, background="#FAF8F4", padx=5, pady=5, width=10)
tax.grid(row=4, column=2, sticky=W)

# Sub Total - - -
sub_total = Label(t_bill, background="#FAF8F4", padx=5, pady=5, width=10)
sub_total.grid(row=5, column=2, sticky=W)

# Total - - -
total_a = Label(t_bill, background="#FAF8F4", padx=5, pady=5, width=10)
total_a.grid(row=6, column=2, sticky=W)

t_bill.grid(row=2, column=2, rowspan=2, padx=5, pady=5, ipadx=5, ipady=20, sticky=NS)


# on Price Click - - - - - -
def on_price():
    price_wind = tk.Tk()
    price_wind.geometry("400x500")
    price_wind.title("Price")
    price_wind.config(bg='#E2FAFC')
    # FRAME - - - - -
    pri_lab = Frame(price_wind, background="#B5E2FA")
    # LABEL - - - - -
    Label(pri_lab, text="Drink : ", width=15, font=font_entry, background="#B5E2FA").grid(row=1, column=1, sticky=W)
    Label(pri_lab, text="300", font=font_entry, background="#B5E2FA").grid(row=1, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Burger King : ", width=15, font=font_entry, background="#B5E2FA").grid(row=2, column=1, sticky=W)
    Label(pri_lab, text="89", font=font_entry, background="#B5E2FA").grid(row=2, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Cherry : ", width=15, font=font_entry, background="#B5E2FA").grid(row=3, column=1, sticky=W)
    Label(pri_lab, text="199", font=font_entry, background="#B5E2FA").grid(row=3, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Nacho Fries : ", width=15, font=font_entry, background="#B5E2FA").grid(row=4, column=1, sticky=W)
    Label(pri_lab, text="67", font=font_entry, background="#B5E2FA").grid(row=4, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Pizza : ", width=15, font=font_entry, background="#B5E2FA").grid(row=5, column=1, sticky=W)
    Label(pri_lab, text="299", font=font_entry, background="#B5E2FA").grid(row=5, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Biscuits : ", width=15, font=font_entry, background="#B5E2FA").grid(row=6, column=1, sticky=W)
    Label(pri_lab, text="10", font=font_entry, background="#B5E2FA").grid(row=6, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Roll : ", width=15, font=font_entry, background="#B5E2FA").grid(row=7, column=1, sticky=W)
    Label(pri_lab, text="10", font=font_entry, background="#B5E2FA").grid(row=7, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)

    Label(pri_lab, text="Tea : ", width=15, font=font_entry, background="#B5E2FA").grid(row=8, column=1, sticky=W)
    Label(pri_lab, text="10", font=font_entry, background="#B5E2FA").grid(row=8, column=2, padx=5, pady=5, ipady=5, ipadx=5, sticky=W)
    pri_lab.pack(pady=15, padx=15, ipadx=15, ipady=15)

    price_wind.mainloop()
    rand(ran)
    return price_wind

# On Reset Click - - - - -
def on_reset():
    var_drink.set(0)
    var_burger.set(0)
    var_biscuit.set(0)
    var_roll.set(0)
    var_tea.set(0)
    var_cherry.set(0)
    var_nacho.set(0)
    var_pizza.set(0)

    order.config(text="")
    cost.config(text="")
    service.config(text="")
    tax.config(text="")
    sub_total.config(text="")
    total_a.config(text="")

# on Total Click - - - - -
global add_quan
def on_total():
    global random_num
    global add_quan
    # calculations - - - - -
    add_quan = (var_drink.get()*drink)+(var_burger.get()*burger)+(var_cherry.get()*cherry)+(var_nacho.get()*nacho)+(var_pizza.get()*pizza)+(var_biscuit.get()*biscuit)+(var_roll.get()*roll)+(var_tea.get()*tea)
    service_cost = round(add_quan*0.02, 2)
    tax_val = round(add_quan * 0.18, 2)
    sub_total_cal = math.floor(tax_val+service_cost)
    total_cal = math.floor(service_cost+tax_val+sub_total_cal+add_quan)
    # config - - - - -
    order.config(text=random_num)
    cost.config(text=add_quan)
    service.config(text=service_cost)
    tax.config(text=tax_val)
    sub_total.config(text=sub_total_cal)
    total_a.config(text=total_cal)

# On Quit Click - - - - -
def on_quit():
    w.destroy()

# frame 4 Functional Buttons ***********************************************
btn=Frame(fr_parent, bg="#0B6DA2")

price = Button(btn, text="Price", background="#F9F7F3", width=9, height=2, bd="3", fg="#053048", activebackground="#EDDEA4", font=Font_tuple2, command=on_price)
total = Button(btn, text="Total", background="#F9F7F3", width=9, height=2, bd="3", fg="#053048", activebackground="#EDDEA4", font=Font_tuple2, command=on_total)
reset = Button(btn, text="Reset", background="#F9F7F3", width=9, height=2, bd="3", fg="#053048", activebackground="#EDDEA4", font=Font_tuple2, command=on_reset)
quit = Button(btn, text="Quit", background="#F9F7F3", width=9, height=2, bd="3", fg="#053048", activebackground="#EDDEA4", font=Font_tuple2, command=on_quit)

price.grid(row=1, column=1, padx=12, pady=15, sticky=NS,)
total.grid(row=1, column=2, padx=12, pady=15, sticky=NS)
reset.grid(row=1, column=3, padx=12, pady=15, sticky=NS)
quit.grid(row=1, column=4, padx=12, pady=15, sticky=NS)

btn.grid(row=4, column=1, columnspan=2, pady=10,sticky=W)

# frame 4 Timer ***********************************************
timer = Frame(fr_parent, bg="#0B6DA2", )
time_label = Label(timer, pady=5, padx=15, font=Font_tuple, bg="#0B6DA2", fg="#F9F7F3")
time_label.pack()
timer.grid(row=1, column=3, pady=10, sticky=W+E)
# upd_time()
def upd_time():
    tym = time.strftime("%H:%M:%S")
    time_label.config(text=tym)
    time_label.after(1000, upd_time)
upd_time()
# frame 5 Calculator ***********************************************
cal_lab_fr = LabelFrame(fr_parent, text="Calulator", bd=0, font=4)
calculator_fr = Frame(cal_lab_fr, bd=2)
expression = ""

def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)
    # equation.set(0)
def equal_func():
    try:
        global expression
        calc_total = int(eval(expression))
        equation.set(calc_total)
    except:
        equation.set("error")
        expression = ""

# ENTRY - -- - -
# row - 1
equation = IntVar()
calc_e = Entry(calculator_fr, font="arial 14",textvariable=equation, justify=RIGHT)
calc_e.grid(row=1, column=1,columnspan=4, ipady=8, sticky=W+E)

# Buttons
# row - 2
one = Button(calculator_fr, text="1", command=lambda : press(1))
one.grid(row=2, column=1, sticky=W+E)

two = Button(calculator_fr, text="2", command=lambda : press(2))
two.grid(row=2, column=2, sticky=W+E)

three = Button(calculator_fr, text="3", command=lambda : press(3))
three.grid(row=2, column=3, sticky=W+E)

# row 3
four = Button(calculator_fr, text="4", command=lambda : press(4))
four.grid(row=3, column=1, sticky=W+E)

five = Button(calculator_fr, text="5", command=lambda : press(5))
five.grid(row=3, column=2, sticky=W+E)

six = Button(calculator_fr, text="6", command=lambda : press(6))
six.grid(row=3, column=3, sticky=W+E)

# row 4
seven = Button(calculator_fr, text="7", command=lambda : press(7))
seven.grid(row=4, column=1, sticky=W+E)

eight = Button(calculator_fr, text="8", command=lambda : press(8))
eight.grid(row=4, column=2, sticky=W+E)

nine = Button(calculator_fr, text="9", command=lambda : press(9))
nine.grid(row=4, column=3, sticky=W+E)

# row 5
zero = Button(calculator_fr, text="0" , command=lambda : press(0))
zero.grid(row=5, column=1, sticky=W+E)

clear = Button(calculator_fr, text="C", command=clear)
clear.grid(row=5, column=2, sticky=W+E)

equal = Button(calculator_fr, text="=", command=equal_func)
equal.grid(row=5, column=3, sticky=W+E)

# Operators
plus = Button(calculator_fr, text="+", command=lambda : press("+"))
plus.grid(row=2, column=4, sticky=W+E)

minus = Button(calculator_fr, text="-", command=lambda : press("-"))
minus.grid(row=3, column=4, sticky=W+E)

mul = Button(calculator_fr, text="x", command=lambda : press("*"))
mul.grid(row=4, column=4, sticky=W+E)

divide = Button(calculator_fr, text="/", command=lambda : press("/"))
divide.grid(row=5, column=4, sticky=W+E)

calculator_fr.grid()
cal_lab_fr.grid(row=2, column=3, sticky=W, padx=10)

# frame 5 Text Area ***********************************************
def t_area_clear():
    t = t_area.get("1.0", "end-1c")
    t_area.delete("1.0", END)
    t_area.insert("1.0", "Enter You text")


t_area_fr = Frame(fr_parent,bg='#B5E2FA', pady=10)

t_area = Text(t_area_fr, height=10, bd=5, width=25, font="arial 12")

clear_text = Button(t_area_fr, text="clear", bd=5, command=t_area_clear)
# save_text = Button(t_area_fr, text="Save", bd=5, command=t_save_func)

clear_text.grid(row=2, column=1, sticky=W, pady=10,)
# save_text.grid(row=2, column=2, sticky=E, pady=10)

t_area.grid(row=1, column=1, columnspan=2)
t_area_fr.grid(row=3, column=3, rowspan=2, sticky=S+N+W+E, padx=10)


fr_parent.pack()
w.mainloop()
