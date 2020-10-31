#looping 
#example 1
namaBand = ['feast',
             'fourtwenty',
             'feby putri',
             'payung teduh']

lagu = ['berita kehilangan',
        'merah jambu',
        'halu',
        'zona nyaman']

for band in namaBand :
    print(band)

print(100*"=")

#example 2
iterasi = 0 
for band in namaBand :
    print('no', iterasi, 'nama band', band)
    iterasi+=1

#example 2 sangat ribet jadi dengan memanfaatakan fungsi dibawah akan menjadi lebih simople

print(100*"=")

#enumerate
for i,bandenu in enumerate(namaBand):
    print(i,":", bandenu)

print(100*"=")

#zip
for i,laguzip in zip(namaBand, lagu):
    print(i," menyanyikan lagu : ", laguzip)

print(100*"=")

#set
playlist = {'kuda', 'kucing', 'ayam', 'tawon', 'babi'}

for index in sorted(playlist):
    print(index)

print(100*"=")

#dictionary
playlist2 = {"linkin park" : "Numb",
             "BMTH" : "sleepwalking",
             "ed sheeran" : "perfect",
             "sales" : "chinese new year"}

for i,V in playlist2.items():
    print(i,'lagunya :',V)

for i in reversed(range(1,10,1)):
    print(i)

for i in playlist2.values():
    print(i)

for i in playlist2.keys():
    print(i)