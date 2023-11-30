#import the modules required......
from tkinter import *
from PIL import Image, ImageTk
from time import *
import datetime
from tkinter import messagebox
import mysql.connector as mysql
from tkinter import ttk
from tkcalendar import *
import pyautogui
import os
import errno
import pyqrcode
import winsound
from imutils.video import VideoStream
import imutils
import cv2
import pyzbar.pyzbar as pyzbar
from AdminData import AdminData
import pyttsx3
import TrainImage
from Appraisal import Appraisal
from employeeEmail import employeeEmail
import csv
from tkinter import filedialog

##################################### creating the main class......
 #text to speech
engine=pyttsx3.init()
#Using female voice
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#rate voice
rate=engine.getProperty('rate')
engine.setProperty('rate',127)

def speak_va(transcribe_query) :
           engine.say(transcribe_query)
           engine.runAndWait()

def main():
       global window
       window=Tk() #calling the main window
       ob=Login(window) #calling the first class and everything inside it
       window.mainloop() #displaying the window

class Login:
    def __init__(self,window):
        self.window=window
        self.appwidth=1366
        self.appheight=768
        self.screenwidth=self.window.winfo_screenwidth()
        self.screenheight=self.window.winfo_screenheight()
        self.x=(self.screenwidth/2)-(self.appwidth/2) 
        self.y=(self.screenheight/2)-(self.appheight/2)
        self.window.geometry(f'{self.appwidth}x{self.appheight}+{int(self.x)}+{int(self.y)}')
        self.icon=PhotoImage(file="yabatech-logo.png")
        self.window.iconphoto(True,self.icon)
        self.window.title('Employee Attendance System')

        #hide main window and show splashscreen
        self.window.withdraw()  
        self.splashScreen()

    
##################################### call the login page ####################################
    def splashScreen(self):
                x=pyautogui.size()[0]
                y=pyautogui.size()[1]
                self.splash=Toplevel()
                self.splash.geometry('900x400+'+str(int(x/2-450))+'+'+str(int(y/2-200)))
                self.splashImage=Image.open('.//Untitled Export//SplashImage.png')
                self.res=self.splashImage.resize((1100,450), Image.ANTIALIAS)
                self.newSplash=ImageTk.PhotoImage(self.res)
                self.LabelSplash=Label(self.splash, image=self.newSplash).pack(fill='both', expand=TRUE)
                self.splash.overrideredirect(True)
                self.splash.after(5000, self.loginform)

################################## define the login page ####################################
    def loginform(self):
        #update the main window 
        self.window.update()
        #show the main window along with the specified window to open
        self.window.deiconify()

########## the below frame shows that this frame will be thesame in all the windows shown linked to the main class window #####
        frm1=Frame(self.window, bg='white', relief='flat' )
        frm1.place(x=0, y=0, height=768, width=1366)

##################### this will also be shown on all the windows linked to the main class window ####################
        lbl=Label(frm1, text='ADMIN PAGE', font=('Arial bold', 18),fg='yellow', bg='green')
        lbl.pack(fill='both',ipady=8)

#################### using the enter button to move to the next window on the main class window ########################################
        self.window.bind("<Return>", self.loginVerification)
        
############################## the date to be displayed on the windows linked to the class window ####################
        datef=Label(self.window, text=day+"-" +mont[month]+"-"+year+"   | ", fg='green', bg='white', font=('Tempus Sans ITC',12, 'bold') )
        datef.place(x=540,y=88)

############################### the time to be dispayed on the windows linked to the main class window ##############################
        self.clock=Label(self.window, fg='green',bg='white', font=('Tempus Sans ITC',12, 'bold'))
        self.clock.place(x=710,y=88)
        self.tick()

########################## resize yabatech logo to be displayed on the body of windows linked to the main class window ##############################
        self.img1=Image.open('yabatech-logo.png')
        self.resize=self.img1.resize((150,150), Image.ANTIALIAS)
        self.newz=ImageTk.PhotoImage(self.resize)

        self.emoj=Image.open('.//Untitled Export//Attendance connection.png')
        self.ress=self.emoj.resize((220,150), Image.ANTIALIAS)
        self.newEmoj=ImageTk.PhotoImage(self.ress)

        self.imgicon=Image.open('.//Untitled Export//Admin image.png')
        self.resizeicon=self.imgicon.resize((40,40), Image.ANTIALIAS)
        self.newicon=ImageTk.PhotoImage(self.resizeicon)

##################### display the yabatech logo to be displayed on the windows linked to the main class window ##########
        self.labImage=Label(self.window, image=self.newz, bg='white').place(x=200, y=300)
        self.labImage=self.newz 
        
        self.labEmoj=Label(self.window, image=self.newEmoj, bg='white').place(x=1000, y=290)
        self.labEmoj=self.newEmoj 
        
########################### login frame to be displayed on the main class window ##############################
        frm=Frame(self.window, bg='green', relief='flat', )
        frm.place(x=485, y=200, height=350, width=400)

########################### Labels, buttons and entry boxes to be displayed on the login frame ##############################
        forgetpassword=Button(frm, text='forgot password?', bg='green', fg='yellow',relief='flat', activebackground='green', 
        activeforeground='green', font=('calibri italic', 11), command=self.confirm, bd=0)
        forgetpassword.pack(pady=(5,3), anchor='ne', padx=(0,4))

        self.labicon=Label(frm, image=self.newicon, bg='green').pack(pady=(0))
        self.labicon=self.newicon

        label2=Label(frm, text='Username', font=('Goudy old style bold', 18),fg='yellow', bg='green')
        label2.pack(pady=(0,6))
        self.e2=Entry(frm,width=40, font=('times new roman', 14), fg='black',relief='flat')
        self.e2.pack(anchor='nw',pady=(5,15),padx=30, ipady=3)

        Label5=Label(frm, text='Password', font=('Goudy old style bold', 18),fg='yellow', bg='green')
        Label5.pack(pady=(5,6))
        self.e5=Entry(frm,width=40, font=('times new roman', 14), fg='black',relief='flat', show='*')
        self.e5.pack(anchor='nw',padx=30, ipady=3)

        btn_submit=Button(frm, text='Login', bg='white', activebackground='white',font=('times new roman', 11)
        , relief='flat', bd=0, width=10, command= self.loginVerification )
        btn_submit.pack(pady=(30,0),)

        btn_submit2=Button(frm, text='Not Registered? Register', bg='green', fg='yellow',relief='flat', activebackground='green', 
        activeforeground='green', font=('calibri italic', 11), command=self.register, bd=0)
        btn_submit2.pack(pady=5, side='top')
       
############################ function to specify what the login button should do ###########################
    def loginVerification(self, event):
        if self.e2.get()=='' or self.e5.get()=='':
            messagebox.showerror('Error', 'All fields are required', parent=self.window)
        else:
            try: #link the app to database
                connect=mysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='employee_attendance')
                cursor=connect.cursor() #allows you to manipulate the data on the database
                cursor.execute("SELECT * FROM admin WHERE username=%s and password=%s", (self.e2.get(), self.e5.get(), ))
                row=cursor.fetchone() #allows you to grab a data on the row of a table on your database
                if row==None:
                     messagebox.showerror('Error', 'Invalid Username and Password', parent=self.window)
                     self.ClearLogin() #a function call to clear the login entry box
                     self.e2.focus() #a function call to 
                else:  
                    self.User_TimeIN()
                    speak_va("WELCOME admin"+self.e2.get())   
                    self.appscreen() #a function call to move to another class window screen
                   
                    connect.close()  #a function call to close the database connection
            except Exception as es:
                 messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window) #function that displays technical error related to the database connection
                 self.ClearLogin()

######################## This Automatically update the last login of the employee on the database ########################### 
    def User_TimeIN(self):
              ts=time()
              self.date=datetime.datetime.now().fromtimestamp(ts).strftime('%Y:%m:%d %H:%M:%S')
              connect=mysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("UPDATE admin SET Last_login=%s WHERE username=%s" , (self.date, self.e2.get(),))
              connect.commit()
              connect.close()
   
    def confirm(self):
               self.app_screen=Toplevel(self.window)
               self.app=AdminData(self.app_screen)
    
                
############################ function indicating the display of the register page when the register button is clicked ###########################
    def register(self):

########################### Register frame to be displayed on the main class window ########################### 
        frm=Frame(self.window, bg='yellow', relief='flat')
        frm.place(x=450, y=200, height=450, width=500)

########################## Labels, buttons and entry boxes to be displayed on the Register frame ##############################
        label21=Label(frm, text='Register Here', font=('impact',20, 'bold'),fg='green', bg='yellow')
        label21.place(x=30, y=20 )

        label=Label(frm, text='Username', font=('Goudy old style bold', 15),fg='green', bg='yellow')
        label.place(x=30, y=110)
        self.e1=Entry(frm,width=20, font=('time new roman', 12), fg='black',relief='flat')
        self.e1.place(x=30, y=145)

        Label2=Label(frm, text='Secret Key', font=('Goudy old style bold', 15),fg='green', bg='yellow')
        Label2.place(x=300, y=110)
        self.e21=Entry(frm,width=20, font=('time new roman', 12), fg='black',relief='flat')
        self.e21.place(x=300, y=145)

        Label3=Label(frm, text='Department', font=('Goudy old style bold', 15),fg='green', bg='yellow')
        Label3.place(x=30, y=200)
        self.e3=ttk.Combobox(frm,width=18, font=('time new roman', 12))
        self.e3['values']=self.combosa_input()
        self.e3.place(x=30, y=235)

        Label4=Label(frm, text='Designation', font=('Goudy old style bold', 15),fg='green', bg='yellow')
        Label4.place(x=300, y=200)
        self.e4=Entry(frm,width=20, font=('time new roman', 12), fg='black',relief='flat')
        self.e4.place(x=300, y=235)

        label5=Label(frm, text='Password', font=('Goudy old style bold', 15),fg='green', bg='yellow')
        label5.place(x=30, y=290)
        self.e51=Entry(frm,width=20, font=('time new roman', 12), fg='black',relief='flat')
        self.e51.place(x=30, y=325)

        Label6=Label(frm, text='Confirm Password', font=('Goudy old style bold', 15),fg='green', bg='yellow')
        Label6.place(x=300, y=290)
        self.e6=Entry(frm,width=20, font=('time new roman', 12), fg='black',relief='flat')
        self.e6.place(x=300, y=325)

        btn_submit3=Button(frm, text='Register', bg='white', activebackground='white',command=self.RegisterVerification,font=('times new roman', 11), bd=0, width=12, )
        btn_submit3.place(x=210, y=380)

        btn_submit4=Button(frm, text='Registered Already? Login', bg='yellow', fg='green',relief='flat', activebackground='yellow',
        activeforeground='green', font=('calibri italic', 11), command=self.loginform, bd=0 )
        btn_submit4.place(x=175, y=410)
        self.window.bind("<Return>", self.RegisterVerification)
        
############################ function to specify what the registration button should do ###########################
    def RegisterVerification(self,event):
        if  self.e51.get()!= self.e6.get():
             messagebox.showerror('Error', 'Password and confirm Password should be same', parent=self.window)
        elif self.e1.get()=='' or self.e21.get()=='' or self.e3.get()=='' or self.e4.get()=='' or self.e51.get()=='' or self.e6.get()=='':
             messagebox.showerror('Error', 'All fields are required', parent=self.window)
        else:
            try:
                connect=mysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM admin WHERE Admin_id =%s", (self.e21.get(),) )
                row=cursor.fetchone()
                if row!=None:
                     messagebox.showerror('Error', 'User already Exist, please try with another Email', parent=self.window)
                     self.ClearReg() #call the clear function to clear the entry box after message pops up
                     self.e21.focus()
                else:
                    cursor.execute("INSERT INTO admin(Admin_id, username, department, position, password, confirm_password,Secret_key) VALUES(%s,%s,%s,%s,%s,%s,%s)", 
                                                                                   ("",
                                                                                    self.e1.get(), 
                                                                                    self.e3.get(), 
                                                                                    self.e4.get(),
                                                                                    self.e51.get(), 
                                                                                    self.e6.get(),
                                                                                    self.e21.get()))
                    connect.commit()
                    connect.close()
                    speak_va('Admin has been registered successfully.')
                    messagebox.showinfo('Success', 'Register successful', parent=self.window)
                    self.ClearReg() #call the clear function after message
            except Exception as es:
                 messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

 ############################# function to pick department from department management ############################      
    def combosa_input(self):
                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM department")
                data=[]
                for rows in cursor.fetchall():
                        data.append(rows[1])
                return data

