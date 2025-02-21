import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Inicializa a janela principal
janela = ttk.Tk()  # Usa ttk.Tk para criar a janela principal
janela.title("Exemplo Caixa de Texto")
janela.geometry("600x400")

# Configura o tema usando o ttkbootstrap
style = ttk.Style(theme="superhero")

# Cria um widget Text estilizado
label_palavra = Text(
    janela,
    height=2,
    font=("Helvetica", 24),
    bg=style.colors.get("info", "#ffffff"),  # Define a cor de fundo baseada no tema
    fg=style.colors.get("secondary", "#000000"),  # Define a cor do texto
)
label_palavra.pack(pady=20)

# Configura a tag de formatação para a letra central
label_palavra.tag_configure(
    "central", 
    font=("Helvetica", 24, "bold"), 
    foreground="red"
)

# Configura a tag para centralizar o texto
label_palavra.tag_configure("center", justify='center')

# Adiciona texto de exemplo
label_palavra.insert("1.0", "Texto de exemplo para centralizar.")
label_palavra.tag_add("center", "1.0", "end")

# Inicia o loop principal da aplicação
janela.mainloop()
