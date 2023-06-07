from tkinter import *
import tkinter as tk
from tkinter import NS, Canvas, Scrollbar, ttk

class Sc:
    def sc(liste):
        try:
            def gir():
                max_ = float(bo_max.get())
                min_ = float(bo_min.get())
                for i in range(len(liste)-1):
                    if not min_<liste[i][0]<max_:
                        liste.pop(i)
        except ValueError:
            ...

        screen = tk.Tk()
        screen.title("yazlab")
        screen.geometry("1000x900")
        #screen.resizable(0, 0)

        screen.configure(bg="LightBlue")

        l1 = Label(screen)
        l1.config(text="Thread Sayısı", font=(10))
        l1.grid(row=0, column=0, pady=10)
        t_sayi = Entry(screen)
        t_sayi.grid(row=1, column=0, pady=10)

        l2 = Label(screen)
        l2.config(text="Benzerlik Oranı:", font=(10))
        l2.grid(row=2, column=0, pady=10)

        l3 = Label(screen)
        l3.config(text="max", font=10)
        l3.grid(row=3, column=0, pady=10)
        bo_max = Entry(screen)
        bo_max.grid(row=4, column=0, pady=10)

        l4 = Label(screen)
        l4.config(text="min", font=10)
        l4.grid(row=5, column=0, pady=10)
        bo_min = Entry(screen)
        bo_min.grid(row=6, column=0, pady=10)

        b1 = Button(screen)
        b1.config(text="Göster", activeforeground="lime", font=7, command=gir)
        b1.grid(row=7, column=0, pady=50)


        def create_table_layout(screen):
            canvas = tk.Canvas(screen)
            yscrollbar = ttk.Scrollbar(canvas, orient='vertical')
            table = ttk.Treeview(canvas, yscrollcommand=yscrollbar.set, columns=("c0","c1","c2"))
            table.grid(row=5, column=0, rowspan=10, columnspan=3)
            table.column("#0", width=90, anchor=tk.W, stretch=tk.NO)
            table.column("#1", width=350, anchor=tk.W, stretch=tk.NO)
            table.column("#2", width=150, anchor=tk.W, stretch=tk.NO)

            table.heading("#0", text="Benzerlik Oranı")
            table.heading("#1", text="Metin-1")
            table.heading("#2", text="Metin-2")

            for i in range(len(liste)):
                table.insert('', 'end', text=liste[i][0], values=(liste[i][1], liste[i][2]))

            yscrollbar.configure(command=table.yview)
            yscrollbar.grid(row=0, column=0, rowspan=10, sticky=NS)

            return canvas



        table_layout = create_table_layout(screen)
        table_layout.grid(column=1,row=1)

        mainloop()


