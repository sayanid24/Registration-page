from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Face_Recognition_Based_Attendance_System Register")
        self.root.geometry("1600x900+0+0")

#____________ bg img____________

        self.bg=ImageTk.PhotoImage(file=r"E:\Final yr pr. doc\white-cube-pattern-4k-bu-1920x1080.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


#____________ box____________

        frame=Frame(self.root,bg="white",bd=10,relief=RIDGE)
        frame.place(x=140,y= 100,width=1080,height=550)

#____________ left img____________

        self.bg1= ImageTk.PhotoImage(file=r"E:\Final yr pr. doc\Untitled-1-01-1024x573.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=150,y= 100,width=440,height=545)

#______________main box___________

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="brown",bg="white")
        register_lbl.place(x=20,y=20)


# _______________enrty______________

#_____________________________________row1__________________

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250 )
        l_name=Label(frame,text="Last Name ",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

#______________________________________________row2_____________________

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

#______________________________row3________________________________________

        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_securiy_Q=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="randomly")
        self.combo_securiy_Q ["values"]=("Select","Your Birth Place","Your Favorite Color","Your Pet Name")
        self.combo_securiy_Q.place(x=50,y=270,width=250)
        self.combo_securiy_Q.current(0)

        security_A =Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

#__________________________________row4__________________________________

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

#__________________________terms&condition btn___________________________

        checkbtn=Checkbutton(frame,text="I Agree All The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

#______________________________________________button____________________________

        img=Image.open(r"E:\Final yr pr. doc\regff.jpg")
        img=img.resize((190,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=30,y=440,width=200)


        img1=Image.open(r"E:\Final yr pr. doc\loginff.jpg")
        img1=img1.resize((190,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=420,y=440,width=190)



if __name__=="__main__":
    root=Tk()
    web=Register(root)
    root.mainloop()