############################# function to display the new window called ############################
    def appscreen(self):  
        admin_user=self.e2.get() #Username to be called in new class 
        self.app_screen=Toplevel(self.window)
        self.app=attendance(self.app_screen,admin_user)
        self.window.withdraw()
      
############################# function to clear entry boxes found in the login frame page ############################
    def ClearLogin(self):
        self.e2.delete(0, END)
        self.e5.delete(0,END)

############################# function to clear the entry boxes found in the register frame page ############################
    def ClearReg(self):
        self.e21.delete(0, END)
        self.e1.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e51.delete(0, END) 
        self.e6.delete(0, END)

############################# function to use when a calling the time to the screen ############################
    def tick(self):
        time=strftime('%I:%M:%S  %p')
        self.clock.config(text=time)
        self.clock.after(200,self.tick)

####################### description of what the date should look like when called to be displayed on the screen ############################
ts=time()
date=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year=date.split('-')
mont={'01':'january', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July',
'08':'August', '09':'September', '10':'October', '11':'November', '12':'December',
}


###################################### New page #######################################
class attendance(Login):
    def __init__(self,window,admin_user):
        self.window=window
        self.appwidth=1366
        self.appheight=768
        self.userA=admin_user #username variable assigned to another variable
        self.screenwidth=self.window.winfo_screenwidth()
        self.screenheight=self.window.winfo_screenheight()
        self.x=(self.screenwidth/2)-(self.appwidth/2) 
        self.y=(self.screenheight/2)-(self.appheight/2)
        self.window.geometry(f'{self.appwidth}x{self.appheight}+{int(self.x)}+{int(self.y)}')
        self.icon=PhotoImage(file='yabatech-logo.png')
        self.window.iconphoto(True,self.icon)
        self.window.title('Employee Attendance System')

 ###################################### Frame to show on top of the main window ####################################################################################
        
        Mainfrm4=Frame(self.window)
        Mainfrm4.place(x=0, y=0, height=768, width=1366)

  ##################################### Text to be shown on top the frame  #####################################################################################      
        lbl=Label( Mainfrm4, font=('Arial bold', 13), bg='#286b12', )
        lbl.pack(fill='both',ipady=12)
       
        self.name20= 'EMPLOYEE ATTENDANCE USING FACE RECOGNITION AND BARCODE'
        self.count=0
        self.text=""
        self.lbl=Label( Mainfrm4, text=self.name20, font=('Arial bold', 13),fg='white', bg='#286b12' )
        self.lbl.place(x=100, y=13)
        self.designer()

 ##################################### Date to be dispayed on the windows linked to the class window #####################################################################################
        datef=Label(Mainfrm4, text=day+"-" +mont[month]+"-"+year+"   |  ", fg='yellow', bg='#286b12', font=('Tempus Sans ITC',12, 'bold') )
        datef.place(x=1050,y=13)

#t############################# The time to be dispayed on the windows linked to the class window ###########################
        self.clock=Label(Mainfrm4, fg='yellow',bg='#286b12', font=('Tempus Sans ITC',12, 'bold'))
        self.clock.place(x=1220,y=13)
        self.tick()

 ############################### Yaba Resized image to be displayed on the windows linked to the class window ###########################################################################################   
        self.img1=Image.open('yabatech-logo.png')
        self.resize=self.img1.resize((60,50), Image.ANTIALIAS)
        self.new=ImageTk.PhotoImage(self.resize)

####################### display the yabatech logo to be displayed on the windows linked to the class window #########################
        self.labImage=Label(Mainfrm4, image=self.new, bg='#286b12').place(x=10, y=0)
        self.labImage=self.new 

 ####################### creating a green background where the date, logo and the project title will be ##################################################################################################        
        PageFrame=Frame(Mainfrm4, bg='green',bd=4)
        PageFrame.pack(fill='both' )

 ########################################## general Accessbar button ################################################################################       
        Dashboardbutton= Button(  PageFrame, text='Dashboard', font=('times new roman', 11, 'bold'), relief='flat',bg='yellow', bd=0,
         width=20, height=2, command=self.app_screen)
        Dashboardbutton.grid(column=0, row=0, padx=(5,0), pady=0)

        Departmentbutton=Button(  PageFrame, text='Department Management',font=('times new roman', 11, 'bold'), relief='flat',
          height=2,width=20,bg='yellow', bd=0, command=self.manageDept)
        Departmentbutton.grid(column=1,row=0, padx=(8,8))

        EmployeeButton=Button(  PageFrame, text='Employee Management',font=('times new roman', 11, 'bold'), relief='flat',bg='yellow', 
        bd=0, height=2, width=20, command=self.manageEmployee)
        EmployeeButton.grid(column=2, row=0, padx=(0,8))

        TakeAttendanceButton=Button(  PageFrame, text='Take Attendance',font=('times new roman', 11, 'bold'), relief='flat',bg='yellow', 
        bd=0, height=2,width=20, command=self.take_attendance)
        TakeAttendanceButton.grid(column=3, row=0, padx=(0,8))

        ViewAttendanceButton=Button(  PageFrame, text='View Attendance',font=('times new roman', 11, 'bold'), relief='flat',bg='yellow', 
        bd=0, width=20, height=2, command=self.view_attendance)
        ViewAttendanceButton.grid(column=4, row=0, padx=(0,8))

        LogoutButton=Button(  PageFrame, text='Log out',font=('times new roman', 11, 'bold'), relief='flat',bg='yellow', bd=0,
          height=2,width=20,command=self.logout)
        LogoutButton.grid(column=5, row=0, padx=(0,8 ))

        ExitButton=Button(  PageFrame, text='Exit',font=('times new roman', 11, 'bold'), relief='flat',bg='yellow', bd=0
        , height=2, width=20, command=self.Exit)
        ExitButton.grid(column=6, row=0, padx=(0,5))

       ###### Call the dashboard to be dispayed ####
        self.app_screen()

########################################## Call for dashboard ##############################################
    def  designer(self):
           try:
              if self.count>len(self.name20):
                     self.count=0
                     self.text=""
                     self.lbl.config(text=self.text)
                     
              else:
                     self.text=self.text+self.name20[self.count]
                     self.lbl.config(text=self.text)
                     self.count+=1
           except IndexError:
                  pass
           self.lbl.after(50,self.designer)
                  
########################################## MANAGE DEPARTMENT ############################################################
    def manageDept(self):

########################################## frame for department Entries ##############################
              CoverFrame=Frame(self.window, bg='white')
              CoverFrame.place(x=0, y=100, height=768, width=1366,anchor='nw')

########################################## code to diaplay Useful info on screen ##############################
              status=Label(self.window, text='Double click the record on the treeview to delete or update your record', 
               relief=FLAT,anchor=SE)
              status.place(y=720, x=800)

              frm2=Frame(self.window, bg='yellow')
              frm2.place(x=230, y=230, height=350, width=900)

#################################### image to be displayed on the created canvas ##############################
              self.bg=ImageTk.PhotoImage(Image.open('.//Untitled Export//background-1740107_1920.jpg'))

################################# a canvas that will allow placement of a transparent label ##############################
              canvas=Canvas(frm2, width=900, height=350)
              canvas.place(x=0, y=0, anchor='nw')

################################## placing the image on the canvas ##############################
              canvas.create_image(0,0, image=self.bg, anchor='nw')

############################### text label to be shown on the created canvas #########################
              canvas.create_text( 152,50, text='Enter Department:', font=('Open Sans SemiBold', 16, 'bold'),fill='black')
              canvas.create_text( 154,225, text='Search Department:', font=('Open Sans SemiBold', 16,'bold'),fill='black')
                            
################################ Search entryboxes and buttons #########################
              self.SearchEntry=Entry(frm2,width=28, font=('times new roman', 14), fg='black',relief='flat',  borderwidth=5)
              self.SearchEntry_window= canvas.create_window(195,270, window= self.SearchEntry)

              self.Searchbutton= Button(frm2, text='search', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=7,
              command=self.Search)
              self.Searchbutton_window= canvas.create_window(150,310, window= self.Searchbutton)

              self.clearSearchbutton= Button(frm2, text='clear', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=7,
              command=self.clearSearch)
              self.clearSearchbutton_win= canvas.create_window(225,310, window=self.clearSearchbutton)

################################ Department entryboxes and buttons #########################
              self.departmentEntry=Entry(frm2,width=28, font=('times new roman', 14), fg='black',relief='flat', borderwidth=5)
              self.departmentEntry_win= canvas.create_window(195,95, window=self.departmentEntry)
              
              self.addbutton= Button(frm2, text='Add', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=9,
              command=self.add)
              self.addbutton_win= canvas.create_window(100,160, window=self.addbutton)

              self.deletebutton=Button(frm2, text='Delete',font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=9, 
              command=self.delete)
              self.deletebutton_win= canvas.create_window(195,160, window=self.deletebutton)
              
              self.updateButton=Button(frm2, text='Update',font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=9,
              command=self.update)
              self.updateButton_win= canvas.create_window(290,160, window=self.updateButton)
              
              self.Clearbutton=Button(frm2, text='Clear',font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=9, 
              command=self.deleteall)
              self.Clearbutton_win= canvas.create_window(385,160, window= self.Clearbutton)
              

       ######################################## Styling treeview ################################################################################
              self.styling=ttk.Style()
              self.styling.theme_use('default')
              self.styling.configure('Treeview', background='white', foreground='white', fieldbackground='white' )
              self.styling.configure('Treeview.Heading', font=('Calibri', 11, 'bold'), background='yellow', foreground='black')
              self.styling.map('Treeview', background=[('selected', 'green')])
              
       ######################################### Treeview creation #################################################################################
              self.listboxscrollbar=Scrollbar(self.window, orient=VERTICAL)
              self.listboxscrollbar1=Scrollbar(self.window, orient=HORIZONTAL)
              self.trv1=ttk.Treeview(self.window, selectmode='extended', yscrollcommand=self.listboxscrollbar.set,
               xscrollcommand=self.listboxscrollbar1.set)
              self.trv1['columns']=('Dept ID', 'department')

               ################################ adding scrollbar to treeview ###############################
              self.listboxscrollbar.config(command=self.trv1.yview)
              self.listboxscrollbar.place(x=1105, y=250,height=298)

              self.listboxscrollbar1.config(command=self.trv1.xview)
              self.listboxscrollbar1.place(x=706, y=548,width=416,)

               ################################ adding columns to treeview.. ###############################
              self.trv1.column('#0', width=0, stretch=FALSE)
              self.trv1.column('Dept ID', width=15, anchor='c')
              self.trv1.column('department', width=80, anchor='c')

               ################################ adding headings for each columns in the treeview ###############################
              self.trv1.heading('Dept ID',text='Dept ID' , anchor='c')
              self.trv1.heading('department',text='DEPARTMENT', anchor='c')

               ################################ packing the treeview ###############################
              self.trv1.place( x=705, y=250,height=298, width=400)

 ################################ function to display the treeview as styled and updated on the screen ###############################             
              self.show1()

 ################################ function to initiate a mouse command when you double click ###############################
              self.trv1.bind("<Double-1>", self.select_record1)

 ################################ creating a variable and declaring the type of variable ###############################
              self.search=StringVar()
              
 ################################### function to describe time to be displayed on the class window frame #######################################################################################     
    def tick(self):
              time=strftime('%I:%M:%S  %p')
              self.clock.config(text=time)
              self.clock.after(200,self.tick)

################## Function to search for record on the treeview and database then display the record on treeview ######################
    def Search(self):
              self.addbutton.config(state=ACTIVE, bg='yellow')
              self.search= self.SearchEntry.get()
              if self.search=='':
                     messagebox.showerror('Error', 'All fields are required', parent=self.window)
              else:
                     try:
                            for rows in self.trv1.get_children():
                                   self.trv1.delete(rows)

                            self.trv1.tag_configure('oddrow', background='#c9c9c9')
                            self.trv1.tag_configure('evenrow', background='white')
                            connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                            cursor=connect.cursor()
                            cursor.execute("SELECT * FROM department WHERE department LIKE %s",(self.SearchEntry.get(),))
                            row=cursor.fetchall()
                            count=1
                            if len(row)!=0:
                                   self.trv1.delete(*self.trv1.get_children())
                            for rows in row:
                                   if count%2==0:
                                          self.trv1.insert(parent="", index='end', text='' ,iid=count, values=(rows), tags=('oddrow',))
                                   else:
                                          self.trv1.insert(parent="", index='end', text='' , iid=count, values=(rows), tags=('evenrow',))
                                   count+= 1
                            connect.commit()
                            connect.close()
                                               
                     except Exception as es:
                            messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

