from tkinter import *
from calculadora import Calculadora

def adicionar(n):
    global apagar
    if n.isnumeric() and apagar:
        resultado['text'] = ""
    if len(resultado['text']) < 12:
        resultado['text'] += str(n)
    apagar = False
        
def remover():
    resultado['text']= resultado['text'][:-1]

def calcular():
    global apagar
    apagar = True
    resultado['text']+='?'
    calculadora = Calculadora()
    try:
        res = '{:.2f}'.format(float(calculadora.calcular(resultado['text'])))
        resultado['text'] = str(res)
    except:
        resultado['text'] = 'Error'

apagar = False
janela = Tk()
janela.title('Calculadora')
janela.resizable(False,False)

resultado = Label(janela,text="",background='lightgray',font=('Arial', 40, 'normal'),justify='left',foreground='black')
resultado.grid(column=0,row=0,sticky=NSEW,columnspan=4)

botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 1), ('+', 4, 3), ('=', 4, 2), ('⬅', 4, 0)
        ]

for (text, row, col) in botoes:
    if text == '=':
        botao = Button(janela, text=text, font=('Arial', 20),width=5,height=2, command=calcular)
        botao.grid(row=row, column=col, sticky='nsew')
    elif text == '⬅':
        botao = Button(janela, text=text, font=('Arial', 20),width=5,height=2, command=remover)
        botao.grid(row=row, column=col, sticky='nsew')
    else:
        botao = Button(janela, text=text, font=('Arial', 20),width=5,height=2, command=lambda t=text: adicionar(t))
        botao.grid(row=row, column=col, sticky='nsew')

janela.mainloop()