import tkinter as tk
import subprocess

def executar_programa1():
    subprocess.Popen(['python', 'extrair_mat/extrator.py'])

def executar_programa2():
    subprocess.Popen(['python', 'pegar_mat/copiador.py'])

root = tk.Tk()
root.title("Launcher de Programas")
root.geometry("400x400")

label = tk.Label(root, text="Launcher de Programas")
label.pack(pady=20)
label.config(font=("Courier New", 18, "bold"))

b1 = tk.Button(root, text="Copiador", command=executar_programa1)
b1.pack(side=tk.TOP, padx=5, pady=10)

b2 = tk.Button(root, text="Extrator", command=executar_programa2)
b2.pack(side=tk.TOP, padx=5, pady=10)

root.mainloop()
