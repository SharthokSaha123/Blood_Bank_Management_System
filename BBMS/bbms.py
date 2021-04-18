from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

#Login or Signup*****************************************************************

class bbms:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank  Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#ffa31a")
        title=Label(self.root,text="Blood Bank Management System",font=("bookman",40,"bold"),bd=10,fg="#ffa31a",bg="#b30000",width=30).pack(pady=50)

        self.log_Frame = LabelFrame(self.root,text="Login or Sign up",bd=10,font=("bookman",20,"bold"), relief=RIDGE,fg="White",bg="#423e3e")
        self.log_Frame.place(x=400, y=180, width=450, height=320)

        self.username=StringVar()
        self.password=StringVar()



        log_title = Label(self.log_Frame,text="username",fg="#ffa31a",bg="#423e3e",font=("bookman", 15,"bold"))
        log_title.place(x=0,y=50,height=40,width=180)
        e = Entry(self.log_Frame,textvariable=self.username,width=250,borderwidth=2).place(x=150,y=55,height=30,width=180)

        log_title2 = Label(self.log_Frame,text="password",fg="#ffa31a",bg="#423e3e",font=("bookman", 15,"bold"))
        log_title2.place(x=0,y=100,height=40,width=180)
        e2 = Entry(self.log_Frame,textvariable=self.password,width=250,borderwidth=2,show="*").place(x=150,y=105,height=30,width=180)

        log_button=Button(self.log_Frame,text="Login",font=("bookman",20,"bold"),padx=120,fg="white",bg="#ff3333",command=self.logincheck)
        log_button.place(x=44,y=170,height=40)

        sign_button = Button(self.log_Frame, text="Sign up", font=("bookman", 20, "bold"), padx=120, fg="white",
                            bg="#ffa31a",command=self.new_windowsign)
        sign_button.place(x=44, y=220, height=40,width=340)

    def logincheck(self):
        user=(self.username.get())
        passw=(self.password.get())

        if(user=="" or passw==""):
            messagebox.showinfo("Login","Please enter your user name and password")
        elif (user == "sharthok" and passw == "123srtk"):
            self.newwindowh = Toplevel(self.root)
            self.us = bbms5(self.newwindowh)
        else:
            messagebox.showerror("Login Error","Please enter correct username or password")

    def new_windowhome(self):
        self.newwindowh=Toplevel(self.root)
        self.us=bbms5(self.newwindowh)

    def new_windowsign(self):
        self.newwindows=Toplevel(self.root)
        self.ug=bbms6(self.newwindows)


#Home.....................................................................