################## Function to clear search for record on the treeview then display all record on treeview ######################
    def clearSearch(self):
              self.addbutton.config(state=ACTIVE, bg='yellow')
              connect=mysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("SELECT * FROM department")
              rows=cursor.fetchall()
              connect.commit()
              connect.close()
              self.trv1.delete(*self.trv1.get_children())
              self.show1()
              self.SearchEntry.delete(0, END) 

################## Function to add record to database then display the record on treeview and database ######################
    def add(self):
              if self.departmentEntry.get()=='':
                     messagebox.showerror('Error', 'All fields are required', parent=self.window)
              else: 
                     try:
                            connect=mysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='employee_attendance')
                            cursor=connect.cursor()
                            cursor.execute("SELECT * FROM department WHERE department=%s", (self.departmentEntry.get(),) )
                            row=cursor.fetchone()
                            if row!=None:
                                   messagebox.showerror('Error', 'Department already Exist, please try with another department ', parent=self.window)
                                   self.ClearDept() #call the clear function to clear the entry box after message pops up      

                            else:
                                   cursor.execute("INSERT INTO department(id,department) VALUES(%s,%s)", ("",self.departmentEntry.get(),))
                                   connect.commit()
                                   connect.close()
                                   self.trv1.delete(*self.trv1.get_children())
                                   self.show1()
                                   speak_va("Department successfully added")
                                   messagebox.showinfo('Success', 'Department successfully Added', parent=self.window)
                                   self.departmentEntry.delete(0, END)  #call the clear function after message

                     except Exception as es:
                            speak_va('An Exception Error!')
                            messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

 ############################## Function to Delete one or many record  from treeview and database ################################################################################ 
    def delete(self):
                            try:
                                   response= messagebox.askyesno('Delete department', 'are you sure you want to delete this department')
                                   if response==1:
                                          #point to selection on treeview
                                          x=self.trv1.selection()
                                          #create list of ids
                                          ids_to_delete=[]
                                          #add selction to id_to_delete list
                                          for row in x:
                                                 ids_to_delete.append(self.trv1.item(row, 'values')[0])
                                          #delete from treeview
                                          for row in x:
                                                 self.trv1.delete(row)
                                          speak_va('Department Successfully deleted')
                                          messagebox.showinfo('Success', 'Delete successful', parent=self.window)
                                   else:
                                          return True
                                   
                                   self.departmentEntry.delete(0, END)  #call the clear function after message
                                   connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
                                   cursor=connect.cursor()
                                   cursor.execute("SELECT * FROM department" )
                                   row=cursor.fetchall()
                                   #Delete everything from the table
                                   cursor.executemany("DELETE FROM department WHERE id=%s", ([(a,) for a in ids_to_delete]))
                                   connect.commit()
                                   connect.close()

                            except Exception as es:
                                   messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

############################## Function to clear all record from department entry and search entry #######################################
    def deleteall(self):
           self.addbutton.config(state=ACTIVE, bg='yellow')
           self.departmentEntry.delete(0, END) 

################################### function to update record on treeview and database #################################################################################### 
    def update(self): 
               self.addbutton.config(state=ACTIVE, bg='yellow')  
               if  self.departmentEntry.get()=="":
                               messagebox.showerror('Error', 'All fields are required', parent=self.window)
               else: 
                            try:
                                   connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
                                   cursor=connect.cursor()
                                   cursor.execute("SELECT * FROM department WHERE department=%s", (self.departmentEntry.get(),) )
                                   row=cursor.fetchone()
                                   if row!=None:
                                          messagebox.showerror('Error', 'Department already Exist, please try with another department ', parent=self.window)
                                          self.departmentEntry.delete(0, END) #call the clear function to clear the entry box after message pops up
              
                                   else:  
                                          self.depart=self.departmentEntry
                                          selected=self.trv1.focus()
                                          values=self.trv1.item(selected,'values')
                                          self.trv1.item(selected,values=(values[0],self.depart.get()))
                                          cursor.execute("UPDATE department SET department=%s WHERE id=%s", (self.departmentEntry.get(),values[0],))
                                          connect.commit()
                                          connect.close()
                                          messagebox.showinfo('Success', 'Department successfully Updated', parent=self.window)
                                          self.departmentEntry.delete(0, END)  #call the clear function after message

                            except Exception as es:
                                   messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

############################## Function to show record on treeview #######################################
    def show1(self):
              self.trv1.tag_configure('oddrow', background='#c9c9c9')
              self.trv1.tag_configure('evenrow', background='white')
              connect=mysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("SELECT * FROM department" )
              row=cursor.fetchall()
              count=1
              if len(row)!=0:
                     self.trv1.delete(*self.trv1.get_children())
                     for rows in row:
                            if count%2==0:
                                   self.trv1.insert(parent="", index='end', text='' ,iid=count, values=(rows), tags=('oddrow',))
                            else:
                                   self.trv1.insert(parent="", index='end', text='' , iid=count, values=(rows), tags=('evenrow',))
                            count+= 1
              connect.commit()
              connect.close()
 
#################### Function to select record from the treeview when we double click into insert them to the department entry box ##################
    def select_record1(self,event):
              self.addbutton.config(state=DISABLED)
              self.depart=self.departmentEntry
              self.departmentEntry.delete(0, END)
              selected=self.trv1.identify_row(event.y)
              values=self.trv1.item(selected,'values')
              self.depart.insert(0,values[1])
              
 ################################################# MANAGE EMPLOYEES ######################################################################### 
    def manageEmployee(self):
        frameBody11=Frame(self.window)
        frameBody11.place(x=0, y=100, height=768, width=1366)

########################################## background picture for frame  #########################################################

        self.img2=Image.open('.//Untitled Export//background-1177469_1920.jpg')
        self.resize1=self.img2.resize((1366,768), Image.ANTIALIAS)
        self.new1=ImageTk.PhotoImage(self.resize1)

        self.labImage1=Label(frameBody11, image=self.new1,).grid(sticky='nw')
        self.labImage1=self.new1 

################################## Subframes for register and treeview ############################################################
        frameBody=Frame(frameBody11, bg='white')
        frameBody1=Frame(frameBody11, bg='white')
       
        frameBody.place(width= 1348,height=328,x=10, y=10)
        frameBody1.place(width= 1348,height=295,x=10, y=344)
        
        for i in range(6):
                frameBody.grid_columnconfigure(3, weight=1)
        for j in range(8):
                         frameBody.grid_rowconfigure(8, weight=1)
               
