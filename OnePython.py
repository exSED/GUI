from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot

class GUI:
    def __init__(self,master, b=0):
#________________________________________________________frame________________________________________________________
        f = Frame(master, width="400", heigh="200",bg= "#2dadc8", cursor="pirate")
        f.pack(fill="both", expand="false")
#________________________________________________________label________________________________________________________
        l1 = Label(f, text="Name student", bg="#2dadc8", fg="black", font="arial")
        l1.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        l3 = Label(f, text="Math", bg="#2dadc8", fg="black", font="arial")
        l3.grid(row=0, column=0)
        l3.place(heigh=0, width=0)

        l4 = Label(f, text="Physical",bg="#2dadc8", fg="black", font="arial")
        l4.grid(row=0, column=0)
        l4.place(heigh=0, width=0)

        l5 = Label(f, text="Chemistry", bg="#2dadc8", fg="black", font="arial")
        l5.grid(row=0, column=0)
        l5.place(heigh=0, width=0)

        l6 = Label(f, text="Programming",bg="#2dadc8", fg="black", font="arial")
        l6.grid(row=0, column=0)
        l6.place(heigh=0, width=0)
#________________________________________________________field________________________________________________________
        fi1 = Entry(f, bd=0, fg="white", bg="#eb5d5d", font="arial")
        fi1.grid(row=0, column=1, sticky="e", padx=10, pady=10)

        fi3 = Entry(f, bd=0, fg="white", bg="#eb5d5d", font="arial")
        fi3.grid(row=0, column=0)
        fi3.place(heigh=0, width=0)

        fi4 = Entry(f, bd=0, fg="white", bg="#eb5d5d", font="arial")
        fi4.grid(row=0, column=0)
        fi4.place(heigh=0, width=0)

        fi5 = Entry(f, bd=0, fg="white", bg="#eb5d5d", font="arial")
        fi5.grid(row=0, column=0)
        fi5.place(heigh=0, width=0)

        fi6 = Entry(f, bd=0, fg="white", bg="#eb5d5d", font="arial")
        fi6.grid(row=0, column=0)
        fi6.place(heigh=0, width=0)
#________________________________________________________using________________________________________________________
        def CB1():
            s = (fi1.get())
            if s is "":
                messagebox.showerror("Error", "do not write")
            else:
                fi1.grid(row=0, column=0)
                fi3.grid(row=0, column=1, sticky="e", padx=10, pady=10)
                fi4.grid(row=1, column=1, sticky="e", padx=10, pady=10)
                fi5.grid(row=2, column=1, sticky="e", padx=10, pady=10)
                fi6.grid(row=3, column=1, sticky="e", padx=10, pady=10)
                b1.grid(row=0, column=0)
                b2.grid(row=4, column=1, sticky="e", padx=10, pady=10)
                l1.place(heigh=0, width=0)
                l3.grid(row=0, column=0, sticky="e", padx=10, pady=10)
                l4.grid(row=1, column=0, sticky="e", padx=10, pady=10)
                l5.grid(row=2, column=0, sticky="e", padx=10, pady=10)
                l6.grid(row=3, column=0, sticky="e", padx=10, pady=10)
                fi1.place(heigh=0, width=0)
                b1.place(heigh=0, width=0)
        def CB2():
            try:
                b3.grid(row=4, column=0, sticky="w", padx=10, pady=10)
                s = fi1.get()
                Materias = ("Math", "Physical", "Chemistry", "Programming")
                Colores = ("#DD98AA", "red", "blue", "green")
                Notas = (float(fi3.get()), float(fi4.get()), float(fi5.get()), float(fi6.get()))
                Separa = (0.1, 0.1, 0.1, 0.1)
                pyplot.pie(Notas, colors=Colores, labels=Materias, autopct='%.1f', explode=Separa)
                pyplot.title(s)
                pyplot.show()
            except ValueError:
                b3.grid(row=0, column=0)
                b3.place(heigh=0, width=0)
                messagebox.showerror("Error", "do not write or value is incorrect, try again")
        def CO():
            fi1.delete(0, END)
            fi3.grid(row=0, column=0)
            fi4.grid(row=0, column=0)
            fi5.grid(row=0, column=0)
            fi6.grid(row=0, column=0)
            b2.grid(row=0, column=0)
            b3.grid(row=0, column=0)
            l3.grid(row=0, column=0)
            l4.grid(row=0, column=0)
            l5.grid(row=0, column=0)
            l6.grid(row=0, column=0)
            fi3.place(heigh=0, width=0)
            fi4.place(heigh=0, width=0)
            fi5.place(heigh=0, width=0)
            fi6.place(heigh=0, width=0)
            b2.place(heigh=0, width=0)
            b3.place(heigh=0, width=0)
            l3.place(heigh=0, width=0)
            l4.place(heigh=0, width=0)
            l5.place(heigh=0, width=0)
            l6.place(heigh=0, width=0)
            l6.place(heigh=0, width=0)
            l1.grid(row=0, column=0)
            fi1.grid(row=0, column=1)
            b1.grid(row=1, column=1)
#________________________________________________________Button________________________________________________________
        b1 = Button(f, text="Accept", font="arial", bd=0, fg="black", bg="#2dadc8", command=CB1)
        b1.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        b2 = Button(f, text="Next", font="arial", bd=0, fg="black", bg="#2dadc8", command=CB2)
        b2.grid(row=0, column=0)
        b2.place(heigh=0, width=0)

        b3 = Button(f, text="New", font="arial", bd=0, fg="black", bg="#2dadc8", command=CO)
        b3.grid(row=0, column=0)
        b3.place(heigh=0, width=0)
#________________________________________________________root________________________________________________________
r = Tk()
r.title("Students")
r.iconbitmap(None)
r.resizable(False, False)
app = C(r)
r.mainloop()
