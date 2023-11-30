
from tkinter import *
from PIL import Image, ImageTk
from time import *
import datetime
from tkinter import messagebox
import mysql.connector as mysql
from tkinter import ttk
from tkcalendar import *
import pyautogui


def main():
       
        window=Tk()
        app=AdminData(window)
        window.mainloop()

class AdminData:
    def __init__(self,window):
                x=pyautogui.size()[0]
                y=pyautogui.size()[1]
                self.confirm=window
                self.confirm.icon=PhotoImage(file='yabatech-logo.png')
                self.confirm.iconphoto(True,self.confirm.icon)
                self.confirm.geometry('300x150+'+str(int(x/2-580))+'+'+str(int(y/2-303)))
                self.confirm.title('Retrieve Password')
                self.confirm.resizable(FALSE,FALSE)

                confirm_label=Label(self.confirm,text="WELCOME", font=('new time roman', 25, 'bold'))
                confirm_label.pack(side='top')
              
                confirm_Id=Label(self.confirm, text='Enter your Secret key', font=('Open Sans semiBold', 14,))
                confirm_Id.pack(side='top')

                self.confirm_entry=Entry(self.confirm, width=22, font=('roboto',12))
                self.confirm_entry.pack()
                
                confirm_Enter=Label(self.confirm, text="Tap 'enter' on your keyboard to commence", font=('calibri italic', 11))
                confirm_Enter.pack(pady=(20,0))
                self.confirm.bind("<Return>", self.activity)
                

    def activity(self,event):
          if self.confirm_entry.get()=='':
            messagebox.showerror('Error', 'field is required', parent=self.confirm)
            return
          else:
            try: #link the app to database
                connect=mysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='employee_attendance')
                cursor=connect.cursor() #allows you to manipulate the data on the database
                cursor.execute("SELECT * FROM admin WHERE Secret_key=%s", (self.confirm_entry.get(), ))
                row=cursor.fetchone() #allows you to grab a data on the row of a table on your database
                if row==None:
                     messagebox.showerror('Error', 'Incorrect Secret key')
                     self.confirm_entry.delete(0,END) #a function call to clear the login entry box
                     
                else:     
                    self.AdminActivity()
                    self.confirm.withdraw() #a function call to move to another class verify screen
                    connect.close()  #a function call to close the database connection
            except Exception as es:
                 messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.confirm) #function that displays technical error related to the database connection
                
 
    def AdminActivity(self):
        x=pyautogui.size()[0]
        y=pyautogui.size()[1]
        self.verify=Toplevel()
        self.verify.geometry('1000x700+'+str(int(x/2-500))+'+'+str(int(y/2-370)))
        self.verify.icon=PhotoImage(file='yabatech-logo.png')
        self.verify.iconphoto(True,self.verify.icon)
        self.verify.title('Employee Attendance System')
        self.verify.resizable(FALSE,FALSE)

        
            
 ######################################Frame to show on top of the main verify####################################################################################
        
        Mainfrm4=Frame(self.verify)
        Mainfrm4.pack(fill='both')

  #####################################Text to be shown on top the frame  #####################################################################################       

        lbl=Label( Mainfrm4, font=('Arial bold', 13), bg='green', )
        lbl.pack(fill='both',ipady=12)

        lbl=Label( Mainfrm4, text='ADMIN ACTIVITY',
        font=('Arial bold', 13),fg='white', bg='green' )
        lbl.place(x=100, y=13)

 ##########################################################################################################################
        datef=Label(Mainfrm4, text=day+"-" +mont[month]+"-"+year+"   | ", fg='yellow', bg='green', font=('Tempus Sans ITC',12,'bold' ) )
        datef.place(x=700,y=13)

#t#############################he time to be dispayed on the verifys linked to the class verify ###########################
        self.clock=Label(Mainfrm4, fg='yellow',bg='green', font=('Tempus Sans ITC',12, 'bold'))
        self.clock.place(x=850,y=13)
        self.tick()
 ##########################################################################################################################   

        self.img1=Image.open('yabatech-logo.png')
        self.resize=self.img1.resize((55,40), Image.ANTIALIAS)
        self.new=ImageTk.PhotoImage(self.resize)
