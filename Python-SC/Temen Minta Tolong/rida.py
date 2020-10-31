
def bubble2(A):
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                print (A, 'cek pada' ,A[j], '>', A[j+1], "True", 'tukar',A[j], 'dengan', A[j+1], 'A menjadi ', A)
                A[j], A[j+1] = A[j+1], A[j]
                # print('tukar', A[j], 'dengan', A[j+1])
                # print ('=============== urutan menjadi ', A)
                tukar=True
            else :
                print (A, 'cek pada' ,A[j], '>', A[j+1], "False : tidak ada pertukaran")
                print('=============== hasil pada iterasi menjadi : ', A)
                
                
#A =[15,13,17,18]
A = [3,1,8,4,2]
bubble2(A)
