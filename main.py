import Haki


print("Untuk Berapa Orang ? ")
people=input()
for x in people :

print ("Masukan Judul : ")
title=input()
print ("Masukan deskripsi : ")
decription=input()
print ("Masukan Nama : ")
name=input()
print("Masukan Alamat : ")
address=input()
print("Masukan Kota : ")
city=input()
print("Masukan Kode Pos : ")
zip_code=input()
print("masukan Provinsi")
province=input()
jalan=Haki.EHaki(title, decription, name, address, city, zip_code, province)
jalan.web()
jalan.permohonan_baru()
jalan.data_pencipta()