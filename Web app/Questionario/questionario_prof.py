import tkinter as tk

test = [
     {
        "domanda": "Quale la media dell' impronta idrica nella classe 1P ?",
        "opzioni": ["Milano", "Roma", "Napoli", "Torino"],
        "risposta_esatta": "//"
    },
   {
        "domanda": "Quanto e la media dell' impronta idrica in Italia ?",
        "opzioni": ["6.300", "8.000", "9", "7.568"],
        "risposta_esatta": "6.300"
    },
   {
        "domanda": "Quanto è la percentuale di acqua nel nostro corpo ?",
        "opzioni": ["50%", "60%", "70%", "80%"],
        "risposta_esatta": "60%"
    },
     {
        "domanda": "Vero o falso: l'acqua è il nostro principale carburante?",
        "opzioni": ["Vero", "Falso"],
        "risposta_esatta": "Vero"
    },
     {
        "domanda": "A quanto bolle l'acqua??",
        "opzioni": ["34", "200", "657", "100"],
        "risposta_esatta": "100"
    },
     {
        "domanda": "DOMANDA CHIMICA",
        "opzioni": ["Dante Alighieri", "Giacomo Leopardi", "Alessandro Manzoni", "Giovanni Boccaccio"],
        "risposta_esatta": "//"
    },
     {
        "domanda": "DOMANDA FISICA",
        "opzioni": ["Dante Alighieri", "Giacomo Leopardi", "Alessandro Manzoni", "Giovanni Boccaccio"],
        "risposta_esatta": "//"
    },
     {
        "domanda": "DOMANDA FISICA",
        "opzioni": ["Dante Alighieri", "Giacomo Leopardi", "Alessandro Manzoni", "Giovanni Boccaccio"],
        "risposta_esatta": "//"
    },
     {
        "domanda": "Nel secondo esperimento di Hera che sapone abbiamo usato?",
        "opzioni": ["Genova", "Marsiglia", "Monaco", "Venezia"],
        "risposta_esatta": "Marsiglia"
    },
     {
        "domanda": "Qual è l'unità di misura per l'acidita di un sistema?",
        "opzioni": ["m", "s", "Ph", "N"],
        "risposta_esatta": "Ph"
    },
]

def print_grafic(text):
    label_grafic = tk.Label(root, text=text, bg="white", font=("Helvetica", 10), wraplength=350, justify="left")
    label_grafic.pack(pady=5)




risposte=[]
punteggio = 0
def mostraRisultati(punteggio):
    for widget in root.winfo_children():
        widget.destroy()
        
    root.geometry("600x900")
    frame_risultati = tk.Frame(root, bg="#eeaa83")
    frame_risultati.pack(expand=True, fill="both")
    
    titolo = tk.Label(frame_risultati)
    titolo.config( text="Risultati del Quiz", font=("Arial", 18, "bold"), bg="#eeaa83")
    titolo.pack(pady=30)

    for i, domanda in enumerate(test):
        risposta_data = risposte[i]
        risposta_giusta = test[i]["risposta_esatta"]
        testo = f"{i+1}. {domanda['domanda']}\nLa tua risposta: {risposta_data} \nRisposta corretta: {risposta_giusta}"
        if risposta_data == risposta_giusta:
            punteggio += 1
        lbl = tk.Label(frame_risultati)
        lbl.config(text=testo, font=("Arial", 12), bg="#eeaa83", fg="blue", justify="left")
        lbl.pack(anchor="w", padx=30, pady=10)
    print_grafic(f"Punteggio finale: {punteggio}/{len(test)}")


    btn_esci = tk.Button(frame_risultati, text="Chiudi Programma", command=root.quit)
    btn_esci.pack(pady=30)   


def salva(risposta,indice,punteggio):
    risposte.append(risposta)
   
    if indice < len(test) - 1:
        mostra(test[indice+1], indice+1, punteggio)   
    else:
        mostraRisultati(punteggio)

def mostra(dom, indice ,punteggio):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame2 = tk.Frame(root)
    frame2.pack(expand=True, fill="both")
    frame2.config(bg="#eeaa83")
    
    
    etichetta = tk.Label(frame2)
    etichetta.config(text=dom["domanda"], font=("Arial", 16, "bold"), bg="#eeaa83", wraplength=500)
    etichetta.pack(pady=(20, 20), anchor="w", padx=30) 
    frame2.var_scelta = tk.StringVar()
    frame2.var_scelta.set("nessuna scelta") 
    
    for opzione in dom["opzioni"]:
      
        btn_risposta = tk.Radiobutton(frame2)
       
        btn_risposta.config(text=opzione, bg="#eeaa83", font=("Arial", 12), variable=frame2.var_scelta,value=opzione)
        btn_risposta.pack(anchor="w", padx=50, pady=5)
    
    bottone = tk.Button(frame2)
    bottone.config(text="Successivo", command=lambda: salva(frame2.var_scelta.get(), indice, punteggio))
       

    bottone.pack(pady=30)
    bottone.pack()



root = tk.Tk()
root.title("Questionario")
root.geometry("600x700")

mostra(test[0],0,0)

root.mainloop()