##########################################Employee frame entry and buttons############################################################       
        self.name1=Label(frameBody, text='Department:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name1.grid(column=0, row=0, sticky='w', padx=10, pady=(10,5))
        self.name1Entry=ttk.Combobox(frameBody,width=23, font=('times new roman', 12), )
        self.name1Entry['values']=self.combo_input()
        self.name1Entry.grid(column=1, row=0, sticky='w', padx=10, pady=(10,5))

        self.name2=Label(frameBody, text='Name:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name2.grid(column=0, row=1, sticky='w', padx=10, pady=5)
        self.name2Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name2Entry.grid(column=1, row=1, sticky='w', padx=10, pady=5)
        
        self.name3=Label(frameBody, text='Designation:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name3.grid(column=0, row=2, sticky='w', padx=10, pady=5)
        self.name3Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name3Entry.grid(column=1, row=2, sticky='w', padx=10, pady=5)

        self.name4=Label(frameBody, text='Contact no:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name4.grid(column=0, row=3, sticky='w', padx=10, pady=5)
        self.name4Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name4Entry.grid(column=1, row=3, sticky='w', padx=10, pady=5)

        self.name5=Label(frameBody, text='Email-id:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name5.grid(column=0, row=4, sticky='w', padx=10, pady=5)
        self.name5Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name5Entry.grid(column=1, row=4, sticky='w', padx=10, pady=5)

        self.name6=Label(frameBody, text='Gender:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name6.grid(column=0, row=5, sticky='w', padx=10, pady=5)
        self.name6Entry=ttk.Combobox(frameBody,values=['male','female',],width=23, font=('times new roman', 12), )
        self.name6Entry.grid(column=1, row=5, sticky='w', padx=10, pady=5)

        self.name7=Label(frameBody, text='Address:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name7.grid(column=0, row=6, sticky='w', padx=10, pady=5)
        self.name7Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name7Entry.grid(column=1, row=6, sticky='w', padx=10, pady=5)

        self.name8=Label(frameBody, text='City:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name8.grid(column=2, row=0, sticky='w', padx=(20,0), pady=5)
        self.name8Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name8Entry.grid(column=3, row=0, sticky='w', padx=10, pady=5)

        self.name9=Label(frameBody, text='Country:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name9.grid(column=2, row=1, sticky='w', padx=(20,0), pady=5)
        self.name9Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name9Entry.grid(column=3, row=1, sticky='w', padx=10, pady=5)

        self.name10=Label(frameBody, text='Marital status:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name10.grid(column=2, row=2, sticky='w', padx=(20,0), pady=5)
        self.name10Entry=ttk.Combobox(frameBody,values=['married','single',],width=23, font=('times new roman', 12), )
        self.name10Entry.grid(column=3, row=2, sticky='w', padx=10, pady=5)

        self.name11=Label(frameBody, text='D.O.B:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name11.grid(column=2, row=3, sticky='w', padx=(20,0), pady=5)
        self.name11Entry=DateEntry(frameBody, date_pattern='dd/mm/yyyy',width=23, font=('times new roman', 12), 
        fg='black',bg='yellow',relief='flat',  command=self.validate_date)
        self.name11Entry.grid(column=3, row=3, sticky='w', padx=10, pady=5)

        self.name12=Label(frameBody, text='D.O.E:', font=('Goudy old style bold ', 14),fg='black',bg='white')
        self.name12.grid(column=2, row=4, sticky='w', padx=(20,0), pady=5)
        self.name12Entry=DateEntry(frameBody, date_pattern='dd/mm/yyyy',width=23, font=('times new roman', 12), 
        fg='black',bg='yellow',relief='flat', command=self.validate_date )
        self.name12Entry.grid(column=3, row=4, sticky='w', padx=10, pady=5)

        self.name13=Label(frameBody, text='Employee ID:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name13.grid(column=2, row=5, sticky='w', padx=(20,0), pady=5)
        self.name13Entry=Entry(frameBody,width=24, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.name13Entry.grid(column=3, row=5, sticky='w', padx=10, pady=5)

        self.name14=Label(frameBody, text='ID Proof:', font=('Goudy old style bold', 14),fg='black',bg='white')
        self.name14.grid(column=2, row=6, sticky='w', padx=(20,0), pady=5)
        self.name14Entry=ttk.Combobox(frameBody,values=['Passport','Voters card', 'Drivers license'],width=23, font=('times new roman', 12), )
        self.name14Entry.grid(column=3, row=6, sticky='w', padx=10, pady=5)

################################################ Frame for fingerprint and barcode #########################################################     
        frameFace=LabelFrame(frameBody, text='Enroll Face',font=('Goudy old style bold', 12),fg='black',
        height=258, width=255)
        frameFace.grid(column=4, row=0, sticky='w', padx=10, pady=5, rowspan=7)

        frameBarcode=LabelFrame(frameBody, text='Barcode ID card',font=('Goudy old style bold', 12),fg='black',
        height=258, width=255)
        frameBarcode.grid(column=8, row=0, sticky='e', padx=10, pady=5, rowspan=7)

################################################ Face Frame ################################################

        facepicFrame=Frame(frameFace)
        facepicFrame.grid(column=0, row=0, padx=0, pady=(0,3), columnspan=3)
################################################ frame inside frameFace ################################################
        self.face1=Image.open('.//Untitled Export//facialrecognition.png')
        self.resizeface=self.face1.resize((320,100), Image.ANTIALIAS)
        self.newface=ImageTk.PhotoImage(self.resizeface)
        self.FaceImage=Label(facepicFrame, image=self.newface, bg='#286b12')
        self.FaceImage.grid( column=0, row=0, padx=(3,3), sticky='n')
        self.FaceImage=self.newface 

################################################ frame inside frameFace ################################################
        faceFrame=Frame(frameFace,width=245, height=100)
        faceFrame.grid(column=0, row=1, padx=0, pady=(3,5), columnspan=3)
################################################ content in faceframe ################################################
        Addface=Button(faceFrame,text='Take face sample',width=35,  font=('roboto', 12, 'bold'), relief='groove',bg='yellow',command=self.face_dataset)
        Updateface=Button(faceFrame,text='View face samples',width=35, font=('roboto', 12, 'bold'), relief='groove',bg='yellow',command=self.open_photo)
        Trainface=Button(faceFrame,text='Train all face samples',width=35,  font=('roboto', 12, 'bold'), relief='groove',bg='yellow', command=self.training)
        Addface.grid( column=0, row=0, padx=(3,3), sticky='n')
        Updateface.grid( column=0, row=1, padx=(3,3), sticky='n')
        Trainface.grid( column=0, row=2, padx=(3,3), sticky='n')

################################################ other contents in frameface ################################################
        self.var_radio=StringVar()
        radiobutton1=ttk.Radiobutton(frameFace, text='Take face sample',variable=self.var_radio,value='yes', command=self.sel)
        radiobutton2=ttk.Radiobutton(frameFace, text='No face sample', variable=self.var_radio,value='no', command=self.sel)
        radiobutton1.grid(column=0, row=2, padx=(5,25), sticky='n')
        radiobutton2.grid(column=1, row=2, padx=(70,0), sticky='n')
        

################################################ Barcode Frame ################################################
        self.frameCanvas=Canvas(frameBarcode,width=245, height=225, bg='yellow')
        self.frameCanvas.create_rectangle(2,2,245,225,)
        self.frameCanvas.place(x=0, y=0,anchor='nw')

################################### Buttons for Register, Update, delete, clear and generate ID card ##########################################
        frameButtons=Frame(frameBody, bg='white', bd=5)
        frameButtons.grid(column=0, row=7, padx=0, pady=8, columnspan=9)

        self.Registerbutton1= Button( frameButtons, text='Register', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=13,
        command=self.deptadd)
        self.Registerbutton1.grid(column=0,row=0, padx=(0,8))

        self.updatebutton= Button( frameButtons, text='Update', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=13,
        command=self.EmpUpdate)
        self.updatebutton.grid(column=1, row=0, padx=8)

        self.Deletebutton= Button( frameButtons, text='Delete', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=13,
        command=self.Empdelete)
        self.Deletebutton.grid(column=2, row=0,padx=8)

        self.clearbutton= Button( frameButtons, text='Clear', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=13,
        command=self.clearall)
        self.clearbutton.grid(column=3, row=0,padx=8)

        self.Generatebutton= Button( frameButtons, text='Generate QRcode', font=('calibre',11, 'bold'), relief='flat',bg='yellow', bd=0, width=16,
        command=self.Generate_barcode)
        self.Generatebutton.grid(column=4, row=0,padx=(8,0))

################################################ Beautify Treeview #########################################################      
        self.styling=ttk.Style()
        self.styling.theme_use('default')
        self.styling.configure('Treeview', background='white', foreground='black', fieldbackground='white' )
        self.styling.configure('Treeview.Heading', font=('Calibri', 10, 'bold'), background='yellow' )
        self.styling.map('Treeview', background=[('selected', 'green')])
        
######################################### Treeview creation #################################################################################
        self.listboxscrollbar=Scrollbar(frameBody1, orient=VERTICAL)
        self.listboxscrollbar1=Scrollbar(frameBody1, orient=HORIZONTAL)
        self.trv=ttk.Treeview(frameBody1, selectmode='extended', yscrollcommand=self.listboxscrollbar.set, xscrollcommand=self.listboxscrollbar1.set)
        self.trv['columns']=('Employee-ID', 'department', 'Name', 'Designation', 'Contact no', 'Email-ID', 'Gender',
        'Address', 'City', 'Country', 'Marital status', 'D.O.B', 'D.O.E','ID-Proof', 'face sample' )


##################################### adding scrollbar to treeview ########################################################################
        self.listboxscrollbar.config(command=self.trv.yview)
        self.listboxscrollbar1.config(command=self.trv.xview)

        self.listboxscrollbar.place(x=1325, y=47,height=230,)
        self.listboxscrollbar1.place(x=10, y=275,width=1332,)

#####################################adding columns to treeview..####################################
        self.trv.column('#0', width=0, stretch='false')
        self.trv.column('Employee-ID', width=80, anchor='c')
        self.trv.column('department', width=100, anchor='c')  

        self.trv.column('Name', width=100, anchor='c')
        self.trv.column('Designation', width=80, anchor='c')
        self.trv.column('Contact no', width=80, anchor='c')
        self.trv.column('Email-ID', width=100, anchor='c')
        self.trv.column('Gender', width=80, anchor='c')
        self.trv.column('Address', width=100, anchor='c')
        self.trv.column('City', width=80, anchor='c')
        self.trv.column('Country', width=80, anchor='c')
        self.trv.column('Marital status', width=80, anchor='c')
        self.trv.column('D.O.B', width=80, anchor='c')
        self.trv.column('D.O.E', width=80, anchor='c')
        self.trv.column('ID-Proof', width=100, anchor='c')
        self.trv.column('face sample', width=100, anchor='c')

 #####################################adding headings for each columns####################################
        self.trv.heading('Employee-ID',text='Employee-ID', anchor='c')
        self.trv.heading('department',text='Department', anchor='c')
        self.trv.heading('Name',text='Name', anchor='c')
        self.trv.heading('Designation',text='Designation', anchor='c')
        self.trv.heading('Contact no',text='Contact no', anchor='c')
        self.trv.heading('Email-ID',text='Email-ID', anchor='c')
        self.trv.heading('Gender',text='Gender', anchor='c')
        self.trv.heading('Address',text='Address', anchor='c')
        self.trv.heading('City',text='City', anchor='c')
        self.trv.heading('Country',text='Country', anchor='c')
        self.trv.heading('Marital status',text='Marital Status', anchor='c')
        self.trv.heading('D.O.B',text='D.O.B', anchor='c')
        self.trv.heading('D.O.E',text='D.O.E', anchor='c')
        self.trv.heading('ID-Proof',text='ID-Proof', anchor='c')
        self.trv.heading('face sample',text='face sample', anchor='c')

 #####################################packing rhe treeview####################################
        self.trv.place(x=10, y=47,height=230, width=1316)
        self.show()

#################################### search bar ####################################
        frameBody2=LabelFrame(frameBody1, relief='ridge',bd=2, bg='white')
        frameBody2.place(x=330, y=8, width=605 ,height=35)

        self.serEntry=ttk.Combobox(frameBody2,values=['Search by...','Employee_ID','Department', 'Name'],
        width=24, font=('times new roman', 12, 'bold') , )
        self.serEntry.current(0)
        self.serEntry.place(x=9, y=4)

        self.SearchEntry1=Entry(frameBody2,width=25, font=('times new roman', 12), fg='black',bg='white',relief='ridge')
        self.SearchEntry1.place(x=230,y=4)
        
        Searchbutton1= Button(frameBody2, text='search', font=('calibre',10, 'bold'), relief='flat',bg='yellow', bd=0, width=8,
        command=self.searching)
        Searchbutton1.place(x=445,y=4)
        clearSearchbutton= Button(frameBody2, text='Refresh', font=('calibre',10, 'bold'), relief='flat',bg='yellow', bd=0, width=8,
        command=self.clearsearch)
        clearSearchbutton.place(x=527,y=4)

        self.trv.bind("<Double-1>", self.select_record)

#################################### Functions ####################################
    def sel(self):
        self.var_radio.get()
        

    def validate_date(self):
            if not self.name12Entry.get_date and self.name11Entry():
                    return True


    def combo_input(self):
                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM department")
                data=[]
                for rows in cursor.fetchall():
                        data.append(rows[1])
                return data
                

    def clearsearch(self):
                
                connect=mysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM Employees")
                rows=cursor.fetchall()
                connect.commit()
                connect.close()
                self.trv.delete(*self.trv.get_children())
                self.show()
                self.clearsearched()


    def clearsearched(self):
            self.SearchEntry1.delete(0, END)  
            self.serEntry.current(0)


    def searching(self):
                self.search= self.SearchEntry1.get()
                if self.search=='':
                                speak_va("field is required!!")
                                messagebox.showerror('Error', 'All fields are required', parent=self.window)
                collect= self.serEntry.get()
               
                try:
                           
                        for rows in self.trv.get_children():
                                self.trv.delete(rows)
                        

                        self.trv.tag_configure('oddrow', background='yellow')
                        self.trv.tag_configure('evenrow', background='white')
                        connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                        cursor=connect.cursor()
                        if collect== 'Search by...':
                                cursor.execute("SELECT * FROM employees")
                                messagebox.showinfo('', 'Select SEARCH BY.. option', parent=self.window)
                        if collect=='Employee_ID':
                                cursor.execute("SELECT * FROM employees WHERE id_number LIKE %s",(self.SearchEntry1.get(),))
                        if collect=='Department':
                                cursor.execute("SELECT * FROM employees WHERE department LIKE %s",(self.SearchEntry1.get(),))
                        if collect=='Name':
                                cursor.execute("SELECT * FROM employees WHERE name LIKE %s",(self.SearchEntry1.get(),))
                        row=cursor.fetchall()
                        count=1
                        if len(row)!=0:
                                self.trv.delete(*self.trv.get_children())
                        for rows in row:
                                if count%2==0:
                                        self.trv.insert(parent="", index='end', text='' ,iid=count, values=(rows), tags=('oddrow',))
                                else:
                                        self.trv.insert(parent="", index='end', text='' , iid=count, values=(rows), tags=('evenrow',))
                                count+= 1
                        connect.commit()
                        connect.close()
                                        
                except Exception as es:
                        messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)


    def select_record(self,event):
                self.Registerbutton1.config(state=DISABLED)
                
                self.department=self.name1Entry
                self.name=self.name2Entry
                self.position=self.name3Entry
                self.contact=self.name4Entry
                self.email=self.name5Entry
                self.gender=self.name6Entry
                self.address=self.name7Entry
                self.city=self.name8Entry
                self.country=self.name9Entry
                self.marital=self.name10Entry
                self.birth=self.name11Entry
                self.job=self.name12Entry
                self.id=self.name13Entry
                self.proof=self.name14Entry
                
                self.ClearEmp()

                selected=self.trv.identify_row(event.y)
                values=self.trv.item(selected,'values')
                self.department.insert(0,values[1])
                self.name.insert(0,values[2])
                self.position.insert(0,values[3])
                self.contact.insert(0,values[4])
                self.email.insert(0,values[5])
                self.gender.insert(0,values[6])
                self.address.insert(0,values[7])
                self.city.insert(0,values[8])
                self.country.insert(0,values[9])
                self.marital.insert(0,values[10])
                self.birth.insert(0,values[11])
                self.job.insert(0,values[12])
                self.id.insert(0,values[0])
                self.proof.insert(0,values[13])
                self.var_radio.set(values[14])
               
                   
    def show(self):

                self.trv.tag_configure('oddrow', background='#c9c9c9')
                self.trv.tag_configure('evenrow', background='white')
                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM Employees" )
                row=cursor.fetchall()
                count=1
                for rows in row:
                        if count%2==0:
                                self.trv.insert(parent="", index='end', text=count ,iid=count, values=(rows), tags=('oddrow'))
                        else:
                                self.trv.insert(parent="", index='end', text=count ,iid=count, values=(rows), tags=('evenrow'))
                        count+= 1
                connect.commit()
                connect.close()   


    def convert_to_binaryData(self):
            self.name=self.name2Entry.get()
            with open ('.//qrcodes//'+(str(self.name)+".png"), 'rb') as file:
                                                self.BinaryData=file.read()
            return self.BinaryData
 

    def deptadd(self):
            self.department=self.name1Entry.get()
            self.name=self.name2Entry.get()
            self.position=self.name3Entry.get()
            self.contact=self.name4Entry.get()
            self.email=self.name5Entry.get()
            self.gender=self.name6Entry.get()
            self.address=self.name7Entry.get()
            self.city=self.name8Entry.get()
            self.country=self.name9Entry.get()
            self.marital=self.name10Entry.get()
            self.birth=self.name11Entry.get_date()
            self.job=self.name12Entry.get_date()
            self.id=self.name13Entry.get()
            self.proof=self.name14Entry.get()

            if not os.path.exists('//qrcodes//'):
                                try:
                                                os.makedirs('.//qrcodes//')
                                except OSError as e:
                                                if e.errno!=errno.EEXIST:
                                                        raise
            try:            
                        self.qr.png(os.path.join('.//qrcodes//'+(str(self.name))+ ".png"), scale=8)

            except AttributeError as es:
                        pass

            if (self.department=='' or self.name=='' or self.position=='' or self.contact=='' or  self.email=='' or self.gender=='' or self.address=='' or 
             self.city=='' or  self.country=='' or self.marital=='' or self.birth=='' or self.job=='' or self.id=='' or  self.proof=='' or  self.var_radio.get()=='' or self.frameCanvas.create_image is NONE):
                speak_va("All fields are required!!!")
                messagebox.showerror('Error', 'All fields are required', parent=self.window)
                                     
            else: 
                     try:
                            connect=mysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='employee_attendance')
                            cursor=connect.cursor()
                            cursor.execute("SELECT * FROM employees")
                            row=cursor.fetchall()
                            if row==None:
                                speak_va("Employee Exist!!") 
                                messagebox.showerror('Error', 'Employee already Exist, please try with another department ', parent=self.window)
                                    #call the clear function to clear the entry box after message pops up
                                   
                            else:
                                   cursor.execute("""INSERT INTO employees(id_number,department,name,position,contact_no,email_ID,gender,address,city,country,marital_status,Birth_Date,Job_Date,ID_proof,face_sample,Barcode)
                                   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (self.name13Entry.get(),
                                                                                        self.name1Entry.get(),
                                                                                        self.name2Entry.get(),
                                                                                        self.name3Entry.get(),
                                                                                        self.name4Entry.get(),
                                                                                        self.name5Entry.get(),
                                                                                        self.name6Entry.get(),
                                                                                        self.name7Entry.get(),
                                                                                        self.name8Entry.get(),
                                                                                        self.name9Entry.get(),
                                                                                        self.name10Entry.get(),
                                                                                        self.name11Entry.get_date(),
                                                                                        self.name12Entry.get_date(),
                                                                                        self.name14Entry.get(),
                                                                                        str(self.var_radio.get()),
                                                                                        self.convert_to_binaryData(),))
                                   connect.commit()                                     
                                   connect.close()
                                   self.trv.delete(*self.trv.get_children())     
                                   self.show()
                                   speak_va(self.name2Entry.get()+" Successfully Added!!")
                                   messagebox.showinfo('Success', 'Employee successfully Added', parent=self.window)
                                   self.ClearEmp() #call the clear function after message
                     except Exception as es:
                            speak_va("Error!!! please contact the Software Engineer!!!")
                            messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)


    def EmpUpdate(self):
                self.name=self.name2Entry.get()
                if not os.path.exists('//qrcodes//'):
                                try:
                                                os.makedirs('.//qrcodes//')
                                except OSError as e:
                                                if e.errno!=errno.EEXIST:
                                                        raise
                try:            
                        self.qr.png(os.path.join('.//qrcodes//'+(str(self.name))+ ".png"), scale=8)

                except AttributeError as es:
                        pass

                if  self.name13Entry.get()=="":
                               messagebox.showerror('Error', 'All fields are required', parent=self.window)
                               
                else:    
            
                        try:
                                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                                cursor=connect.cursor()
                                cursor.execute("SELECT * FROM employees")
                                row=cursor.fetchall()
                                if row==None:
                                        messagebox.showerror('Error', 'Employee already Exist, please try with another employee ', parent=self.window)
                                        #call the clear function to clear the entry box after message pops up
                                        
                                else:  
                                        self.department=self.name1Entry
                                        self.name=self.name2Entry
                                        self.position=self.name3Entry
                                        self.contact=self.name4Entry
                                        self.email=self.name5Entry
                                        self.gender=self.name6Entry
                                        self.address=self.name7Entry
                                        self.city=self.name8Entry
                                        self.country=self.name9Entry
                                        self.marital=self.name10Entry
                                        self.birth=self.name11Entry
                                        self.job=self.name12Entry
                                        self.id=self.name13Entry
                                        self.proof=self.name14Entry

                                        selected=self.trv.focus()
                                        values=self.trv.item(selected,'values')
                                        self.trv.item(selected,values=(self.id.get(),self.department.get(),self.name.get(),self.position.get(),self.contact.get(),
                                        self.email.get(),self.gender.get(),self.address.get(),self.city.get(),self.country.get(),self.marital.get(),
                                        self.birth.get_date(),self.job.get_date(),self.proof.get(),self.var_radio.get()))

                                        cursor.execute("""UPDATE employees SET department=%s,name=%s,position=%s,contact_no=%s,
                                        email_ID=%s,gender=%s,address=%s,city=%s,country=%s,marital_status=%s,
                                        Birth_Date=%s,Job_Date=%s,ID_proof=%s,face_sample=%s,Barcode=%s WHERE id_number=%s""",(
                                                                                self.name1Entry.get(),                                 
                                                                                self.name2Entry.get(),
                                                                                self.name3Entry.get(),
                                                                                self.name4Entry.get(),
                                                                                self.name5Entry.get(),
                                                                                self.name6Entry.get(),
                                                                                self.name7Entry.get(),
                                                                                self.name8Entry.get(),
                                                                                self.name9Entry.get(),
                                                                                self.name10Entry.get(),
                                                                                self.name11Entry.get_date(),
                                                                                self.name12Entry.get_date(),
                                                                                self.name14Entry.get(),
                                                                                self.var_radio.get(),
                                                                                self.convert_to_binaryData(),
                                                                                self.name13Entry.get(),))
                                        connect.commit()
                                        connect.close()
                                        speak_va(self.name2Entry.get()+" Successfully Updated!!")
                                        messagebox.showinfo('Success', 'Employee successfully Updated', parent=self.window)
                                        
                                        self.ClearEmp() #call the clear function after message
                        except Exception as es:
                                speak_va("Error!!! please contact the Software Engineer!!!")
                                messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)


    def Empdelete(self):
                        self.name=self.name2Entry.get()
                        self.Registerbutton1.config(state=ACTIVE, bg='yellow')
                        try:
                                os.remove(".//qrcodes//"+(str(self.name))+ ".png")
                        except FileNotFoundError:
                                print("file not found")
                        try:
                                response= messagebox.askyesno('Delete Employee', 'are you sure you want to delete Employee')
                                if response==1:
                                        #point to selection on treeview
                                        x=self.trv.selection()
                                        #create list of ids
                                        ids_to_delete=[]
                                        #add selction to id_to_delete list
                                        for row in x:
                                                ids_to_delete.append(self.trv.item(row, 'values')[0])
                                        #delete from treeview
                                        for row in x:
                                                self.trv.delete(row)
                                        speak_va(self.name2Entry.get()+" Successfully Deleted!!")
                                        messagebox.showinfo('Success', 'Delete successful', parent=self.window)
                                else:
                                        return True
                                
                                self.ClearEmp() #call the clear function after message
                                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                                cursor=connect.cursor()
                                cursor.execute("SELECT * FROM employees" )
                                row=cursor.fetchall()
                                #Delete everything from the table
                                cursor.executemany("DELETE FROM employees WHERE id_number=%s", ([(a,) for a in ids_to_delete]))
                                connect.commit()
                                connect.close()

                        except Exception as es:
                                speak_va("Error!!! please contact the Software Engineer!!!")
                                messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)


    def clearall(self):
           self.Registerbutton1.config(state=ACTIVE, bg='yellow')
           self.ClearEmp()


    def ClearEmp(self):
            
            self.name1Entry.delete(0, END)
            self.name2Entry.delete(0, END) 
            self.name3Entry.delete(0, END) 
            self.name4Entry.delete(0, END) 
            self.name5Entry.delete(0, END) 
            self.name6Entry.delete(0, END) 
            self.name7Entry.delete(0, END) 
            self.name8Entry.delete(0, END) 
            self.name9Entry.delete(0, END) 
            self.name10Entry.delete(0, END) 
            self.name11Entry.delete(0, END) 
            self.name12Entry.delete(0, END) 
            self.name13Entry.delete(0, END) 
            self.name14Entry.delete(0, END) 
            self.frameCanvas.delete("all")
            self.var_radio.set(None)

    def Generate_barcode(self):
                global qr,img
                L1=[]
                
                self.name=self.name2Entry.get()
                self.id=self.name13Entry.get()
                self.department=self.name1Entry.get()
                self.position=self.name3Entry.get()
                self.contact=self.name4Entry.get()

                L1.extend([self.id, self.department, self.name,self.position,self.contact])
                listToStr=" ".join([str(elem) for elem in L1])
        
                if self.name=='' or self.id=="" or self.department=='' or self.id==" " or self.contact=='':
                        messagebox.showerror('Error', 'All fields are required', parent=self.window)
                else:
                        
                        self.qr=pyqrcode.create(listToStr)
                        self.img=BitmapImage(data=self.qr.xbm(scale=5))
                        self.display_code()
               
                             
    def display_code(self):
                self.frameCanvas.create_image(5,0, image=self.img, anchor='nw') 
                self.frameCanvas.create_text( 80,9, text=self.name, font=('time new roman',14, 'bold'),fill='black')


    def  face_dataset(self):
        self.name=self.name2Entry.get()
        if  self.name13Entry.get()=="":
                               messagebox.showerror('Error', 'All fields are required', parent=self.window)
                   
        else: 
                 try:
                        connect=mysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='employee_attendance')
                        cursor=connect.cursor()
                        cursor.execute("SELECT * FROM employees")
                        row=cursor.fetchall()
                        if len(row)>0:
                               
                                self.department=self.name1Entry
                                self.name=self.name2Entry
                                self.position=self.name3Entry
                                self.contact=self.name4Entry
                                self.email=self.name5Entry
                                self.gender=self.name6Entry
                                self.address=self.name7Entry
                                self.city=self.name8Entry
                                self.country=self.name9Entry
                                self.marital=self.name10Entry
                                self.birth=self.name11Entry
                                self.job=self.name12Entry
                                self.id=self.name13Entry
                                self.proof=self.name14Entry

                                selected=self.trv.focus()
                                values=self.trv.item(selected,'values')
                                self.trv.item(selected,values=(self.id.get(),self.department.get(),self.name.get(),self.position.get(),self.contact.get(),
                                self.email.get(),self.gender.get(),self.address.get(),self.city.get(),self.country.get(),self.marital.get(),
                                self.birth.get_date(),self.job.get_date(),self.proof.get(),self.var_radio.get()))
                
                                        

                                cursor.execute("""UPDATE employees SET department=%s,name=%s,position=%s,contact_no=%s,
                                email_ID=%s,gender=%s,address=%s,city=%s,country=%s,marital_status=%s,
                                Birth_Date=%s,Job_Date=%s,ID_proof=%s,face_sample=%s,Barcode=%s WHERE  id_number=%s""",( self.name1Entry.get(),                                 
                                                                                                                                self.name2Entry.get(),
                                                                                                                                self.name3Entry.get(),
                                                                                                                                self.name4Entry.get(),
                                                                                                                                self.name5Entry.get(),
                                                                                                                                self.name6Entry.get(),
                                                                                                                                self.name7Entry.get(),
                                                                                                                                self.name8Entry.get(),
                                                                                                                                self.name9Entry.get(),
                                                                                                                                self.name10Entry.get(),
                                                                                                                                self.name11Entry.get_date(),
                                                                                                                                self.name12Entry.get_date(),
                                                                                                                                self.name14Entry.get(),
                                                                                                                                self.var_radio.get(),
                                                                                                                                self.convert_to_binaryData(),
                                                                                                                                self.name13Entry.get(),))
                                connect.commit()
                                connect.close()
                               
                                # To capture video from webcam.
                                cap = cv2.VideoCapture(0)
                                cap.set(3,640)
                                cap.set(4,480)
                                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                                id=self.name13Entry.get()
                                count=0
                                while True:
                                        # Read the frame
                                        ret, img = cap.read()
                                        # Convert to grayscale
                                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                                        # Detect the faces
                                        faces = face_cascade.detectMultiScale(gray, 1.6, 3, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

                                        # Draw the rectangle around each face
                                        for (x, y, w, h) in faces:
                                                cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 3)
                                                roi_gray=gray[y:y+h, x:x+w]
                                                roi_color=img[y:y+h, x:x+w]
                                                count+=1
                                                cv2.imwrite('data/user.'+str(id)+'.'+str(count)+'.jpg',roi_gray)
                                        # Display
                                                cv2.imshow('Webcam Check', img)

                                        # Stop if escape key is pressed
                                        if cv2.waitKey(1) & 0xFF == ord('q'):
                                                break
                                        
                                        elif count>=30:
                                                break

                                # Release the VideoCapture object
                                cap.release()
                                cv2.destroyAllWindows()
                                speak_va(self.name2Entry.get()+" Images Successfully Added!!")
                        #load predefined on face frontals from openCV
                 except Exception as es:
                                        speak_va("Error!!! please contact the Software Engineer!!!")
                                        messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)


    def open_photo(self):
            os.startfile('data')
            

    def training(self):
        TrainImage.Train()
        speak_va("All data set successfully trained") 
        messagebox.showinfo('Result', 'Face_samples Successfully Trained')    


 ##################################### FUNCTION TO LOG OUT #####################################################################################     
    def logout(self):
        global window
        mlog_out=messagebox.askquestion('Confirm','Are you sure you want to log out?')
        if mlog_out=='yes':
            Login(window)
            Login.loginform(self)  
            self.User_TimeOUT()
        else:
            return


##################################### function to record the time log_out #################################
    def User_TimeOUT(self):
              ts=time()
              self.date1=datetime.datetime.now().fromtimestamp(ts).strftime('%Y:%m:%d %H:%M:%S')
              connect=mysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("UPDATE admin SET Last_logout=%s", (self.date1,))
              connect.commit()
              connect.close()

    def Exit(self):
              global window
              mExit=messagebox.askquestion('Confirm','Are you sure you want to Exit?')
              if mExit=='yes':
                     window.destroy()
              else:
                      return



######################################### DASHBOARD CREATION ##################################################   
    def app_screen(self):
              frameBody13=Frame(self.window)
              frameBody13.place(x=0, y=100, height=768, width=1366)

       ########################################## background picture for frame  #########################################################

              self.img21=Image.open('.//Untitled Export//background-1783718_1920.jpg')
              self.resize11=self.img21.resize((1366,768), Image.ANTIALIAS)
              self.new11=ImageTk.PhotoImage(self.resize11)

              self.labImage11=Label(frameBody13, image=self.new11,).grid(sticky='nwse')
              self.labImage11=self.new11 

       ################################## Subframes for register and treeview ############################################################
              
              frame1=Frame(self.window, bg='green', height=250, width=350)
              frame2=Frame(self.window, bg='green', height=250, width=350)
              frame3=Frame(self.window, bg='green', height=250, width=350)
              frame4=Frame(self.window, bg='green', height=250, width=350)
              frame5=Frame(self.window, bg='green', height=250, width=350)
              frame6=Frame(self.window, bg='green', height=250, width=350)
              
              frame1.grid(column=0, row=0, sticky='nw', padx=(130,10),pady=(180,0))
              frame2.grid(column=1, row=0, sticky='nw', padx=(10,10),pady=(180,0))
              frame3.grid(column=2, row=0, sticky='nw', padx=(10,0),pady=(180,0))
              frame4.grid(column=0, row=1, sticky='nw',padx=(130,10),pady=(20,0))
              frame5.grid(column=1, row=1, sticky='nw',padx=(10,10), pady=(20,0))
              frame6.grid(column=2, row=1, sticky='nw',padx=(10,0),pady=(20,0))


              self.image1=Image.open(
                     './/Untitled Export//employeees.png')
              self.resizing1=self.image1.resize((350,250), Image.ANTIALIAS)
              self.imaging1=ImageTk.PhotoImage(self.resizing1)

              self.image2=Image.open(
                     './/Untitled Export//Developers.png')
              self.resizing2=self.image2.resize((350,250), Image.ANTIALIAS)
              self.imaging2=ImageTk.PhotoImage(self.resizing2)

              self.image3=Image.open(
                     './/Untitled Export//department.png')
              self.resizing3=self.image3.resize((350,250), Image.ANTIALIAS)
              self.imaging3=ImageTk.PhotoImage(self.resizing3)

              self.image4=Image.open(
                     './/Untitled Export//attendance.png')
              self.resizing4=self.image4.resize((350,250), Image.ANTIALIAS)
              self.imaging4=ImageTk.PhotoImage(self.resizing4)

              self.image5=Image.open(
                     './/Untitled Export//Barcode.png')
              self.resizing5=self.image5.resize((390,250), Image.ANTIALIAS)
              self.imaging5=ImageTk.PhotoImage(self.resizing5)

              self.image6=Image.open(
                     './/Untitled Export//admin.png')
              self.resizing6=self.image6.resize((350,250), Image.ANTIALIAS)
              self.imaging6=ImageTk.PhotoImage(self.resizing6)

       ################################# a canvas that will allow placement of a transparent label ##############################
              self.canvas1=Canvas(frame3, width=350, height=250)
              self.canvas1.grid(sticky='nwse')

              self.canvas2=Canvas(frame6, width=350, height=250)
              self.canvas2.grid(sticky='nwse')

              self.canvas3=Canvas(frame2, width=350, height=250)
              self.canvas3.grid(sticky='nwse')

              self.canvas4=Canvas(frame1, width=350, height=250)
              self.canvas4.grid(sticky='nwse')

              self.canvas5=Canvas(frame4, width=350, height=250)
              self.canvas5.grid(sticky='nwse')

              self.canvas6=Canvas(frame5, width=350, height=250)
              self.canvas6.grid(sticky='nwse')

              
       ################################## placing the image on the canvas ##############################
              self.canvas1.create_image(2,1, image=self.imaging1,anchor='nw')
              self.canvas2.create_image(2,1, image=self.imaging2,anchor='nw')
              self.canvas3.create_image(2,1, image=self.imaging3,anchor='nw')
              self.canvas4.create_image(2,1, image=self.imaging4,anchor='nw')
              self.canvas5.create_image(2,1, image=self.imaging5,anchor='nw')
              self.canvas6.create_image(2,1, image=self.imaging6,anchor='nw')
       

       ############################### text label to be shown on the created canvas #########################
              self.canvas1.create_text( 170,25, text='Total Employee', font=('Open Sans ExtraBold', 18, 'bold'),fill='black')
              self.canvas2.create_text( 170,25, text='Developers', font=('Open Sans ExtraBold', 18, 'bold'),fill='black')
              self.canvas3.create_text( 170,25, text='Total Department', font=('Open Sans ExtraBold', 18, 'bold'),fill='black')
              self.canvas4.create_text( 170,25, text='Today Total Attendance', font=('Open Sans ExtraBold', 18, 'bold'),fill='black')
              self.canvas5.create_text( 170,25, text='Total Barcode Generated', font=('Open Sans ExtraBold', 18, 'bold'),fill='black')
              self.canvas6.create_text( 170,25, text='Admin Login Status', font=('Open Sans ExtraBold', 18, 'bold'),fill='black')
              self.get_total_department()
              self.get_total_employee()
              self. get_total_barcode()
              self.get_view_attendance()
              self.get_Admin_Last_Login()
              self.developers()

    def get_total_department(self):
            
              connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("SELECT  COUNT(id) FROM department")
              result=cursor.fetchall()
              for i in result:
                     self.canvas3.create_text( 170,130, text=i, font=('time new roman', 45, 'bold'),fill='White')
              connect.commit()
              connect.close()

    def get_total_employee(self):
              connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("SELECT  COUNT(id_number) FROM employees")
              result=cursor.fetchall()
              for i in result:
                     self.canvas1.create_text( 170,130, text=i, font=('time new roman', 45, 'bold'),fill='black')
              connect.commit()
              connect.close()

    def get_total_barcode(self):
              connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
              cursor=connect.cursor()
              cursor.execute("SELECT  COUNT(Barcode) FROM employees")
              result=cursor.fetchall()
              for i in result:
                     self.canvas5.create_text( 170,130, text=i, font=('time new roman', 45, 'bold'),fill='black')
              connect.commit()
              connect.close()
              

    def get_view_attendance(self):
                     connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                     cursor=connect.cursor()
                     cursor.execute("SELECT  COUNT(id_number) FROM view_attendance")
                     result=cursor.fetchall()
                     for i in result:
                            self.canvas4.create_text( 170,130, text=i, font=('time new roman', 45, 'bold'),fill='black')
                     connect.commit()
                     connect.close()

    def get_Admin_Last_Login(self):
                     connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                     cursor=connect.cursor()
                     cursor.execute("SELECT * FROM admin WHERE username=%s",(str(self.userA),))
                     result=cursor.fetchone()
                     self.canvas6.create_text( 140,65, text='User_ID:', font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas6.create_text( 200,65, text=str(result[0]), font=('time new roman', 13, 'bold'),fill='white')
                     self.canvas6.create_text( 130,95, text='Username:', font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas6.create_text( 210,95, text=str(result[1]), font=('time new roman', 13, 'bold'),fill='white')
                     self.canvas6.create_text( 105,125, text='Department:', font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas6.create_text( 230,125, text=str(result[2]), font=('time new roman', 13, 'bold'),fill='white')
                     self.canvas6.create_text( 136,155, text='Position:', font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas6.create_text( 210,155, text=str(result[3]), font=('time new roman', 13, 'bold'),fill='white')
                     self.canvas6.create_text( 100,185, text='Last Login:', font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas6.create_text( 230,185, text=str(result[6]), font=('time new roman', 13, 'bold'),fill='white')
                     self.canvas6.create_text( 97,215, text='Last Logout:', font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas6.create_text( 230,215, text=str(result[7]), font=('time new roman', 13, 'bold'),fill='white')
                    
                     connect.commit()
                     connect.close()

    def developers(self):
                     self.canvas2.create_text( 177,68, text='AYEBIELE HABEEB - F/HD/19/3210053',font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas2.create_text( 177,88, text='Project Manager',font=('time new roman', 13, 'bold','italic'),fill='black')

                     self.canvas2.create_text( 177,118, text='HASSAN SAMUEL - F/HD/19/3210067',font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas2.create_text( 177,138, text='Programmer',font=('time new roman', 13, 'bold','italic'),fill='black')

                     self.canvas2.create_text( 177,168, text='OLASANMI GLORY - F/HD/19/3210010',font=('time new roman', 13, 'bold'),fill='black')
                     self.canvas2.create_text( 177,188, text='Project writer',font=('time new roman', 13, 'bold','italic'),fill='black')

                     self.canvas2.create_text( 177,235, text='visit our help desk @ sirmuhell45@gmail.com\nor call 08028509719',
                     font=('time new roman', 10, 'bold'),fill='white')

            
########################################## VIEW ATTENDANCE #########################################################
    def view_attendance(self):

       ########################################## View attendance frame  #########################################################
                frameBody13=Frame(self.window)
                frameBody13.place(x=0, y=100, height=768, width=1366)

        ########################################## background picture for frame  #########################################################
                self.img21=Image.open('.//Untitled Export//background-1783718_1920.jpg')
                self.resize11=self.img21.resize((1366,768), Image.ANTIALIAS)
                self.new11=ImageTk.PhotoImage(self.resize11)

                self.labImage11=Label(frameBody13, image=self.new11,).grid(sticky='nw')
                self.labImage11=self.new11 

        ################################## Subframes for search and treeview ############################################################
                frameBody19=Frame(frameBody13, bg='white')
                frameBody21=Frame(frameBody13, bg='green')
        
                frameBody19.place(width= 990,height=150,x=190, y=45)
                frameBody21.place(width= 1347,height=420,x=10, y=210)
                
        ########################################## Searchframe and buttons ############################################################       
                Searchframe=Frame(frameBody19, bg='White', bd=5)
                Searchframe.grid(column=0, row=0, padx=6, pady=(20,2), columnspan=9)

                self.searchByEntry=ttk.Combobox( Searchframe,values=['Search by...','Employee_ID','Department', 'Name'],
                width=24, font=('times new roman', 12, 'bold') , )
                self.searchByEntry.current(0)
                self.searchByEntry.grid(column=0, row=0, sticky='w', padx=(30,10), )

                self.SearchdEntry2=Entry( Searchframe,width=28, font=('times new roman', 12), fg='black',bg='white',relief='groove')
                self.SearchdEntry2.grid(column=1, row=0, sticky='w', padx=(6,10), )
                
                Searchbutton1= Button( Searchframe, text='Enter', font=('calibre',10, 'bold'), relief='flat',bg='yellow', bd=0, width=12,
                command=self.Entersearching)
                Searchbutton1.grid(column=2, row=0, sticky='w', padx=(6,10), )

                Todaybutton= Button(Searchframe, text='Today', font=('calibre',10, 'bold'), relief='flat',bg='yellow', bd=0, width=12,
                command=self.ShowToday)
                Todaybutton.grid(column=3, row=0, sticky='w', padx=(0,10), )

                ShowAllbutton= Button( Searchframe, text='Show all', font=('calibre',10, 'bold'), relief='flat',bg='yellow', bd=0, width=12,
                command=self.Refresh)
                ShowAllbutton.grid(column=4, row=0, sticky='w', padx=(0,10), )

                DeleteAllbutton= Button( Searchframe, text='Delete', font=('calibre',10, 'bold'), relief='flat',bg='yellow', bd=0, width=12,
                command=self.deleteAll)
                DeleteAllbutton.grid(column=5, row=0, sticky='w', padx=(0,10), )

                Dateframe=Frame(frameBody19, bg='White', bd=5)
                Dateframe.grid(column=0, row=2, padx=0, pady=15, columnspan=9)

                self.searchy=Label( Dateframe, text='Date From:', font=('Open Sans SemiBold', 14, ),fg='black',bg='white')
                self.searchy.grid(column=0, row=0, padx=(0,10))

                self.searchy12Entry=DateEntry( Dateframe, date_pattern='dd/mm/yyyy',width=13, font=('times new roman', 12), 
                fg='black',bg='green',relief='flat', )
                self.searchy12Entry.grid(column=1, row=0, padx=10)

                self.searchy12=Label( Dateframe, text='To:', font=('Open Sans SemiBold', 14, ),fg='black',bg='white')
                self.searchy12.grid(column=2, row=0, padx=10)

                self.searchingEntry=DateEntry(Dateframe, date_pattern='dd/mm/yyyy',width=13, font=('times new roman', 12), 
                fg='black',bg='green',relief='flat', )
                self.searchingEntry.grid(column=3, row=0, padx=10)

                Searchbutton2= Button( Dateframe, text='Generate CSV file', font=('calibre',10, 'bold'),bg='yellow', relief='groove', width=14,
                 activebackground='yellow', command=self.export_attendance)
                Searchbutton2.grid(column=4, row=0, padx=(10,0))

                Importbutton2= Button( Dateframe, text='Import CSV file', font=('calibre',10, 'bold'),bg='yellow', relief='groove', width=14,
                 activebackground='yellow', command=self.importing)
                Importbutton2.grid(column=5, row=0, padx=(10,0))

                Searchbutton4= Button( Dateframe, text='Send Email', font=('calibre',10, 'bold'),bg='yellow', relief='groove', width=14,
                 activebackground='yellow', command=self.sender)
                Searchbutton4.grid(column=6, row=0, padx=(10,0))

        ################################################ Beautify Treeview #########################################################      
                self.styling=ttk.Style()
                self.styling.theme_use('default')
                self.styling.configure('Treeview', background='white', foreground='black', fieldbackground='white' )
                self.styling.configure('Treeview.Heading', font=('Calibri', 10, 'bold'), background='Yellow' )
                self.styling.map('Treeview', background=[('selected', 'green')])
                
        ######################################### Treeview creation #################################################################################
                self.listboxscrollbar=Scrollbar(frameBody21, orient=VERTICAL)
                self.listboxscrollbar1=Scrollbar(frameBody21, orient=HORIZONTAL)
                self.trv2=ttk.Treeview(frameBody21, selectmode='extended', yscrollcommand=self.listboxscrollbar.set, xscrollcommand=self.listboxscrollbar1.set)
                self.trv2['columns']=('Employee-ID', 'department', 'Name', 'Designation', 'Contact no','date', 'Time-in',
                'Time-out', 'Total hours')

        ##################################### Adding scrollbar to treeview ########################################################################
                self.listboxscrollbar.config(command=self.trv2.yview)
                self.listboxscrollbar1.config(command=self.trv2.xview)

                self.listboxscrollbar.place(x=1320, y=10,height=407,)
                self.listboxscrollbar1.place(x=10, y=400,width=1310,)

        ##################################### Adding columns to treeview..####################################
                self.trv2.column('#0', width=0, stretch='false')
                self.trv2.column('Employee-ID', width=80, anchor='c')
                self.trv2.column('department', width=100, anchor='c')  
                self.trv2.column('Name', width=100, anchor='c')
                self.trv2.column('Designation', width=80, anchor='c')
                self.trv2.column('Contact no', width=100, anchor='c')
                self.trv2.column('date', width=100, anchor='c')
                self.trv2.column('Time-in', width=80, anchor='c')
                self.trv2.column('Time-out', width=100, anchor='c')
                self.trv2.column('Total hours', width=80, anchor='c')

        ##################################### Adding headings for each columns ####################################
                self.trv2.heading('Employee-ID',text='Employee-ID', anchor='c')
                self.trv2.heading('department',text='Department', anchor='c')
                self.trv2.heading('Name',text='Name', anchor='c')
                self.trv2.heading('Designation',text='Designation', anchor='c')
                self.trv2.heading('Contact no',text='Contact no', anchor='c')
                self.trv2.heading('date',text='date', anchor='c')
                self.trv2.heading('Time-in',text='Time-in', anchor='c')
                self.trv2.heading('Time-out',text='Time-out', anchor='c')
                self.trv2.heading('Total hours',text='Total hours', anchor='c')
        
        ##################################### Packing rhe treeview ####################################
                self.trv2.place(x=10, y=10,height=390, width=1310)
                self.showAttendance()

        ################################### Refresh and ShowAll and the app  ####################################
    def Refresh(self):
                        connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                        cursor=connect.cursor()
                        cursor.execute("SELECT * FROM view_attendance")
                        rows=cursor.fetchall()
                        connect.commit()
                        connect.close()
                        self.trv2.delete(*self.trv2.get_children())
                        self.showAttendance()
                        self.SearchdEntry2.delete(0,END)
                        messagebox.showinfo("Appraisal","Attendance Summary can be used at month end for appraisal")
                        self.Appraise()
        
        ################################### Delete all record on treeview  ####################################
    def deleteAll(self):
                            try:
                                   response= messagebox.askyesno('Delete Attendance', 'are you sure you want to delete Attendance?')
                                   if response==1:
                                          #point to selection on treeview
                                          x=self.trv2.selection()
                                          #create list of ids
                                          ids_to_delete=[]
                                          #add selction to id_to_delete list
                                          for row in x:
                                                 ids_to_delete.append(self.trv2.item(row, 'values')[0])
                                          #delete from treeview
                                          for row in x:
                                                 self.trv2.delete(row)
                                          speak_va('Attendance Successfully deleted')
                                          messagebox.showinfo('Success', 'Delete successful', parent=self.window)
                                   else:
                                          return True
                                   
                                   connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
                                   cursor=connect.cursor()
                                   cursor.execute("SELECT * FROM view_attendance" )
                                   row=cursor.fetchall()
                                   #Delete everything from the table
                                   cursor.executemany("DELETE FROM view_attendance WHERE id_number=%s", ([(a,) for a in ids_to_delete]))
                                   connect.commit()
                                   connect.close()

                            except Exception as es:
                                   messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

         ################################### Import Attendance record to treeview  ####################################
    def importing(self):
                try:
                        connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                        cursor=connect.cursor()
                        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="import CSV", filetypes=(("CSV file","*.csv"),("All files","*.*")))
                        with open(fln) as myfile:
                                exp_read=csv.reader(myfile, delimiter=",")
                                header=next(exp_read)
                                for row in exp_read:
                                        cursor.execute("""INSERT IGNORE INTO view_attendance(id_number,department,name,position,contact_no,Date,time_in,time_out,total_time) 
                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(row))
                                connect.commit()
                                connect.close()
                                self. showAttendance()
                                speak_va('Attendance successfully imported!!!')
                                messagebox.showinfo('Success', 'Import successful', parent=self.window)
                except Exception as es:
                        speak_va('Attendance successfully imported!!!')
                        pass
        #################################### TAKE ATTENDANCE  ####################################            
    def take_attendance(self):
                        frequency=600
                        duration=800
                        images=[]
                        i=0
                        vs=VideoStream(src=0).start()
                        import time
                        time.sleep(2.0)
                        images=[]
                        while i<1:
                                images=vs.read()
                                images=imutils.resize(images, width=600)
                                barcodes=pyzbar.decode(images)
                                for barcode in barcodes:
                                        (x,y, width,height)= barcode.rect
                                        cv2.rectangle(images, (x,y),(x+width, y+height), (0,0,255),2)
                                        barcodeData=barcode.data.decode("utf-8")
                                        barcodeType=barcode.type
                                        import datetime as dt
                                        date=dt.datetime.now()
                                        textData="{} ({}) {}".format(barcodeData, barcodeType, date)
                                        cv2.putText(images, textData,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
                                        i+=1
                                        if barcodeData  is not None:
                                                if barcodeData:
                                                        winsound.Beep(frequency,duration)
                                        self.id, self.department, self.name, self.position, self.contact=barcodeData.split(" ")
                                       
                                cv2.imshow("QRCODE SCANNER", images)
                                key=cv2.waitKey(1) & 0xFF
                                if key==ord('q'):
                                        cv2.destroyAllWindows()
                                        vs.stop()
                                        break  
                                        
                        vs.stop()   
                        cv2.destroyAllWindows()
                        self.mark()

        ################################### Function to see if data on barcode is in database  ####################################
    def mark(self):
                        try:
                                                connect=mysql.connect(host='localhost',
                                                                user='root',
                                                                password='',
                                                                database='employee_attendance')
                                                cursor=connect.cursor()
                                                cursor.execute("SELECT * FROM employees WHERE id_number=%s", ((self.id),))
                                                row=cursor.fetchone()
                                                if row is None:
                                                        speak_va("Employee does not exist in the system!!!")
                                                        messagebox.showerror('Error', 'Employee does not Exist, please scan QRcode again ', parent=self.window)
                                                       
                                                else:   
                                                        speak_va("WELCOME "+self.name+". Please scan your face for verification!!!")
                                                        self.showVerification()

                        except Exception as es:
                                                 messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

        ################################### Face Recognition window ####################################
    def showVerification(self):
                        x=pyautogui.size()[0]
                        y=pyautogui.size()[1]
                        self.verify=Toplevel()
                        self.verify.geometry('1200x500+'+str(int(x/2-600))+'+'+str(int(y/2-250)))
                        self.verify.icon=PhotoImage(file='yabatech-logo.png')
                        self.verify.iconphoto(True,self.verify.icon)
                        self.verify.title('Employee Attendance System')
                        self.verify.resizable(FALSE,FALSE)

                        self.img21=Image.open('.//Untitled Export//facerecog.png')
                        self.resize11=self.img21.resize((1200,600), Image.ANTIALIAS)
                        self.new11=ImageTk.PhotoImage(self.resize11)
                        self.labImage11=Label(self.verify, image=self.new11,).pack(fill='both', expand='true')
                        self.labImage11=self.new11 

                        framesverify=Frame(self.verify)
                        framesverify.place(x=20, y=20)
                        verify_Id1=Label(framesverify, text='Employee ID:', font=('Open Sans ExtraBold', 14, 'bold'), fg='green')
                        verify_department1=Label(framesverify, text='Name:', font=('Open Sans ExtraBold', 14, 'bold'), fg='green')
                        verify_name1=Label(framesverify, text='Department:', font=('Open Sans ExtraBold', 14, 'bold'), fg='green')
                        verify_position1=Label(framesverify, text='Position:', font=('Open Sans ExtraBold', 14, 'bold'), fg='green')
                        verify_contact1=Label(framesverify, text='Contact:', font=('Open Sans ExtraBold', 14, 'bold'), fg='green')

                        verify_Id=Label(framesverify, text=self.id, font=('Open Sans ExtraBold', 14, 'bold'))
                        verify_department=Label(framesverify, text=self.name, font=('Open Sans ExtraBold', 14, 'bold'))
                        verify_name=Label(framesverify, text=self.department, font=('Open Sans ExtraBold', 14, 'bold'))
                        verify_position=Label(framesverify, text=self.position, font=('Open Sans ExtraBold', 14, 'bold'))
                        verify_contact=Label(framesverify, text=self.contact, font=('Open Sans ExtraBold', 14, 'bold'))
                        
                        Initiatebutton= Button( self.verify, text='Scan Face for verification', font=('calibre',10, 'bold'),bg='yellow', relief='groove', width=21,
                        command=self.recognizer, activebackground='yellow')

                        verify_Id1.grid(column=0, row=0,sticky='w', padx=3, pady=(0,5))
                        verify_department1.grid(column=0, row=1 ,sticky='w', padx=3, pady=(0,5))
                        verify_name1.grid(column=0, row=2, sticky='w', padx=3, pady=(0,5))
                        verify_position1.grid(column=0, row=3, sticky='w', padx=3, pady=(0,5))
                        verify_contact1.grid(column=0, row=4, sticky='w', padx=3, pady=(0,7))

                        verify_Id.grid(column=1, row=0,sticky='w' , pady=(0,5))
                        verify_department.grid(column=1, row=1 ,sticky='w', pady=(0,5))
                        verify_name.grid(column=1, row=2, sticky='w', pady=(0,5))
                        verify_position.grid(column=1, row=3, sticky='w',  pady=(0,5))
                        verify_contact.grid(column=1, row=4, sticky='w',  pady=(0,7))
                        Initiatebutton.place(x=50,y=400)

                        self.verify.mainloop()

    def recognizer(self):
                        recognizer=cv2.face.LBPHFaceRecognizer_create()
                        recognizer.read('./TrainedImages.xml')
                        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                        font=cv2.FONT_HERSHEY_SIMPLEX

                        # start realtime video capture
                        count=0
                        cam=cv2.VideoCapture(0)
                        cam.set(3,640)
                        cam.set(4,480)
                        minW=0.1 * cam.get(3)
                        minH=0.1 * cam.get(4)

                        while True:
                                ret,img= cam.read()
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces= face_cascade.detectMultiScale(gray,1.6,3, 
                                minSize=(int(minW), int(minH)),flags=cv2.CASCADE_SCALE_IMAGE)
                                for (x,y,w,h) in faces:
                                        cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0),2)
                                        id,predict=recognizer.predict(gray[y:y+h,x:x+w])
                                       
                                        confidence=int((100*(1-predict/300)))
                                        connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                                        cursor=connect.cursor()
                                        cursor.execute("SELECT name FROM employees WHERE id_number="+str(id))
                                        n=cursor.fetchone()
                                        n="+".join(n)

                                        cursor.execute("SELECT department FROM employees WHERE id_number="+str(id))
                                        d=cursor.fetchone()
                                        d="+".join(d)

                                        cursor.execute("SELECT position FROM employees WHERE id_number="+str(id))
                                        p=cursor.fetchone()
                                        p="+".join(p)

                                        cursor.execute("SELECT contact_no FROM employees WHERE id_number="+str(id))
                                        c=cursor.fetchone()
                                        c="+".join(c)

                                        cursor.execute("SELECT id_number FROM employees WHERE id_number="+str(id))
                                        i=cursor.fetchone()
                                        i="+".join(i)

                                        if confidence>77:
                                                cv2.putText(img,f"ID: {i}", (x,y-105),font,0.6,(255,255,255),2)
                                                cv2.putText(img,f"Name: {n}", (x,y-80),font,0.6,(255,255,255),2)
                                                cv2.putText(img,f"Dep: {d}", (x,y-55),font,0.6,(255,255,255),2)
                                                cv2.putText(img,f"Pos: {p}", (x,y-30),font,0.6,(255,255,255),2)
                                                cv2.putText(img,f"Cnt: {c}", (x,y-5),font,0.6,(255,255,255),2)
                                                self.mark_attendance(i,n,d,p,c)
                                                count=+1
                                        else:
                                                cv2.rectangle(img,(x,y),(x+w, y+h), (0,0,255),2)
                                                cv2.putText(img, "Unknown Face", (x,y-5),font,0.6,(255,255,255),2)
                                cv2.imshow('WELCOME TO FACE RECOGNITION', img)
                                
                                if (cv2.waitKey(1)==ord('q')):
                                        break
                                elif count>=1:
                                    break
                        cam.release()
                        cv2.destroyAllWindows()

        ################################### Function to mark attendance after fac verification ####################################                             
    def mark_attendance(self, i,n,d,p,c):
                                from datetime import datetime
                                datin=datetime.now()
                                self.datin=datin.strftime("%I:%M:%S_%p")
                                datout=datetime.now()
                                self.datout=datout.strftime("%I:%M:%S_%p")
                                
                                
                                if (self.id==i) and (self.name==n) and (self.department==d) and (self.position==p):
                                    try:
                                            connect=mysql.connect(host='localhost',
                                                            user='root',
                                                            password='',
                                                            database='employee_attendance')
                                            cursor=connect.cursor()
                                            cursor.execute("SELECT * FROM view_attendance WHERE id_number=%s AND name=%s", ((i,n,)))
                                            row=cursor.fetchall()

                                            if len(row) > 0:
                                                    self.dato=datout.strptime(self.datout,"%I:%M:%S_%p")
                                                    self.Totalhours=(self.dato) - (self.date)
                                                    
                                                    cursor.execute("UPDATE view_attendance SET time_out=%s, total_time=%s WHERE id_number=%s AND name=%s", ((str(self.datout),str(self.Totalhours),i,n,)))
                                                    connect.commit()                                     
                                                    connect.close()
                                                    self.trv2.delete(*self.trv2.get_children())     
                                                    self. showAttendance()
                                                    self.verify.destroy()
                                                    speak_va(n+" Timed out Successfully!!!")
                                                    messagebox.showinfo('Success', 'Employee successfully Time out', parent=self.window)
                                                    self.take_attendance()
                                            else:
                                                    self.date=datin.strptime(self.datin,"%I:%M:%S_%p")
                                                    cursor.execute("""INSERT INTO view_attendance(id_number,department,name,position,contact_no,time_in)
                                                    VALUES(%s,%s,%s,%s,%s,%s)""", ((i, d, n, p, c,str(self.datin))))
                                                    connect.commit()                                     
                                                    connect.close()
                                                    self.trv2.delete(*self.trv2.get_children())     
                                                    self. showAttendance()
                                                    self.verify.destroy()
                                                    speak_va(n+" Timed in Successfully!!!")
                                                    messagebox.showinfo('Success', 'Employee successfully timed in', parent=self.window)
                                                    self.take_attendance()
                                            #call the clear function after message
                                    except Exception as es:
                                        # messagebox.showerror('Error',  'Employee does not exist', parent=self.window)
                                        messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)
                                else:
                                        speak_va("facial identification mismatch!!!")
                                        messagebox.showinfo('Attendance verification', 'Please scan face again', parent=self.window)
                                        
        #################################### function to show the attendance taken on treeview and database  ####################################           
    def showAttendance(self):
                        self.trv2.tag_configure('oddrow', background='#c9c9c9')
                        self.trv2.tag_configure('evenrow', background='white')
                        connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                        cursor=connect.cursor()
                        cursor.execute("SELECT * FROM view_attendance" )
                        row=cursor.fetchall()
                        count=1
                        for rows in row:
                                if count%2==0:
                                        self.trv2.insert(parent="", index='end', text=count ,iid=count, values=(rows), tags=('oddrow'))
                                else:
                                        self.trv2.insert(parent="", index='end', text=count ,iid=count, values=(rows), tags=('evenrow'))
                                count+= 1
                        connect.commit()
                        connect.close()   

    #################################### function to show Todays record  ####################################    
    def ShowToday(self):
                from datetime import date
                self.today=date.today()
                self.searchd=  self.SearchdEntry2.get()
                if self.searchd=='':
                                messagebox.showerror('Error', 'field is required', parent=self.window)

                collected= self.searchByEntry.get()
                
                try:  
                        for rows in self.trv2.get_children():
                                self.trv2.delete(rows)
                        
                        self.trv2.tag_configure('oddrow', background='#c9c9c9')
                        self.trv2.tag_configure('evenrow', background='white')
                        connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                        cursor=connect.cursor()
                        if collected== 'Search by...':
                                cursor.execute("SELECT * FROM view_attendance")
                                messagebox.showinfo('', 'Select SEARCH BY.. option', parent=self.window)
                        if collected=='Employee_ID':
                                cursor.execute("SELECT * FROM view_attendance WHERE date=%s AND id_number=%s",(str(self.today),self.SearchdEntry2.get(),))
                        if collected=='Department':
                                cursor.execute("SELECT * FROM view_attendance WHERE date=%s AND department=%s",(str(self.today), self.SearchdEntry2.get(),))
                        if collected=='Name':
                                cursor.execute("SELECT * FROM view_attendance WHERE date=%s AND name=%s",(str(self.today), self.SearchdEntry2.get(),))
                        row=cursor.fetchall()
                        count=1
                        if len(row)!=0:
                                self.trv2.delete(*self.trv2.get_children())
                        for rows in row:
                                if count%2==0:
                                        self.trv2.insert(parent="", index='end', text='' ,iid=count, values=(rows), tags=('oddrow',))
                                else:
                                        self.trv2.insert(parent="", index='end', text='' , iid=count, values=(rows), tags=('evenrow',))
                                count+= 1
                        connect.commit()
                        connect.close()
                                        
                except Exception as es:
                        messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

        #################################### function to show the attendance base on the date and searchby record ####################################
    def Entersearching(self):
                
                self.date1=self.searchy12Entry.get_date()
                self.date2=self.searchingEntry.get_date()
                self.searchd=  self.SearchdEntry2.get()
                if self.searchd=='':
                                messagebox.showerror('Error', 'field is required', parent=self.window)

                collected= self.searchByEntry.get()
                
                try:  
                        
                        for rows in self.trv2.get_children():
                                self.trv2.delete(rows)
                        self.trv2.tag_configure('oddrow', background='#c9c9c9')
                        self.trv2.tag_configure('evenrow', background='white')
                        connect=mysql.connect(host='localhost',
                                                        user='root',
                                                        password='',
                                                        database='employee_attendance')
                        cursor=connect.cursor()
                        if collected== 'Search by...':
                                cursor.execute("SELECT * FROM view_attendance")
                                messagebox.showinfo('', 'Select SEARCH BY.. option', parent=self.window)
                        if collected=='Employee_ID':
                                cursor.execute("SELECT * FROM view_attendance WHERE id_number=%s AND date BETWEEN '"+str(self.date1)+"'AND'"+str(self.date2)+"'",(self.SearchdEntry2.get(),))
                        if collected=='Department':
                                cursor.execute("SELECT * FROM view_attendance WHERE department=%s AND date BETWEEN '"+str(self.date1)+"'AND'"+str(self.date2)+"'",(self.SearchdEntry2.get(),))
                        if collected=='Name':
                                cursor.execute("SELECT * FROM view_attendance WHERE name=%s AND date BETWEEN '"+str(self.date1)+"'AND'"+str(self.date2)+"'",(self.SearchdEntry2.get(),))
                        row=cursor.fetchall()
                        count=1
                        if len(row)!=0:
                                self.trv2.delete(*self.trv2.get_children())
                        for rows in row:
                                if count%2==0:
                                        self.trv2.insert(parent="", index='end', text='' ,iid=count, values=(rows), tags=('oddrow',))
                                else:
                                        self.trv2.insert(parent="", index='end', text='' , iid=count, values=(rows), tags=('evenrow',))
                                count+= 1
                        connect.commit()
                        connect.close()
                                        
                except Exception as es:
                        messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.window)

 #################################### function to save record as a csv file ####################################
    def export_attendance(self):
                self.date1=self.searchy12Entry.get_date()
                self.date2=self.searchingEntry.get_date()
                self.searchd=  self.SearchdEntry2.get()
        
                collected= self.searchByEntry.get()
        
                for rows in self.trv2.get_children():
                        self.trv2.delete(rows)
                self.trv2.tag_configure('oddrow', background='#c9c9c9')
                self.trv2.tag_configure('evenrow', background='white')
                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                cursor=connect.cursor()
                if collected== 'Search by...':
                        cursor.execute("SELECT * FROM view_attendance")
                        messagebox.showinfo('', 'Please remember to Select SEARCH BY.. option for individual attendance', parent=self.window)
                if collected=='Employee_ID':
                        cursor.execute("SELECT * FROM view_attendance WHERE id_number=%s AND date BETWEEN '"+str(self.date1)+"'AND'"+str(self.date2)+"'",(self.SearchdEntry2.get(),))
                if collected=='Department':
                        cursor.execute("SELECT * FROM view_attendance WHERE department=%s AND date BETWEEN '"+str(self.date1)+"'AND'"+str(self.date2)+"'",(self.SearchdEntry2.get(),))
                if collected=='Name':
                        cursor.execute("SELECT * FROM view_attendance WHERE name=%s AND date BETWEEN '"+str(self.date1)+"'AND'"+str(self.date2)+"'",(self.SearchdEntry2.get(),))
                row=cursor.fetchall()
                count=1
                if len(row)!=0:
                        self.trv2.delete(*self.trv2.get_children())
                for rows in row:
                        if count%2==0:
                                self.trv2.insert(parent="", index='end', text='' ,iid=count, values=(rows), tags=('oddrow',))
                        else:
                                self.trv2.insert(parent="", index='end', text='' , iid=count, values=(rows), tags=('evenrow',))
                        count+= 1
                connect.commit()
                connect.close()
        
                if len(row)==0:
                        messagebox.showerror('No data',"No data available to be exported")
                        
                else:
                        try:
                                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="save CSV", filetypes=(("CSV file","*.csv"),("All files","*.*")))
                                with open(fln,mode="w") as myfile:
                                        exp_writer=csv.writer(myfile, delimiter=",", newline='')
                                        field=['Employee_ID','Department','Name','Position','Contact_no','date','Time-in','Time-out','Total_hours']
                                        writer=csv.DictWriter(myfile,fieldnames=field)
                                        writer.writeheader()
                                        for i in self.trv2.get_children():
                                                row=self.trv2.item(i)['values']
                                                exp_writer.writerow(row)
                                speak_va('Attendance successfully Exported!!!')
                                messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(fln)+" successfully")

                        except FileNotFoundError as es:
                                        pass
        ################################### function to call Email sender window from another file and also for appraisal ##############################################
    def sender(self):
                self.app_screen=Toplevel(self.window)
                self.app=employeeEmail(self.app_screen)

    def Appraise(self):
                self.app_screen=Toplevel(self.window)
                self.app=Appraisal(self.app_screen)     
           
 ####################################### closing the main class window #############################################################        

if __name__=='__main__':
    main()


