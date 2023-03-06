from tkinter import *
from time import *
import locale

def update():
    string_tempo = strftime('%H:%M:%S')
    label_tempo.config(text=string_tempo)
    
    string_dia = strftime('%A')
    label_dia.config(text=string_dia)
    
    label_tempo.after(1000,update)
    label_dia.after(1000000,update)

locale.setlocale(locale.LC_TIME, 'pt_PT.utf8')

window = Tk()

window.wm_attributes('-topmost', True)
window.resizable(False, False) 
window.configure(bg='black')


label_tempo = Label(window,font=('Arial',50),fg='#64F58D',bg='black')
label_tempo.pack()

label_dia = Label(window,font=('Arial',25),fg='#64F58D',bg='black')
label_dia.pack()


update()


window.mainloop()