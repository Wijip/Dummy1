import time
menu_tampil = ("1. Nasi Goreng   Rp, 15.000", "2. Nasi Pecel    Rp, 12.000", "3. Rawon   \t\t Rp, 15.000", "4. Soto Ayam \t Rp, 20.000", "5. Capcay     \t Rp, 25.000","6. Bakso       \t Rp, 15.000",
                  "7. Gado Gado     Rp, 15.000","8. Tahu Campur   Rp, 25.000", "9. Ayam Bakar  Rp, 20.000", "10. Ayam Geprek   Rp, 30.000")

menu = ("1. Nasi Goreng","2. Nasi Pecel","3. Rawon","4. Soto Ayam",
        "5. Capcay","6. Bakso","7. Gado Gado","8. Tahu Campur","9. Ayam Bakar","10. Ayam Geprek")
harga = (15000,12000,15000,20000,25000,15000,15000,25000,20000,30000)
pesanan = []


while True:
    print("====================================")
    print("=               Menu               =")
    print("====================================")
    for m in menu_tampil:
        print(m)
    print("====================================")
    pilihan = int(input("Silahkan ketikkan nomor menu yang akan dipesan: "))
    porsi = int(input("Berapa porsi yang akan dipesan: "))
    for po in range(porsi):
        pesanan.append(pilihan - 1)
    lagi = input("Ingin memesan lagi? (1=ya / 0=tidak): ")
    if lagi == "1":
        print("================================")
        print("Pesanan saat ini")
        print("================================")
        for p in pesanan:
            print(f"{menu[p]} - Rp{harga[p]}")
        print("================================\n")
        time.sleep(2)
    elif lagi == "0":
        print("================================")
        print("Menu yang dipesan")
        print("================================")
        for p in pesanan:
            print(f"{menu[p]} - Rp{harga[p]}")
        jumlah = len(pesanan)
        total = sum(harga[p] for p in pesanan)
        print("================================")
        print(f"Total Harga : Rp.{total}")
        print("================================")
        break