class bbms5:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#b30000")
        title=Label(self.root,text="HOME",font=("aldus",40,"bold"),bd=10,fg="#ffa31a",bg="#423e3e",width=50).pack()

        Home_Frame = LabelFrame(self.root,bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#ffa31a")
        Home_Frame.place(x=110, y=152, width=1070, height=320)

        Blood_button = Button(self.root, text="Blood\n Information", font=("bookman",20, "bold"), padx=20, fg="#ffa31a", bg="#333333",bd=10,command=self.new_windowblood)
        Blood_button.place(x=225, y=200, height=225,width=240)

        Donor_button = Button(self.root, text="DONOR", font=("bookman", 20, "bold"), padx=20, fg="#ffa31a",bg="#333333", bd=10,command=self.new_windowdonor)
        Donor_button.place(x=525, y=200, height=225, width=240)

        Stock_button = Button(self.root, text="Stock\n Information", font=("bookman", 20, "bold"), padx=20, fg="#ffa31a",
                              bg="#333333", bd=10,command=self.new_windowstock)
        Stock_button.place(x=825, y=200, height=225, width=240)

        mov = Label(self.root, text='"20 minuities of your time and 250 cc of your blood,may make the difference between life and death-"\n So donate blood and save life....!', bg="#b30000", fg="#ffffe6", font=("Calisto MT", 17, "bold"))
        mov.place(height=50,width=1070,y=500,x=110)

    def new_windowblood(self):
        self.newwindowb = Toplevel(self.root)
        self.sa = bbms1(self.newwindowb)

    def new_windowdonor(self):
        self.newwindowd = Toplevel(self.root)
        self.sh = bbms2(self.newwindowd)

    def new_windowstock(self):
        self.newwindows = Toplevel(self.root)
        self.sr = bbms3(self.newwindows)

#Signup.........................................................

class bbms6:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#ffa31a")
        title=Label(self.root,text="Blood Bank Management System",font=("aldus",40,"bold"),bd=10,fg="#ffa31a",bg="#423e3e",width=50).pack()

        sign_Frame=LabelFrame(self.root,text="Sign up",bd=10,font=("bookman",20,"bold"), relief=RIDGE,fg="White",bg="#423e3e")
        sign_Frame.place(x=360, y=155, width=525, height=430)

        self.fname=StringVar()
        self.lname = StringVar()
        self.username=StringVar()
        self.bg=StringVar()
        self.email=StringVar()
        self.phone=StringVar()
        self.passw=StringVar()
        self.cpassw=StringVar()

        fname = Label(sign_Frame, text="First Name", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        fname.grid(row=1, column=0, pady=0, padx=10, sticky="w")

        e_fname = Entry(sign_Frame, textvariable=self.fname, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,width=25)
        e_fname.grid(row=2, column=0, pady=0, padx=10, sticky="w")

        lname = Label(sign_Frame, text="Last Name", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        lname.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        e_lname = Entry(sign_Frame, textvariable=self.lname, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_lname.grid(row=2, column=1, pady=0, padx=10, sticky="w")

        uname = Label(sign_Frame, text="Username", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        uname.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        e_uname = Entry(sign_Frame, textvariable=self.username, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_uname.grid(row=4, column=0, pady=0, padx=10, sticky="w")

        bg = Label(sign_Frame, text="Blood Group", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        bg.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        e_bg = Entry(sign_Frame, textvariable=self.bg, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,width=25)
        e_bg.grid(row=4, column=1, pady=0, padx=10, sticky="w")

        opt1_bg = ttk.Combobox(sign_Frame, textvariable=self.bg, font=("Calisto MT", 12, "bold"), state='readonly',width=26)
        opt1_bg['values'] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        opt1_bg.grid(row=4, column=1, pady=0, padx=10)

        email = Label(sign_Frame, text="Email", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        email.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        e_email = Entry(sign_Frame, textvariable=self.email, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_email.grid(row=6, column=0, pady=0, padx=10, sticky="w")

        phone = Label(sign_Frame, text="Phone", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        phone.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        e_phone = Entry(sign_Frame, textvariable=self.phone, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_phone.grid(row=6, column=1, pady=0, padx=10, sticky="w")

        passw = Label(sign_Frame, text="Password", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        passw.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        e_passw = Entry(sign_Frame, textvariable=self.passw, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_passw.grid(row=8, column=0, pady=0, padx=10, sticky="w")

        cpassw = Label(sign_Frame, text="Confirm Password", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        cpassw.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        e_cpassw = Entry(sign_Frame, textvariable=self.cpassw, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_cpassw.grid(row=8, column=1, pady=0, padx=10, sticky="w")

        sign_button = Button(sign_Frame, text="Sign up", font=("bookman", 20, "bold"), padx=120, fg="white",
                             bg="#ffa31a",command=self.signincheck)
        sign_button.place(x=80, y=325, height=40, width=340)

    def signincheck(self):

        fname=(self.fname.get())
        lname=(self.lname.get())
        username=(self.username.get())
        bg=(self.bg.get())
        email=(self.email.get())
        phone=(self.phone.get())
        passw=(self.passw.get())
        cpassw=(self.cpassw.get())

        if (fname=="" or lname=="" or username=="" or bg=="" or email=="" or phone=="" or passw=="" or cpassw==""):
            messagebox.showinfo("Sign up Error","Please fillup all fields")
        elif(passw!=cpassw):
            messagebox.showerror("Sign up Error", "Password do not match !")
        else:
            self.newwindowl = Toplevel(self.root)
            self.os = bbms(self.newwindowl)

    def new_windowlogin(self):
        self.newwindowl=Toplevel(self.root)
        self.os=bbms(self.newwindowl)

#Blood...................................................................................

class bbms1:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#b30000")
        title=Label(self.root,text="   BLOOD INFORMATION",font=("aldus",40,"bold"),bd=10,fg="#e86464",bg="#423e3e",width=50).pack()

        blood_Frame1 = LabelFrame(self.root, text="Common Blood types", bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#423e3e")
        blood_Frame1.place(x=40, y=170, width=580, height=370)

        heading1_frame1 = Label(blood_Frame1, text="Blood Group", fg="white", bg="#e86464", font=("Calisto MT", 15, "bold"))
        heading1_frame1.grid(row=1, column=0, pady=15, padx=20, sticky="w")

        heading2_frame1 = Label(blood_Frame1, text="Antigen", fg="white", bg="#e86464",width=28,font=("Calisto MT", 15, "bold"))
        heading2_frame1.grid(row=1, column=1, pady=15, padx=20, sticky="w")

        value1_frame1 = Label(blood_Frame1, text="A", bg="#423e3e", fg="#e86464",font=("Calisto MT", 15, "bold"))
        value1_frame1.grid(row=2, column=0, pady=5, padx=50, sticky="w")

        value2_frame1 = Label(blood_Frame1, text="B", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        value2_frame1.grid(row=3, column=0, pady=5, padx=50, sticky="w")

        value3_frame1 = Label(blood_Frame1, text="O", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        value3_frame1.grid(row=4, column=0, pady=5, padx=50, sticky="w")

        value4_frame1 = Label(blood_Frame1, text="AB", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        value4_frame1.grid(row=5, column=0, pady=5, padx=45, sticky="w")

        Avalue1_frame1 = Label(blood_Frame1, text="Red Cells: A antigen\nPlasma: B antibody", bg="#423e3e", fg="white", width=28,padx=0,font=("Calisto MT", 15, "bold"))
        Avalue1_frame1.grid(row=2, column=1, pady=5, padx=0, sticky="w")

        Avalue2_frame1 = Label(blood_Frame1, text="Red Cells: B antigen\nPlasma: A antibody", bg="#423e3e", fg="white",width=28,padx=0,font=("Calisto MT", 15, "bold"))
        Avalue2_frame1.grid(row=3, column=1, pady=5, padx=0, sticky="w")

        Avalue3_frame1 = Label(blood_Frame1, text="Red Cells: A & B antigen\nPlasma: No antibody", bg="#423e3e", fg="white",width=28,padx=0,font=("Calisto MT", 15, "bold"))
        Avalue3_frame1.grid(row=4, column=1, pady=5, padx=0, sticky="w")

        Avalue4_frame1 = Label(blood_Frame1, text="Red Cells:No antigen\nPlasma:A & B antibody", bg="#423e3e", fg="white",width=28,padx=0,font=("Calisto MT", 15,"bold"))
        Avalue4_frame1.grid(row=5, column=1, pady=5, padx=0, sticky="w")


        blood_Frame2 = LabelFrame(self.root, text="Compatitible Blood Type Donors", bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#423e3e")
        blood_Frame2.place(x=655, y=140, width=580, height=415)

        Table_Frame = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame.place(x=0, y=10, width=558, height=35)

        heading1_frame2 = Label(Table_Frame, text="Blood Group", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        heading1_frame2.grid(row=1, column=0, pady=0, padx=0, sticky="w")

        heading2_frame2 = Label(Table_Frame, text="Donate Blood To", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        heading2_frame2.grid(row=1, column=1, pady=0, padx=35, sticky="w")

        heading3_frame2 = Label(Table_Frame, text="Receive Blood From", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        heading3_frame2.grid(row=1, column=2, pady=0, padx=0, sticky="w")

        Table_Frame2 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame2.place(x=0, y=50, width=558, height=35)


        value1_frame2 = Label(Table_Frame2, text="A+", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        value1_frame2.grid(row=2, column=0, pady=0, padx=0, sticky="w")

        value12_frame2 = Label(Table_Frame2, text="A+ , AB+", fg="white", bg="#e86464",
                                font=("Calisto MT", 13, "bold"))
        value12_frame2.grid(row=2, column=1, pady=0, padx=145, sticky="w")

        value13_frame2 = Label(Table_Frame2, text="  A+ , A- , O+ , O-", fg="white", bg="#e86464",
                                font=("Calisto MT", 13, "bold"))
        value13_frame2.grid(row=2, column=2, pady=0, padx=0, sticky="w")


        Table_Frame3 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame3.place(x=0, y=87, width=558, height=35)

        value2_frame2 = Label(Table_Frame3, text="A-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=3, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame3, text="A+ , A- , AB+ , AB-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=3, column=1, pady=0, padx=149, sticky="w")

        value23_frame2 = Label(Table_Frame3, text="  A- , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=3, column=2, pady=0, padx=0, sticky="w")

        Table_Frame4 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame4.place(x=0, y=124, width=558, height=35)

        value2_frame2 = Label(Table_Frame4, text="B+", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=3, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame4, text="B+ , AB+", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=3, column=1, pady=0, padx=148, sticky="w")

        value23_frame2 = Label(Table_Frame4, text="B+ , B- , O+, O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=3, column=2, pady=0, padx=18, sticky="w")

        Table_Frame4 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame4.place(x=0, y=161, width=558, height=35)

        value2_frame2 = Label(Table_Frame4, text="B-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=4, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame4, text=" B+ , B- , AB+ , AB-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=4, column=1, pady=0, padx=150, sticky="w")

        value23_frame2 = Label(Table_Frame4, text="   B- , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=4, column=2, pady=0, padx=0, sticky="w")

        Table_Frame5 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame5.place(x=0, y=198, width=558, height=35)

        value2_frame2 = Label(Table_Frame5, text="O+", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=5, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame5, text="O+ , A+ , B+ , AB+", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=5, column=1, pady=0, padx=145, sticky="w")

        value23_frame2 = Label(Table_Frame5, text=" O+ , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=5, column=2, pady=0, padx=0, sticky="w")

        Table_Frame6 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame6.place(x=0, y=235, width=558, height=35)

        value2_frame2 = Label(Table_Frame6, text="O-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=6, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame6, text="Everyone", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=6, column=1, pady=0, padx=150, sticky="w")

        value23_frame2 = Label(Table_Frame6, text="  O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=6, column=2, pady=0, padx=80, sticky="w")

        Table_Frame7 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame7.place(x=0, y=272, width=558, height=35)

        value2_frame2 = Label(Table_Frame7, text="AB+", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=7, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame7, text="AB+", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=7, column=1, pady=0, padx=133, sticky="w")

        value23_frame2 = Label(Table_Frame7, text="Everyone", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=7, column=2, pady=0, padx=100, sticky="w")

        Table_Frame8 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame8.place(x=0, y=309, width=558, height=35)

        value2_frame2 = Label(Table_Frame8, text="AB-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=8, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame8, text="AB+ , AB-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=8, column=1, pady=0, padx=137, sticky="w")

        value23_frame2 = Label(Table_Frame8, text="   AB- , A- , B- , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=8, column=2, pady=0, padx=0, sticky="w")

#Donor..........................................................................

class bbms2:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System".center(330))
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#f50b07")
        title=Label(self.root,text="DONOR INFORMATION",font=("aldus",40,"bold"),bd=10,fg="#e86464",bg="#423e3e",width=50).pack()

        self.did= StringVar()
        self.dname= StringVar()
        self.dbg = StringVar()
        self.dage = StringVar()
        self.dgender= StringVar()
        self.dcontact= StringVar()
        self.daddress = StringVar()
        self.dlast_donate = StringVar()
        self.dnext_donate= StringVar()

        donor_Frame = LabelFrame(self.root,text="Donor Registration", bd=10, relief=RIDGE,font=("Calisto MT", 20, "bold"),fg="#e86464", bg="#423e3e")
        donor_Frame.place(x=20, y=100, width=440, height=550)


        #m_title = Label(donor_Frame, text="Donor Registration", bg="#e86464", fg="black", font=("Calisto MT", 20, "bold"))
        #m_title.grid(row=0, columnspan=2, padx=80,pady=10)

        dn_id = Label(donor_Frame, text="Donor Id", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        e_id = Entry(donor_Frame, textvariable=self.did, font=("Calisto MT", 13, "bold"), bd=5,relief=GROOVE)
        e_id.grid(row=1, column=1, pady=0, padx=0, sticky="w")

        dn_name = Label(donor_Frame, text="Donor Name", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        e2_name = Entry(donor_Frame, textvariable=self.dname, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e2_name.grid(row=2, column=1, pady=10, padx=0, sticky="w")

        dn_bg = Label(donor_Frame, text="Blood Group", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_bg.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        e3_bg = Entry(donor_Frame, textvariable=self.dbg, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e3_bg.grid(row=3, column=1, pady=0, padx=0, sticky="w")

        opt_bg = ttk.Combobox(donor_Frame, textvariable=self.dbg, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_bg['values'] = ("A+","A-","B+","B-","O+","O-","AB+","AB-")
        opt_bg.grid(row=3, column=1, pady=10, padx=0)

        dn_age = Label(donor_Frame, text="Donor Age", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_age.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        e4_age = Entry(donor_Frame, textvariable=self.dage, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e4_age.grid(row=4, column=1, pady=10, padx=0, sticky="w")

        dn_gender = Label(donor_Frame, text="Donor Gender", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        e5_gender = Entry(donor_Frame, textvariable=self.dgender, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e5_gender.grid(row=5, column=1, pady=10, padx=0, sticky="w")

        opt_gender = ttk.Combobox(donor_Frame, textvariable=self.dgender, font=("Calisto MT", 12, "bold"),state='readonly')
        opt_gender['values'] = ("Male", "Female", "Other")
        opt_gender.grid(row=5, column=1, pady=10, padx=0)

        dn_cnt = Label(donor_Frame, text="Donor Phn", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_cnt.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        e6_cnt = Entry(donor_Frame, textvariable=self.dcontact, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e6_cnt.grid(row=6, column=1, pady=10, padx=0, sticky="w")

        dn_ld = Label(donor_Frame, text="Last Donate", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_ld.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        e7_ld = Entry(donor_Frame, textvariable=self.dlast_donate, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e7_ld.grid(row=7, column=1, pady=10, padx=0, sticky="w")

        dn_nd = Label(donor_Frame, text="Next Donate avl.", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_nd.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        e8_nd = Entry(donor_Frame, textvariable=self.dnext_donate, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e8_nd.grid(row=8, column=1, pady=10, padx=0, sticky="w")

        dn_add = Label(donor_Frame, text="Donor Address", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_add.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        e9_add = Entry(donor_Frame, textvariable=self.daddress, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e9_add.grid(row=9, column=1, pady=10, padx=0, sticky="w")


        save_button = Button(donor_Frame, text="Save", font=("bookman", 13, "bold"), padx=20, fg="white", bg="#e86464",command=self.save)
        save_button.place(x=202, y=465, height=25)

        clear_button = Button(donor_Frame, text="Clear", font=("bookman", 13, "bold"), padx=18, fg="white", bg="#e86464",command=self.clear)
        clear_button.place(x=302, y=465, height=25)


        #donor databaase
        database_Frame=Frame(self.root, bd=10, relief=RIDGE, bg="#423e3e")
        database_Frame.place(x=500, y=100,height=550,width=760)

        deletebtn = Button(database_Frame, text="Delete",font=("bookman", 13, "bold"), padx=18,fg="white", bg="#e86464",command=self.delete_donor)
        deletebtn.place(x=515,y=500,height=25)

        updatebtn = Button(database_Frame, text="Update", font=("bookman", 13, "bold"), padx=18, fg="white",bg="#e86464",command=self.update_data)
        updatebtn.place(x=624, y=500, height=25)



        self.search_by = StringVar()
        self.search_here = StringVar()

        don_search = Label(database_Frame, text="Search By :", bg="#423e3e", fg="#e86464", font=("Calisto MT", 20, "bold"))
        don_search.grid(row=0, column=0, pady=0, padx=25, sticky="w")

        e10_search = Entry(database_Frame, textvariable=self.search_by, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e10_search.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        opt_search = ttk.Combobox(database_Frame, textvariable=self.search_by, width=20,
                                    font=("Calisto MT", 12, "bold"), state='readonly')
        opt_search['values'] = ("D_Id", "D_Name", "D_Blood_Group","D_Address")
        opt_search.grid(row=0, column=1, padx=4, pady=0)

        e11_Search = Entry(database_Frame, textvariable=self.search_here, width=20, font=("Calisto MT", 14, "bold"),bd=5, relief=GROOVE)
        e11_Search.grid(row=0, column=2, pady=10, padx=15, sticky="w")

        searchbtn = Button(database_Frame, text="Search", width=10,command=self.search_data)
        searchbtn.grid(row=0,column=3)

        Table_Frame = Frame(database_Frame, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame.place(x=10, y=60, width=720, height=435)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.database_table = ttk.Treeview(Table_Frame,
                    columns=("did", "dname","dbg", "dage", "dgender", "dcontact","dlast_donate","dnext_donate","daddress"),
                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.database_table.xview)
        scroll_y.config(command=self.database_table.yview)

        self.database_table.heading("did", text="Donor Id")
        self.database_table.heading("dname", text="Name")
        self.database_table.heading("dbg", text="Blood Group")
        self.database_table.heading("dage", text="Age")
        self.database_table.heading("dgender", text="Gender")
        self.database_table.heading("dcontact", text="Phone")
        self.database_table.heading("dlast_donate", text="Last Donate")
        self.database_table.heading("dnext_donate", text="Next Donate Avl")
        self.database_table.heading("daddress", text="Address")

        self.database_table['show'] = 'headings'

        self.database_table.column("did", width=60)
        self.database_table.column("dname", width=180)
        self.database_table.column("dbg", width=80)
        self.database_table.column("dage",width=70)
        self.database_table.column("dgender", width=70)
        self.database_table.column("dcontact", width=110)
        self.database_table.column("daddress", width=210)
        self.database_table.column("dlast_donate", width=110)
        self.database_table.column("dnext_donate", width=110)

        self.database_table.pack(fill=BOTH, expand=1)
        self.database_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def search_data(self):
        sercon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sercon.cursor()

        cur.execute("select * from donor where "+str(self.search_by.get())+" LIKE '%"+str(self.search_here.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.database_table.delete(*self.database_table.get_children())
            for row in rows:
                self.database_table.insert('', END, values=row)
            sercon.commit()
        sercon.close()

    def save (self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sqlcon.cursor()
        cur.execute("insert into donor values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.did.get(),
            self.dname.get(),
            self.dbg.get(),
            self.dage.get(),
            self.dgender.get(),
            self.dcontact.get(),
            self.dlast_donate.get(),
            self.dnext_donate.get(),
            self.daddress.get()
        ))

        sqlcon.commit()
        self.fetch_data()
        self.clear()
        sqlcon.close()


    def fetch_data(self):
        felcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = felcon.cursor()
        cur.execute("Select * from donor")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.database_table.delete(*self.database_table.get_children())
            for row in rows:
                self.database_table.insert('', END, values=row)
            felcon.commit()
        felcon.close()

    def clear(self):
        self.did.set("")
        self.dname.set("")
        self.dbg.set("")
        self.dage.set("")
        self.dgender.set("")
        self.dcontact.set("")
        self.dlast_donate.set("")
        self.dnext_donate.set("")
        self.daddress.set("")

    def get_cursor(self, ev):
        cursor_row = self.database_table.focus()
        contents = self.database_table.item(cursor_row)
        row = contents['values']

        self.did.set(row[0])
        self.dname.set(row[1])
        self.dbg.set(row[2])
        self.dage.set(row[3])
        self.dgender.set(row[4])
        self.dcontact.set(row[5])
        self.dlast_donate.set(row[6])
        self.dnext_donate.set(row[7])
        self.daddress.set(row[8])

    def delete_donor(self):
        delcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = delcon.cursor()
        cur.execute("delete from donor where D_Id=%s", self.did.get())

        delcon.commit()
        delcon.close()
        self.fetch_data()
        self.clear()

    def update_data(self):
        updcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = updcon.cursor()
        cur.execute("update donor set D_Name=%s,D_Blood_Group=%s,D_Age=%s,D_Gender=%s,D_Phone=%s,D_Last_Donate=%s,D_Next_Donate=%s,D_Address=%s where D_Id=%s",(

            self.dname.get(),
            self.dbg.get(),
            self.dage.get(),
            self.dgender.get(),
            self.dcontact.get(),
            self.dlast_donate.get(),
            self.dnext_donate.get(),
            self.daddress.get(),
            self.did.get()

        ))

        updcon.commit()
        self.fetch_data()
        self.clear()
        updcon.close()

#Stock..................................................................

class bbms3:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System".center(330))
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#f50b07")
        title=Label(self.root,text="STOCK INFORMATION",font=("aldus",40,"bold"),bd=10,fg="#e86464",bg="#423e3e",width=50).pack()

        donor_Frame = LabelFrame(self.root, text="ADD BLOOD", bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#423e3e")
        donor_Frame.place(x=20, y=100, width=440, height=550)

        self.sid = StringVar()
        #self.sbid = StringVar()
        self.sbg = StringVar()
        self.status= StringVar()
        self.quantity =StringVar()
        self.hname = StringVar()
        self.hadd = StringVar()
        self.hphn = StringVar()

        st_id = Label(donor_Frame, text="Stock Id", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        e_id = Entry(donor_Frame, textvariable=self.sid, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e_id.grid(row=1, column=1, pady=0, padx=0, sticky="w")

        '''st_bid = Label(donor_Frame, text="Blood Id", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_bid.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        e2_bid = Entry(donor_Frame, textvariable=self.sbid, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e2_bid.grid(row=2, column=1, pady=10, padx=0, sticky="w")

        opt_bid = ttk.Combobox(donor_Frame, textvariable=self.sbid, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_bid['values'] = ("101 [A+]", "102 [A-]", "103 [B+]", "104 [B-]", "105 [O+]", "106 [O-]", "107 [AB+]", "109 [AB-]")
        opt_bid.grid(row=2, column=1, pady=10, padx=0)'''

        st_bg = Label(donor_Frame, text="Blood Group", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_bg.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        e3_bg = Entry(donor_Frame, textvariable=self.sbg, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e3_bg.grid(row=2, column=1, pady=0, padx=0, sticky="w")

        opt_bg = ttk.Combobox(donor_Frame, textvariable=self.sbg, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_bg['values'] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        opt_bg.grid(row=2, column=1, pady=10, padx=0)

        st_status = Label(donor_Frame, text="Blood Status", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_status.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        e4_status = Entry(donor_Frame, textvariable=self.status, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e4_status.grid(row=3, column=1, pady=10, padx=0, sticky="w")

        opt_status = ttk.Combobox(donor_Frame, textvariable=self.status, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_status['values'] = ("Availavle","Not Availavle")
        opt_status.grid(row=3, column=1, pady=10, padx=0)

        quantity = Label(donor_Frame, text="Quantity", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        quantity.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        e5_quantity = Entry(donor_Frame, textvariable=self.quantity, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e5_quantity.grid(row=4, column=1, pady=10, padx=0, sticky="w")

        H_name = Label(donor_Frame, text="Hospital Name", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        H_name.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        e6_Hname = Entry(donor_Frame, textvariable=self.hname, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e6_Hname.grid(row=5, column=1, pady=10, padx=0, sticky="w")

        H_add = Label(donor_Frame, text="Hospital Address", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        H_add.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        e7_Hadd = Entry(donor_Frame, textvariable=self.hadd, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e7_Hadd.grid(row=6, column=1, pady=10, padx=0, sticky="w")

        H_cont = Label(donor_Frame, text="Hospital Phn", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        H_cont.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        e6_Hcont = Entry(donor_Frame, textvariable=self.hphn, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e6_Hcont.grid(row=7, column=1, pady=10, padx=0, sticky="w")

        save_button = Button(donor_Frame, text="Add", font=("bookman", 13, "bold"), padx=20, fg="white", bg="#e86464",command=self.save)
        save_button.place(x=202, y=422, height=25)

        clear_button = Button(donor_Frame, text="Clear", font=("bookman", 13, "bold"), padx=18, fg="white",bg="#e86464",command=self.clear)
        clear_button.place(x=302, y=422, height=25)

        #stockframe

        stock_Frame = Frame(self.root, bd=10, relief=RIDGE, bg="#423e3e")
        stock_Frame.place(x=500, y=100, height=550, width=760)

        deletebtn = Button(stock_Frame, text="Delete", font=("bookman", 13, "bold"), padx=18, fg="white",
                           bg="#e86464",command=self.delete_Blood)
        deletebtn.place(x=515, y=500, height=25)

        updatebtn = Button(stock_Frame, text="Update", font=("bookman", 13, "bold"), padx=18, fg="white",
                           bg="#e86464",command=self.update_data)
        updatebtn.place(x=624, y=500, height=25)

        self.search_by = StringVar()
        self.search_here = StringVar()

        don_search = Label(stock_Frame, text="Search By :", bg="#423e3e", fg="#e86464",
                           font=("Calisto MT", 20, "bold"))
        don_search.grid(row=0, column=0, pady=0, padx=25, sticky="w")

        e10_search = Entry(stock_Frame, textvariable=self.search_by, font=("Calisto MT", 13, "bold"), bd=5,
                           relief=GROOVE)
        e10_search.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        opt_search = ttk.Combobox(stock_Frame, textvariable=self.search_by, width=20,
                                  font=("Calisto MT", 12, "bold"), state='readonly')
        opt_search['values'] = ("Stock_id","Blood_Group","Hospital_Name","Hospital_Address")
        opt_search.grid(row=0, column=1, padx=4, pady=0)

        e11_Search = Entry(stock_Frame, textvariable=self.search_here, width=20, font=("Calisto MT", 14, "bold"),
                           bd=5, relief=GROOVE)
        e11_Search.grid(row=0, column=2, pady=10, padx=15, sticky="w")

        searchbtn = Button(stock_Frame, text="Search", width=10,command=self.search_data)
        searchbtn.grid(row=0, column=3)

        Table_Frame = Frame(stock_Frame, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame.place(x=10, y=60, width=720, height=435)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.stock_table = ttk.Treeview(Table_Frame,
                                           columns=(
                                           "sid","sbg", "status", "quantity", "hname", "hadd",
                                           "hphn"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.stock_table.xview)
        scroll_y.config(command=self.stock_table.yview)

        self.stock_table.heading("sid", text="Stock Id")
        #self.stock_table.heading("sbid", text="Blood Id")
        self.stock_table.heading("sbg", text="Blood Group")
        self.stock_table.heading("status", text="Status")
        self.stock_table.heading("quantity", text="Quantity")
        self.stock_table.heading("hname", text="Hospital Name")
        self.stock_table.heading("hadd", text="Hospital Address")
        self.stock_table.heading("hphn", text="Hospital Phone")


        self.stock_table['show'] = 'headings'

        self.stock_table.column("sid", width=70)
        #self.stock_table.column("sbid", width=70)
        self.stock_table.column("sbg", width=80)
        self.stock_table.column("status", width=90)
        self.stock_table.column("quantity", width=70)
        self.stock_table.column("hname", width=250)
        self.stock_table.column("hadd", width=250)
        self.stock_table.column("hphn", width=110)

        self.stock_table.pack(fill=BOTH, expand=1)
        self.stock_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def search_data(self):
        sercon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sercon.cursor()

        cur.execute(
            "select * from stock where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_here.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert('', END, values=row)
            sercon.commit()
        sercon.close()

    def save(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sqlcon.cursor()
        cur.execute("insert into stock values(%s,%s,%s,%s,%s,%s,%s)", (
            self.sid.get(),
            #self.bid.get(),
            self.sbg.get(),
            self.status.get(),
            self.quantity.get(),
            self.hname.get(),
            self.hadd.get(),
            self.hphn.get()
        ))

        sqlcon.commit()
        self.fetch_data()
        self.clear()
        sqlcon.close()

    def fetch_data(self):
        felcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = felcon.cursor()
        cur.execute("Select * from stock")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert('', END, values=row)
            felcon.commit()
        felcon.close()

    def clear(self):
        self.sid.set("")
        #self.sbid.set("")
        self.sbg.set("")
        self.status.set("")
        self.quantity.set("")
        self.hname.set("")
        self.hadd.set("")
        self.hphn.set("")

    def get_cursor(self, ev):
        cursor_row = self.stock_table.focus()
        contents = self.stock_table.item(cursor_row)
        row = contents['values']

        self.sid.set(row[0])
        #self.sbid.set(row[1])
        self.sbg.set(row[1])
        self.status.set(row[2])
        self.quantity.set(row[3])
        self.hname.set(row[4])
        self.hadd.set(row[5])
        self.hphn.set(row[6])

    def delete_Blood(self):
        delcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = delcon.cursor()
        cur.execute("delete from stock where Stock_id=%s", self.sid.get())

        delcon.commit()
        delcon.close()
        self.fetch_data()
        self.clear()

    def update_data(self):
        updcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = updcon.cursor()
        cur.execute("update stock set Blood_Group=%s,Stock_status=%s,Stock_Quantity=%s,Hospital_Name=%s,Hospital_Address=%s,Hospital_Phone=%s where Stock_id=%s",(

            #self.sbid.get(),
            self.sbg.get(),
            self.status.get(),
            self.quantity.get(),
            self.hname.get(),
            self.hadd.get(),
            self.hphn.get(),
            self.sid.get()


        ))

        updcon.commit()
        self.fetch_data()
        self.clear()
        updcon.close()


root = Tk()
ss = bbms(root)
root.mainloop()