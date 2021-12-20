from tkinter import*
import tkinter.messagebox
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier


class PHONE_NUMBER_FINDER:

    def __init__(self, root):
        self.root = root
        self.root.title("Phone FLCG")
        self.root.geometry("600x380+0+0")

        frame1 = Frame(self.root,padx=20,bd=16,relief=RIDGE)
        frame1.grid()

        frame2 = Frame(frame1, width=600,height=200, padx=20,bd=16,relief=RIDGE)
        frame2.grid(row = 0, column = 0)

        frame3 = Frame(frame1,width=600,height=150, padx=36,bd=16,relief=RIDGE)
        frame3.grid(row = 1, column = 0)

        PhoneNum= StringVar()
        Location = StringVar()
        Carrier = StringVar()
        Geo = StringVar()

        self.lblPhoneNum = Label(frame2, text='Enter Phone Number', font=('arial',14,'bold'),bd=12)
        self.lblPhoneNum.grid(row = 0, column=0, sticky=W)
        self.txtPhoneNum = Entry(frame2, textvariable=PhoneNum, font=('arial',14,'bold'),bd=12)
        self.txtPhoneNum.grid(row=0,column=1)

        self.lblLocation = Label(frame2, text='Location', font=('arial',14,'bold'),bd=12)
        self.lblLocation.grid(row=1, column=0,sticky=W)
        self.txtLocation = Entry(frame2, textvariable=Location, font=('arial',14,'bold'),bd=12)
        self.txtLocation.grid(row=1, column=1)

        self.lblCarrier = Label(frame2, text='Carrier', font=('arial', 14, 'bold'), bd=12)
        self.lblCarrier.grid(row=2, column=0,sticky=W)
        self.txtCarrier = Entry(frame2, textvariable=Carrier, font=('arial', 14, 'bold'), bd=12)
        self.txtCarrier.grid(row=2, column=1)

        self.lblgeo = Label(frame2, text='Geo', font=('arial', 14, 'bold'), bd=12)
        self.lblgeo.grid(row=3, column=0,sticky=W)
        self.txtgeo = Entry(frame2, textvariable=Geo, font=('arial', 14, 'bold'), bd=12)
        self.txtgeo.grid(row=3, column=1)

        def finder():
            f = PhoneNum.get()
            r = phonenumbers.parse(f,"CH")
            v=geocoder.description_for_number(r,"en")
            Location.set(print(v))
            m=print(carrier.name_for_number(r, "en"))
            Carrier.set(m)
            n=print(timezone.time_zones_for_number(r))
            Geo.set(n)

        def Reset():
            PhoneNum.set("")
            Location.set("")
            Carrier.set("")
            Geo.set("")

        def Exit():
            root.destroy()

        self.btnFinder = Button(frame3, text="Find", font=('arial',14,'bold'),bd=12,pady=14,padx=12,width=7,command=finder).grid(row=0,column=0)
        self.btnReset = Button(frame3, text="Reset", font=('arial',14,'bold'),bd=12,pady=14,padx=12,width=7, command=Reset).grid(row=0,column=1)
        self.btnExit = Button(frame3, text="Exit", font=('arial',14,'bold'),bd=12,pady=14,padx=12,width=7, command=Exit).grid(row=0,column=2)




if __name__=='__main__':
    root = Tk()
    application = PHONE_NUMBER_FINDER(root)
    root.mainloop()