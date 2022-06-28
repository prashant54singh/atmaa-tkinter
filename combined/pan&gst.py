#Made by Adokshaj Bhandarkar [NMAMIT, 2nd Year ISE]
#Made for Atmanirbhar Business Consultancy LLP
from tkinter import *
from tkinter import messagebox
import os

root=Tk()
root.title('COMBINED')
root.geometry('750x350')

mycolor='#1C202B'
mycolor2='#984DE5'
mycolor3='#0A0B1D'

root.configure(bg=mycolor3)
root.resizable(False,False)


def openpan():
    top1=Toplevel()
    top1.title('PAN MODULE V2.0')
    #mycolor='#1C202B'
    #mycolor2='#984DE5'
    #mycolor3='#0A0B1D'
    top1.configure(bg=mycolor3)
    top1.geometry('600x500')
    top1.resizable(False, False)

    def saveinfo():
        if lastname.get() and firstname.get() and dob.get() and email.get() and mobilenum.get() and var1.get() != '---Please Select---' and var2.get() != '---Please Select---': 
            b = open("DETAILS.csv","a")
            b.write('PAN')
            b.write(',')
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
            messagebox.showinfo("Saved!","DATA SAVED SUCCESSFULLY! \n\n1) Please open DETAILS.csv for viewing the details. \n2) DETAILS.csv can be found in the same folder as the .exe file.\n3) You may ADD details of another individual OR EXIT the module now.")
        else:
            messagebox.showinfo("FAILED!","Please Enter all the details!")
       
    
    var1=StringVar(top1)
    var1.set("---Please Select---")
    drop1=OptionMenu(top1,var1,"New PAN - Indian Citizen (Form 49A)","New PAN - Foreign Citizen (Form 49A)","Changes or Correction in existing PAN data")
    drop1.grid(row=2, column=1)


    var2=StringVar(top1)
    var2.set("---Please Select---")
    drop2=OptionMenu(top1, var2, "INDIVIDUAL","ASSOCIATION OF PERSONS","BODY OF INDIVIDUALS","COMPANY","TRUST","LIMITED LIABILITY PARTNERSHIP")
    drop2.grid(row=3, column=1)

    img = PhotoImage(file = "icon.png") 
    img1 = img.subsample(2, 2) 
    Label(top1, image = img1).grid(row = 0, column = 0, sticky=W) 

    Label(top1, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=1, column=0)
    Label(top1, text='ENTER PAN DETAILS ', bg=mycolor2, font=("Arial",18), fg='white').grid(row=0, column=1, sticky=E)
    Label(top1, text='*Application Type: ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=2, column=0, sticky=E)
    Label(top1, text='*Category: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=3, column=0, sticky=E)
    Label(top1, text='*Last Name/Surname: ', bg=mycolor3, font=("Arial",18),  fg='white').grid(row=4, column=0, sticky=E)
    Label(top1, text='*First Name: ', font=("Arial",18), bg=mycolor3, fg='white').grid(row=5, column=0, sticky=E)
    Label(top1, text='Middle Name: ', font=("Arial",18), bg=mycolor3, fg='white').grid(row=6, column=0, sticky=E)
    Label(top1, text='*DOB (DD-MM-YYYY): ', bg=mycolor3, font=("Arial",18),  fg='white').grid(row=7, column=0, sticky=E)
    Label(top1, text='*Email: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=8, column=0, sticky=E)
    Label(top1, text='*Mobile Number: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=9, column=0, sticky=E)
    Label(top1, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=10, column=0)

    Button(top1, text='Submit', bg=mycolor2, fg='white', font=("Arial",18), command=saveinfo).grid(row=16, column=1)

    Label(top1, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=17, column=0)
    Label(top1, text='- All fields marked with * are mandatory. ', font=("Arial",10),  bg=mycolor3, fg='white').grid(row=16, column=0, sticky=W, padx=5)
    Label(top1, text='- DOB Example: 31-01-2001', font=("Arial",10),  bg=mycolor3, fg='white').grid(row=17, column=0, sticky=W, padx=5)

    tbutt2 = Button(top1, text='Close Window',bg=mycolor2, fg='white', font=("Arial",18), command=top1.destroy)
    tbutt2.grid(row=17, column=1)

#Entry(root).grid(row=0, column=10)
#Entry(root).grid(row=1, column=10)
#lastname = StringVar(root)
    lastname = Entry(top1, font=("Arial",13))
    lastname.grid(row=4, column=1)
    firstname = Entry(top1, font=("Arial",13))
    firstname.grid(row=5,column=1)
    middlename = Entry(top1, font=("Arial",13))
    middlename.grid(row=6,column=1)
    dob = Entry(top1, font=("Arial",13))
    dob.grid(row=7,column=1)
    email = Entry(top1, font=("Arial",13))
    email.grid(row=8,column=1)
    mobilenum = Entry(top1, font=("Arial",13))
    mobilenum.grid(row=9,column=1)
    
    top1.mainloop()

    

#Checkbutton(root, text='Cricket').grid(row=3, column=1, sticky=W)
#Checkbutton(root, text='Volleyball').grid(row=4, column=1, sticky=W)
#Checkbutton(root, text='Basketball').grid(row=5, column=1, sticky=W)
#Checkbutton(root, text='Badminton').grid(row=6, column=1, sticky=W)
#Made by Adokshaj Bhandarkar [NMAMIT, 2nd Year ISE]   

def opengst():
    top2=Toplevel()
    top2.configure(bg=mycolor3)
    top2.title('GST MODULE')
    top2.geometry('740x470')
    top2.resizable(False, False)

    def saveinfo():
        if stateut.get() and district.get() and legal.get() and pan.get() and email.get() and mobilenum.get() and var1.get() != '---Please Select---':
            b = open("DETAILS.csv","a")
            b.write('GST')
            b.write(',')
            b.write(var1.get())
            b.write(",")
            b.write(stateut.get())
            b.write(",")
            b.write(district.get())
            b.write(",")
            b.write(legal.get())
            b.write(",")
            b.write(pan.get())
            b.write(",")
            b.write(email.get())
            b.write(",")
            b.write(mobilenum.get())
            b.write("\n")
            b.close()
            messagebox.showinfo("Saved!","DATA SAVED SUCCESSFULLY! \n\n1) Please open DETAILS.csv for viewing the details. \n2) DETAILS.csv can be found in the same folder as the .exe file.\n3) You may ADD details of another individual OR EXIT the module now.")
        else:
            messagebox.showinfo("FAILED!","Please enter all details.")
       
    
    var1=StringVar(top2)
    var1.set("---Please Select---")
    drop1=OptionMenu(top2,var1,"Taxpayer","Tax Deductor","Tax Collector(e-Commerce)","GST Practitioner","Non Resident Taxable Person","United Nation Body", "Consulate or Embassy of Foreign Country","Other Notified Person","Non-Resident Online Service Provider")
    drop1.grid(row=2, column=1)

#var2=StringVar(root)
#var2.set("---Please Select---")
#drop2=OptionMenu(root, var2, "INDIVIDUAL","ASSOCIATION OF PERSONS","BODY OF INDIVIDUALS","COMPANY","TRUST","LIMITED LIABILITY PARTNERSHIP")
#drop2.grid(row=3, column=1)

    img = PhotoImage(file = "icon.png") 
    img1 = img.subsample(2, 2) 
    Label(top2, image = img1).grid(row = 0, column = 0, sticky=W) 

    Label(top2, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=1, column=0)
    Label(top2, text='ENTER GST DETAILS ', bg=mycolor2, font=("Arial",18), fg='white').grid(row=0, column=1, sticky=W)
    Label(top2, text='*I am a: ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=2, column=0, sticky=E)
    Label(top2, text='*State/UT: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=3, column=0, sticky=E)
    Label(top2, text='*District: ', bg=mycolor3, font=("Arial",18),  fg='white').grid(row=4, column=0, sticky=E)
    Label(top2, text='*Legal Name of the Business: ', font=("Arial",18), bg=mycolor3, fg='white').grid(row=5, column=0, sticky=E)
    Label(top2, text='*Permanent Account Number (PAN): ', font=("Arial",18), bg=mycolor3, fg='white').grid(row=6, column=0, sticky=E)
    Label(top2, text='*Email: ', bg=mycolor3, font=("Arial",18),  fg='white').grid(row=7, column=0, sticky=E)
    Label(top2, text='*Mobile Number: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=8, column=0, sticky=E)
#Label(root, text='Mobile Number: ', font=("Arial",18),  bg=mycolor3, fg='white').grid(row=9, column=0)
    Label(top2, text=' ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=9, column=0)

    Button(top2, text='Submit', bg=mycolor2, fg='white', font=("Arial",18), command=saveinfo).grid(row=16, column=1)

    Label(top2, text='- All fields marked with * are mandatory. ', font=("Arial",10),  bg=mycolor3, fg='white').grid(row=16, column=0, sticky=W, padx=5)
    Label(top2, text='- DOB Example: 31-01-2001', font=("Arial",10),  bg=mycolor3, fg='white').grid(row=17, column=0, sticky=W, padx=5)

    tbutt2 = Button(top2, text='Close Window',bg=mycolor2, fg='white', font=("Arial",18), command=top2.destroy)
    tbutt2.grid(row=17, column=1)

#Entry(root).grid(row=0, column=10)
#Entry(root).grid(row=1, column=10)
#lastname = StringVar(root)
    stateut = Entry(top2, font=("Arial",13))
    stateut.grid(row=3, column=1)
    district = Entry(top2, font=("Arial",13))
    district.grid(row=4, column=1)
    legal = Entry(top2, font=("Arial",13))
    legal.grid(row=5,column=1)
    pan = Entry(top2, font=("Arial",13))
    pan.grid(row=6,column=1)
    email = Entry(top2, font=("Arial",13))
    email.grid(row=7,column=1)
    mobilenum = Entry(top2, font=("Arial",13))
    mobilenum.grid(row=8,column=1)
#mobilenum = Entry(top2, font=("Arial",13))
#mobilenum.grid(row=9,column=1)
    top2.mainloop()     

def closeall():
    root.destroy()

img = PhotoImage(file = "icon.png") 
img1 = img.subsample(2, 2) 
Label(root, image = img1).grid(row = 0, column = 0, sticky=W) 

Label(root, text='    ', bg=mycolor3, font=("Arial",18), fg='white').grid(row=0, column=1)

Label(root, text='ABOUT',font=("Arial",18), fg='white',  bg=mycolor2).grid(row=0, column=3)

Label(root, text='ATMAA PAN & GST Module is a computer application\nthat is used for storing PAN & GST information.\n\nIt stores the user details in a centralized database.\n\nSingle module for both PAN & GST.\n\nMade for Atmanirbhar Business Consultancy LLP', bg=mycolor, font=("Arial",15), fg='white', justify='left').grid(row=2, column=3, sticky=W, rowspan=5)

Label(root, text=' ', bg=mycolor3, font=("Arial",16), fg='white').grid(row=1, column=0)

tbutt = Button(root, text='PAN Details', bg=mycolor2, fg='white',font=("Arial",18), command=openpan)
tbutt.grid(row=2, column=0)

Label(root, text=' ', bg=mycolor3, font=("Arial",16), fg='white').grid(row=3, column=0)

tbutt2 = Button(root, text='GST Details', bg=mycolor2, fg='white',font=("Arial",18), command=opengst)
tbutt2.grid(row=4, column=0)

Label(root, text=' ', bg=mycolor3, font=("Arial",16), fg='white').grid(row=5, column=0)

tbutt3=tbutt = Button(root, text='Quit', bg=mycolor2, fg='white',font=("Arial",18), command=closeall)
tbutt3.grid(row=6, column=0)

Label(root, text=' ', bg=mycolor3, font=("Arial",16), fg='white').grid(row=7, column=0)

root.mainloop()
