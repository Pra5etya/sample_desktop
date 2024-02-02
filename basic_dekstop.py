import tkinter as tk
from desktop_dev.child_windows.sample_new_window import sample_text_area, sample_text_excel

class Percobaan(tk.Tk):
    def __init__(self):
        super().__init__() # initialize in class parameter

        self.title('Percobaan Awal membuat Aplikasi Desktop') # title app
        self.geometry('600x200') # window app size

        # make label
        self.label1 = tk.Label(self, text = 'Label 1')
        self.label1.pack(padx = 6, pady = 10, side = 'top')

        # make button 
        self.button1 = tk.Button(self, text = 'Tampilkan Pesan Label 1', command = self.tampilkan_pesan1)
        self.button1.pack(padx = 20, pady = 5, side = 'top')

        # make label
        self.label2 = tk.Label(self, text = 'Label 2')
        self.label2.pack(padx = 20, pady = 4, side = 'left')

        # make button 
        self.button2 = tk.Button(self, text = 'Buka Jendela text area', command = self.tampilkan_pesan2)
        self.button2.pack(padx = 2, pady = 5, side = 'left')

        # make label
        self.label3 = tk.Label(self, text = 'Label 3')
        self.label3.pack(padx = 20, pady = 4, side = 'bottom')

        # make button 
        self.button3 = tk.Button(self, text = 'Buka Jendela excel format', command = self.tampilkan_pesan3)
        self.button3.pack(padx = 2, pady = 5, side = 'bottom')

    def tampilkan_pesan1(self):
        self.label1.config(text = 'Halo dari Label 1!')

    def tampilkan_pesan2(self):
        sample_text_area(self)

    def tampilkan_pesan3(self):
        sample_text_excel(self)

# if __name__ == '__main__':
#     app = Percobaan()
#     app.mainloop()