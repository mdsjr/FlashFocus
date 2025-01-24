import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

app = ttk.Window("Bootstrap Example")
app.geometry("550x500")
style = Style(theme="superhero")

label = ttk.Label(app, text="Hello, World!", style="success.TLabel")
label.pack(pady=35)
label.config(font=("Arial", 24, 'bold'))

nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome, text="Nome:").pack(side=LEFT, padx=5)
ttk.Entry(nome).pack(side=LEFT, fill="x", expand=True, padx=5)

email = ttk.Frame(app)
email.pack(pady=18, padx=10, fill="x")
ttk.Label(email, text="Email:").pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, fill="x", expand=True, padx=5)

idade = ttk.Frame(app)
idade.pack(pady=18, padx=10, fill="x")
ttk.Label(idade, text="Idade:").pack(side=LEFT, padx=5)
ttk.Entry(idade).pack(side=LEFT, fill="x", expand=True, padx=5)

checkbox = ttk.Frame(app)
checkbox.pack(pady=15, padx=10, fill="x")
ttk.Checkbutton(checkbox, bootstyle="round-toggle", text="Lembrar dados?").pack(side=LEFT, padx=5)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao, text="Enviar", bootstyle=SUCCESS).pack(side=LEFT, padx=15)
ttk.Button(botao, text="Cancelar", bootstyle=DANGER).pack(side=LEFT, padx=15)

app.mainloop()

