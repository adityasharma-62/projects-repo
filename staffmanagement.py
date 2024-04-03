from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
            self.root=root
            self.root.title("Mall staff manage ")
            self.root.geometry("1550x800+0+0")

            self.bg=ImageTk.PhotoImage(file=r"C:\Users\adity\Downloads\pexels-pixabay-414102.jpg")
            bg_lbl=Label(self.root,image=self.bg)
            bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

            self.var_email=StringVar()
            self.var_pass=StringVar()

            frame=Frame(self.root,bg='white')
            frame.place(x=500,y=130,width=340,height=450)

            img=Image.open(r"C:\Users\adity\Downloads\filelogin.png")
            img=img.resize((100,100),Image.ANTIALIAS)
            self.photoimage1=ImageTk.PhotoImage(img)
            imglbl=Label(image=self.photoimage1,bg="white",borderwidth=0)
            imglbl.place(x=550,y=135)

            get_str=Label(frame,text="Let's",font=("times new roman",20,"bold"),fg="black",bg="white")
            get_str.place(x=170,y=30) 
            get_str=Label(frame,text="Start",font=("times new roman",20,"bold"),fg="black",bg="white")
            get_str.place(x=190,y=60)

            username=lb1=Label(frame,text="User email",font=("times new roman",15,"bold"),fg="black",bg="white")
            username.place(x=40,y=120)
            self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
            self.txtuser.place(x=30,y=150,width=270)

            password=lb2=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
            password.place(x=40,y=183)
            self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
            self.txtpass.place(x=30,y=214,width=270)

            loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="blue",command=self.login)
            loginbtn.place(x=100,y=255,width=120,height=35)

            registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("Arial",12,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
            registerbtn.place(x=15,y=300,width=160)

            forgetpassbtn=Button(frame,text="Forgot Password",command=self.forget_window,font=("Arial",12,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
            forgetpassbtn.place(x=15,y=325,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def forget_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","enter email")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
            my_cursor=conn.cursor()
            querry=("select * from admin where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(querry,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","email is not valid!")
            else:
                self.new_window1=Toplevel(self.root)
                self.app1=Forget(self.new_window1)

    
    
        

    def login(self):


        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","both field required")
        elif  self.txtuser.get()=="aditya" and self.txtpass.get()=="9369":
               messagebox.showinfo("success","Welcome to the Mall Management")
               
               
        else :
            conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from admin where email=%s and password=%s",(
                                                                            self.var_email.get(),
                                                                            self.var_pass.get()

                                                                                         ))
            row=my_cursor.fetchone()
            if row == None :
                messagebox.showerror('Error','Invalid user email OR password')
            else:
                open_main=messagebox.askyesno('YesNo','Access only Admin')
                if open_main >0:
                    self.new_window2=Toplevel(self.root)
                    self.app2=Staff(self.new_window2)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


class Register:
    def __init__(self,root):
            self.root=root
            self.root.title("Registration window ")
            self.root.geometry("1550x800+0+0")


            self.var_fname=StringVar()
            self.var_mname=StringVar()
            self.var_lname=StringVar()
            self.var_contact=IntVar()
            self.var_email=StringVar() 
            self.var_security1=StringVar()
            self.var_password=StringVar()
            self.var_cpassword=StringVar()
            self.var_security=StringVar()
            self.var_check=IntVar()


            self.bg=ImageTk.PhotoImage(file=r"C:\Users\adity\Downloads\pexels-pixabay-414102.jpg")
            bg_lbl=Label(self.root,image=self.bg)
            bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

            

            frame = Frame(self.root,bg="white",border=20)
            frame.place(x=300,y=75,width=800,height=550)
            
            register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",30,"bold"),fg="black",bg="white")
            register_lbl.place(x=20,y=20)

            fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
            fname.place(x=20,y=80)
            fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Arial",15,"bold"))
            fname_entry.place(x=20,y=120)

            mname=Label(frame,text="Middle Name",font=("times new roman",20,"bold"),bg="white")
            mname.place(x=250,y=80)
            mname_entry=ttk.Entry(frame,textvariable=self.var_mname,font=("Arial",15,"bold"))
            mname_entry.place(x=250,y=120)

            lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="white")
            lname.place(x=480,y=80)
            lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Arial",15,"bold"))
            lname_entry.place(x=480,y=120)

            contact=Label(frame,text="Contact Number",font=("times new roman",20,"bold"),bg="white")
            contact.place(x=20,y=170)
            contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("Arial",15,"bold"))
            contact_entry.place(x=20,y=210)

            email=Label(frame,text="Email",font=("times new roman",20,"bold"),bg="white")
            email.place(x=380,y=170)
            email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Arial",15,"bold"))
            email_entry.place(x=380,y=210)


            security=Label(frame,text="Security Question",font=("times new roman",20,"bold"),bg="white")
            security.place(x=20,y=260)

            self.combo_security=ttk.Combobox(frame,textvariable=self.var_security,font=("Arial",15,"bold"),state="readonly")
            self.combo_security["values"]=("Select","Your birth","Your crush","Your pet")
            self.combo_security.place(x=20,y=300,width=250)
            self.combo_security.current(0)

            security1=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="white")
            security1.place(x=380,y=260)
            security1_entry=ttk.Entry(frame,textvariable=self.var_security1,font=("Arial",15,"bold"))
            security1_entry.place(x=380,y=300)

            password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
            password.place(x=20,y=350)
            password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("Arial",15,"bold"))
            password_entry.place(x=20,y=390)

            cpassword=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
            cpassword.place(x=380,y=350)
            cpassword_entry=ttk.Entry(frame,textvariable=self.var_cpassword,font=("Arial",15,"bold"))
            cpassword_entry.place(x=380,y=390)

            checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the term and conditions",font=("Arial",15,"bold"),onvalue=1,offvalue=0)
            checkbtn.place(x=25,y=440)

            img=Image.open(r"C:\Users\adity\Downloads\logoregister.jpg")
            img=img.resize((200,50),Image.ANTIALIAS)
            self.photoimage=ImageTk.PhotoImage(img)
            b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",bg="white",activebackground="white",command=self.register_data)
            b1.place(x=380,y=445,width=300)

           

    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select":
                
                messagebox.showerror("Error","Required All fields",parent=self.root)
                
            elif self.var_password.get()!=self.var_cpassword.get():
                messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree to the terms and conditions",parent=self.root)
            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
                my_cursor=conn.cursor()
                querry=("select * from admin where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(querry,value)
                row=my_cursor.fetchone()
                if row != None:
                    messagebox.showinfo("Error","email already exist")
                else:
                    my_cursor.execute("insert into admin(fname,mname,lname,contact,email,securityQ,secuA,password) values(%s,%s,%s,%s,%s,%s,%s,%s)" , (
                                                                                           self.var_fname.get(),
                                                                                           self.var_mname.get(),
                                                                                           self.var_lname.get(),
                                                                                           self.var_contact.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_security.get(),
                                                                                           self.var_security1.get(),
                                                                                           self.var_password.get()
                                                                                           
                                                                                          
                    
                    
                    
                                                                                                                      ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registration Success")

class Forget:
    def forgot(self):
            
            if self.var_fsecurity1.get()=="":
                messagebox.showerror("Error","Required All fields",parent=self.root)
            elif self.var_newpass1.get()=="":
                messagebox.showerror("error","enter new password",parent=self.root)
            else :
                
                conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
                my_cursor=conn.cursor()
                querry=("select * from admin where email=%s and secuA=%s")
                value=(self.var_email.get(),self.var_fsecurity1.get())
                my_cursor.execute(querry,value)
                row=my_cursor.fetchall()
                print(row)
                print(row[0][6])
                
                
                if row[0][6] != self.var_fsecurity1.get():
                    messagebox.showerror("error","wrong answer")
                else:
                    my_cursor.execute("update admin set password=%s where email=%s",(self.var_newpass1.get(),self.var_email.get()))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","password Changed")
    def __init__(self,root):
            self.root=root
            self.root.title("Forget window ")
            self.root.geometry("1550x800+0+0")

            self.var_email=StringVar()
            self.var_newpass1=StringVar()
            self.var_fsecurity1=StringVar()

            self.bg=ImageTk.PhotoImage(file=r"C:\Users\adity\Downloads\pexels-pixabay-414102.jpg")
            bg_lb2=Label(self.root,image=self.bg)
            bg_lb2.place(x=0,y=0,relwidth=1,relheight=1)

            frame = Frame(self.root,bg="white",border=20)
            frame.place(x=475,y=50,width=400,height=600)

            


            forget_lbl=Label(frame,text="Forgot",font=("times new roman",30,"bold"),fg="black",bg="white")
            forget_lbl.place(x=50,y=20)
            forget_lb2=Label(frame,text="Password",font=("times new roman",30,"bold"),fg="black",bg="white")
            forget_lb2.place(x=190,y=60)

            femail=Label(frame,text="Enter em@il",font=("times new roman",20,"bold"),bg="white")
            femail.place(x=20,y=150)
            femail_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Arial",15,"bold"))
            femail_entry.place(x=20,y=190)

            fsecurity=Label(frame,text="Security Question",font=("times new roman",20,"bold"),bg="white")
            fsecurity.place(x=20,y=230)

            self.combo_security=ttk.Combobox(frame,font=("Arial",15,"bold"),state="readonly")
            self.combo_security["values"]=("Select","Your birth","Your crush","Your pet name")
            self.combo_security.place(x=20,y=270,width=250)
            self.combo_security.current(0)

            fsecurity1=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="white")
            fsecurity1.place(x=20,y=310)
            fsecurity1_entry=ttk.Entry(frame,textvariable=self.var_fsecurity1,font=("Arial",15,"bold"))
            fsecurity1_entry.place(x=20,y=350)

            newpass=Label(frame,text="New Password",font=("times new roman",20,"bold"),bg="white")
            newpass.place(x=20,y=390)
            newpass1_entry=ttk.Entry(frame,textvariable=self.var_newpass1, font=("Arial",15,"bold"))
            newpass1_entry.place(x=20,y=430)

            img=Image.open(r"C:\Users\adity\Downloads\reset.jpg")
            img=img.resize((130,50),Image.ANTIALIAS)
            self.photoimage=ImageTk.PhotoImage(img)
            b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",bg="white",activebackground="white",command=self.forgot)
            b1.place(x=85,y=485)

class Staff:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Staff Management System")

        # variables

        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_sal=StringVar()
        self.var_email=StringVar()
        self.var_add=StringVar()
        self.var_marr=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_id=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_contry=StringVar()
        self.var_desig=StringVar()


        lbl_title=Label(self.root,text="STAFF MANAGEMENT",font=("times new roman",37,"bold"),fg="black",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)

        img_logo=Image.open(r"C:\Users\adity\Downloads\pngstaff.png")   
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=430,y=0,width=50,height=50) 
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=50,width=1360,height=160)
        # 1st
        img_logo1=Image.open(r"C:\Users\adity\Downloads\1st.webp")   
        img_logo1=img_logo1.resize((300,160),Image.ANTIALIAS)
        self.photo_logo1=ImageTk.PhotoImage(img_logo1)

        self.logo1=Label(img_frame,image=self.photo_logo1)
        self.logo1.place(x=0,y=0,width=300,height=160) 
        #2nd
        img_logo2=Image.open(r"C:\Users\adity\Downloads\2nd.webp")   
        img_logo2=img_logo2.resize((300,160),Image.ANTIALIAS)
        self.photo_logo2=ImageTk.PhotoImage(img_logo2)

        self.logo2=Label(img_frame,image=self.photo_logo2)
        self.logo2.place(x=300,y=0,width=300,height=160) 
        #3rd
        img_logo3=Image.open(r"C:\Users\adity\Downloads\3rd.webp")   
        img_logo3=img_logo3.resize((300,160),Image.ANTIALIAS)
        self.photo_logo3=ImageTk.PhotoImage(img_logo3)

        self.logo3=Label(img_frame,image=self.photo_logo3,borderwidth=0)
        self.logo3.place(x=600,y=0,width=300,height=160) 

        #4th
        img_logo4=Image.open(r"C:\Users\adity\Downloads\4th.jpg")   
        img_logo4=img_logo4.resize((300,160),Image.ANTIALIAS)
        self.photo_logo4=ImageTk.PhotoImage(img_logo4)

        self.logo4=Label(img_frame,image=self.photo_logo4,borderwidth=0)
        self.logo4.place(x=900,y=0,width=300,height=160) 

        #5th
        img_logo5=Image.open(r"C:\Users\adity\Downloads\5rd.jpg")   
        img_logo5=img_logo5.resize((300,160),Image.ANTIALIAS)
        self.photo_logo5=ImageTk.PhotoImage(img_logo5)

        self.logo5=Label(img_frame,image=self.photo_logo5,borderwidth=0)
        self.logo5.place(x=1200,y=0,width=300,height=160)

        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=10,y=225,width=1345,height=462)

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text='Staff Information',font=("times new roman",11,"bold"),fg="red")
        upper_frame.place(x=10,y=5,width=1320,height=230)


        lbl_dep=Label(upper_frame,text='Department',font=("Arial",11,"bold"),fg="black",bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department',"Fashion",'Electronics',"Appliances","Grocery","Beauty Product","Gaming","Food & items","others")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        lbl_Name=Label(upper_frame,text='Name :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_Nmae=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("Arial",11,"bold"))
        txt_Nmae.grid(row=0,column=3,padx=2,pady=7)

        lbl_phone=Label(upper_frame,text='Phone no :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("Arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        lbl_desig=Label(upper_frame,text='Designation :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_desig.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_desig,width=22,font=("Arial",11,"bold"))
        txt_desig.grid(row=1,column=1,padx=2,pady=7)

        lbl_email=Label(upper_frame,text='Email :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("Arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        lbl_loc=Label(upper_frame,text='Country :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_loc.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_loc=ttk.Entry(upper_frame,textvariable=self.var_contry,width=22,font=("Arial",11,"bold"))
        txt_loc.grid(row=1,column=5,padx=2,pady=7)

        lbl_add=Label(upper_frame,text='Address :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_add.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_add=ttk.Entry(upper_frame,textvariable=self.var_add,width=22,font=("Arial",11,"bold"))
        txt_add.grid(row=2,column=1,padx=2,pady=7)

        lbl_married=Label(upper_frame,text='Married status :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_married.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        combo_married=ttk.Combobox(upper_frame,textvariable=self.var_marr,font=('arial',12,'bold'),width=17,state='readonly')
        combo_married['value']=('Married',"Unmarried")
        combo_married.current(0)
        combo_married.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        lbl_Salary=Label(upper_frame,text='Salary (CTC) :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_Salary.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_Salary=ttk.Entry(upper_frame,textvariable=self.var_sal,width=22,font=("Arial",11,"bold"))
        txt_Salary.grid(row=2,column=5,padx=2,pady=7)

        lbl_dob=Label(upper_frame,text='DOB :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("Arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        lbl_doj=Label(upper_frame,text='DOJ :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("Arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        combo_id=ttk.Combobox(upper_frame,textvariable=self.var_id,font=('arial',12,'bold'),width=17,state='readonly')
        combo_id['value']=('Select ID Proof',"Aadhar","PAN Card","DL")
        combo_id.current(0)
        combo_id.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        txt_id=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("Arial",11,"bold"))
        txt_id.grid(row=4,column=1,padx=2,pady=7)

        lbl_sex=Label(upper_frame,text='Gender :',font=("Arial",12,"bold"),fg="black",bg='white')
        lbl_sex.grid(row=4,column=2,padx=2,pady=7,sticky=W)


        combo_sex=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_sex['value']=('Male',"Female","Others")
        combo_sex.current(0)
        combo_sex.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        img_mask=Image.open(r"C:\Users\adity\Downloads\mask.jpeg")   
        img_mask=img_mask.resize((200,220),Image.ANTIALIAS)
        self.photo_mask=ImageTk.PhotoImage(img_mask)

        self.mask=Label(upper_frame,image=self.photo_mask)
        self.mask.place(x=990,y=0,width=200,height=220) 

        btnadd=Button(upper_frame,text="Save",command=self.add_data,font=("Arial",12,"bold"),borderwidth=2,fg="white",bg="blue",activeforeground="black",activebackground="green")
        btnadd.place(x=1205,y=10,width=100)

        btnupdate=Button(upper_frame,command=self.update_data,text="Update",font=("Arial",12,"bold"),borderwidth=2,fg="white",bg="blue",activeforeground="black",activebackground="green")
        btnupdate.place(x=1205,y=60,width=100)

        btndel=Button(upper_frame,command=self.delete_data,text="Delete",font=("Arial",12,"bold"),borderwidth=2,fg="white",bg="blue",activeforeground="black",activebackground="green")
        btndel.place(x=1205,y=130,width=100)

        btnclear=Button(upper_frame,command=self.reset,text="Clear",font=("Arial",12,"bold"),borderwidth=2,fg="white",bg="blue",activeforeground="black",activebackground="green")
        btnclear.place(x=1205,y=180,width=100)


        lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text=' Table',font=("times new roman",11,"bold"),fg="red")
        lower_frame.place(x=10,y=240,width=1320,height=210)

        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg="white",text='search info.',font=("times new roman",11,"bold"),fg="red")
        search_frame.place(x=5,y=0,width=1300,height=60)

        lbl_search=Label(search_frame,text='Search By :',font=("Arial",12,"bold"),fg="white",bg='green')
        lbl_search.grid(row=0,column=0,padx=5,pady=7,sticky=W)

        self.var_com_search=StringVar()

        combo_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=17,state='readonly')
        combo_search['value']=('Select option',"Phone","ID_proof")
        combo_search.current(0)
        combo_search.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("Arial",11,"bold"))
        txt_search.grid(row=0,column=3,padx=2,pady=7)

        btnsearch=Button(search_frame,command=self.search_data,text="Search",font=("Arial",12,"bold"),borderwidth=2,fg="white",bg="blue",activeforeground="black",activebackground="green",width=14)
        btnsearch.grid(row=0,column=4,padx=10)

        btnshow=Button(search_frame,text="Show All",command=self.fetch_data,font=("Arial",12,"bold"),borderwidth=2,fg="white",bg="blue",activeforeground="black",activebackground="green",width=14)
        btnshow.grid(row=0,column=5,padx=5)

        # staff table

        table_frame=Frame(lower_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=60,width=1300,height=125)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.emp_table=ttk.Treeview(table_frame,column=('dep','name','email','add','marr','dob','doj','id','desig','idproof','gender','phone','contry','sal'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)



        self.emp_table.heading('dep',text='Department')
        self.emp_table.heading('name',text='Name')
        self.emp_table.heading('sal',text='Salary')
        self.emp_table.heading('email',text='Email')
        self.emp_table.heading('add',text='Address')
        self.emp_table.heading('marr',text='status ')
        self.emp_table.heading('dob',text='birth date')
        self.emp_table.heading('doj',text='joining date')
        self.emp_table.heading('id',text='idproof')
        self.emp_table.heading('idproof',text='ID Number')
        self.emp_table.heading('gender',text='Gender')
        self.emp_table.heading('phone',text='Contact')
        self.emp_table.heading('contry',text='country')
        self.emp_table.heading('desig',text='designation')


        self.emp_table["show"]="headings"
        
        self.emp_table.column('dep',width=100)
        self.emp_table.column('name',width=100)
        self.emp_table.column('sal',width=100)
        

        self.emp_table.pack(fill=BOTH,expand=1)
        self.emp_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()



    def add_data(self):
        if self.var_dep.get() =="" :
            messagebox.showerror('Error','All field Required',parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into staff(Department,Name,Salary,Email,Address,Married_status,DOB,DOJ,ID,ID_proof,Gender,Phone,Country,Designation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                        self.var_dep.get(),
                                                                        self.var_name.get(),
                                                                        self.var_sal.get(),
                                                                        self.var_email.get(),
                                                                        self.var_add.get(),
                                                                        self.var_marr.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_doj.get(),
                                                                        self.var_id.get(),
                                                                        self.var_idproof.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_contry.get(),
                                                                        self.var_desig.get()









                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('succes','staff added !',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from staff ")
        data=my_cursor.fetchall()
        if len(data)!=0:
         self.emp_table.delete(*self.emp_table.get_children())
         for i in data:
            self.emp_table.insert("",END,values=i)
         conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.emp_table.focus()
        content=self.emp_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_sal.set(data[13])
        self.var_email.set(data[2])
        self.var_add.set(data[3])
        self.var_marr.set(data[4])
        self.var_dob.set(data[5])
        self.var_doj.set(data[6])
        self.var_id.set(data[7])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_contry.set(data[12])
        self.var_desig.set(data[8])

    def update_data(self):
        if self.var_dep.get() =="" or self.var_name.get()=="" :
            messagebox.showerror('Error','All field Required',parent=self.root)

        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update data',parent=self.root)

                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update staff set Department=%s,Name=%s,Salary=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,ID=%s,Gender=%s,Phone=%s,Country=%s,Designation=%s where ID_proof=%s',(
                                                                        self.var_dep.get(),
                                                                        self.var_name.get(),
                                                                        self.var_sal.get(),
                                                                        self.var_email.get(),
                                                                        self.var_add.get(),
                                                                        self.var_marr.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_doj.get(),
                                                                        self.var_id.get(),
                                                                        
                                                                        self.var_gender.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_contry.get(),
                                                                        self.var_desig.get(),
                                                                        self.var_idproof.get()
                                                                                                ))

                else:
                    if not update:
                      return

                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo('success','staff info updated!',parent=self.root)
            except Exception as es :
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)

    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror("Error","select id for delete",parent=self.root)

        else:
            try:

                delete=messagebox.askyesno('Deletion','Are you sure!',parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
                    my_cursor=conn.cursor()
                    sql='delete from staff where ID_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo('Deleted','staff deleted',parent=self.root)
            except Exception as es :
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)   

    def reset(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_sal.set("")
        self.var_email.set("")
        self.var_add.set("")
        self.var_marr.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_id.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_contry.set("")
        self.var_desig.set("")

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("error","please select option")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='nehaadi',database='staff_info')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from staff where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                
                rows=my_cursor.fetchall()
                if len(rows) != 0:
                    self.emp_table.delete(*self.emp_table.get_children())
                    for i in rows:
                        self.emp_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except EXCEPTION as es:
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)


if __name__ == "__main__":
    main()
