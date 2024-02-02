import tkinter as tk
from tkinter import ttk

class sample_text_excel(tk.Toplevel): # membuat window baru dari window master
    def __init__(self, master):
        super().__init__(master)

        self.title("Jendela Baru")
        self.geometry("600x300")

        self.label = tk.Label(self, text="Ini adalah jendela baru!")
        self.label.pack(pady=10)

        # Membuat ttk.Treeview sebagai tabel
        self.tabel = ttk.Treeview(self, columns=("No", "Nama", "Usia"), show="headings", height=8)
        self.tabel.heading("No", text="No")
        self.tabel.heading("Nama", text="Nama")
        self.tabel.heading("Usia", text="Usia")
        self.tabel.pack(pady=10)

        # Menambahkan fungsi untuk menampilkan teks sebagai tabel
        self.tampilkan_excel()

    def tampilkan_excel(self): 
        # Contoh data untuk tabel
        data_tabel = [
            (1, "John", 25),
            (2, "Jane", 30),
            (3, "Doe", 22)
        ]

        # Menampilkan data di ttk.Treeview
        for data in data_tabel:
            self.tabel.insert("", "end", values=data)


class sample_text_area(tk.Toplevel): 
    def __init__(self, master):
        super().__init__(master)

        self.title("Jendela Baru")
        self.geometry("600x200")

        self.label = tk.Label(self, text="Ini adalah jendela baru!")
        self.label.pack(pady=10)

        # Menambahkan widget tk.Text untuk menampilkan teks sebagai tabel
        self.text_area = tk.Text(self, height=8, width=30)
        self.text_area.pack(pady=10)

        # Menambahkan fungsi untuk menampilkan teks sebagai tabel
        self.tampilkan_tabel()

    def tampilkan_tabel(self):
        # Contoh teks untuk tabel
        teks_tabel = "No\tNama\tUsia\n"
        teks_tabel += "1\tJohn\t25\n"
        teks_tabel += "2\tJane\t30\n"
        teks_tabel += "3\tDoe\t22"

        # Menampilkan teks di widget tk.Text
        self.text_area.insert(tk.END, teks_tabel)
        # Menonaktifkan editing pada widget tk.Text
        self.text_area.config(state=tk.DISABLED)