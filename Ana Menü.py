

def yapımcılar():
    Yapımcılar = tk.Tk()
    Yapımcılar.geometry("1000x1000")
    Yapımcılar.title("YAPIMCILAR")
    arkaplan = tk.Label(Yapımcılar,font="100000000")
    Baslık = tk.Label(Yapımcılar,text="--YAPIMCILAR--",font="Times 30 italic",fg="blue")
    Ata = tk.Label(Yapımcılar,text="ATA",font="Times 20 italic",fg="Red")
    Umut = tk.Label(Yapımcılar,text="UMUT",font="Times 20 italic",fg="Gray")
    Burak = tk.Label(Yapımcılar,text="Burak",font="Times 20 italic",fg="Green")
    Melih = tk.Label(Yapımcılar,text="Melih",font="Times 20 italic",fg="Orange")
    Baslık.pack()
    Ata.pack()
    Umut.pack()
    Burak.pack()
    Melih.pack()


    Yapımcılar.mainloop()


    Yapımcılar.mainloop()

def AnaMenu():
    window = tk.Tk()
    window.title("Bilgi Yarismasi")
    etiket1 = tk.Label(window, text="--BİLGİ YARIŞMASI--",font="Times 100 italic",fg="Blue")

    etiket1.pack()
    etiket2 = tk.Label(window, text="---Başlamak için Oyna ya tıklayın---",font="Times 50 italic",fg="Green")
    etiket2.pack()
    buton = tk.Button(window,text="oyna",font="Times 30 italic",command=oynat)
    buton.pack()


    buton2 = tk.Button(window,text="Yapımcılar",font="Times 30 italic",command=yapımcılar)
    buton2.pack()

    window.geometry("10000x10000")





    window.mainloop()

AnaMenu()

