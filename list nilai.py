#tampilkan list
list_nilai = [1,2,3,4,5,6,7,8,9,10]
jumlah_index = len (list_nilai)
print ("jumlah index dalam list adalah: ", jumlah_index)

#program menggunakan count
list_nilai = [1,2,3,4,5,6,7,8,9,10]
count_10 = list_nilai.count(10)
print("jumlah nilai dalam count : ",count_10)

#program tambah nilai menggunakan append()
list_nilai = [1,2,3,4,5,6,7,8,9,10]
list_nilai.append("11")
print (list_nilai)

#tambah nilai menggunakan insert
list_nilai = [1,2,3,4,5,6,7,8,9,10]
list_nilai.insert(4,97)
print (list_nilai)

#tampilan nilai tiga terakhir
list_nilai = [1,2,3,4,5,6,7,8,9,10]
last_three = list_nilai[-3:]
print (last_three)

#tampilan nilai 7 terakhir
list_nilai = [1,2,3,4,5,6,7,8,9,10]
last_seven = list_nilai[-7:]
print(last_seven)

#tampilan nilai kecuali 1 dan 2
list_nilai = [1,2,3,4,5,6,7,8,9,10]
for nilai in list_nilai:
    if nilai =1 and nilai =2:
        print (nilai)

