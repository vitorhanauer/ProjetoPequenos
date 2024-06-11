import database
from customtkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image

def search_image():
    global img_path
    global photo
    try:
        img_path = None
        img_path = askopenfilename()
        img = CTkImage(light_image=Image.open(img_path),dark_image=Image.open(img_path),size=(100,100))
    except:
        img = None
    finally:
        photo.configure(image = img,width=100,height=100)

def contact_window(title,com):
    global name
    global contact
    global cellphone
    global email
    global img
    global photo
    global img_path

    img = None
    img_path = None

    contact = CTkToplevel(root) 
    contact.title(title)
    contact.wm_transient(root)
    contact.geometry('220x320')
    contact.resizable(False,False)

    photo = CTkButton(contact, width=100,height=100,corner_radius=50,fg_color='transparent',border_width=1,border_color='white',text='',image=img,command=search_image)
    photo.pack(pady=10)

    name = CTkEntry(contact,placeholder_text='Nome',width=200,corner_radius=2)
    name.pack(pady=10,padx=10,anchor='w')

    cellphone = CTkEntry(contact,placeholder_text='Telefone',width=200,corner_radius=2)
    cellphone.pack(pady=10,padx=10,anchor='w')

    email = CTkEntry(contact,placeholder_text='Email',width=200,corner_radius=2)
    email.pack(pady=10,padx=10,anchor='w')

    
    savebtn =  CTkButton(contact,text='Salvar',command=com)
    savebtn.place(x=10,y=270)


def save_edited_contact(t,i):
    global img_path
    if photo.__getattribute__('_image') == None:
        s_img = f"'{i}'"
    else:
        s_img = f"'{img_path}'"
    t = f"'{t}'"
    database.connect('./agenda.db')
    s_name = f"'{name.get()}'"
    s_phone = f"'{cellphone.get()}'"
    s_email = f"'{email.get()}'"

    database.update_itens('contatos','nome',s_name,'telefone',t)
    database.update_itens('contatos','email',s_email,'telefone',t)
    database.update_itens('contatos','img',s_img,'telefone',t)
    database.update_itens('contatos','telefone',s_phone,'telefone',t)

    searchContact()
    contact.destroy()

def delete(t):
    database.delete('contatos','telefone',f"'{t}'")
    searchContact()
    contact.destroy()

def edit(n,t,e,i):
    try:
        contact.destroy()
        contact_window('Editar Contato',lambda t=t,i=i:save_edited_contact(t,i))
    except:
        contact_window('Editar Contato',lambda t=t,i=i:save_edited_contact(t,i))
    finally:
        CTkButton(contact,text='Apagar',width=40,command=lambda t=str(t) :delete(t)).place(x=155,y=270),
        try:
            img = CTkImage(light_image=Image.open(i),dark_image=Image.open(i),size=(100,100))
            photo.configure(image = img,width=100,height=100)
        except:
            photo.configure(width=100,height=100)
        finally:
            cellphone.insert(0,str(t))
            name.insert(0,str(n))
            email.insert(0,str(e))


def show_contact(select):
    global names
    for children in contactFrame.winfo_children():
        children.destroy()
    for x in select:
        global img
        try:
            img = CTkImage(light_image=Image.open(x[3]),dark_image=Image.open(x[3]),size=(50,50))
            CTkButton(contactFrame, text=x[0],command=(lambda n=x[0],t=x[1],e=x[2],i=x[3]:edit(n,t,e,i)),font=('Arial',16),anchor='w',fg_color='#0C1E2B',image=img).pack(pady=2,fill='x')
        except:
            CTkButton(contactFrame, text=x[0],command=(lambda n=x[0],t=x[1],e=x[2],i=x[3]:edit(n,t,e,i)),font=('Arial',16),anchor='w',fg_color='#0C1E2B').pack(pady=2,fill='x')

def save_new_contact():
    global img_path
    if name.get() == '' or cellphone.get() == '':
        return
    s_name = f"'{name.get()}'"
    s_cell = f"'{cellphone.get()}'"
    s_email = f"'{email.get()}'"
    s_img = f"'{img_path}'"

    if img_path == '':
        if database.insert_itens('contatos',cols[0:3],[s_name,s_cell,s_email]) == False:
            return
    
    elif database.insert_itens('contatos',cols,[s_name,s_cell,s_email,s_img]) == False:
        return

    searchContact()
    contact.destroy()

def new_contact():
    try:
        contact.destroy()
        contact_window('Novo contato',save_new_contact)
    except:
        contact_window('Novo contato',save_new_contact)
    

def searchContact():
    if searchBar.get() != ' ':
        show_contact(database.select_especific('contatos','nome',str(searchBar.get())))
        return
    show_contact(database.select('contatos'))

cols = ['nome','telefone','email','img']

database.connect('./agenda.db')
database.create_table('contatos',cols,['varchar(60)','varchar(14) primary key','varchar(60)','TEXT'])

root = CTk()
root.geometry('380x500')
root.resizable(False,False)
root.title('Agenda')

searchFrame = CTkFrame(root,height=40,corner_radius=0,fg_color='#0C1E2B')
searchFrame.pack(fill='x',anchor='n')

contactFrame = CTkScrollableFrame(root,fg_color='#0C1E2B')
contactFrame.pack(fill='both',expand=True,anchor='n')

searchBar = CTkEntry(searchFrame,placeholder_text='Pesquisar Contatos',width=270,height=30,border_width=0,corner_radius=30,fg_color='#143348')
searchBar.place(x=50,y=5)

searchIcon = CTkImage(light_image=Image.open('./magnifying glass white.png'),dark_image=Image.open('./magnifying glass white.png'),size=(15,15))
searchButton = CTkButton(searchFrame,image=searchIcon,text='',width=30,height=30,corner_radius=10,fg_color='#143348',border_spacing=0,command=searchContact)
searchButton.place(x=10,y=5)

CTkButton(searchFrame,text='+',width=30,height=30,corner_radius=10,font=('Arial',20),command=new_contact,fg_color='#143348').place(x=330,y=5)

show_contact(database.select('contatos'))

root.mainloop()