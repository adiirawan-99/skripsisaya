'''
import cv2
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('webcam', frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cam.release() 
'''
'''
panjang = input('Masukkan Panjang: ')
lebar = input('Masukkan Lebar :')
luas = int(panjang)*int(lebar)
print('Hasil dari perhitungan: ', luas)

'''
'''
tinggi = input('masukkan tinggi ')
lebar = input('masukkan lebar ')
luas = 0.5*(int(tinggi)*int(lebar))

print('Luas Segitiga', luas)
'''
'''
nilai = input('masukkan nilai anda :')
if int(nilai) >= 75:
    print('Anda mendapat nilai', nilai, 'dengan predikat Lulus')
else:
    print('Anda mendapat nilai :', nilai, 'dengan predikat tidak lulus')

'''    
'''
nilai = int(input('masukkan nilai anda :'))
if nilai >= 75:
    print('Anda mendapat nilai', nilai, 'dengan predikat Lulus')
else:
    print('Anda mendapat nilai :', nilai, 'dengan predikat tidak lulus')

'''  
'''  
suhu = int(input('Masukkan suhu tubuh'))

if suhu <=35:
    print('Anda Butuh Kehangatan')
elif suhu >=35 or suhu <=38:
    print('Suhu Anda Normal')
else:
    print('Anda Demam Kali')

'''
'''
angka_yang_dicari = [1, 2, 3, 4, 5, 6, 7, 8, 9]
angka = int(input('Masukkan angka yang dicari :'))

if angka in angka_yang_dicari:
    print('Angka yang ada cari ada')
else:
    print('Angka yang dicari tidak ada')
'''
tinggi = int(input('Masukkan tinggi badan: '))
berat = int(input('Masukkan berat badan: '))
berat = berat_badan_ideal = 0.9*(tinggi-100)

if tinggi >=160:
    if berat_badan_ideal < berat or berat == berat_badan_ideal:
        print('Berat Badan Ideal Anda', berat_badan_ideal)
        print('Tinggi dan Berat Badan Anda ideal')
    else:
        print('Berat Badan Ideal Anda', berat_badan_ideal)
        print('Berat Badan Anda Tidak Ideal')
else:
    if berat_badan_ideal < berat or berat == berat_badan_ideal:
        print('Berat Badan Ideal Anda', berat_badan_ideal)
        print ('Tinggi dan berat Badan Anda tidak ideal')
    else:
        print('Berat Badan Ideal Anda', berat_badan_ideal)
        print('Tinggi dan Berat Badan Anda Tidak ideal')