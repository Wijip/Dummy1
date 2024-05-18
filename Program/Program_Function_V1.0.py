menu_tampil = ("1. Nasi Goreng   Rp, 15.000", "2. Nasi Pecel    Rp, 12.000", "3. Rawon   \t\t Rp, 15.000", "4. Soto Ayam \t Rp, 20.000", "5. Capcay     \t Rp, 25.000","6. Bakso       \t Rp, 15.000",
                  "7. Gado Gado     Rp, 15.000","8. Tahu Campur   Rp, 25.000", "9. Ayam Bakar    Rp, 20.000", "10. Ayam Geprek  Rp, 30.000")
menu = ("Nasi Goreng","Nasi Pecel","Rawon","Soto Ayam",
        "Capcay","Bakso","Gado Gado","Tahu Campur","Ayam Bakar","Ayam Geprek")
harga = (15000,12000,15000,20000,25000,15000,15000,25000,20000,30000)
pesanan = []

def tampilan_menu():
    print("====================================")
    print("=               Menu               =")
    print("====================================")
    for m in menu_tampil:
        print(m)
    print("====================================")

def pesan_menu(pesanan):
    while True:
        tampilan_menu()
        pilihan = int(input("Silahkan ketikkan nomor menu yang akan dipesan: "))
        if 1 <= pilihan <= len(menu):
            porsi = int(input("Berapa porsi yang akan dipesan: "))
            for po in range(porsi):
                pesanan.append(pilihan - 1)
            if pesanan is not None:
                print("Pesanan berhasil di tambahkan")
            else:
                print("Terjadi kesalahan")
            break
        else:
            print("================================")
            print("Pilihan tidak valid. Masukkan nomor menu yang sesuai.")

def tampilkan_pesanan(pesanan):
    if pesanan:
        print("================================")
        print("Pesanan saat ini")
        print("================================")
        for p in pesanan:
            i = 0
            i += 1
            print(f"{i}. {menu[p]} - Rp{harga[p]}")
        print("================================")
    else:
        print("================================")
        print("Belum ada pesanan.")

def hitung_total(pesanan, harga):
    jumlah = len(pesanan)
    total = sum(harga[p] for p in pesanan)
    return total

def tampilkan_total(pesanan, harga):
    if pesanan:
        total = hitung_total(pesanan, harga)
        print("================================")
        print("Menu yang dipesan")
        print("================================")
        for p in pesanan:
            print(f"{menu[p]} - Rp{harga[p]}")
        print("================================")
        print(f"Total Harga : Rp.{total}")
        print("================================")
    else:
        print("================================")
        print("Belum ada pesanan")

def selesaikan_pesanan(pesanan, harga):
    if pesanan:
        total = hitung_total(pesanan, harga)
        print("================================")
        print("Menu yang dipesan")
        print("================================")
        for p in pesanan:
            print(f"{menu[p]} - Rp{harga[p]}")
        print("================================")
        print(f"Total Harga : Rp.{total}")
        for i in range(len(pesanan)):
            del pesanan[0]
        print("================================")
    else:
        print("================================")
        print("Belum ada pesanan")

def hapus_pesanan(pesanan):
    if pesanan:
        while True:
            try:
                hapus = int(input(f"Masukkan nomor pesanan yang ingin di hapus (1 {format(len(pesanan))}): "))
                if 1 <= hapus <= len(pesanan):
                    pesanan.remove(hapus -1 )
                    break
                else:
                    print(f"Nomot pesanan tidak valid. masukkan nomor antar 1 dan {format(len(pesanan))}")
            except ValueError:
                print("Masukan tidak valid. Harap maukkan angka.")
    else:
        print("================================")
        print("Belum ada pesanan yang bisa dihapus")
while True:
    try:
        print("\n===============================")
        print("=   Program Pesanan Makanan   =")
        print("===============================")
        print("1. Tampilkan Menu")
        print("2. Pesan Menu")
        print("3. Tampilkan Pesanan")
        print("4. Hitung Total")
        print("5. Hapus Pesanan")
        print("6. Selesaikan Pesanan")
        print("7. Keluar")
        print("=============================")

        pilihan = int(input("Masukkan pilihan Anda: "))

        if pilihan == 1:
            tampilan_menu()
        elif pilihan == 2:
            pesan_menu(pesanan)
        elif pilihan == 3:
            tampilkan_pesanan(pesanan)
        elif pilihan == 4:
            tampilkan_total(pesanan, harga)
        elif pilihan == 5:
            hapus_pesanan(pesanan)
        elif pilihan == 6:
            selesaikan_pesanan(pesanan, harga)
        elif pilihan == 7:
            print("Terima kasih telang menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka yang sesuai")
    except ValueError:
        print("Input Invalid")