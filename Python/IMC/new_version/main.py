from customtkinter import * 

def verify(text,type,off_limit=None,on_limit=None):
    try:
        if type(text)>=off_limit and type(text)<=on_limit:
            return True
        return False
    except:
        return False

def show_error():
    error = False
    if entry_name.get().isalpha() == False:
        entry_name.configure(border_color='red')
        message_alert.configure(text='CAMPOS ERRONEAMENTE PREENCHIDOS')
        error = True
    else:
        entry_name.configure(border_color='white')

    if verify(entry_age.get(),int,0,100) == False:
        entry_age.configure(border_color='red')
        message_alert.configure(text='CAMPOS ERRONEAMENTE PREENCHIDOS\nIDADE FORA DOS LIMITES 0 A 120 ANOS')
        error = True
    else: 
        entry_age.configure(border_color='white')

    if verify(entry_weight.get(),float,0,300) == False:
        entry_weight.configure(border_color='red')
        message_alert.configure(text='CAMPOS ERRONEAMENTE PREENCHIDOS \nPESO FORA DOS LIMITES 0 A 300KG')
        error = True
    else:
        entry_weight.configure(border_color='white')

    if verify(entry_height.get(),float,0,3) == False:
        entry_height.configure(border_color='red')
        message_alert.configure(text='CAMPOS ERRONEAMENTE PREENCHIDOS \nALTURA FORA DOS LIMITES 0 A 3M')
        error = True
    else:
        entry_height.configure(border_color='white')
    return error
    

def calculate():
    if show_error():
        return
    imc = float(entry_weight.get()) / (float(entry_height.get())**2)
    label_imc.configure(text=f'IMC: {imc}')
    
    if imc>=40 and entry_sex.get() == 'M':
        class_imc.configure(text=f'Você está com obesidade grau II')
    elif (imc>=30 and imc<40) and entry_sex.get() == 'M':
        class_imc.configure(text=f'Você está com obesidade grau I')
    elif (imc>=25 and imc<30) and entry_sex.get() == 'M':
        class_imc.configure(text=f'Você está acima do peso')
    elif (imc>=20 and imc<25) and entry_sex.get() == 'M':
        class_imc.configure(text=f'Você está com o peso normal')
    elif imc<20 and entry_sex.get() == 'M':
        class_imc.configure(text=f'Você está abaixo do peso')

    if imc>=39 and entry_sex.get() == 'F':
        class_imc.configure(text=f'Você está com obesidade grau II')
    elif (imc>=29 and imc<39) and entry_sex.get() == 'F':
        class_imc.configure(text=f'Você está com obesidade grau I')
    elif (imc>=24 and imc<29) and entry_sex.get() == 'F':
        class_imc.configure(text=f'Você está acima do peso')
    elif (imc>=19 and imc<24) and entry_sex.get() == 'F':
        class_imc.configure(text=f'Você está com o peso normal')
    elif imc<19 and entry_sex.get() == 'F':
        class_imc.configure(text=f'Você está abaixo do peso')

def delete():
    entry_age.delete(0,END)
    entry_height.delete(0,END)
    entry_name.delete(0,END)
    entry_weight.delete(0,END)


root = CTk()
root.geometry('640x420')
root.resizable(False,False)
root.title('Calculadora IMC')

frame = CTkFrame(root,height=300,width=300)
frame.pack(pady=20)

#Register Interface

label_name = CTkLabel(frame,text='Nome').place(x=10,y=0)
entry_name = CTkEntry(frame,width=200)
entry_name.place(x=10,y=25)

label_sex = CTkLabel(frame,text='Sexo:').place(x=220,y=0)
entry_sex = CTkOptionMenu(frame,values=['M','F'],width=60)
entry_sex.place(x=220,y=25)

label_age = CTkLabel(frame,text='Idade').place(x=10,y=55)
entry_age = CTkEntry(frame,width=40)
entry_age.place(x=10,y=80)

label_weight = CTkLabel(frame,text='Peso(kg)').place(x=60,y=55)
entry_weight = CTkEntry(frame,width=60)
entry_weight.place(x=60,y=80)

label_height = CTkLabel(frame,text='Altura(cm)').place(x=130,y=55)
entry_height = CTkEntry(frame,width=40)
entry_height.place(x=130,y=80)


label_imc = CTkLabel(frame,text='IMC:')
label_imc.place(x=10,y=110)

class_imc = CTkLabel(frame,text='',font=('Arial',18))
class_imc.place(x=10,y=130)

button_delete = CTkButton(frame,text='Apagar',width=75,command=delete).place(x=110,y=160)
button_calculate = CTkButton(frame,text='Calcular',width=75,command=calculate).place(x=10,y=160)

message_alert = CTkLabel(frame,text='',anchor='w')
message_alert.place(x=10,y=195)

root.mainloop()