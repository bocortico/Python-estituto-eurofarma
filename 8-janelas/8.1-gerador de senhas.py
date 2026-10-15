#importando biblioteca e nomeando de 'tk'
import tkinter as tk
import random
import string
ALTURA='400'
LARGURA='450' 
#=========================================
#0.logica por traz de tudo isso...
#=========================================
def gerar_senha():
    try:
        tamanho =int(tamanho=entry_tamanho_senha.get())

    
        if tamanho < 4:
            lbl_resultado.config(
                text='erro, minimo de 4 caracteres',
                fg='#FF05DF'
            )
            return

        caracteres =''

        if var_maiusculas.get():
            caracteres +=string.ascii_uppercase
        if var_minusculas.get():
            caracteres +=string.ascii_lowercase
        if var_numero.get():
            caracteres +=string.digits
        if var_simbolo.get():
            caracteres +=string.punctuation
        if not caracteres:
            lbl_resultado.config(
                text='erro selecione ao menos uma opção',
                fg='#FF05DF'
            )
            return
    
        senha = "".join(random.choice(caracteres) for i in range (tamanho))    
        lbl_resultado.config(
            text= ('senha: (senha)'),
            fg= '#FF05DF'
        )
    except ValueError:
        lbl_resultado.config(
            text='error digite algum numero valido',
            fg='#FF05DF'
        )



#=========================================
#1.configuração de janela principal.
#=========================================

janela = tk.Tk()
janela.title('senha segura')
janela.geometry(f'{LARGURA}x{ALTURA}')
janela.config(bg="#2E3440")

#=========================================
#2.titulo principal do arquivo
#=========================================

titulo = tk.Label(
    text = 'senhas ultra iradas ',
    font  = ('Comic Sans MS' ,16, 'bold'),
    bg = "#2E3440",
    fg = "#FF05DF"
)

titulo.pack(pady=20)

#=========================================
#3.Label tamanho senha
#=========================================

lbl_tamanho_senha = tk.Label(
    text = 'insira uma senha abaixo',
    font  = ('Comic Sans MS' ,13, 'bold'),
    bg = "#2E3440",
    fg = "#FF05DF"
)

lbl_tamanho_senha.pack(pady=20)

#=========================================
#4.entrada tamanho ou senha
#=========================================

entry_tamanho_senha = tk.Entry(
    janela,
    font = ('Comic Sans MS', 13),
    width=12,
    justify='center',
)

entry_tamanho_senha.pack(pady=20)

#=========================================
#5.criando variaveis de crontrole (true e false)
#=========================================

var_maiusculas=tk.BooleanVar(value=False)
var_minusculas=tk.BooleanVar(value=True)
var_numero=tk.BooleanVar(value=True)
var_simbolo=tk.BooleanVar(value=True)

#=========================================
#6.criando as caixinhas de seleção
#=========================================

chk_maiuscula = tk.Checkbutton(
    janela,
    text = 'maiusculas',
    variable = var_maiusculas,
    bg = "#FF05DF",
    fg = "#2E3440",
    selectcolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_maiuscula.pack(anchor='w', padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text = 'minusculas',
    variable = var_minusculas,
    bg = "#FF05DF",
    fg = "#2E3440",
    selectcolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_minuscula.pack(anchor='w', padx=60, pady=2)

chk_numero = tk.Checkbutton(
    janela,
    text = 'numero',
    variable = var_numero,
    bg = "#FF05DF",
    fg = "#2E3440",
    selectcolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_numero.pack(anchor='w', padx=60, pady=2)

chk_simbolo = tk.Checkbutton(
    janela,
    text = 'simbolos',
    variable = var_simbolo,
    bg = "#FF05DF",
    fg = "#2E3440",
    selectcolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_simbolo.pack(anchor='w', padx=60, pady=2)


#========================================
#7.criar botão gerador de senha
#========================================

btg_gerar= tk.Button(
    janela,
    text="gerar senha safada",
    command = gerar_senha,    
    bg='#FF05DF',
    fg="#2E3440",
    padx=10,
    pady=5
)
btg_gerar.pack(pady=15)

lbl_resultado = tk.Label(
    janela,
    text= 'a senha aparecera aqui',
        font=('Comic Sans MS', 11, 'bold'),
        bg= '#FF05DF',
        fg= '#2E3440',
)
lbl_resultado.pack(pady=5)

janela.mainloop()