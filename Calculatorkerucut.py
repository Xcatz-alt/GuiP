from tkinter import *
import tkinter

def hitung():
    num1 = Entry.get(nomor1)
    num2 = Entry.get(nomor2)
    nums1 = float(num1)
    nums2 = float(num2)
    hasil = 1 / 3 * nums1 * nums2
    Entry.insert(jawaban,0,hasil)
    print(hasil)
tabel = tkinter.Tk()
label1 = Label(tabel, text = 'Perhitungan volume kerucut').grid(row = 0, column = 1)
label2 = Label(tabel, text = 'Diameter Alas').grid(row = 1, column = 0)
label3 = Label(tabel, text = 'tinggi').grid(row = 2, column = 0)
label4 = Label(tabel, text = 'hasil').grid(row = 3, column = 0)
nomor1 = Entry(tabel, bd =5)
nomor1.grid(row=1,column=1)
nomor2 = Entry(tabel, bd =5)
nomor2.grid(row=2,column=1)
jawaban = Entry(tabel, bd =5)
jawaban.grid(row=3,column=1)
b = Button(tabel, text = 'Submit', command = hitung).grid(row = 5, column = 1)

tabel.mainloop()
    