def menu_utama():
    print("===================================")
    print("=           Menu Utama            =")
    print("===================================")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Pembayaran")
    print("4. Keluar")
    print("===================================")
    pilihan = int(input("Silahkan masukkan pilihan: "))
    if pilihan == 1:
        menu_makanan()
    elif pilihan == 2:
        menu_minuman()
    elif pilihan == 3:
        print("Soon")
    elif pilihan == 4:
        print("Bye")
        exit()
    else:
        print("Pilihan tidak valid")


def menu_makanan():
    print("===================================")
    print("=           Menu Makanan          =")
    print("===================================")
    print("1. Nasi Goreng")
    print("2. Mie Goreng")
    print("3. Gado Gado")
    print("4. Soto Ayam")
    print("5. Ayam Bakar")
    print("6. Ayam Geprek")
    print("7. Tahu Campur")
    print("0. Kembali")
    print("===================================")

def menu_minuman():
    print("===================================")
    print("=           Menu Minuman          =")
    print("===================================")
    print("1. Es Teh")
    print("2. Es Jeruk")
    print("3. Kopi")
    print("4. Kopi Susu")
    print("5. Es Kopi")
    print("0. Kembali")
    print("===================================")

while True:
    menu_utama()