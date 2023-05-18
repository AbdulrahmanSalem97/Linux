from tkinter import *

def Func():
    print("Abdulrahman Salem")

window_1= Tk()

window_1.title("Hello From Tkinter ")

label_1 = Label(window_1 , text = "Abdulrahman")
label_1.pack(side = TOP)

#geometry 
window_1.geometry('500x700')

#add Button
#b1=Button(window_1,text="Name", bd ='5',command= Func)
#b2 = Button(window_1,text="exit",bd='5',command=window_1.destroy)

photo_1 = PhotoImage(file='image.png')
photo_1 = photo_1.subsample(2,2)

b1 = Button(window_1 , text= "Increment the Button", bd='5',image=photo_1, command = Func)
b1.pack(side = TOP)



#b3 =Button(window_1, text= "Button3")


#b4 =Button(window_1, text= "Button4")


#b1.pack(side = TOP)
#b2.pack(side = LEFT)
#b3.pack(side = RIGHT)
#b4.pack(side = BOTTOM)

window_1.mainloop()