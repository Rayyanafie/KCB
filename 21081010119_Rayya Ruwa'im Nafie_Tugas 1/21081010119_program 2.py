print("Program Konversi Suhu")
print("Pilih satuan suhu awal:")
print("1. Celcius")
print("2. Reamur")
print("3. Fahrenheit")
print("4. Kelvin")
pilihan_awal = int(input("Masukkan pilihan: "))

suhu_awal = float(input("Masukkan suhu awal: "))
tipe_suhu = ["Celcius", "Reamur", "Fahrenheit", "Kelvin"]

if pilihan_awal == 1:
    celcius = suhu_awal
elif pilihan_awal == 2:
    celcius = (4/5) * suhu_awal
elif pilihan_awal == 3:
    celcius = (5/9) * (suhu_awal - 32)
elif pilihan_awal == 4:
    celcius = suhu_awal - 273.15
else:
    print("Pilihan tidak valid")
    exit()
print("Pilih satuan suhu akhir:")
print("1. Celcius")
print("2. Reamur")
print("3. Fahrenheit")
print("4. Kelvin")
pilihan_akhir = int(input("Masukkan pilihan: "))

if pilihan_akhir == 1:
    suhu_akhir = celcius
elif pilihan_akhir == 2:
    suhu_akhir = (5/4) * celcius
elif pilihan_akhir == 3:
    suhu_akhir = (9/5) * celcius + 32
elif pilihan_akhir == 4:
    suhu_akhir = celcius + 273.15
else:
    print("Pilihan tidak valid")
    exit()
print("Hasil konversi suhu adalah: ", suhu_akhir, tipe_suhu[pilihan_akhir - 1])


