#input output file
#membuat file text

"""
w = write mode /mode menulis dan overwrite, jika file kosong, maka akan di buat file baru
r = read only mode 
a = appending mode 
r+ = write and read mode
"""

#membuat file teks
file = open("data.txt", 'w')

file.write("ini adalah data teks yang di buat dengan phytoh 3")
file.write("\ninibaris ke dua")
file.write("\ninibaris ke tiga")
file.write("\ninibaris ke empat")
file.close()

#membaca file teks

file2 = open("data.txt","r")
print(file2.readline())
file2.close

#appending mode

file3 = open("data.txt", 'a')
file3.write("\nbaris ini dibuat dengan appending mode")
file3.close