# importar as bibliotecas ------------------------------------------------------------
from tkinter import *
import threading
#-------------------------------------------------------------------------------------
# importar o backend -----------------------------------------------------------------
# criar uma interface -----------------------------------------------------------------------------------
def create_interface():
    global Janela
    global equation_var
#--------------------------------------------------------------------------------------------------------

def on_closing():
        Janela.destroy()

def press(num):
    global equation
    if num == '%':
        equation = equation + '/100'
    else:
        equation = equation + str(num)
    equation_var.set(equation)


def remove_last_character():
    global equation
    equation = equation[:-1]
    equation_var.set(equation)


def equalpress():
    try:
        global equation
        total = str(eval(equation))
        equation_var.set(total)
        equation = ""
    except:
        equation_var.set(" error ")
        equation = ""


def clear():
    global equation
    equation = ""
    equation_var.set("")
#--------------------------------------------------------------------------------------------------------
# Definir cores------------------------------------------------------------------------------------------
co0 = '#ffffff'  # cor branca de fundo
co1 = '#f7f7ff'  # cinza claro para o visor
co2 = '#917867'  # castanho para os botões
#--------------------------------------------------------------------------------------------------------
# Configurar a janela -----------------------------------------------------------------------------------
Janela = Tk()
Janela.geometry('200x235+100+100')
Janela.resizable(False, False)
Janela.title('calc')
Janela.configure(bg=co0)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\Calculadora\\icon.ico')
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# Variável para armazenar a expressão -------------------------------------------------------------------
equation = ""
equation_var = StringVar()
#--------------------------------------------------------------------------------------------------------
# Criar o visor -----------------------------------------------------------------------------------------
Eecra = Entry(Janela, textvariable=equation_var, bg=co1, font=('arial 12 bold'), width=19, justify=RIGHT)
Eecra.place(x=10, y=0)
#--------------------------------------------------------------------------------------------------------
# Criar os botões de números ----------------------------------------------------------------------------
Bnove = Button(Janela, text='9', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(9))
Bnove.place(x=100, y=65)
Boito = Button(Janela, text='8', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(8))
Boito.place(x=55, y=65)
Bsete = Button(Janela, text='7', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(7))
Bsete.place(x=10, y=65)
Bseis = Button(Janela, text='6', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(6))
Bseis.place(x=100, y=99)
BCinco = Button(Janela, text='5', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(5))
BCinco.place(x=55, y=99)
BQuatro = Button(Janela, text='4', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(4))
BQuatro.place(x=10, y=99)
Btres = Button(Janela, text='3', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(3))
Btres.place(x=100, y=134)
Bdois = Button(Janela, text='2', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(2))
Bdois.place(x=55, y=134)
BUm = Button(Janela, text='1', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(1))
BUm.place(x=10, y=134)
Bzero = Button(Janela, text='0', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press(0))
Bzero.place(x=10, y=169)
Bponto = Button(Janela, text=',', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press('.'))
Bponto.place(x=55, y=169)
Bigual = Button(Janela, text='=', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=equalpress)
Bigual.place(x=100, y=169)
#-------------------------------------------------------------------------------------------------------
# Criar o botão de limpar-------------------------------------------------------------------------------
BClear = Button(Janela, text='C', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=clear)
BClear.place(x=10, y=30)
#-------------------------------------------------------------------------------------------------------
# Criar o botão backspace ------------------------------------------------------------------------------
BBack = Button(Janela, text='⌫', font=('arial 12 bold'), width=8, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=remove_last_character)
BBack.place(x=52, y=30)
#-------------------------------------------------------------------------------------------------------
# Criar os operadores aritméticos ----------------------------------------------------------------------
BModulo = Button(Janela, text='%', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press('%'))
BModulo.place(x=145, y=30)
BDiv = Button(Janela, text='/', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press('/'))
BDiv.place(x=145, y=65)
BMul = Button(Janela, text='X', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press('*'))
BMul.place(x=145, y=99)
BSub = Button(Janela, text='-', font=('arial 12 bold'), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press('-'))
BSub.place(x=145, y=134)
BAdd = Button(Janela, text='+', font=('arial 12 bold '), width=3, relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1, command=lambda: press('+'))
BAdd.place(x=145, y=169)
#------------------------------------------------------------------------------------------------------
# criar o label Autor----------------------------------------------------------------------------------
Lautor = Label(Janela, text='Dev Joel 2024 Portugal ©', bg=co0, font=('Arial 11 bold'))
Lautor.place(x=10, y=210)
#------------------------------------------------------------------------------------------------------
# bloqueio de rastriamento ----------------------------------------------------------------------------
Janela.protocol("WM_DELETE_WINDOW", on_closing)
Janela.mainloop() 
#------------------------------------------------------------------------------------------------------
# Criar um thread para a função de criação de interface -----------------------------------------------
interface_thread = threading.Thread(target=create_interface)
interface_thread.start()
#------------------------------------------------------------------------------------------------------
# Iniciar a janela-------------------------------------------------------------------------------------
Janela.mainloop()
#------------------------------------------------------------------------------------------------------
