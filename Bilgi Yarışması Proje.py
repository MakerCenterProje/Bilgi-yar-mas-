import tkinter as tk
import random as rand
import time


def oynat():
    window.destroy()
    with open("Sorular.txt", "r+") as file:
        p = 0
        s = 0

        for i in file:
            z = i.split("|")

    root = tk.Tk()
    root.title("_umt")


    def n():
        print("pressed")
        s =+ 5

    def n1():
        print("pressed")
        s =+ 5

    def n2():
        print("pressed")
        s =+ 5

    def n3():
        print("pressed")
        s =+ 5


    label1 = tk.Label(root,text=p)
    label0 = tk.Label(root,text="s")

    button1 = tk.Button(root,text=z[s+1],command=n)
    button2 = tk.Button(root,text=z[s+2],command=n1)
    button3 = tk.Button(root,text=z[s+3],command=n2)
    button4 = tk.Button(root,text=z[s+4],command=n3)


    label1.grid(row=0,column=15)
    label0.grid(row=0,column=1)

    button1.grid(row=1,column=1)
    button2.grid(row=2,column=1)
    button3.grid(row=3,column=1)
    button4.grid(row=4,column=1)

    root.mainloop()



def yapımcılar():
    Yapımcılar = tk.Tk()
    Yapımcılar.geometry("1000x1000")
    Yapımcılar.title("YAPIMCILAR")
    Baslık = tk.Label(Yapımcılar,text="--YAPIMCILAR--",font="100000")
    Ata = tk.Label(Yapımcılar,text="ATA",font="10000")
    Umut = tk.Label(Yapımcılar,text="UMUT",font="10000")
    Burak = tk.Label(Yapımcılar,text="Burak",font="10000")
    Melih = tk.Label(Yapımcılar,text="Melih",font="10000")
    Baslık.pack()
    Ata.pack()
    Umut.pack()
    Burak.pack()
    Melih.pack()


    Yapımcılar.mainloop()

def AnaMenu():
    window = tk.Tk()
    window.title("bilgi yarismasi")
    etiket1 = tk.Label(window, text="---BİLGİ YARIŞMASI---",font="10000",fg="Blue")
    etiket1.pack()
    etiket2 = tk.Label(window, text="---Başlamak için Oyna ya tıklayın---",font="1000",fg="Green")
    etiket2.pack()
    buton = tk.Button(window,text="oyna",command=oynat)
    buton.pack()

    buton2 = tk.Button(window,text="Yapımcılar",command=yapımcılar)
    buton2.pack()
    window.geometry("10000x10000")





    window.mainloop()
AnaMenu()




