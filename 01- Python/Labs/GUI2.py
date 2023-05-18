from tkinter import *
def ButtonPressed():
   ButtonPressed.counter+=1

   print("TheButtonPressed",ButtonPressed.counter)
    
ButtonPressed.counter = 0 

window_1 = Tk()
window_1.title("Hello ")
lable1=Label(window_1,text="label1")
lable1.pack(side=TOP)
window_1.geometry('1000x500')
b1=Button(window_1,text="click here to print your name ",bd='5',command=ButtonPressed)
b2 = Button(window_1,text="close",bd='5',command=window_1.destroy)
b3=  Button(window_1,text="counter")
photo_1 = PhotoImage(file='image.png')
photo_1 = photo_1.subsample(2,2)
b4=  Button(window_1,text = "Increment The button " , bd = '5' ,image=photo_1, command = ButtonPressed)

b1.pack(side=TOP)
b2.pack(side=RIGHT)
b3.pack(side=LEFT)
b4.pack(side=BOTTOM)
b4.place(x=500,y=250)
lable1.pack(side=BOTTOM)

window_1.mainloop()