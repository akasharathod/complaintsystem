
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase

#Config

conn = ConnectionDatabase()
root = Tk()
root.geometry('1000x500')
root.title('Complaint Management System')
root.configure(bg='grey')

#Style


style = Style()
style.theme_use('classic')
for styles in ['TLabel', 'TButton', 'TRadioButton']:
    style.configure(styles, bg='grey')


labels = ['First Name:', 'Last Name:', 'Address:', 'Email ID:', 'Phone no:', 'Gender:', 'Comment:']
for i in range(7):
    Label(root, text=labels[i]).grid(row=i, column=0, padx=30, pady=30)


ButtonList = Button(root, text='View Complain')
ButtonList.grid(row=7, column=1)

ButtonSubmit = Button(root, text='Submit Now')
ButtonSubmit.grid(row=7, column=2)

# Entries
firstname = Entry(root, width=40, font=('Arial', 14))
firstname.grid(row=0, column=1, columnspan=2)

lastname = Entry(root, width=40, font=('Arial', 14))
lastname.grid(row=1, column=1, columnspan=2)

address = Entry(root, width=40, font=('Arial', 14))
address.grid(row=2, column=1, columnspan=2)

emailid = Entry(root, width=40, font=('Arial', 14))
emailid.grid(row=3, column=1, columnspan=2)

phoneno = Entry(root, width=40, font=('Arial', 14))
phoneno.grid(row=4, column=1, columnspan=2)

GenderGroup = StringVar()
Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=5, column=1)
Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=5, column=2)


comment = Text(root, width=40, height=5, font=('Arial', 14))
comment.grid(row=6, column=1, columnspan=2, padx=30, pady=30)

def SaveData():
    message = conn.Add(firstname.get(), lastname.get(), address.get(), emailid.get(), phoneno.get(), GenderGroup.get(), comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    address.delete(0, 'end')
    emailid.delete(0, 'end')
    phoneno.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)

def ShowComplainList():

    listrequest = ComplaintListing()


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)

root.mainloop()
