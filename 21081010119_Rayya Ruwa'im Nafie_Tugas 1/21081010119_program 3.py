print("Program Penghitung luas dan volume bangun ruang")
print("Pilih bangun ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Tabung")
print("4. Kerucut")
pilihan = int(input("Masukkan pilihan: "))
if pilihan == 1:
    print("Pilihan: Kubus")
    print("1. Luas")
    print("2. Volume")
    pilihan_kubus = int(input("Masukkan pilihan: "))
    if pilihan_kubus == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        luas = 6 * sisi * sisi
        print("Luas kubus adalah: ", luas)
    elif pilihan_kubus == 2:
        sisi = float(input("Masukkan panjang sisi: "))
        volume = sisi * sisi * sisi
        print("Volume kubus adalah: ", volume)
    else:
        print("Pilihan tidak valid")
elif pilihan == 2:
    print("Pilihan: Balok")
    print("1. Luas")
    print("2. Volume")
    pilihan_balok = int(input("Masukkan pilihan: "))
    if pilihan_balok == 1:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        print("Luas balok adalah: ", luas)
    elif pilihan_balok == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = panjang * lebar * tinggi
        print("Volume balok adalah: ", volume)
    else:
        print("Pilihan tidak valid")
elif pilihan == 3:
    print("Pilihan: Tabung")
    print("1. Luas")
    print("2. Volume")
    pilihan_tabung = int(input("Masukkan pilihan: "))
    if pilihan_tabung == 1:
        jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 2 * 3.14 * jari * (jari + tinggi)
        print("Luas tabung adalah: ", luas)
    elif pilihan_tabung == 2:
        jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = 3.14 * jari * jari * tinggi
        print("Volume tabung adalah: ", volume)
    else:
        print("Pilihan tidak valid")
elif pilihan == 4:
    print("Pilihan: Kerucut")
    print("1. Luas")
    print("2. Volume")
    pilihan_kerucut = int(input("Masukkan pilihan: "))
    if pilihan_kerucut == 1:
        jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 3.14 * jari * (jari + tinggi)
        print("Luas kerucut adalah: ", luas)
    elif pilihan_kerucut == 2:
        jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = 1/3 * 3.14 * jari * jari * tinggi
        print("Volume kerucut adalah: ", volume)
    else:
        print("Pilihan tidak valid")
else:
    print("Pilihan tidak valid")
    