from tkinter import *
from time import *
import mysql.connector as mysql
from tkinter import ttk
from tkcalendar import *
import pyautogui


def main():

    window=Tk()
    app=Appraisal(window)
    window.mainloop()

 ########################################Class to define the screen to show first############################################################################
class Appraisal:
                    def __init__(self,window):
                        x=pyautogui.size()[0]
                        y=pyautogui.size()[1]
                        self.verify=window
                        self.verify.geometry('700x400+'+str(int(x/2-600))+'+'+str(int(y/2-250)))
                        self.verify.icon=PhotoImage(file='yabatech-logo.png')
                        self.verify.iconphoto(True,self.verify.icon)
                        self.verify.title('Employee Attendance System')
                        self.verify.resizable(FALSE,TRUE)
                        Title=Label(self.verify, text='Attendance Summary', font=('Open Sans ExtraBold', 13, 'bold'), fg='green')
                        Title.pack(side='top')
                       
                        self.listboxscrollbar=Scrollbar(self.verify, orient=VERTICAL)
                        self.listboxscrollbar1=Scrollbar(self.verify, orient=HORIZONTAL)
                        self.trv3=ttk.Treeview(self.verify, selectmode='extended', yscrollcommand=self.listboxscrollbar.set, xscrollcommand=self.listboxscrollbar1.set)
                        self.trv3['columns']=('Employee-ID', 'Name', 'Department', 'Designation', 'Contact no','no of times present')

                ##################################### Adding scrollbar to treeview ########################################################################
                        self.listboxscrollbar.config(command=self.trv3.yview)
                        self.listboxscrollbar1.config(command=self.trv3.xview)

                        self.listboxscrollbar.pack(side=RIGHT, fill=Y)
                        self.listboxscrollbar1.pack(side=BOTTOM, fill=X)

                ##################################### Adding columns to treeview..####################################
                        self.trv3.column('#0', width=0, stretch='false')
                        self.trv3.column('Employee-ID', width=70, anchor='c')
                        self.trv3.column('Name', width=100, anchor='c')  
                        self.trv3.column('Department', width=125, anchor='c')
                        self.trv3.column('Designation', width=80, anchor='c')
                        self.trv3.column('Contact no', width=100, anchor='c')
                        self.trv3.column('no of times present', width=100, anchor='c')
                
                ##################################### Adding headings for each columns ####################################
                        self.trv3.heading('Employee-ID',text='Employee-ID', anchor='c')
                        self.trv3.heading('Name',text='Name', anchor='c')
                        self.trv3.heading('Department',text='Department', anchor='c')
                        self.trv3.heading('Designation',text='Designation', anchor='c')
                        self.trv3.heading('Contact no',text='Contact no', anchor='c')
                        self.trv3.heading('no of times present',text='no of times present', anchor='c')
                        
                ##################################### Packing The treeview ####################################
                        self.trv3.pack(fill=BOTH,expand=TRUE)
                       
                        connect=mysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='employee_attendance')
                        cursor=connect.cursor()
                        cursor.execute("SELECT id_number,name,department,position,contact_no,COUNT(*) AS Total FROM view_attendance group by id_number")
                        count=1
                        result=cursor.fetchall()
                        for i in result:
                                self.trv3.insert(parent="", index='end', text=count ,iid=count, values=(i))
                                count+=1
                               
                        self.verify.mainloop()
if __name__=='__main__':
    main()