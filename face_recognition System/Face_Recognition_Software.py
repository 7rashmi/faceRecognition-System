from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")
        
        #self.bg=ImageTk.PhotoImage(file=r"college_images\D:\face_recognition System\login.jpg")
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        img=Image.open("college_images\artificial.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img)
        bg_lbl=Label(self.root,image=self.photoimg)
        bg_lbl.place(x=0,y=0,width=1530,height=800)
        
        title=Label(bg_lbl,text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=120,width=1550,height=45)
        
        #===================Project button (description)=============
        #downtitle=Label(self.root,text="Note:Enter valid username and valid password",font("times new roman",15,"bold"))
        #downtitle.place(x=0,y=740,width=1600,height=35)
        
        myname=Label(self.root,text="Developed by Rashmi Kanyal",fg="black",bg="white",font=("times new roman",15,"bold"))
        myname.place(x=0,y=0)
        
        img10=Image.open(r"college_images\sdetials.jpg")
        img10=img10.resize((500,120),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        f_lbl=Label(bg_lbl,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=500,height=120)
        
        img11=Image.open(r"college_images\facialrecognition.jpg")
        img11=img11.resize((500,120),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        f_lbl=Label(bg_lbl,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=120)
        
        img12=Image.open(r"college_images\sdetials.jpg")
        img12=img12.resize((500,120),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        f_lbl=Label(bg_lbl,image=self.photoimg_left)
        f_lbl.place(x=1000,y=0,width=500,height=120)  

        
        frame=frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=450)
        
        img1=Image.open(r"college_images\D:\face_recognition System\icon.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #===========================img icon===========
        img2=Image.open(r"college_images\D:\face_recognition System\login1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"college_images\D:\face_recognition System\password.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        # login button
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white" ,activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #register button
        registerbtn=Button(frame,command=self.register_Window  ,text="New User Register",font=("times new roman",10,"bold"),bd=3,borderwidth=0 ,fg="white",bg="black",activeforeground="white" ,activebackground="red")
        registerbtn.place(x=15,y=350,width=160)
        
        #forgetpass
        forgetbtn =Button(frame,command=self.forget_password_window
                          ,text="Forget Password",font=("times new roman",10,"bold"),bd=3,borderwidth=0 ,fg="white",bg="black",activeforeground="white" ,activebackground="red")
        forgetbtn.place(x=10,y=370,width=160)
        
        def register_window(self):
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)
        
        def login(self):
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error","all field required")
            elif self.txtuser.get()=="kapu" and self.txtpass.get()=="adhu":
                messagebox.shoeinfo("Success" "Welcome ")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("selec* from register where email=%s and password=%s",(
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.gery()
                                                                                       ))
                row=my_cursor.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password")
                else:
                    open_main=messagebox.askyesno("YesNo","Access only Authority Person")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
                
        #================================reset password===============
        def reset_pass(self):
            if self.combo_securityQ.get()=="Select":
                messagebox.showerror("Error","Select security Question",parent=self.root2)
            elif self.txt_securityA.get()=="":
                messagebox.showerror("Error","Please enter the Answer",parent=self.root2)
            elif self.txt_newpass.get()=="":
                messagebox.showerror("Error","Please enter the new password",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("select* from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_securityQ.get(),self.txt_securityA.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                if row==None:
                    messagebox.showerror(" Error","Please enter correct Answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value(self.txt_newpass.get(),self.txtuser.get())
                    my_cursor.execute(query,value)
                    
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                    self.root2.destroy()
                
        #=================================forget password==========================       
        def forget_password_window(self):
            if self.txtuser.get()=="":
                messagebox.showerror("Error","Please Enter the Email address to reset password")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("select* from register where email=%s")
                value=(self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                if row==None:
                    messagebox.showerror("My Error","Please enter the valid user name")
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2geometry("340x450+610+170")
                    
                    l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                    l.place(x=0,y=10,relwidth=1)
                    
                    security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="blakc")
                    security_Q.place(x=50,y=80)
        
                    self.combo_security_Q=ttk.Combobox(self.root2,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
                    self.combo_ssecurity_Q["values"]=("Select","Your Birth Place","Your Fvrt Colour","Your Pet Name")
                    self.combo_security_Q.place(x=50,y=110,width=250)
                    self.combo_security_Q.current(0)
        
        
                    security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                    security_A.place(x=50,y=150)
        
                    self.txt_security=ttk.Entry(self.root2,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
                    self.txt_security.place(x=50,y=180,width=250)
                    
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                    new_password.place(x=50,y=220)
                    
                    self.txt_newpass=ttk.Entry(self.root2,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
                    self.txt_newpass.place(x=50,y=250,width=250)
                    
                    btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                    btn.place(x=100,y=200)
                    
                    
        
                    
                                   
                
                
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Login")
        
        #===================variables=======================
        self.var_fname.get()
        self.var_lname.get()
        self.var_contact.get()
        self.var_email.get()
        self.var_securityQ.get()
        self.var_securityA.get()
        self.var_pass.get()
        self.var_confpass.get()
        
        
                
        #======================background image===================
        self.bg=ImageTk.PhotoImage(file=r"college_images\D:\face_recognition System\login.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #=================left img==============
        self.bg1=ImageTk.PhotoImage(file=r"college_images\D:\face_recognition System\background.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        #==================main frame=========
        frame=frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label (frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #====================label & entry===========
        
        #=========row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
         
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #===================row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #=================row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="blakc")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_ssecurity_Q["values"]=("Select","Your Birth Place","Your Fvrt Colour","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #======================row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310) 
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250) 
        
        #=======================checkbutton============
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)
        
        #=====================buttons=============
        img=Image.open(r"D:\face_recognition System\college_images\register.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)      
        
        img1=Image.open(r"D:\face_recognition System\college_images\now.jpg")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,compound=self.return_login,command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)   
        
        
        #=====================function declaration==============
        def register_data(self):
            if self.var_fname.get()==""or self.vae_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password & Confirm Password must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Pl4ease agree our term & condition")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("select*from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                            self.var_pass.get()
                                                                                          ))
                conn.commit()
                conn.close()
                messagebox.showerror("Success","Register Successfully")    
                
        def return_login(self):
            self.root.destroy()   
    
if __name__ == " __main__ ":
    main()