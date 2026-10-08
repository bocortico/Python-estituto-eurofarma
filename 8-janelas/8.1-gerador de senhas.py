#importando biblioteca e nomeando de 'tk'
import tkinter as tk
ALTURA='400'
LARGURA='450'
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
    bg = "#2E3440",
    fg = "#FF05DF",
    seleccolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_maiuscula.pack(anchor='w', padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text = 'minusculas',
    variable = var_minusculas,
    bg = "#2E3440",
    fg = "#FF05DF",
    seleccolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_minuscula.pack(anchor='w', padx=60, pady=2)

chk_numero = tk.Checkbutton(
    janela,
    text = 'minusculas',
    variable = var_numero,
    bg = "#2E3440",
    fg = "#FF05DF",
    seleccolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_numero.pack(anchor='w', padx=60, pady=2)

chk_simbolo = tk.Checkbutton(
    janela,
    text = 'simbolos',
    variable = var_simbolo,
    bg = "#2E3440",
    fg = "#FF05DF",
    seleccolor = "#FF05DF",
    activebackground = "#FF05DF",
    activeforeground = "#2E3440"
)

chk_simbolo.pack(anchor='w', padx=60, pady=2)

janela.mainloop()