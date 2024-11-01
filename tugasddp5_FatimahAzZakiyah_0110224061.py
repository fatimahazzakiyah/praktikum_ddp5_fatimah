#1
kendaraan = ['yatch', 'kapal laut', 800, 'putih', 5]
print(kendaraan)

kendaraan.append('4,8M')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'History Supreme')
print(kendaraan)


print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))


#2
hitung_luas = int(input("""pilih salah 
satu:
1. hitung luas persegi
2. hitung luas lingkaran
3. hitung luas segitiga
"""))

match hitung_luas:
    case 1:
        print('menghitung luas persegi')
        sisi = int(input('masukan nilai sisi: '))
        hitung_luas_persegi = sisi **2
        print (f'jadi luas persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi} cm^2')

    case 2:
        print('menghitung luas lingkaran')
        jari_jari = float(input('masukan nilai jari-jari: '))
        hitung_luas_lingkaran = 3.14 * jari_jari * jari_jari
        print(f'jadi luas lingkaran dengan jari-jari{jari_jari} cm adalah {hitung_luas_lingkaran} cm^2')

    case 3:
        print('menghitung luas segitiga')
        alas = float(input('masukkan panjang alas: '))
        tinggi = float(input('masukkan tinggi: '))
        luas_segitiga = 0.5 * alas * tinggi
        print(f'luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas_segitiga} cm^2')


    case _:
        print('pilihan tidak valid')
    

