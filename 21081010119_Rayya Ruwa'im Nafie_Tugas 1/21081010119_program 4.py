import random
print("Permainan Tebak Angka")
print("Pilih level: ")
print("1. Mudah")
print("2. Sedang")
print("3. Sulit")
level = int(input("Masukkan pilihan: "))
if level == 1:
    print("Pilihan: Mudah")
    print("Tebak angka dari 1-10")
    angka = random.randint(1, 10)
    nyawa = 3;
    while nyawa > 0:
        tebakan = int(input("Masukkan tebakan: "))
        if tebakan == angka:
            print("Tebakan benar!")
            print("Total percobaan: ", 3 - nyawa + 1, "kali")
            break
        elif tebakan > angka:
            print("Tebakan terlalu besar")
        else:
            print("Tebakan terlalu kecil")
        nyawa -= 1
        print("Nyawa tersisa: ", nyawa)
    if nyawa == 0:
        print("Game over")
        print("Angka yang dicari adalah: ", angka)
elif level == 2:
    print("Pilihan: Sedang")
    print("Tebak angka dari 1-50")
    angka = random.randint(1, 50)
    nyawa = 5;
    while nyawa > 0:
        tebakan = int(input("Masukkan tebakan: "))
        if tebakan == angka:
            print("Tebakan benar!")
            print("Total percobaan: ", 5 - nyawa + 1, "kali")
            break
        elif tebakan > angka:
            print("Tebakan terlalu besar")
        else:
            print("Tebakan terlalu kecil")
        nyawa -= 1
        print("Nyawa tersisa: ", nyawa)
    if nyawa == 0:
        print("Game over")
        print("Angka yang dicari adalah: ", angka)
elif level == 3:
    print("Pilihan: Sulit")
    print("Tebak angka dari 1-100")
    angka = random.randint(1, 100)
    nyawa = 10;
    while nyawa > 0:
        tebakan = int(input("Masukkan tebakan: "))
        if tebakan == angka:
            print("Tebakan benar!")
            print("Total percobaan: ", 10 - nyawa + 1, "kali")
            break
        elif tebakan > angka:
            print("Tebakan terlalu besar")
        else:
            print("Tebakan terlalu kecil")
        nyawa -= 1
        print("Nyawa tersisa: ", nyawa)
    if nyawa == 0:
        print("Game over")
        print("Angka yang dicari adalah: ", angka)
else:
    print("Pilihan tidak valid")
    exit()