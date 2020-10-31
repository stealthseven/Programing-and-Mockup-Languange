import tkinter 

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Nama = Rafa")
label2 = tkinter.Label(main_window, text = "Umur = 19 ")

tombol1 = tkinter.Button(main_window, text = "tombol1")
tombol2 = tkinter.Button(main_window, text = "tombol2")

#method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#method menampilkan gui 
main_window.mainloop()


'''
import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan <_>")
    label2.pack()

label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana dengan menggunakan phyton3")
tombol = tkinter.Button(main_window, text="tekan aku yaa", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()

'''