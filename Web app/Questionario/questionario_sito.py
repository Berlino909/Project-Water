import tkinter as tk

dizionario_risposte = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None}
dizionario_risposte_giuste = {
    1: "fiume",
    2: "6.300",
    3: "60%",
    4: "Vero",
    5: "100",
    6: "//",
    7: "//",
    8: "//",
    9: "marsiglia",
    10: "Ph",
}

punteggio = 0


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
    label_grafic = tk.Label(root, text=text, bg="white", font=("Helvetica", 10), wraplength=350, justify="left")
    label_grafic.pack(pady=5)

def pulisci_schermo():
    for widget in root.winfo_children():
        widget.destroy()

def invia(index , entry_risposta , nikename , nrisposta):
    risposta = entry_risposta.get().strip()
    dizionario_risposte[nrisposta] = risposta
    mostra_domanda(nikename, index + 1)

def fine_questionario(nikename , punteggio):
    pulisci_schermo()
    print_grafic(f"Grazie per aver completato il questionario, {nikename}!")
    print_grafic("Le tue risposte:")
    for n , risposta in dizionario_risposte.items():
        if risposta == dizionario_risposte_giuste[n]:
            punteggio += 1
        print_grafic(f"Domanda {n}: {risposta} (Risposta corretta: {dizionario_risposte_giuste[n]})")
    print_grafic(f"Punteggio finale: {punteggio}/10")

def mostra_domanda(nikename, index):
    pulisci_schermo()
    if index >= len(questions):
        fine_questionario(nikename, punteggio)
        return
    nrisposta = questions[index][0]
    testo = questions[index][1]
    print_grafic(f"Domanda {nrisposta}: {testo}")
    entry_risposta = tk.Entry(root, font=("Helvetica", 10), width=40)
    entry_risposta.pack(pady=5)

    button = tk.Button(root, text="Invia", command=lambda: invia(index , entry_risposta , nikename , nrisposta))
    button.pack(pady=5)



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