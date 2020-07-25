# this is a Filw how to save a data in our form

from tkinter import *
root = Tk()
root.geometry("500x500")

def name():
    with open("Data.xls","a") as Data:
        Data.write(f"The name is :{uservalue.get()}  The Password is :{passwordvalue.get()}")

user = Label(root,text = "User Name :",font = 20)
password = Label(root,text = "Password :",font = 20)
user.place(x = 120,y = 120)# this is a User name (using a new place function) 
password.place(x = 120,y = 170) # this is aPassword

uservalue = StringVar() 
passwordvalue = StringVar()

user_input = Entry(root,textvariable = uservalue)
password_input = Entry(root,textvariable = passwordvalue)

user_input.place(x = 240,y = 123)# this is user box input
password_input.place(x = 240,y = 170) # this is a passord box input


# button to submit the data 

b1 = Button(root,text = "Submit",bg = "Black",fg = "White",font = 20,command = name,padx = 30).place(x =120,y = 230)

# # Exit button
b2 = Button(root,text = "Exit",font = 20,bg = "Black",fg = "White",command = root.destroy,padx = 30).place(x = 250,y = 230)



root.mainloop()