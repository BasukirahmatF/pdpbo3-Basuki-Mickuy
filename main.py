from tkinter import *
from PIL import ImageTk, Image

top = Tk()
top.title("Microphone")

frameSaya = Frame(top, width=100, height=100)
frameSaya.grid(row=0, column=0)

myLabel1 = Label(top, text="Nama Microphone :").grid(row=0, column=0)
merk = Entry(top, background = "blue")
merk.insert(0, "")
merk.grid(column=1, row=0)

myLabel1 = Label(top, text="Harga Microphone :").grid(row=1, column=0,padx=5,
pady=5)
harga = Entry(top, background = "blue")
harga.insert(0, "")
harga.grid(column=1, row=1)

myLabel1 = Label(top, text="Plug Type :").grid(row=2, column=0, columnspan=1)
options = [
    "USB",
    "XLR",
]
tipe = StringVar()
tipe.set(options[0])

drop = OptionMenu(top, tipe, *options)
drop.grid(column=1, row=2, columnspan=1)

myLabel2 = Label(top, text="Type Micprhone :").grid(row=3, column=0)
Jenis = [
    ("Condenser Microphone", "Condenser Microphone"),
    ("Dynamic Microphone", "Dynamic Microphone")
]

tpe = StringVar()
tpe.set("")

i = 1
for text, jenis, in Jenis:
    Radiobutton(top, text=text, variable=tpe, value=jenis).grid(column=i, row=3)
    i = i + 1

myLabel = Label(top, text="Terdapat Aksesoris :").grid(row=4, column=0)
var1 = StringVar()

aksesoris = Checkbutton(top, text="POP Filter", variable=var1, onvalue = "POP Filter", offvalue="")
aksesoris.deselect()
aksesoris.grid(column=1, row=4)

var2 = StringVar()

aksesoris = Checkbutton(top, text="Stand Mic", variable=var2, onvalue = "Stand Mic", offvalue="")
aksesoris.deselect()
aksesoris.grid(column=2, row=4)

var3 = StringVar()

aksesoris = Checkbutton(top, text="Busa Angin", variable=var3, onvalue = "Busa Angin", offvalue="")
aksesoris.deselect()
aksesoris.grid(column=3, row=4)

myButton = Button(top, text="Open Photo File", command=Image, fg="Black", bg="#FFFFFF")
myButton.grid(row=2, column=4)

myButton = Button(top, text="Submit", command=Image, fg="Black", bg="#FFFFFF")
myButton.grid(row=3, column=4)

myButton = Button(top, text="See All Submissons", command=Image, fg="Black", bg="#FFFFFF")
myButton.grid(row=5, column=1)

myButton = Button(top, text="Clear Submissons", command=Image, fg="Black", bg="#FFFFFF")
myButton.grid(row=6, column=1)

myButton = Button(top, text="Exit", command=Image, fg="Black", bg="#FFFFFF")
myButton.grid(row=6, column=4)

# def popup(nama):
#  response = messagebox.showinfo("This is my Popup", nama)
#     Label(root, text=response).pack()

top.mainloop()