import tkinter as tk
from tkinter import messagebox
import sqlite3

# ============================
# 1. KONEKSI DATABASE & TABEL
# ============================
conn = sqlite3.connect("nilai_siswa.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT
)
""")
conn.commit()


def submit_nilai():
    nama = entry_nama.get()
    bio = entry_bio.get()
    fis = entry_fis.get()
    ing = entry_ing.get()

    # Validasi input
    if nama == "" or bio == "" or fis == "" or ing == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    try:
        bio = int(bio)
        fis = int(fis)
        ing = int(ing)
    except:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

 
    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    elif ing > bio and ing > fis:
        prediksi = "Bahasa"
    else:
        prediksi = "Tidak dapat ditentukan (Nilai sama)"

 
    cursor.execute("""
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, prediksi))
    conn.commit()

    messagebox.showinfo("Berhasil", f"Prediksi Fakultas: {prediksi}")


root = tk.Tk()
root.title("Prediksi Fakultas Siswa")
root.geometry("350x320")
tk.Label(root, text="Nama Siswa").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()
tk.Label(root, text="Nilai Biologi").pack()
entry_bio = tk.Entry(root)
entry_bio.pack()
tk.Label(root, text="Nilai Fisika").pack()
entry_fis = tk.Entry(root)
entry_fis.pack()
tk.Label(root, text="Nilai Inggris").pack()
entry_ing = tk.Entry(root)
entry_ing.pack()
tk.Button(root, text="Submit", command=submit_nilai, bg="lightblue").pack(pady=15)

root.mainloop()
