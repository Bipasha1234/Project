
from tkinter import *
from tkinter import messagebox ,ttk
from PIL import ImageTk,Image
import ast
window= Tk()
window.geometry('1250x1000')
window.title("Learners")
window.configure(bg='#E2C5ED')
window.minsize(width=900,height=600)   
window.maxsize(width=1600,height=1000)

imgpath = 'Rectangle 1.png'
img = PhotoImage(file=imgpath)
img = img.zoom(33) #with 250, I ended up running out of memory
img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel = Label(window, image = img)

Label(window,image=img,bg='#E2C5ED').place(x=10,y=55)

# Main___Frame
frame=Frame(window,width=320,height=390,bg='#F3EEE5')
frame.place(x=835,y=195)

heading=Label(text="Learners",fg="red",bg='#E2C5ED',font=('Ink Free',70,'bold'))
heading.place(x=500,y=-5)


details=Label(frame,text="Your Hub for learning",font=("Calibiri",18,"bold"),bg='#F3EEE5',fg="black").place(x=29,y=26)

# UserName                                            

username=Label(frame,text="Username",font=('Inter Normal',14),bg='#F3EEE5',fg="black").place(x=25,y=80)
username_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0).place(x=30,y=120)

# username_______image
imgpath_1 = 'Group.png'
Username_image = PhotoImage(file=imgpath_1)
Username_image = Username_image.zoom(29) #with 250, I ended up running out of memory
Username_image = Username_image.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel_1 = Label(window, image = Username_image,bg='#F3EEE5')

Label(window,image=Username_image,bg='#F3EEE5').place(x=952,y=280)

# Password

password=Label(frame,text="Password",font=("Inter Normal",14),bg='#F3EEE5',fg="black").place(x=25,y=160)
password_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0).place(x=30,y=199)

# password____Image
imgpath_2 = 'ABC.png'
password_image = PhotoImage(file=imgpath_2)
password_image = password_image.zoom(30) #with 250, I ended up running out of memory
password_image = password_image.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel_1 = Label(window, image = password_image,bg='#F3EEE5')

Label(window,image=password_image,bg='#F3EEE5').place(x=952,y=356)


def signup():
    window=Toplevel()
    window.title("Sign Up")
    window.maxsize(width=1290,height=1000)
    window.minsize(width=900,height=600)
    window.config(bg='#F3EEE5')
    window.focus_force()
    window.grab_set()

    frame_2=Frame(window,width=500,height=583,bg='#E2C5ED')
    frame_2.place(x=80,y=68)

    text=Label(frame_2,text="CREATE YOUR ACCOUNT",fg='#4F1D63',bg='#E2C5ED',font=('Calibri',29,'bold'))
    text.place(x=60,y=35)

    def on_enter_1(e):
        x=user_1.get()
        if x=='  First Name':
            user_1.delete(0,'end')
    def on_leave_1(e):
        if user_1.get()=='':
         user_1.insert(0,'  First Name')

    user_1=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_1.place(x=80,y=110)
    user_1.insert(0,'  First Name')
    user_1.bind("<FocusIn>",on_enter_1)
    user_1.bind("<FocusOut>",on_leave_1)

    # Frame(frame_2,width=285,height=2,bg='black').place(x=15,y=130)


