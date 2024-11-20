import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to predict faculty based on scores
def predict_faculty(biology, physics, english):
    if biology >= physics and biology >= english:
        return "Kedokteran"
    elif physics >= biology and physics >= english:
        return "Teknik"
    else:
        return "Bahasa"

# Function to submit data
def submit_data():
    name = entry_name.get()
    biology = int(entry_biology.get())
    physics = int(entry_physics.get())
    english = int(entry_english.get())
    faculty = predict_faculty(biology, physics, english)
    
    # Insert data into SQLite database
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)", 
                   (name, biology, physics, english, faculty))
    conn.commit()
    messagebox.showinfo("Success", "Data berhasil disimpan!")

# Create SQLite database and table
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

# Create Tkinter window
root = tk.Tk()
root.title("Prediksi Fakultas Berdasarkan Nilai")

# Labels and Entry Widgets
tk.Label(root, text="Nama Siswa:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Nilai Biologi:").grid(row=1, column=0, padx=10, pady=10)
entry_biology = tk.Entry(root)
entry_biology.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Nilai Fisika:").grid(row=2, column=0, padx=10, pady=10)
entry_physics = tk.Entry(root)
entry_physics.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Nilai Bahasa Inggris:").grid(row=3, column=0, padx=10, pady=10)
entry_english = tk.Entry(root)
entry_english.grid(row=3, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run Tkinter Event Loop
root.mainloop()

# Close SQLite connection when done
conn.close()
