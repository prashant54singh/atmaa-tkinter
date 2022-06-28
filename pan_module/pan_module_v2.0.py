#Made by Adokshaj Bhandarkar [NMAMIT, 2nd Year ISE]
#Made for Atmanirbhar Business Consultancy LLP
from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('PAN MODULE V2.0')
mycolor='#1C202B'
mycolor2='#984DE5'
mycolor3='#0A0B1D'
root.configure(bg=mycolor3)
root.geometry('600x480')
root.resizable(False, False)

def saveinfo():
    if lastname.get() and firstname.get() and dob.get() and email.get() and mobilenum.get() and var1.get() != '---Please Select---' and var2.get() != '---Please Select---':
        b = open("PAN_DETAILS.csv","a")
        b.write(var1.get())
        b.write(",")
        b.write(var2.get())
        b.write(",")
        b.write(lastname.get())
        b.write(",")
        b.write(firstname.get())
        b.write(",")
        b.write(middlename.get())
        b.write(",")
        b.write(dob.get())
        b.write(",")
        b.write(email.get())
        b.write(",")
        b.write(mobilenum.get())
        b.write("\n")
        b.close()
        messagebox.showinfo("Saved!","DATA SAVED SUCCESSFULLY! \n\n1) Please open PAN_DETAILS.csv for viewing the details. \n2) PAN_DETAILS.csv can be found in the same folder as the .exe file. \n3) You may ADD details of another individual OR EXIT the module now.")
    else:
       messagebox.showinfo("FAILED!","Please Enter all the details!")
       
    
var1=StringVar(root)
var1.set("---Please Select---")
drop1=OptionMenu(root,var1,"New PAN - Indian Citizen (Form 49A)","New PAN - Foreign Citizen (Form 49A)","Changes or Correction in existing PAN data")
drop1.grid(row=2, column=1)


var2=StringVar(root)
var2.set("---Please Select---")
drop2=OptionMenu(root, var2, "INDIVIDUAL","ASSOCIATION OF PERSONS","BODY OF INDIVIDUALS","COMPANY","TRUST","LIMITED LIABILITY PARTNERSHIP")
drop2.grid(row=3, column=1)

img = PhotoImage(file = "icon.png") 
img1 = img.subsample(2, 2) 
Label(root, image = img1).grid(row = 0, column = 0, sticky=W) 

Label(root, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=1, column=0)
Label(root, text='ENTER PAN DETAILS ', bg=mycolor2, font=("Arial",18), fg='white').grid(row=0, column=1, sticky=E)
Label(root, text='*Application Type: ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=2, column=0, sticky=E)
Label(root, text='*Category: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=3, column=0, sticky=E)
Label(root, text='*Last Name/Surname: ', bg=mycolor3, font=("Arial",18),  fg='white').grid(row=4, column=0, sticky=E)
Label(root, text='*First Name: ', font=("Arial",18), bg=mycolor3, fg='white').grid(row=5, column=0, sticky=E)
Label(root, text='Middle Name: ', font=("Arial",18), bg=mycolor3, fg='white').grid(row=6, column=0, sticky=E)
Label(root, text='*DOB (DD-MM-YYYY): ', bg=mycolor3, font=("Arial",18),  fg='white').grid(row=7, column=0, sticky=E)
Label(root, text='*Email: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=8, column=0, sticky=E)
Label(root, text='*Mobile Number: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=9, column=0, sticky=E)
Label(root, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=10, column=0)

Button(root, text='Submit', bg=mycolor2, fg='white', font=("Arial",18), command=saveinfo).grid(row=16, column=1)

Label(root, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=17, column=0)
Label(root, text='- All fields marked with * are mandatory. ', font=("Arial",10),  bg=mycolor3, fg='white').grid(row=16, column=0, sticky=W, padx=5)
Label(root, text='- DOB Example: 31-01-2001', font=("Arial",10),  bg=mycolor3, fg='white').grid(row=17, column=0, sticky=W, padx=5)

#Entry(root).grid(row=0, column=10)
#Entry(root).grid(row=1, column=10)
#lastname = StringVar(root)
lastname = Entry(root, font=("Arial",13))
lastname.grid(row=4, column=1)
firstname = Entry(root, font=("Arial",13))
firstname.grid(row=5,column=1)
middlename = Entry(root, font=("Arial",13))
middlename.grid(row=6,column=1)
dob = Entry(root, font=("Arial",13))
dob.grid(row=7,column=1)
email = Entry(root, font=("Arial",13))
email.grid(row=8,column=1)
mobilenum = Entry(root, font=("Arial",13))
mobilenum.grid(row=9,column=1)

root.mainloop()

#Checkbutton(root, text='Cricket').grid(row=3, column=1, sticky=W)
#Checkbutton(root, text='Volleyball').grid(row=4, column=1, sticky=W)
#Checkbutton(root, text='Basketball').grid(row=5, column=1, sticky=W)
#Checkbutton(root, text='Badminton').grid(row=6, column=1, sticky=W)
