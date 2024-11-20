import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to predict faculty based on scores
def predict_faculty(biology, physics, english):
    # Menentukan fakultas berdasarkan nilai tertinggi
    if biology >= physics and biology >= english:
        return "Kedokteran"  # Jika Biologi adalah nilai tertinggi
    elif physics >= biology and physics >= english:
        return "Teknik"  # Jika Fisika adalah nilai tertinggi
    else:
        return "Bahasa"  # Jika Bahasa Inggris adalah nilai tertinggi

# Function to submit data
def submit_data():
    # Mengambil data dari entry field
    name = entry_name.get()
    biology = int(entry_biology.get())
    physics = int(entry_physics.get())
    english = int(entry_english.get())
    
    # Prediksi fakultas berdasarkan nilai
    faculty = predict_faculty(biology, physics, english)
    
    # Menyimpan data ke dalam database SQLite
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)", 
                   (name, biology, physics, english, faculty))
    conn.commit()  # Menyimpan perubahan ke database
    messagebox.showinfo("Success", "Data berhasil disimpan!")  # Memberikan notifikasi bahwa data telah disimpan

# Membuat database SQLite dan tabel jika belum ada
conn = sqlite3.connect("nilai_siswa.db")  # Membuka koneksi ke database
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  # ID unik untuk setiap entri
    nama_siswa TEXT,  # Nama siswa
    biologi INTEGER,  # Nilai Biologi
    fisika INTEGER,  # Nilai Fisika
    inggris INTEGER,  # Nilai Bahasa Inggris
    prediksi_fakultas TEXT  # Hasil prediksi fakultas
)
""")
conn.commit()  # Menyimpan perubahan ke database

# Membuat jendela utama menggunakan Tkinter
root = tk.Tk()
root.title("Prediksi Fakultas Berdasarkan Nilai")

# Label dan Entry untuk nama siswa
tk.Label(root, text="Nama Siswa:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk nilai Biologi
tk.Label(root, text="Nilai Biologi:").grid(row=1, column=0, padx=10, pady=10)
entry_biology = tk.Entry(root)
entry_biology.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk nilai Fisika
tk.Label(root, text="Nilai Fisika:").grid(row=2, column=0, padx=10, pady=10)
entry_physics = tk.Entry(root)
entry_physics.grid(row=2, column=1, padx=10, pady=10)

# Label dan Entry untuk nilai Bahasa Inggris
tk.Label(root, text="Nilai Bahasa Inggris:").grid(row=3, column=0, padx=10, pady=10)
entry_english = tk.Entry(root)
entry_english.grid(row=3, column=1, padx=10, pady=10)

# Tombol untuk mengirimkan data
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan event loop Tkinter
root.mainloop()

# Menutup koneksi SQLite saat aplikasi selesai
conn.close()