# Frame(frame,width=295,height=2,bg='black').place(x=15,y=192)

    def on_enter_1(e):
        x=user_2.get()
        if x=='  Last Name':
            user_2.delete(0,'end')
    def on_leave_1(e):
        if user_2.get()=='':
         user_2.insert(0,'  Last Name')

    user_2=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_2.place(x=80,y=155)
    user_2.insert(0,'  Last Name')
    user_2.bind("<FocusIn>",on_enter_1)
    user_2.bind("<FocusOut>",on_leave_1)
    
    gender=Label(frame_2,text="Gender",fg='black',bg='#E2C5ED',font=('Inter Normal',15))
    gender.place(x=85,y=200)

    var=IntVar()
    ca=Checkbutton(window,text=("Male"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var)
    ca.place(x=240,y=265)
    var_1=IntVar
    ca_1=Checkbutton(window,text=("Female"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_1)
    ca_1.place(x=309,y=265)
    var_2=IntVar
    ca_2=Checkbutton(window,text=("Others"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_2)
    ca_2.place(x=399,y=265)
    
    def on_enter_1(e):
        user_3.delete(0,'end')
    def on_leave_1(e):
        if user_2.get()=='':
         user_3.insert(0,' Year')

    user_3=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
    user_3.place(x=95,y=276)
    user_3.insert(0,' Year')
    user_3.bind("<FocusIn>",on_enter_1)
    user_3.bind("<FocusOut>",on_leave_1)
    
    dob=Label(frame_2,text="Date of Birth",font=('Inter Normal',15),bg='#E2C5ED',fg="black")
    dob.place(x=85,y=237)

    DOBimage=PhotoImage(file='DOB.png')
    DOBimage= DOBimage.zoom(17) #with 250, I ended up running out of memory
    DOBimage = DOBimage.subsample(20)
    imageofdob=Label(window,image=DOBimage,bg='#E2C5ED')
    imageofdob.place(x=282,y=304)
    
    

    def on_enter_1(e):
        user_4.delete(0,'end')
    def on_leave_1(e):
        if user_4.get()=='':
         user_4.insert(0,' Month')

    user_4=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=6)
    user_4.place(x=170,y=276)
    user_4.insert(0,' Month')
    user_4.bind("<FocusIn>",on_enter_1)
    user_4.bind("<FocusOut>",on_leave_1)

    def on_enter_1(e):
        user_5.delete(0,'end')
    def on_leave_1(e):
        if user_5.get()=='':
         user_5.insert(0,' Date')

    user_5=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
    user_5.place(x=248,y=276)
    user_5.insert(0,' Date')
    user_5.bind("<FocusIn>",on_enter_1)
    user_5.bind("<FocusOut>",on_leave_1)
    

    def on_enter_1(e):
        x=user_6.get()
        if x=='  Username':
            user_6.delete(0,'end')
        
    def on_leave_1(e):
        if user_6.get()=='':
         user_6.insert(0,'  Username')

    
    user_6=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_6.place(x=75,y=360)
    user_6.insert(0,'  Username')
    user_6.bind("<FocusIn>",on_enter_1)
    user_6.bind("<FocusOut>",on_leave_1)
    

    hi=Label(frame_2,text="Type",width=15,bg="#E2C5ED",font=("Inter Normal",16))
    hi.place(x=20,y=316)
    user7_var=StringVar(value='  Student')
    user7_combobox=ttk.Combobox(frame_2,values=['Teacher','Student'],font=('Inter Normal',15),width=8, textvariable=user7_var)
    user7_combobox.place(x=158,y=316)
    

    def on_enter_1(e):
        x=user_7.get()
        if x=='  New Password':
            user_7.delete(0,'end')
    def on_leave_1(e):
        if user_7.get()=='':
         user_7.insert(0,'  New Password')

    
    user_7=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_7.place(x=75,y=404)
    user_7.insert(0,'  New Password')
    user_7.bind("<FocusIn>",on_enter_1)
    user_7.bind("<FocusOut>",on_leave_1)
    
    def on_enter_1(e):
        x=user_8.get()
        if x=='  Confirm Password':
            user_8.delete(0,'end')
    def on_leave_1(e):
        if user_8.get()=='':
         user_8.insert(0,'  Confirm Password')

    
    user_8=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_8.place(x=75,y=449)
    user_8.insert(0,'  Confirm Password')
    user_8.bind("<FocusIn>",on_enter_1)
    user_8.bind("<FocusOut>",on_leave_1)

    button_register=Button(frame_2,pady=3,width=8,height=-9,border=0,text="Register",bg="#AE08ED",fg="White",font=("Inter Normal",16))
    button_register.place(x=200,y=495)



# Photo__Of__Signup__window

    
    image_2=PhotoImage(file='Rectangle 6.png')
    image_2=image_2.zoom(30) #with 250, I ended up running out of memory
    image_2=image_2.subsample(32) #mechanically, here it is adjusted to 32 instead of 320

    why=Label(window,image=image_2,bg="#F3EEE5")
    why.place(x=720,y=115)
    Label(window,image=image_2,command=signup)


label=Label(frame,text="Don't have an account?",fg='black',bg='#F3EEE5',font=('Inter Normal',14),   padx=20,pady=20)
label.place(x=45,y=280)
sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
sign_in.place(x=125,y=323) 

def home_page():
    
    window=Toplevel()
    window.title("Home Page")
    window.maxsize(width=1290,height=1000)
    window.minsize(width=900,height=600)
    window.config(bg='white')
    window.focus_force()
    window.grab_set()


    frame_home=Frame(window,width=1280,height=66,bg="#BE63D9")
    frame_home.place(x=0,y=0)

    

    learners=Label(frame_home,text="Learners",font=("Ink Free",24,'bold'),bg="#BE63D9",fg="#221C35")
    learners.place(x=8,y=20)

    # image1= PhotoImage(file='p.png')
    # panel_4 = Label(window,image = image1)
    # panel_4.place(x=10,y=5)
    # # Label(window,image=image1)
        
    # image2= PhotoImage(file='math.png')
    # image3= PhotoImage(file='Software.png')
    # frame=Frame(window,bg="white")
    # frame.pack(pady=100)
    # button1=Button(frame,image=image1,bg='#FFF1F0',width=300,height=377)
    # button1.grid(row=2,column=1)
    # button2=Button(frame,image=image2,bg='#FFF1F0',width=300,height=377)
    # button2.grid(row=2,column=2,padx=60,pady=30)
    # button3=Button(frame,image=image3,bg='#FFF1F0',width=300,height=377)
    # button3.grid(row=2,column=3)

     
    # prog_text=Label(button1,text="Programming and Algorithms",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
    # prog_text.place(x=470,y=330)
    # prog_text_1=Label(button1,text="This subject explains various",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    # prog_text_1.place(x=470,y=360)
    # prog_text_2=Label(window,text="concepts of programming and",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    # prog_text_2.place(x=470,y=400)
    # prog_text_3=Label(window,text="algorithms",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    # prog_text_3.place(x=470,y=440)


    # Label(window,image=img_4)

         # # frame of math part
    frame_math=Button(window,width=44,height=25,bg="#FFF1F0",activebackground="#FFF1F0")
    frame_math.place(x=100,y=175)
       
    m_text=Label(window,text="Mathematics",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
    m_text.place(x=170,y=401)
   
    m_text_1=Label(window,text="This subject teaches about",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    m_text_1.place(x=115,y=440)
    m_text_2=Label(window,text="ways of combining maths with",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    m_text_2.place(x=115,y=470)
    m_text_3=Label(window,text="programming",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    m_text_3.place(x=115,y=499)

    imgpath_6 = 'p.png'
    img_6 = PhotoImage(file=imgpath_6)
    img_6= img_6.zoom(19) #with 250, I ended up running out of memory
    img_6 = img_6.subsample(20)
    panel_6 = Label(window,image = img_6,bg="#FFF1F0")
    panel_6.place(x=100,y=180)

    frame_sd=Button(window,width=44,height=25,bg="#FFF1F0",activebackground="#FFF1F0")
    frame_sd.place(x=870,y=170)

    sd_text1=Label(window,text="Software Design",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
    sd_text1.place(x=931,y=397)
    
    sd_text2=Label(window,text="This subject explains about the",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    sd_text2.place(x=884,y=435)
    sd_text3=Label(window,text="principles of designing a ",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    sd_text3.place(x=884,y=465)
    sd_text4=Label(window,text="software and best practices",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    sd_text4.place(x=884,y=495)

    imgpath_5 = 'Software.png'
    img_5 = PhotoImage(file=imgpath_5)
    img_5= img_5.zoom(19) #with 250, I ended up running out of memory
    img_5 = img_5.subsample(20) #mechanically, here it is adjusted to 32 instead of 320
    panel_5 = Label(window,image = img_5,bg="#FFF1F0")
    panel_5.place(x=889,y=171)

    


    frame_prog=Button(window,width=44,height=25,bg="#FFF1F0",activebackground="#FFF1F0")
    frame_prog.place(x=485,y=172)
        
        
    
    prog_text=Label(window,text="Programming and Algorithms",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
    prog_text.place(x=495,y=400)
    
    prog_text_1=Label(window,text="This subject explains various",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    prog_text_1.place(x=501,y=440)
    prog_text_2=Label(window,text="concepts of programming and",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    prog_text_2.place(x=501,y=470)
    prog_text_3=Label(window,text="algorithms",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    prog_text_3.place(x=501,y=500)

    imgpath_4 = 'math.png'
    img_4 = PhotoImage(file=imgpath_4)
    img_4= img_4.zoom(20) #with 250, I ended up running out of memory
    img_4 = img_4.subsample(21) #mechanically, here it is adjusted to 32 instead of 320
    panel_4 = Label(window,image = img_4,bg="#FFF1F0")
    panel_4.place(x=492,y=173)

    #     # frame of software design
    
    
    

    def onbutton1(e):
        subj['bg']='#E2C5ED'
    def leavebutton1(e):
        subj['bg']="#BE63D9"
        
    subj=Button(frame_home,text="Subjects",font=('Inter Normal',20),bg='#BE63D9',fg="black",bd=0)
    subj.place(x=360,y=20)

    # bind methods
    subj.bind('<Enter>',onbutton1)
    subj.bind('<Leave>',leavebutton1)
    labell=Label(frame_home,text=None,font=10)
    labell.place(x=3,y=30)
    

    def onbutton3(e):
        Button2['bg']='#E2C5ED'
    def leavebutton3(e):
        Button2['bg']="#BE63D9"
    Button2=Button(frame_home,text="Tickets",font=('Inter Normal',20),bg="#BE63D9",fg="black",bd=0)
    Button2.place(x=627,y=20)

    # bind methods
    Button2.bind('<Enter>',onbutton3)
    Button2.bind('<Leave>',leavebutton3)
    labell2=Label(frame_home,text=None,font=10)
    labell2.place(x=3,y=30)

    def onbutton3(e):
        Button3['bg']='#E2C5ED'
    def leavebutton3(e):
        Button3['bg']="#BE63D9"
        
    Button3=Button(frame_home,text="Notices",font=('Inter Normal',20),bg="#BE63D9",fg="black",bd=0)
    Button3.place(x=905,y=20)

    # bind methods
    Button3.bind('<Enter>',onbutton3)
    Button3.bind('<Leave>',leavebutton3)
    labell3=Label(frame_home,text=None,font=10)
    labell3.place(x=3,y=30)


# yo eroor ayepaxi balla photo visible bhayoo
    def onbutton(e):
             Button1['bg']='#E2C5ED'
    def leavebutton(e):
             Button1['bg']="#BE63D9"
        
    Button1=Button(frame_home,text="Subjects",font=('Inter Normal',20),bg='white',fg="black",bd=0,command=subject)
    Button1.place(x=360,y=20)
 

log_in=Button(frame,width=9,pady=3,text="Log in",bg="#2586DA",fg="White",border=0,font=('Calibri',13),command=home_page)
log_in.place(x=113,y=242)

    
window.mainloop()
    

        # frame of programming
    
    # def subject():



# image1= PhotoImage(file='p.png')
# image2= PhotoImage(file='math.png')
# image3= PhotoImage(file='math.png')
# frame=Frame(window,)
# frame.pack(pady=100)
# button1=Button(frame,image=image1,bg='black')
# button1.grid(row=0,column=0)
# button2=Button(frame,image=image2,bg='black')
# button2.grid(row=0,column=1,padx=30)
# button3=Button(frame,image=image3,bg='black')
# button3.grid(row=0,column=2)
# window.mainloop()