#display the yabatech logo to be displayed on the verifys linked to the class verify
        self.labImage=Label(Mainfrm4, image=self.new, bg='green').place(x=10, y=3)
        self.labImage=self.new 

########################################## Employees frame  #########################################################

        frameBody13=Frame(self.verify)
        frameBody13.pack(fill='both', expand='true')

################################## Subframes for register and treeview ############################################################
        frameBody19=Frame(frameBody13, bg='green')
        frameBody21=Frame(frameBody13, bg='green')
       
        frameBody19.place(width= 980,height=150,x=10, y=23)
        frameBody21.place(width= 980,height=428,x=10, y=210)
        
        
########################################## Admin frame entry and buttons ############################################################       
        
        admin_frame=Frame(frameBody19, bg='green', bd=5)
        admin_frame.grid(column=0, row=0, padx=8, pady=(10,2), columnspan=9)

        self.adminLabel=Label(admin_frame,text='Secret Key:', font=('roboto', 12,'bold'), fg='white',bg='green',relief='flat')
        self.adminLabel.grid(column=0, row=0, sticky='w', padx=(0,10),pady=6 )
        self.adminEntry=Entry(admin_frame,width=23, font=('roboto', 11), fg='black',bg='white',relief='flat')
        self.adminEntry.grid(column=1, row=0, sticky='w', padx=(4,10),pady=6 )
        
        self.UserLabel=Label(admin_frame,text='Username:', font=('roboto', 12,'bold'), fg='white',bg='green',relief='flat')
        self.UserLabel.grid(column=2, row=0, sticky='w', padx=(6,10), pady=6)
        self.UserEntry=Entry(admin_frame,width=23, font=('roboto', 11, ), fg='black',bg='white',relief='flat')
        self.UserEntry.grid(column=3, row=0, sticky='w', padx=(4,10), pady=6)
        
        self.deptLabel=Label(admin_frame,text='Department:', font=('roboto',12,'bold'), fg='white',bg='green',relief='flat')
        self.deptLabel.grid(column=4, row=0, sticky='w', padx=(6,4),pady=6 )
        self.deptEntry=ttk.Combobox(admin_frame,width=20, font=('roboto', 11, ))
        self.deptEntry['values']=self.combos_input()
        self.deptEntry.grid(column=5, row=0, sticky='w', padx=(2,10), pady=6)
    
        self.posLabel=Label(admin_frame,text='Designation:', font=('roboto',12,'bold'), fg='white',bg='green',relief='flat')
        self.posLabel.grid(column=0, row=1, sticky='w', padx=(0,10), pady=6)
        self.posEntry=Entry(admin_frame,width=23, font=('roboto', 11, ), fg='black',bg='white',relief='flat')
        self.posEntry.grid(column=1, row=1, sticky='w', padx=(4,10), pady=6)

        self.passLabel=Label(admin_frame,text='Password:', font=('roboto',12, 'bold'), fg='white',bg='green',relief='flat')
        self.passLabel.grid(column=2, row=1, sticky='w', padx=(6,10), pady=6)
        self.passEntry=Entry(admin_frame,width=23, font=('roboto', 11,), fg='black',bg='white',relief='flat')
        self.passEntry.grid(column=3, row=1, sticky='w', padx=(4,10), pady=6)

        self.confLabel=Label(admin_frame,text='Confirm Password:', font=('roboto',12, 'bold'), fg='white',bg='green',relief='flat')
        self.confLabel.grid(column=4, row=1, sticky='w', padx=(6,4), pady=6)
        self.confEntry=Entry(admin_frame,width=21, font=('roboto', 11, ), fg='black',bg='white',relief='flat')
        self.confEntry.grid(column=5, row=1, sticky='w', padx=(2,10), pady=6)

