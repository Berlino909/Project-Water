import tkinter as tk

dizionario_risposte = {i: None for i in range(1, 11)}
dizionario_risposte_giuste = {
    1: "fiume",
    2: "6.300 ",
    3: "60%",
    4: "Vero",
    5: "100",
    6: "//",
    7: "//",
    8: "//",
    9: "marsiglia",
    10: "ph",
}

questions = [
    (1, "Quale la media dell' impronta idrica nella classe 1P ?"),
    (2, "Quanto e la media dell' impronta idrica in Italia ?"),
    (3, "Quanto è la percentuale di acqua nel nostro corpo ?"),
    (4, "Vero o falso: l'acqua è il nostro principale carburante?"),
    (5, "A quanto bolle l'acqua?"),
    (6, "DOMANDA CHIMICA"),
    (7, "DOMANDA FISICA"),
    (8, "DOMANDA FISICA"),
    (9, "Nel secondo esperimento che sapone abbiamo usato?"),
    (10, "Qual è l'unità di misura per l'acidita di un sistema?"),
]

def print_grafic(text):
    label_grafic = tk.Label(root, text=text, bg="lightgray", font=("Helvetica", 10), wraplength=350, justify="left")
    label_grafic.pack(pady=5)

def pulisci_schermo():
    for widget in root.winfo_children():
        widget.destroy()

def mostra_domanda(nikename, index=0):
    if index >= len(questions):
        fine_questionario(nikename)
        return

    nr, testo = questions[index]
    pulisci_schermo()
    print_grafic(f"Domanda {nr}: {testo}")

    entry = tk.Entry(root, font=("Helvetica", 10), width=40)
    entry.pack(pady=5)

    def invia():
        risposta = entry.get().strip()
        dizionario_risposte[nr] = risposta
        mostra_domanda(nikename, index + 1)

    botton_invia = tk.Button(
        root,
        text="Invia la risposta",
        command=invia,
        bg="blue",
        fg="white",
        font=("Helvetica", 10),
    )
    botton_invia.pack(pady=20)


def fine_questionario(nikename):
    pulisci_schermo()
    print_grafic("Questionario completato! Grazie per le tue risposte.")
    print_grafic(f"Nickname: {nikename}")
    print_grafic("Risposte salvate:")
    for nr in range(1, len(questions) + 1):
        risposta = dizionario_risposte[nr] or 'Nessuna risposta'
        risposta_giusta = dizionario_risposte_giuste.get(nr)
        if risposta == risposta_giusta:
            print_grafic(f"{nr}: {risposta} (Corretta)")
        else:
            print_grafic(f"{nr}: {risposta} (Errata - Risposta corretta: {risposta_giusta})")

def main(nikename):
    mostra_domanda(nikename, 0)

root = tk.Tk()
root.geometry("400x600")
root.configure(bg="blue")
root.title("Questionario sull'acqua")

label_benvenuto = tk.Label(root, text="Benvenuto al questionario sull'acqua", bg="blue", font=("Helvetica", 12))
label_benvenuto.pack(pady=20)

label_info = tk.Label(root, text="Rispondi alle seguenti domande con le informazioni apprese sul sito dell'acqua", bg="white" ,fg ="black", font=("Helvetica", 10), wraplength=350, justify="left")
label_info.pack(pady=10)

label_nikename = tk.Label(root, text="Inserisci il tuo nickname:", bg="blue",fg ="black", font=("Helvetica", 10))
label_nikename.pack(pady=10)

text_nikename = tk.Text(root, height=3, width=40)
text_nikename.pack(pady=10)

botton_inizia = tk.Button(
    root,
    text="Inizia il questionario",
    command=lambda: main(text_nikename.get("1.0", tk.END).strip()),
    bg="red",
    fg="white",
    font=("Helvetica", 10),
)
botton_inizia.pack(pady=20)

root.mainloop()

root.mainloop()