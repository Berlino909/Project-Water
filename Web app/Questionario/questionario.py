import tkinter as tk

dizionario_risposte = {}

def print_grafic(text):
    label_grafic = tk.Label(root, text=text, bg="lightgray", font=("Helvetica", 10))
    label_grafic.pack(pady=5)

def input_grafic(prompt):
    label_prompt = tk.Label(root, text=prompt, bg="lightgray", font=("Helvetica", 10))
    label_prompt.pack(pady=5)
    entry = tk.Entry(root, font=("Helvetica", 10))
    entry.pack(pady=5)
    return entry.get()

def domada1(nikename):
    print_grafic("Domanda 1: Qual è la fonte principale di acqua potabile nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")
    

def domada2(nikename):
    print_grafic("Domanda 2: Quante persone vivono nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada3(nikename):
    print_grafic("Domanda 3: Quale è la principale fonte di inquinamento dell'acqua nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada4(nikename):
    print_grafic("Domanda 4: Quante fonti di acqua potabile ci sono nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada6(nikename):
    print_grafic("Domanda 6: Qual è il principale utilizzo dell'acqua nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada7(nikename):
    print_grafic("Domanda 7: Quante persone hanno accesso all'acqua potabile nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada8(nikename):
    print_grafic("Domanda 8: Qual è il principale problema legato all'acqua nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada9(nikename):
    print_grafic("Domanda 9: Quante fonti di acqua potabile sono monitorate nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")

def domada10(nikename):
    
    print_grafic("Domanda 10: Qual è il principale fattore che influisce sulla qualità dell'acqua nella tua zona?")
    risposta = input_grafic("Risposta: ")
    print_grafic(f"{nikename} ha risposto: {risposta}")


def main(nikename):

    domada1(nikename)
    domada2(nikename)
    domada3(nikename)
    domada4(nikename)
    domada6(nikename)
    domada7(nikename)
    domada8(nikename)
    domada9(nikename)
    domada10(nikename)



root = tk.Tk()
root.geometry("400x500")
root.configure(bg="lightgray")
root.title("Questionario sull'acqua")

label_benvenuto = tk.Label(root, text="Benvenuto al questionario sull'acqua", bg="lightgray", font=("Helvetica", 12))
label_benvenuto.pack(pady=20)

label_info = tk.Label(root, text="Rispondi alle seguenti domande con le informazioni apprese sul sito dell' acqua", bg="lightgray", font=("Helvetica", 10))
label_info.pack(pady=10)

label_nikename = tk.Label(root, text="Inserisci il tuo nickname:", bg="lightgray", font=("Helvetica", 10))
label_nikename.pack(pady=10)

text_nikename = tk.Text(root, height=3, width=40)
text_nikename.pack(pady=10)

botton_inizia = tk.Button(
    root,
    text="Inizia il questionario",
    command=lambda: main(text_nikename.get("1.0", tk.END).strip()),
    bg="blue",
    fg="white",
    font=("Helvetica", 10),
)
botton_inizia.pack(pady=20)

root.mainloop()