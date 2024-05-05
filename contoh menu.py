def menu_utama():
    print("===================================")
    print("=              Menu Utama           =")
    print("===================================")
    print("1. Menu 1")
    print("2. Menu 2")
    print("3. Keluar")
    print("===================================")
    pilihan = int(input("Silahkan masukkan pilihan: "))

    if pilihan == 1:
        menu_1()
    elif pilihan == 2:
        menu_2()
    elif pilihan == 3:
        print("Terima kasih!")
        exit()
    else:
        print("Pilihan tidak valid. Silahkan masukkan angka 1, 2, atau 3.")

def menu_1():
    print("===================================")
    print("=              Menu 1               =")
    print("===================================")
    print("1. Sub Menu 1")
    print("2. Sub Menu 2")
    print("3. Kembali")
    print("===================================")
    pilihan = int(input("Silahkan masukkan pilihan: "))

    if pilihan == 1:
        print("Sub Menu 1")
        kembali = input("Tekan enter untuk kembali ke menu sebelumnya...")
        menu_1()
    elif pilihan == 2:
        print("Sub Menu 2")
        kembali = input("Tekan enter untuk kembali ke menu sebelumnya...")
        menu_1()
    elif pilihan == 3:
        menu_utama()
    else:
        print("Pilihan tidak valid. Silahkan masukkan angka 1, 2, atau 3.")

def menu_2():
    print("===================================")
    print("=              Menu 2               =")
    print("===================================")
    print("1. Sub Menu 1")
    print("2. Sub Menu 2")
    print("3. Kembali")
    print("===================================")
    pilihan = int(input("Silahkan masukkan pilihan: "))

    if pilihan == 1:
        print("Sub Menu 1")
        kembali = input("Tekan enter untuk kembali ke menu sebelumnya...")
        menu_2()
    elif pilihan == 2:
        print("Sub Menu 2")
        kembali = input("Tekan enter untuk kembali ke menu sebelumnya...")
        menu_2()
    elif pilihan == 3:
        menu_utama()
    else:
        print("Pilihan tidak valid. Silahkan masukkan angka 1, 2, atau 3.")

while True:
    menu_utama()
