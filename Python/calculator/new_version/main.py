import customtkinter as ctk
from calculator import Calculadora

def adicionar(n):
    global apagar
    global vs
    if n.isnumeric() and apagar:
        vs.set("")
    if len(vs.get()) < 14:
        vs.set(vs.get()+str(n))
    view_result.configure(text=vs.get())
    apagar = False
        
def remover():
    vs.set(vs.get()[:-1])
    view_result.configure(text=vs.get())

def calcular():
    global apagar
    global vs
    apagar = True
    vs.set(vs.get()+'?')
    calculadora = Calculadora()
    try:
        res = '{:.2f}'.format(float(calculadora.calcular(vs.get())))
        vs.set(str(res))
    except:
        vs.set('Error')
    view_result.configure(text=vs.get())

apagar = False

root = ctk.CTk()
root.title('Calculator')
root.resizable(False,False)

vs = ctk.StringVar()
vs.set('')

view_result = ctk.CTkLabel(root,bg_color='#313131',text=vs.get(),height=90,anchor='e',font=('Arial',40,'bold'),corner_radius=15)
view_result.pack(anchor='n',fill='x',expand=True)

frame_button = ctk.CTkFrame(root,fg_color='#202020')
frame_button.pack(fill='both',expand=True)

symbols = [['7',0,0],['8',0,1],['9',0,2],['/',0,3],
           ['4',1,0],['5',1,1],['6',1,2],['x',1,3],
           ['1',2,0],['2',2,1],['3',2,2],['-',2,3],
           ['⇤',3,0],['0',3,1],['=',3,2],['+',3,3]]

for text,row,col in symbols:
    try:
        int(text)
        color = '#454545'
    except:
        color = '#FF6D0A'
    if text == '⇤':
        ctk.CTkButton(frame_button,text=text,width=75,height=75,corner_radius=45,border_spacing=0,font=('Arial',26,'bold'),fg_color=color,command=remover).grid(column=col,row=row,padx=5,pady=5)
    elif text == '=':
        ctk.CTkButton(frame_button,text=text,width=75,height=75,corner_radius=45,border_spacing=0,font=('Arial',26,'bold'),fg_color=color,command=calcular).grid(column=col,row=row,padx=5,pady=5)
    else:
        ctk.CTkButton(frame_button,text=text,width=75,height=75,corner_radius=45,border_spacing=0,font=('Arial',26,'bold'),fg_color=color,command=lambda t=text: adicionar(t)).grid(column=col,row=row,padx=5,pady=5)

root.mainloop()