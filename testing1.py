import tkinter as tk

menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Goreng": 18000,
    "Gado Gado":20000,
    "Ikan Bakar":35000,
    "Es Teh": 5000,
    "Es Jeruk": 7000,
    "Es Oyen": 15000,
    "Es Teh Jumbo": 8000,
}

total_harga = 0

pesanan = []

def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")

    menu_title_label = tk.Label(menu_window, text="Daftar Menu")
    menu_title_label.pack()

    for item, harga in menu.items():
        item_label = tk.Label(menu_window, text=f"{item}: Rp{harga}")
        item_label.pack()

def add_item():
    global total_harga

    nama_item = item_entry.get()
    jumlah = int(jumlah_entry.get())

    if nama_item not in menu:
        error_label.config(text="Item tidak ditemukan!")
        return

    pesanan.append((nama_item, jumlah))

    # Menghitung harga total item
    harga_item = menu[nama_item] * jumlah

    total_harga += harga_item

    total_label.config(text=f"Total: Rp{total_harga}")

    item_entry.delete(0, tk.END)
    jumlah_entry.delete(0, tk.END)

def hapus_pesanan():
    global total_harga

    nama_pesanan = nama_entry.get()

    jumlah_dihapus = 0

    for pesanan_item in pesanan[:]:
        if pesanan_item[0] == nama_pesanan:
            harga_item = menu[pesanan_item[0]] * pesanan_item[1]
            total_harga -= harga_item

            pesanan.remove(pesanan_item)

            jumlah_dihapus += pesanan_item[1]

    total_label.config(text=f"Total: Rp{total_harga}")

    if jumlah_dihapus > 0:
        error_label.config(text=f"{jumlah_dihapus} {nama_pesanan} dihapus dari keranjang.")
    else:
        error_label.config(text=f"Tidak ada {nama_pesanan} dalam keranjang.")

    nama_entry.delete(0, tk.END)

def finish_transaction():
    global total_harga

    if total_harga == 0:
        error_label.config(text="Keranjang kosong!")
        return

    confirmation_message = f"""
    Total pembayaran: Rp{total_harga}

    Apakah Anda ingin menyelesaikan transaksi? (Y/N)
    """
    confirmation_window = tk.Toplevel(root)
    confirmation_label = tk.Label(confirmation_window, text=confirmation_message)
    confirmation_label.pack()

    def yes():
        total_harga = 0
        total_label.config(text=f"Total: Rp{total_harga}")
        item_entry.delete(0, tk.END)
        jumlah_entry.delete(0, tk.END)

        success_label = tk.Label(root, text="Transaksi selesai!")
        success_label.pack()

        confirmation_window.destroy()

    def no():
        confirmation_window.destroy()

    yes_button = tk.Button(confirmation_window, text="Ya", command=yes)
    yes_button.pack()
    no_button = tk.Button(confirmation_window, text="Tidak", command=no)
    no_button.pack()

def exit_program():
    root.destroy()

root = tk.Tk()
root.geometry('300x400')
root.title("Kasir Sederhana")

title_label = tk.Label(root, text="Kasir Sederhana")
title_label.pack()

menu_button = tk.Button(root, text="Tampilkan Menu", command=show_menu)
menu_button.pack()

item_frame = tk.Frame(root)
item_frame.pack()

item_label = tk.Label(item_frame, text="Nama Item:")
item_label.pack()
item_entry = tk.Entry(item_frame)
item_entry.pack()

jumlah_label = tk.Label(item_frame, text="Jumlah:")
jumlah_label.pack()

jumlah_entry = tk.Entry(item_frame)
jumlah_entry.pack()

add_button = tk.Button(item_frame, text="Tambah", command=add_item)
add_button.pack()

total_label = tk.Label(root, text=f"Total: Rp{total_harga}")
total_label.pack()

hapus_frame = tk.Frame(root)
hapus_frame.pack()

nama_label = tk.Label(hapus_frame, text="Nama Pesanan:")
nama_label.pack()

nama_entry = tk.Entry(hapus_frame)
nama_entry.pack()

hapus_button = tk.Button(hapus_frame, text="Hapus Pesanan", command=hapus_pesanan)
hapus_button.pack()

finish_button = tk.Button(root, text="Selesai", command=finish_transaction)
finish_button.pack()

error_label = tk.Label(root, text="")
error_label.pack()

exit_button = tk.Button(root, text="Keluar", command=exit_program)
exit_button.pack()

root.mainloop()