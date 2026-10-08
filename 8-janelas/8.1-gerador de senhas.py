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

janela.mainloop()