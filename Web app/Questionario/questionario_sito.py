import tkinter as tk

# Dizionario risposte utente
dizionario_risposte = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None}

# RISPOSTE CORRETTE AGGIORNATE IN BASE AI TESTI DEL SITO
# Nota: convertiamo tutto in minuscolo durante il controllo per evitare errori di battitura (es. Vero vs vero)
dizionario_risposte_giuste = {
    1: "elevata",
    2: "6300",
    3: "60%",
    4: "falso",
    5: "98",
    6: "tensioattivo",
    7: "4",
    8: "ghiaccio",
    9: "marsiglia",
    10: "ph",
}

questions = [
    (1, "Quanti litri di acqua virtuale servono (in media) per un chilo di carne bovina?"),
    (2, "Qual è la percentuale media di acqua nel corpo di un essere umano adulto?"),
    (3, "Vero o falso: l'acqua è il nostro principale carburante energetico durante lo sport?"),
    (4, "A quale temperatura (in °C) è iniziata l'ebollizione tumultuosa nel vostro esperimento 1?"),
    (5, "Quale sostanza (es. detersivo) spezza i legami della tensione superficiale dell'acqua?"),
    (6, "A quale temperatura (in °C) l'acqua raggiunge il suo picco di massima densità?"),
    (7, "Quale stato dell'acqua galleggia a causa del reticolo cristallino esagonale espanso?"),
    (8, "Nel secondo esperimento di Hera che sapone abbiamo usato?"),
    (9, "Qual è l'unità di misura (scritto con la corretta maiuscola/minuscola) per l'acidità di un sistema?"),
]

def print_grafic(text):
    label_grafic = tk.Label(root, text=text, bg="white", fg="black", font=("Helvetica", 10), wraplength=350, justify="left")
    label_grafic.pack(pady=5)

def pulisci_schermo():
    for widget in root.winfo_children():
        widget.destroy()

def invia(index, entry_risposta, nikename, nrisposta):
    risposta = entry_risposta.get().strip()
    dizionario_risposte[nrisposta] = risposta
    mostra_domanda(nikename, index + 1)

def fine_questionario(nikename):
    pulisci_schermo()
    print_grafic(f"Grazie per aver completato il questionario, {nikename}!")
    print_grafic("Le tue risposte:")
    
    punteggio_finale = 0
    for n, risposta in dizionario_risposte.items():
        # Controllo case-insensitive (ignora maiuscole e minuscole)
        corretta = dizionario_risposte_giuste[n]
        if str(risposta).lower() == str(corretta).lower():
            punteggio_finale += 1
            esito = "✅ Corretta"
        else:
            esito = f"❌ Errata (Risposta corretta: {corretta})"
            
        print_grafic(f"Domanda {n}: {risposta} -> {esito}")
        
    print_grafic(f"\nPunteggio finale di {nikename}: {punteggio_finale}/10")

def mostra_domanda(nikename, index):
    pulisci_schermo()
    if index >= len(questions):
        fine_questionario(nikename)
        return
        
    nrisposta = questions[index][0]
    testo = questions[index][1]
    
    print_grafic(f"Domanda {nrisposta}: {testo}")
    
    entry_risposta = tk.Entry(root, font=("Helvetica", 10), width=40)
    entry_risposta.pack(pady=5)
    entry_risposta.focus_set() # Mette il cursore pronto per scrivere

    button = tk.Button(root, text="Invia", command=lambda: invia(index, entry_risposta, nikename, nrisposta))
    button.pack(pady=5)

def main(nikename):
    if not nikename:
        nikename = "Anonimo"
    mostra_domanda(nikename, 0)

# Configurazione Finestra Principale
root = tk.Tk()
root.geometry("400x650")
root.configure(bg="#1a2a6c") # Cambiato blu elettrico con il blu scuro del vostro sito

label_benvenuto = tk.Label(root, text="Benvenuto al questionario sull'acqua", bg="#1a2a6c", fg="white", font=("Helvetica", 14, "bold"))
label_benvenuto.pack(pady=20)

label_info = tk.Label(root, text="Rispondi alle seguenti domande basandoti sulle informazioni apprese all'interno del portale interdisciplinare.", bg="white", fg="black", font=("Helvetica", 10), wraplength=350, justify="center")
label_info.pack(pady=10)

label_nikename = tk.Label(root, text="Inserisci il tuo nickname:", bg="#1a2a6c", fg="white", font=("Helvetica", 10, "bold"))
label_nikename.pack(pady=10)

# Usiamo un Entry per il nickname (più facile da gestire per una riga singola rispetto a Text)
entry_nikename = tk.Entry(root, font=("Helvetica", 11), width=30)
entry_nikename.pack(pady=5)

botton_inizia = tk.Button(
    root,
    text="Inizia il questionario",
    command=lambda: main(entry_nikename.get().strip()),
    bg="#00c3ff", # Colore azzurro ripreso dal sottotitolo del vostro sito
    fg="black",
    font=("Helvetica", 11, "bold"),
    padx=10,
    pady=5
)
botton_inizia.pack(pady=20)

root.mainloop()