########################################## frame for buttons #########################################################

        adminButtons=Frame(frameBody19, bg='green', bd=5)
        adminButtons.grid(column=0, row=2, padx=0, pady=10, columnspan=9)

        self.UpdateButton= Button(adminButtons, text='Update', font=('calibre',10,'bold' ),bg='yellow', relief='flat', width=12,
        command=self.AdminUpdate, activebackground='yellow')
        self.UpdateButton.grid(column=0, row=0, padx=(10,0))

        self.DeleteButton= Button(adminButtons, text='Delete', font=('calibre',10,'bold' ),bg='yellow', relief='flat', width=12,
        command=self.DeleteAdmin, activebackground='yellow')
        self.DeleteButton.grid(column=1, row=0, padx=(10,0))

        self.Refbutton= Button(adminButtons, text='Refresh', font=('calibre',10, 'bold'), relief='flat',bg='yellow', activebackground='yellow',
          width=12, command=self.adminRefresh)
        self.Refbutton.grid(column=2, row=0, padx=(10,0))

        self.Exitbutton= Button(adminButtons, text='Exit', font=('calibre',10, 'bold'), relief='flat',bg='yellow', activebackground='yellow',
          width=12, command=self.AdminExit)
        self.Exitbutton.grid(column=3, row=0, padx=(10,0))

        
################################################ Beautify Treeview #########################################################      
        self.styling=ttk.Style()
        self.styling.theme_use('default')
        self.styling.configure('Treeview', background='white', foreground='black', fieldbackground='white' )
        self.styling.configure('Treeview.Heading', font=('Calibri', 10, ), background='Yellow' )
        self.styling.map('Treeview', background=[('selected', 'green')])
        
#########################################Treeview creation#################################################################################
        self.listboxscrollbar=Scrollbar(frameBody21, orient=VERTICAL)
        self.listboxscrollbar1=Scrollbar(frameBody21, orient=HORIZONTAL)
        self.trv4=ttk.Treeview(frameBody21, selectmode='extended', yscrollcommand=self.listboxscrollbar.set, xscrollcommand=self.listboxscrollbar1.set)
        self.trv4['columns']=('Admin-ID', 'Username', 'Department', 'Designation', 'Password','Confirm password', 'Last-login',
        'Last-logout')


#####################################adding scrollbar to treeview ########################################################################
        self.listboxscrollbar.config(command=self.trv4.yview)
        self.listboxscrollbar1.config(command=self.trv4.xview)

        self.listboxscrollbar.place(x=950, y=10,height=407,)
        self.listboxscrollbar1.place(x=10, y=400,width=940,)
