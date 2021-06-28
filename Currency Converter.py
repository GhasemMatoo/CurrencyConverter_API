# import modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests, json
import time

#----------------------------function--ALL------
def country_changed(event):
    my_text1=selected_cb_1.get()
    x = requests.get("https://api.exchangerate-api.com/v4/latest/"+my_text1)
    json_val.update(x.json())

def Converter():
    
    az.config(text = json_val["rates"][selected_cb_1.get()])
    to.config(text = json_val["rates"][selected_cb_2.get()])
def on_close():
    response=messagebox.askyesno('Exit','Ghasem Matoo,Thank you very mach for Testing',icon='info')
    if response:
        win.destroy()
#--------------------- win config-----------
win = Tk()  
win.geometry("500x300")
win.resizable(0,0)
win.config(bg ='#b5b5b3')
win.iconphoto(False,PhotoImage(file='iconPhoto.png'))
win.title('Currency Converter')
win.protocol('WM_DELETE_WINDOW',on_close)
###################
selected_cb_1 = StringVar()
selected_cb_2 = StringVar()
country =[]
##--------------------------------------------API-requests----
x = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
json_val=x.json()
for val in json_val["rates"]:
    country.append(val)
#-------------------------------label--------------
Label(win, text = '    Welcom to real time Currency Converter   ',
      font='Calibri 20 bold',
      bg = '#273db5',fg="#f8f7f6").pack()
Com=Label(win, text = '1USD = {} Iran Riyal'.format(json_val["rates"]["IRR"]),
      font='Times 20 bold', bg = '#b5b5b3')
Label(win, text = 'Date_API:',
      font='Times 17 bold', bg = '#b5b5b3',
      fg='#d2272c').place(x=10,y=260)
Label(win, text = 'Date_SIS:',
      font='Times 17 bold', bg = '#b5b5b3',
      fg='#ffda57').place(x=270,y=260)
Tim_API=Label(win, text =json_val["date"],
      font='Times 17 bold', bg = '#b5b5b3')
Label(win, text =time.strftime('%Y/%d/%m'),
      font='Times 17 bold', bg = '#b5b5b3').place(x=380,y=260)
#--------------------------Combobox------

##############################
cb_1 = ttk.Combobox(win, textvariable= selected_cb_1,
                    justify='center',state = 'readonly',
                        width =7,font="Bodoni 25 bold")
cb_1['values'] = country
cb_1.place(x=50,y=80)
#----------------------------------
cb_2= ttk.Combobox(win, textvariable= selected_cb_2,
                   justify='center',state = 'readonly',
                        width =7,font="Bodoni 25 bold")
cb_2['values'] = country
cb_2.place(x=320,y=80)
###########################

az=Label(win, text ="", fg = 'black', bg = 'white', relief = 'ridge',
      font="Bodoni 17 bold",justify = 'center',
      width = 7)
#---------------------------------------
to=Label(win, text ="", fg = 'black', bg = 'white', relief = 'ridge',
      font="Bodoni 17 bold",justify = 'center',
      width = 7)
#################################################
cb_1.bind('<<ComboboxSelected>>', country_changed)
cb_2.bind('<<ComboboxSelected>>', country_changed)
###############################################
cb_1.set("USD")
cb_2.set("IRR")

#----------------------------Buttom-----
border = LabelFrame(win, bd = 6, bg = "black")
border.pack(pady = 10)
  
btn = Button(border, text="Converter", width = 8,
             font="Bodoni 15 bold",command =Converter,
             bg = "#6CD300", fg = "black")
#---------------
btn.pack()
border.place(x = 200, y = 160)
Com.place(x=100,y=220)
Tim_API.place(x=120,y=260)
az.place(x=80,y=130)
to.place(x=340,y=130)
win.mainloop()  
  
