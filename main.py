#importando tkinter
from tkinter import *
from tkinter import ttk 

#cores
cor1 = "#127369"
cor2 = "#10403B"
cor3 = "#8AA6A3"
cor4 = "#4C5958"
cor5 = "#BFBFBF"


janela =Tk();
janela.title("Calculadora")
#primeirop valor largura segundo comprimento
janela.geometry("234x301")
janela.config(bg=cor1)

#criando frames
frame_tela = Frame(janela, width=235, height=50, bg = cor5)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


# Variável global para armazenar a expressão completa
todos_valores = ""

# --------------------------
# FUNÇÕES DE CÁLCULO E LÓGICA
# --------------------------

# 1. Função para acumular e ENTRAR valores (números e operadores)
def Entrar_valore(valor):
    global todos_valores
    
    # Adiciona o valor do botão à expressão
    todos_valores = todos_valores + str(valor)

    # Passa o valor acumulado para a tela
    valor_texto.set(todos_valores)

# 2. Função para limpar a tela (Botão DEL/C)
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# 3. Função para calcular o resultado (Botão =)
def calcular():
    global todos_valores
    try:
        # Usa eval() para executar a expressão matemática
        resultado = str(eval(todos_valores))
        
        # Exibe o resultado na tela
        valor_texto.set(resultado)
        
        # Mantém o resultado para que o usuário possa continuar a operação
        todos_valores = resultado 
        
    except Exception:
        # Em caso de erro (como divisão por zero ou operador sem segundo número), exibe "Erro"
        valor_texto.set("Erro")
        todos_valores = ""

# 4. Função para calcular a porcentagem (Botão %)
def calcular_porcentagem():
    global todos_valores
    
    if not todos_valores:
        return # Não faz nada se a tela estiver vazia

    try:
        # Pega a expressão atual (ex: "50" ou "200+10") e calcula 1% do resultado
        # Isso faz com que, ao apertar %, o valor seja dividido por 100.
        # Ex: Se todos_valores = "50", o resultado de eval("50/100") é 0.5
        resultado_porcentagem = str(eval(f'({todos_valores})/100'))
        
        valor_texto.set(resultado_porcentagem)
        todos_valores = resultado_porcentagem
            
    except Exception:
        # Erro caso a expressão seja inválida antes da porcentagem
        valor_texto.set("Erro %")
        todos_valores = ""


# Definição e inicialização da variável de controle para a Label
valor_texto = StringVar()

#criando label
app_label = Label(frame_tela, textvariable= valor_texto,width=16, height=2, padx=7, relief= FLAT, anchor="e", justify=RIGHT, font=('Ivy 17 bold'),bg=cor3, fg=cor4)
app_label.place( x=0, y=0)

# --------------------------
# CRIAÇÃO E MAPEAMENTO DOS BOTÕES
# --------------------------

#linha1
# Botão DEL (Limpa tudo)
b_1 = Button(frame_corpo, command=limpar_tela, text="DEL", width=11,height=2, bg=cor4, fg= cor5,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
# Botão % (Chama a função de porcentagem)
b_2 = Button(frame_corpo, command=calcular_porcentagem, text="%",width=5,height=2, bg= cor3,fg= cor5,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
# Botão /
b_3 = Button(frame_corpo, command= lambda:Entrar_valore('/'), text="/",width=5,height=2, bg= cor4,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_3.place(x=177,y=0)

#linha2
b_5 = Button(frame_corpo, command= lambda:Entrar_valore('7'), text="7",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_5.place(x=0,y=52)
b_6 = Button(frame_corpo, command= lambda:Entrar_valore('8'), text="8",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_6.place(x=59,y=52)
b_7 = Button(frame_corpo, command= lambda:Entrar_valore('9'), text="9",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_7.place(x=118,y=52)
b_8 = Button(frame_corpo, command= lambda:Entrar_valore('*'), text="*",width=5,height=2, bg= cor4,fg= cor5,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_8.place(x=177, y=52)

#linha3
b_9 = Button(frame_corpo, command= lambda:Entrar_valore('6'), text="6",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_9.place(x=0,y=103)
b_10 = Button(frame_corpo, command= lambda:Entrar_valore('5'), text="5",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_10.place(x=59,y=103)
b_11 = Button(frame_corpo, command= lambda:Entrar_valore('4'), text="4",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_11.place(x=118,y=103)
b_12 = Button(frame_corpo, command= lambda:Entrar_valore('-'), text="-",width=5,height=2, bg= cor4,fg= cor5,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_12.place(x=177, y=103)

#linha4
b_13 = Button(frame_corpo, command= lambda:Entrar_valore('3'), text="3",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_13.place(x=0,y=152)
b_14 = Button(frame_corpo, command= lambda:Entrar_valore('2'), text="2",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_14.place(x=59,y=152)
b_15 = Button(frame_corpo, command= lambda:Entrar_valore('1'), text="1",width=5,height=2, bg= cor3,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_15.place(x=118,y=152)
b_16 = Button(frame_corpo, command= lambda:Entrar_valore('+'), text="+",width=5,height=2, bg= cor4,fg= cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_16.place(x=177, y=152)

#linha5
b_17 = Button(frame_corpo, command= lambda:Entrar_valore('0'), text="0", width=11,height=2, bg=cor3,fg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_17.place(x=0, y=200)
# Botão IGUAL (=) - Chama calcular
b_18 = Button(frame_corpo, command=calcular, text="=",width=5,height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_18.place(x=177,y=200)
# Botão PONTO (.)
b_19 = Button(frame_corpo, command= lambda:Entrar_valore('.'), text=".",width=5,height=2, bg= cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_19.place(x=118, y=200)


janela.mainloop()