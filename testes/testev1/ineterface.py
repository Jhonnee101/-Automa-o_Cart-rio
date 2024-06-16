
from func import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window("Extrator de Matriculas")
style = ttk.Style("darkly")

label = ttk.Label(root, text="Extrator de Matriculas")
label.pack(pady=20)
label.config(font=("Arial", 20, "bold"))


b1 = ttk.Button(root, text="Selecionar Planilha", command=selecionar_entrada, bootstyle=INFO)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Selecionar Pasta", command=selecionar_pasta, bootstyle=INFO)
b2.pack(side=LEFT, padx=5, pady=10)

b3 = ttk.Button(root, text="Iniciar Extração", command=extrair_matriculas, bootstyle=SUCCESS)
b3.pack(side=LEFT, padx=5, pady=10)

root.mainloop()