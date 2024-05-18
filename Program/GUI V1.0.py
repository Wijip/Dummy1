import tkinter as tk
from tkinter import messagebox

menu_tampil = (
    "1. Nasi Goreng   \tRp. 15.000",
    "2. Nasi Pecel    \tRp. 12.000",
    "3. Rawon         \tRp. 15.000",
    "4. Soto Ayam     \tRp. 20.000",
    "5. Capcay        \tRp. 25.000",
    "6. Bakso         \tRp. 15.000",
    "7. Gado Gado     \tRp. 15.000",
    "8. Tahu Campur   \tRp. 25.000",
    "9. Ayam Bakar    \tRp. 20.000",
    "10. Ayam Geprek  \tRp. 30.000"
)
tampil_pesan = (
    " Nasi Goreng   Rp. 15.000",
    " Nasi Pecel    Rp. 12.000",
    " Rawon         Rp. 15.000",
    " Soto Ayam     Rp. 20.000",
    " Capcay        Rp. 25.000",
    " Bakso         Rp. 15.000",
    " Gado Gado     Rp. 15.000",
    " Tahu Campur   Rp. 25.000",
    " Ayam Bakar    Rp. 20.000",
    " Ayam Geprek  Rp. 30.000"
)

# Variabel untuk menyimpan pesanan
pesanan = []
# Variabel untuk menyimpan harga setiap item
harga = [15000, 12000, 15000, 20000, 25000, 15000, 15000, 25000, 20000, 30000]

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")

    menu_title_label = tk.Label(menu_window, text="Daftar Menu", font=("Helvetica", 16, "bold"))
    menu_title_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    for idx, menu in enumerate(menu_tampil, start=1):
        menu_label = tk.Label(menu_window, text=menu, font=("Helvetica", 12), anchor="w")
        menu_label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)

# Fungsi untuk pesan menu
def pesan_menu():
    pesan_window = tk.Toplevel(root)
    pesan_window.title("Pesan Menu")

    pesan_title_label = tk.Label(pesan_window, text="Pesan Menu", font=("Helvetica", 16, "bold"))
    pesan_title_label.pack()

    pilihan_label = tk.Label(pesan_window, text="Masukkan nomor menu yang akan dipesan:", font=("Helvetica", 12))
    pilihan_label.pack()

    pilihan_entry = tk.Entry(pesan_window)
    pilihan_entry.pack()

    porsi_label = tk.Label(pesan_window, text="Masukkan jumlah porsi:", font=("Helvetica", 12))
    porsi_label.pack()

    porsi_entry = tk.Entry(pesan_window)
    porsi_entry.pack()

    def tambahkan_pesanan():
        pilihan = pilihan_entry.get()
        porsi = porsi_entry.get()
        try:
            nomor_menu = int(pilihan) - 1
            jumlah_porsi = int(porsi)
            pesanan.extend([nomor_menu] * jumlah_porsi)
            messagebox.showinfo("Info", "Pesanan berhasil ditambahkan!")
            pesan_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Masukkan nomor menu dan jumlah porsi yang valid.")

    pesan_button = tk.Button(pesan_window, text="Pesan", command=tambahkan_pesanan, font=("Helvetica", 12))
    pesan_button.pack()

# Fungsi untuk menampilkan pesanan
def tampilkan_pesanan():
    if pesanan:
        pesanan_window = tk.Toplevel(root)
        pesanan_window.title("Pesanan Anda")

        pesanan_title_label = tk.Label(pesanan_window, text="Pesanan Anda", font=("Helvetica", 16, "bold"))
        pesanan_title_label.pack()

        for idx, pesanan_idx in enumerate(pesanan, start=1):
            menu_label = tk.Label(pesanan_window, text=f"{idx}. {tampil_pesan[pesanan_idx]}", font=("Helvetica", 12))
            menu_label.pack()
    else:
        messagebox.showinfo("Info", "Belum ada pesanan.")

# Fungsi untuk menghapus pesanan
def hapus_pesanan():
    if pesanan:
        hapus_window = tk.Toplevel(root)
        hapus_window.title("Hapus Pesanan")

        hapus_title_label = tk.Label(hapus_window, text="Hapus Pesanan", font=("Helvetica", 16, "bold"))
        hapus_title_label.pack()

        pesanan_label = tk.Label(hapus_window, text="Masukkan nomor pesanan yang ingin dihapus:", font=("Helvetica", 12))
        pesanan_label.pack()

        pesanan_entry = tk.Entry(hapus_window)
        pesanan_entry.pack()

        def hapus():
            try:
                nomor_pesanan = int(pesanan_entry.get()) - 1
                if nomor_pesanan < len(pesanan):
                    del pesanan[nomor_pesanan]
                    messagebox.showinfo("Info", "Pesanan berhasil dihapus!")
                    hapus_window.destroy()
                else:
                    messagebox.showwarning("Peringatan", "Nomor pesanan tidak valid.")
            except ValueError:
                messagebox.showerror("Error", "Masukkan nomor pesanan yang valid.")

        hapus_button = tk.Button(hapus_window, text="Hapus", command=hapus, font=("Helvetica", 12))
        hapus_button.pack()
    else:
        messagebox.showinfo("Info", "Belum ada pesanan yang bisa dihapus.")

# Fungsi untuk menyelesaikan pesanan
def selesaikan_pesanan():
    if pesanan:
        total_harga = sum(harga[i] for i in pesanan)
        messagebox.showinfo("Info", f"Total harga pesanan Anda: Rp. {total_harga}")
        pesanan.clear()
    else:
        messagebox.showinfo("Info", "Belum ada pesanan.")

def keluar_program():
    root.destroy()


root  = tk.Tk()
root.geometry('400x500')
root.title("Program Pemesanan Makanan")
root.resizable(False, False)

title_label = tk.Label(root, text="Selamat Datang", font=("Arial",20))
title_label.pack()

menu_button = tk.Button(root, text="Tampilkan Menu", command=tampilkan_menu, font=("Arial", 12), height=1, width=45)
menu_button.pack(pady=10)

pesan_button = tk.Button(root, text="Pesan Menu", command=pesan_menu, font=("Arial", 12), height=1, width=45)
pesan_button.pack(pady=10)

tampilkan_button = tk.Button(root, text="Tampilkan Pesanan", command=tampilkan_pesanan, font=("Arial", 12), height=1, width=45)
tampilkan_button.pack(pady=10)

hapus_button = tk.Button(root, text="Hapus Pesanan", command=hapus_pesanan, font=("Arial", 12), height=1, width=45)
hapus_button.pack(pady=10)

selesai_button = tk.Button(root, text="Selesaikan Pesanan", command=selesaikan_pesanan, font=("Arial", 12), height=1, width=45)
selesai_button.pack(pady=10)

keluar_button = tk.Button(root, text="Keluar", command=keluar_program, font=("Arial", 12), height=1, width=45)
keluar_button.pack(pady=10)

root.mainloop()