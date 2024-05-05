menu_tampil = ("1. Nasi Goreng   Rp, 15.000", "2. Nasi Pecel    Rp, 12.000", "3. Rawon   \t\t Rp, 15.000", "4. Soto Ayam \t Rp, 20.000", "5. Capcay     \t Rp, 25.000","6. Bakso       \t Rp, 15.000",
                  "7. Gado Gado     Rp, 15.000","8. Tahu Campur   Rp, 25.000", "9. Ayam Bakar  Rp, 20.000", "10. Ayam Geprek   Rp, 30.000")
menu = ("1. Nasi Goreng","2. Nasi Pecel","3. Rawon","4. Soto Ayam",
        "5. Capcay","6. Bakso","7. Gado Gado","8. Tahu Campur","9. Ayam Bakar","10. Ayam Geprek")
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
            break
        else:
            print("Pilihan tidak valid. Masukkan nomor menu yang sesuai.")

def tampilkan_pesanan(pesanan):
    if pesanan:
        print("================================")
        print("Pesanan saat ini")
        print("================================")
        for p in pesanan:
            print(f"{menu[p]} - Rp{harga[p]}")
        print("================================")
    else:
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
        print("Belum ada pesanan")

while True:
    print("\n===============================")
    print("=   Program Pesanan Makanan   =")
    print("===============================")
    print("1. Tampilkan Menu")
    print("2. Pesan Menu")
    print("3. Tampilkan Pesanan")
    print("4. Hitung Total")
    print("5. Selesaikan Pesanan")
    print("6. Keluar")
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
        selesaikan_pesanan(pesanan, harga)
    elif pilihan == 6:
        print("Terima kasih telang menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka yang sesuai")