#struktur data tuple
#tuple mirip dengan list

#list 
ganjil = [1,3,5,7,9] #dapat di ubah 

#tuple
genap = (2,4,6,8,10) #data tidak bisa di edit/dirubah
                     #data tuple relatif lebih ringan daripada data list dan pengerjaan waktunya lebih singkat
print(type(ganjil))
print(type(genap))

print(dir(ganjil)) #data list bisa menggunakan fungsi 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(75*"=")
print(dir(genap)) #data tuple hanya bisa digunakan dengan fungsi "count" dan "index"