#####################################adding columns to treeview..####################################
        self.trv4.column('#0', width=0, stretch='false')
        self.trv4.column('Admin-ID', width=50, anchor='c')
        self.trv4.column('Username', width=80, anchor='c')  
        self.trv4.column('Department', width=100, anchor='c')
        self.trv4.column('Designation', width=80, anchor='c')
        self.trv4.column('Password', width=100, anchor='c')
        self.trv4.column('Confirm password', width=100, anchor='c')
        self.trv4.column('Last-login', width=100, anchor='c')
        self.trv4.column('Last-logout', width=100, anchor='c')

 ##################################### adding headings for each columns ####################################
        self.trv4.heading('Admin-ID',text='Admin-ID', anchor='c')
        self.trv4.heading('Username',text='Username', anchor='c')
        self.trv4.heading('Department',text='Department', anchor='c')
        self.trv4.heading('Designation',text='Designation', anchor='c')
        self.trv4.heading('Password',text='Password', anchor='c')
        self.trv4.heading('Confirm password',text='Confirm password', anchor='c')
        self.trv4.heading('Last-login',text='Last-login', anchor='c')
        self.trv4.heading('Last-logout',text='Last-logout', anchor='c')
       
       
 ##################################### packing rhe treeview ####################################
        self.trv4.place(x=10, y=10,height=390, width=940)
        self.showAdmins()
        
        self.trv4.bind("<Double-1>", self.select_Admins)
   
    def combos_input(self):
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

    def showAdmins(self):

                self.trv4.tag_configure('oddrow', background='#c9c9c9')
                self.trv4.tag_configure('evenrow', background='white')
                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM admin" )
                row=cursor.fetchall()
                count=1
                for rows in row:
                        if count%2==0:
                                self.trv4.insert(parent="", index='end', text=count ,iid=count, values=(rows), tags=('oddrow'))
                        else:
                                self.trv4.insert(parent="", index='end', text=count ,iid=count, values=(rows), tags=('evenrow'))
                        count+= 1
                connect.commit()
                connect.close()   

    def select_Admins(self,event):
                self.ClearAdmin()
                selected=self.trv4.identify_row(event.y)
                values=self.trv4.item(selected,'values')
                self.adminEntry.insert(0,values[8])
                self.UserEntry.insert(0,values[1])
                self.deptEntry.insert(0,values[2])
                self.posEntry.insert(0,values[3])
                self.passEntry.insert(0,values[4])
                self.confEntry.insert(0,values[5])
        
                print(values)

    def ClearAdmin(self):
            self.adminEntry.delete(0, END)
            self.UserEntry.delete(0, END) 
            self.deptEntry.delete(0, END) 
            self.posEntry.delete(0, END) 
            self.passEntry.delete(0, END) 
            self.confEntry.delete(0, END) 
           
    def adminRefresh(self):
                connect=mysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='employee_attendance')
                cursor=connect.cursor()
                cursor.execute("SELECT * FROM admin")
                rows=cursor.fetchall()
                connect.commit()
                connect.close()
                self.trv4.delete(*self.trv4.get_children())
                self.showAdmins()
                self.ClearAdmin()

    def AdminUpdate(self):
            if  self.adminEntry.get()=="" :
                               messagebox.showerror('Error', 'All fields are required', parent=self.verify)
            else:   
                        try:
                                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                                cursor=connect.cursor()
                                cursor.execute("SELECT * FROM admin")
                                row=cursor.fetchall()
                                if row==None:
                                        messagebox.showerror('Error', 'Employee already Exist, please try with another employee ', parent=self.verify)
                                        #call the clear function to clear the entry box after message pops up 
                                else:
                                        selected=self.trv4.focus()
                                        values=self.trv4.item(selected,'values')
                                        self.trv4.item(selected,values=(self.adminEntry.get(),self.UserEntry.get(),self.deptEntry.get(),self.posEntry.get(),
                                        self.passEntry.get(),self.confEntry.get() ))

                                        cursor.execute("""UPDATE admin SET username=%s,department=%s,position=%s,password=%s,
                                        confirm_password=%s, Secret_key=%s WHERE  Admin_id=%s""",(self.UserEntry.get(),
                                                                                    self.deptEntry.get(),
                                                                                    self.posEntry.get(),
                                                                                    self.passEntry.get(),
                                                                                    self.confEntry.get(), 
                                                                                    self.adminEntry.get(),
                                                                                    values[0]),)                      
                                        connect.commit()
                                        connect.close()
                                        messagebox.showinfo('Success', 'Admin successfully Updated', parent=self.verify)
                                        
                                        self.ClearAdmin() #call the clear function after message
                        except Exception as es:
                                pass

    def DeleteAdmin(self):
                        try:
                                response= messagebox.askyesno('Delete Admin', 'are you sure you want to delete Admin')
                                if response==1:
                                        #point to selection on treeview
                                        x=self.trv4.selection()
                                        #create list of ids
                                        ids_to_delete=[]
                                        #add selction to id_to_delete list
                                        for row in x:
                                                ids_to_delete.append(self.trv4.item(row, 'values')[0])
                                        #delete from treeview
                                        for row in x:
                                                self.trv4.delete(row)
                                        messagebox.showinfo('Success', 'Delete successful', parent=self.verify)
                                else:
                                        return True
                                self.ClearAdmin() #call the clear function after message
                                connect=mysql.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='employee_attendance')
                                cursor=connect.cursor()
                                cursor.execute("SELECT * FROM admin" )
                                row=cursor.fetchall()
                                #Delete everything from the table
                                cursor.executemany("DELETE FROM admin WHERE Admin_id=%s", ([(a,) for a in ids_to_delete]))
                                connect.commit()
                                connect.close()

                        except Exception as es:
                                messagebox.showerror('Error',  f'Error Due to: {str(es)}', parent=self.verify)

    def AdminExit(self):
        global window
        aExit=messagebox.askquestion('Confirm', 'Are you sure you want to Exit?')
        if aExit=='yes':
            self.verify.destroy()
            self.confirm.destroy()
        else:
            return

    def tick(self):
        time=strftime('%I:%M:%S  %p')
        self.clock.config(text=time)
        self.clock.after(200,self.tick)


ts=time()
date=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year=date.split('-')
mont={'01':'january', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July',
'08':'August', '09':'September', '10':'October', '11':'November', '12':'December',
}

if __name__=='__main__':
    main()
