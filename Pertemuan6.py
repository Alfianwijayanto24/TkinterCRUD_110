import tkinter as Pr
from tkinter import messagebox
root = Pr.Tk()
root.title("Prodi")
var = Pr.StringVar()
label = Pr.Label(root, textvariable=var, relief=Pr.RAISED)
var.set("APLIKASI PERODI")

label.pack(pady=10)
frame_input = Pr.Frame(root)
frame_input.pack(pady=10)
entries = []
for i in range(10):
    Pr.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}").grid(row=i, column=0, sticky="w", padx=5, pady=3)
    entry = Pr.Entry(frame_input, width=10)
    entry.grid(row=i, column=1, padx=5, pady=3)
    entries.append(entry)



def helloCallBack():
    messagebox.showinfo("Hello Teman", "Hello Siswa")


def show_selection():
    try:
        selected = Lb1.get(Lb1.curselection())
        messagebox.showinfo("Pilihan Anda", f"Anda memilih: {selected}")
        var.set(f"Anda memilih: {selected}")
    except:
        messagebox.showwarning("Peringatan", "Silakan pilih item dulu!")


btn_hello = Pr.Button(root, text="Hasil Perediksi", command=helloCallBack)
btn_hello.pack(pady=5)

root.mainloop()


