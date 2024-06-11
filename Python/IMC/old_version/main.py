from tkinter import *

class Cadastros():

    def __init__(self,window,x):
        self.window = window
        self.x = x
        self.labels()
        self.entradas()
        
    def finalizar_Cadastro(self):
        cadastroFinalizado = []
        cadastroFinalizado.append(self.entradaNome.get())
        cadastroFinalizado.append(self.entradaIdade.get())
        cadastroFinalizado.append(self.entradaPeso.get())
        cadastroFinalizado.append(self.entradaAltura.get())
        cadastroFinalizado.append(self.entradaSexo.get())
        return cadastroFinalizado

        
    def destroy(self):
        self.labelNome.destroy()
        self.labelIdade.destroy()
        self.labelPeso.destroy()
        self.labelAltura.destroy()
        self.labelSexo.destroy()

        self.entradaNome.destroy()
        self.entradaIdade.destroy()
        self.entradaPeso.destroy()
        self.entradaAltura.destroy()
        self.entradaSexo.destroy()

    def labels(self):
        self.labelNome = Label(self.window,text='Nome:')
        self.labelNome.grid(row=self.x,column=0,sticky=W)

        self.labelIdade = Label(self.window,text='Idade:')
        self.labelIdade.grid(row=self.x,column=3,sticky=W)

        self.labelPeso = Label(self.window,text='Peso(kg):')
        self.labelPeso.grid(row=self.x,column=5,sticky=W)

        self.labelAltura = Label(self.window,text='Altura(m):')
        self.labelAltura.grid(row=self.x,column=7,sticky=W)

        self.labelSexo = Label(self.window,text='Sexo(M/F):')
        self.labelSexo.grid(row=self.x,column=9,sticky=W)

    def entradas(self):

        self.entradaNome = Entry(self.window,width=40)
        self.entradaNome.grid(row=self.x,column=0,columnspan=3,sticky=E)

        self.entradaIdade = Entry(self.window,width=5)
        self.entradaIdade.grid(row=self.x,column=3,sticky=E)

        self.entradaPeso = Entry(self.window,width=5)
        self.entradaPeso.grid(row=self.x,column=6)

        self.entradaAltura = Entry(self.window,width=5)
        self.entradaAltura.grid(row=self.x,column=8)

        self.entradaSexo = Entry(self.window,width=5)
        self.entradaSexo.grid(row=self.x,column=10)

def adicionar_Campo(window):
    global x
    global cadastro
    if x < 10:
        cadastro.append(Cadastros(window,x))
        x+=1

def remover_Campo():
    global x
    if len(cadastro)>0:
        cadastro[len(cadastro)-1].destroy()
        cadastro.pop()
        x-=1

def is_float(string):
    if string.isnumeric() or string.replace(".", "").isnumeric():
        return True
    else:
        return False

def verifica_Campos(x):
    for i in x:
         if i.entradaNome.get().isalnum() == False:
            labelAviso['text'] = 'Campos não preenchidos'
            return False
         if i.entradaIdade.get().isascii() == False:
            labelAviso['text'] = 'Campos não preenchidos'
            return False
         if i.entradaPeso.get().isascii() == False:
            labelAviso['text'] = 'Campos não preenchidos'
            return False
         if i.entradaAltura.get().isascii() == False:
            labelAviso['text'] = 'Campos não preenchidos'
            return False
         if i.entradaSexo.get().isalnum() == False:
            labelAviso['text'] = 'Campos não preenchidos'
            return False  
    return True

def tratatamento_Campos(x):
    for i in range(len(x)):
        if x[i].entradaNome.get().isalpha() == False:
            labelAviso['text'] = 'Campos não preenchidos'
            return False
        if x[i].entradaIdade.get().isnumeric() == False:
            labelAviso['text'] = 'Campo Idade com valores não numéricos'
            return False
        if is_float(x[i].entradaPeso.get()) == False:
            labelAviso['text'] = 'Campo Peso com valores não numéricos'
            return False
        if is_float(x[i].entradaAltura.get()) == False:
            labelAviso['text'] = 'Campo Altura com valores não numéricos'
            return False
        if x[i].entradaSexo.get() != 'M' and x[i].entradaSexo.get() != 'F':
            labelAviso['text'] = 'Campo Sexo errado, digite M ou F'
            return False
    return True

def enviar_Cadastros():
    global labelAviso

    if not verifica_Campos(cadastro):
        return
    if not tratatamento_Campos(cadastro):
        return

    labelAviso.destroy()
    labelAviso = Label(window,text='')
    labelAviso.grid(row=10,column=0,columnspan=2,sticky=W)
      
    for i in range(len(cadastro)):
        pessoas.append(cadastro[i].finalizar_Cadastro())
        cadastro[i].entradaNome.delete(0,'end')
        cadastro[i].entradaIdade.delete(0,'end')
        cadastro[i].entradaPeso.delete(0,'end')
        cadastro[i].entradaAltura.delete(0,'end')
        cadastro[i].entradaSexo.delete(0,'end')
        
def tabela(x,nome,idade,altura,peso,sexo,imc):
    labelNome = Label(window,text=nome)
    labelNome.grid(row=x,column=0,columnspan=2,sticky=W)

    labelIdade = Label(window,text=idade)
    labelIdade.grid(row=x,column=2,sticky=W)

    labelAltura = Label(window,text=altura)
    labelAltura.grid(row=x,column=3,sticky=W)

    labelPeso = Label(window,text=peso)
    labelPeso.grid(row=x,column=5,sticky=W)

    labelSexo = Label(window,text=sexo)
    labelSexo.grid(row=x,column=6,sticky=W)

    labelIMC = Label(window,text=imc)
    labelIMC.grid(row=x,column=7,sticky=W)

def calcular_IMC(peso,altura):
    i = float(peso) / (float(altura)*float(altura))
    imc = '{:.2f}'.format(i)
    return imc

def mostrar_Cadastros():

    tabela(12,'Nome','Idade','Peso','Altura','Sexo','IMC')

    for i in range(len(pessoas)):
        tabela(13+i,pessoas[i][0],pessoas[i][1],pessoas[i][2],pessoas[i][3],pessoas[i][4],calcular_IMC(pessoas[i][2],pessoas[i][3]))

def botoes():
    global x
    botaoAdicionar = Button(window,text='Adicionar Campo',command=lambda:adicionar_Campo(window))
    botaoAdicionar.grid(row=0,column=0)

    botaoEnviar = Button(window,text='Enviar Cadastros',command=enviar_Cadastros)
    botaoEnviar.grid(row=0,column=1)

    botaoMostrarBanco = Button(window,text='Mostrar Cadastros',command=mostrar_Cadastros)
    botaoMostrarBanco.grid(row=0,column=2)

    botaoRemover = Button(window,text='Remover Campo',command=remover_Campo)
    botaoRemover.grid(row=0,column=3)

window = Tk()
window.grid()
window.title('CalculoIMC')
window.geometry('800x450')

labelAviso = Label(window,text='')
labelAviso.grid(row=10,column=0,columnspan=3,sticky=W)

x = 1
cadastro = []
pessoas = []

botoes()

window.mainloop()