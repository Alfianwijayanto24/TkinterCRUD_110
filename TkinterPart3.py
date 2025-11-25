###Menambahkan kondisi nilaiyang berbeda untuk setiap pilihan prodi yang diinginkan
#Menambahkan update dan delete data ke SQLite
#Buat Fungsi untuk update dan delete
#Buat 2 Tombol button baru
#Jika nilai Biologi paling tinggi, maka hasil prediksi = Kedokteran
#Jika nilai Fisika paling tinggi, maka hasil prediksi = Teknik
#Jika nilai Inggris paling tinggi, maka hasil prediksi = Bahasa
#Terdapat button tkinter untuk submit nilai


import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

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

def hitung_prediksi(bio, fis, ing):
    if bio > fis and bio > ing:
        return "Kedokteran"
    elif fis > bio and fis > ing:
        return "Teknik"
    elif ing > bio and ing > fis:
        return "Bahasa"
    else:
        return "Tidak dapat ditentukan"


def submit_nilai():
    nama = entry_nama.get()
    bio = entry_bio.get()
    fis = entry_fis.get()
    ing = entry_ing.get()

    if nama == "" or bio == "" or fis == "" or ing == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    try:
        bio = int(bio); fis = int(fis); ing = int(ing)
    except:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    prediksi = hitung_prediksi(bio, fis, ing)

    cursor.execute("""
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, prediksi))
    conn.commit()

    messagebox.showinfo("Berhasil", f"Data berhasil disimpan!\nPrediksi: {prediksi}")
    tampilkan_data()



def update_data():
    id_siswa = entry_id.get()
    nama = entry_nama.get()
    bio = entry_bio.get()
    fis = entry_fis.get()
    ing = entry_ing.get()

    if id_siswa == "":
        messagebox.showwarning("Peringatan", "Masukkan ID yang akan diupdate!")
        return

    try:
        bio = int(bio); fis = int(fis); ing = int(ing)
    except:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    prediksi = hitung_prediksi(bio, fis, ing)

    cursor.execute("""
        UPDATE nilai_siswa
        SET nama_siswa=?, biologi=?, fisika=?, inggris=?, prediksi_fakultas=?
        WHERE id=?
    """, (nama, bio, fis, ing, prediksi, id_siswa))
    conn.commit()

    messagebox.showinfo("Update", f"Data ID {id_siswa} berhasil diupdate!\nPrediksi Baru: {prediksi}")
    tampilkan_data()



def hapus_data():
    id_siswa = entry_id.get()
    if id_siswa == "":
        messagebox.showwarning("Peringatan", "Masukkan ID yang akan dihapus!")
        return

    cursor.execute("DELETE FROM nilai_siswa WHERE id=?", (id_siswa,))
    conn.commit()

    messagebox.showinfo("Hapus", f"Data ID {id_siswa} berhasil dihapus!")
    tampilkan_data()



def tampilkan_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM nilai_siswa")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)



root = tk.Tk()
root.title("Prediksi Fakultas Siswa")
root.geometry("700x500")



frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="ID (untuk Update/Delete)").grid(row=0, column=0)
entry_id = tk.Entry(frame_input)
entry_id.grid(row=0, column=1)

tk.Label(frame_input, text="Nama Siswa").grid(row=1, column=0)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=1, column=1)

tk.Label(frame_input, text="Nilai Biologi").grid(row=2, column=0)
entry_bio = tk.Entry(frame_input)
entry_bio.grid(row=2, column=1)

tk.Label(frame_input, text="Nilai Fisika").grid(row=3, column=0)
entry_fis = tk.Entry(frame_input)
entry_fis.grid(row=3, column=1)

tk.Label(frame_input, text="Nilai Inggris").grid(row=4, column=0)
entry_ing = tk.Entry(frame_input)
entry_ing.grid(row=4, column=1)



tk.Button(root, text="Submit", width=15, bg="lightblue", command=submit_nilai).pack()
tk.Button(root, text="Update", width=15, bg="yellow", command=update_data).pack()
tk.Button(root, text="Delete", width=15, bg="red", fg="white", command=hapus_data).pack()



tree = ttk.Treeview(root, columns=("ID", "Nama", "Biologi", "Fisika", "Inggris", "Prediksi"), show="headings")
tree.pack(pady=20)

tree.heading("ID", text="ID")
tree.heading("Nama", text="Nama")
tree.heading("Biologi", text="Biologi")
tree.heading("Fisika", text="Fisika")
tree.heading("Inggris", text="Inggris")
tree.heading("Prediksi", text="Prediksi Fakultas")

tree.column("ID", width=40)

tampilkan_data()

root.mainloop()
