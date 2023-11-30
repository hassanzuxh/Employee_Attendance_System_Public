from tkinter import *
from PIL import Image, ImageTk
from time import *
import datetime
from tkcalendar import *
import pyautogui
from tkinter import messagebox,filedialog
from pygame import mixer
from email.message import EmailMessage
import smtplib
import os
import imghdr
import pandas
import speech_recognition





def main():
    global check
    check=False
    window=Tk()
    app=employeeEmail(window)
    window.mainloop()

 ########################################Class to define the screen to show first############################################################################
class employeeEmail:
        def __init__(self,window):
                x=pyautogui.size()[0]
                y=pyautogui.size()[1]
                self.email=window
                self.email.geometry('1000x700+'+str(int(x/2-500))+'+'+str(int(y/2-370)))
               
                self.email.title('Employee Attendance System')
                self.email.resizable(FALSE,FALSE)


        ########################################## General frame  #########################################################
                Mainfrm4=Frame(self.email)
                Mainfrm4.pack(fill='both')

  ##################################### Text,frame,time,date and logo to be shown on top the frame  #####################################################################################       
                #frame
                lbl=Label( Mainfrm4, font=('Arial bold', 13), bg='Yellow', )
                lbl.pack(fill='both',ipady=12)

                #Logo and Text
                self.imgLOGO=Image.open('.//Untitled Export//email.png')
                self.resizeLOGO=self.imgLOGO.resize((50,40), Image.ANTIALIAS)
                self.newLOGO=ImageTk.PhotoImage(self.resizeLOGO)
                lblLOGO=Label( Mainfrm4,text='    EMAIL SENDER' ,image=self.newLOGO,compound=LEFT,font=('Roboto', 18, 'bold'),fg='#286b12', bg='Yellow' )
                lblLOGO.place(x=320, y=3)

                #Executable Logo
                self.imgSETTINGS=Image.open('.//Untitled Export//setting.png')
                self.resizeSETTING=self.imgSETTINGS.resize((50,40), Image.ANTIALIAS)
                self.newSETTING=ImageTk.PhotoImage(self.resizeSETTING)
                SettingButton=Button(Mainfrm4,image=self.newSETTING,bd=0,bg='yellow',cursor='hand2',activebackground='yellow',command=self.settings)
                SettingButton.place(x=590, y=3)
                
                #Date
                datef=Label(Mainfrm4, text=day+"-" +mont[month]+"-"+year+"   | ", fg='green', bg='yellow', font=('Tempus Sans ITC',12,'bold' ) )
                datef.place(x=700,y=13)

                #Time
                self.Time=Label(Mainfrm4, fg='green',bg='Yellow', font=('Tempus Sans ITC',12, 'bold'))
                self.Time.place(x=850,y=13)
                self.tick()

                # Yabatech logo 
                self.img1=Image.open('yabatech-logo.png')
                self.resize=self.img1.resize((55,40), Image.ANTIALIAS)
                self.new=ImageTk.PhotoImage(self.resize)
                self.labImage=Label(Mainfrm4, image=self.new, bg='yellow').place(x=20, y=3)
                self.labImage=self.new 
               
        ################################## Body Subframes   ############################################################
                frameBody13=Frame(self.email)
                frameBody13.pack(fill='both', expand='true')

         ################################## images, buttons, textboxes, and entryboxes on subframe ############################################################
                #Background Image
                self.img21=Image.open('.//Untitled Export//project.jpg')
                self.resize11=self.img21.resize((1000,650), Image.ANTIALIAS)
                self.new11=ImageTk.PhotoImage(self.resize11)
                self.labImage11=Label(frameBody13, image=self.new11,).pack(fill='both', expand='true')
                self.labImage11=self.new11 

                #Radio buttons
                self.choice=StringVar()
                singleRadioButton=Radiobutton(frameBody13,text='Single',font=('roboto',20,'bold')
                              ,variable=self.choice,value='single',bg='white',activebackground='white',fg='green',
                              command=self.button_check)
                singleRadioButton.place(x=200, y=60)

                multipleRadioButton=Radiobutton(frameBody13,text='Multiple',font=('roboto',20,'bold')
                                        ,variable=self.choice,value='multiple',bg='white',activebackground='white',fg='green',
                                                command=self.button_check)
                multipleRadioButton.place(x=600, y=60)

                self.choice.set('single')

                #Entry frame for  receivers Address
                self.toLabelFrame=LabelFrame(frameBody13,text='To (Email Address)',font=('roboto',16,'bold'),bd=0,fg='white',bg='green')
                self.toLabelFrame.place(x=197, y=170)

                self.toEntryField=Entry(self.toLabelFrame,font=('roboto',18,'bold'),width=30, relief='groove')
                self.toEntryField.grid(row=0,column=0)

                #image for Button
                self.imgBrowse=Image.open('.//Untitled Export//browse.png')
                self.resizeBrowse=self.imgBrowse.resize((40,35), Image.ANTIALIAS)
                self.newBrowse=ImageTk.PhotoImage(self.resizeBrowse)
                self.browseButton=Button(self.toLabelFrame,text=' Browse',image=self.newBrowse,compound=LEFT,font=('arial',12,'bold'),
                cursor='hand2',bd=0,bg='green',activebackground='green',state=DISABLED,command=self.browse,fg='white')
                self.browseButton.grid(row=0,column=1,padx=20)

                #Entry Frame for sender Address
                subjectLabelFrame=LabelFrame(frameBody13,text='Subject',font=('roboto',16,'bold'),bd=0,fg='white',bg='green')
                subjectLabelFrame.place(x=250,y=250)

                self.subjectEntryField=Entry(subjectLabelFrame,font=('roboto',18,'bold'),width=30, relief='groove')
                self.subjectEntryField.grid(row=0,column=0)

                #frame for Compose Email Textbox
                emailLabelFrame=LabelFrame(frameBody13,text='Compose Email',font=('roboto',16,'bold'),bd=2,fg='white',bg='green')
                emailLabelFrame.place(x=120,y=350)

                #images for speak button
                self.imgSpeak=Image.open('.//Untitled Export//mic.png')
                self.resizeSpeak=self.imgSpeak.resize((35,30), Image.ANTIALIAS)
                self.newSpeak=ImageTk.PhotoImage(self.resizeSpeak)
                Button(emailLabelFrame,text=' Speak',image=self.newSpeak,compound=LEFT,font=('arial',12,'bold'),
                cursor='hand2',bd=0,bg='green',activebackground='green',command=self.speak).grid(row=0,column=0)

                #images for Attachment button
                self.imgAttach=Image.open('.//Untitled Export//attachments.png')
                self.resizeAttach=self.imgAttach.resize((35,30), Image.ANTIALIAS)
                self.newAttach=ImageTk.PhotoImage(self.resizeAttach)
                Button(emailLabelFrame,text=' Attachment',image=self.newAttach,compound=LEFT,font=('arial',12,'bold'),
                cursor='hand2',bd=0,bg='green',activebackground='green',command=self.attachment).grid(row=0,column=1)

                #Textbox
                self.textarea=Text(emailLabelFrame,font=('times new roman',14,),height=8,)
                self.textarea.grid(row=1,column=0,columnspan=2)

                #Send mail button image
                Button(frameBody13,text='send Email',font=('arial',12,'bold'),relief='groove',width=12,
                cursor='hand2',bd=0,bg='yellow',activebackground='yellow',command=self.send_email).place(x=600,y=600)

                #clear button image
                Button(frameBody13,text='Clear',font=('arial',12,'bold'),relief='groove',width=12,
                cursor='hand2',bd=0,bg='yellow',activebackground='yellow',command=self.clear).place(x=730,y=600)
                
                #Exit button image
                Button(frameBody13,text='Exit',font=('arial',12,'bold'),relief='groove',width=12,
                cursor='hand2',bd=0,bg='yellow',activebackground='yellow',command=self.iexit).place(x=860,y=600)

                #Label to display extra Email info
                self.totalLabel=Label(frameBody13,font=('roboto',14,'bold'),bg='white',fg='black')
                self.totalLabel.place(x=10,y=600)

                self.sentLabel=Label(frameBody13,font=('roboto',14,'bold'),bg='white',fg='black')
                self.sentLabel.place(x=100,y=600)

                self.leftLabel=Label(frameBody13,font=('roboto',14,'bold'),bg='white',fg='black')
                self.leftLabel.place(x=190,y=600)

                self.failedLabel=Label(frameBody13,font=('roboto',14,'bold'),bg='white',fg='black')
                self.failedLabel.place(x=280,y=600)

         ########################################### FUNCTIONS ########################################
       
        #clear entry and textboxes
        def clear(self):
                self.toEntryField.delete(0,END)
                self.subjectEntryField.delete(0,END)
                self.textarea.delete(1.0,END)

        #Exit windows
        def iexit(self):
                result=messagebox.askyesno('Notification','Do you want to exit?')
                if result:
                        self.email.destroy()
                else:
                        pass
        
        #speak
        def speak(self):
                mixer.init()
                mixer.music.load('music1.mp3')
                mixer.music.play()
                sr=speech_recognition.Recognizer()
                with speech_recognition.Microphone() as m:
                        try:
                                sr.adjust_for_ambient_noise(m,duration=0.2)
                                audio=sr.listen(m)
                                text=sr.recognize_google(audio)
                                self.textarea.insert(END,text+'.')

                        except:
                                 pass
                
        #Radiobutton function
        def button_check(self):
                if self.choice.get()=='multiple':
                        self.browseButton.config(state=NORMAL)
                        self.toEntryField.config(state='readonly')

                if self.choice.get()=='single':
                        self.browseButton.config(state=DISABLED)
                        self.toEntryField.config(state=NORMAL)
        
        #def browse
        def browse(self):
                global final_emails
                path=filedialog.askopenfilename(initialdir='c:/',title='Select csv File')
                if path=='':
                        messagebox.showerror('Error','Please select an Excel File')

                else:
                        data=pandas.read_excel(path)
                        if 'Email' in data.columns:
                                emails=list(data['Email'])
                                final_emails=[]
                                for i in emails:
                                        if pandas.isnull(i)==False:
                                                final_emails.append(i)

                                if len(final_emails)==0:
                                        messagebox.showerror('Error','File does not contain any email addresses')

                                else:
                                        self.toEntryField.config(state=NORMAL)
                                        self.toEntryField.insert(0,os.path.basename(path))
                                        self.toEntryField.config(state='readonly')
                                        self.totalLabel.config(text='Total: '+str(len(final_emails)))
                                        self.sentLabel.config(text='Sent:')
                                        self.leftLabel.config(text='Left:')
                                        self.failedLabel.config(text='Failed:')

        #attachment
        def attachment(self):
                global filename,filetype,filepath,check
                check=True

                filepath=filedialog.askopenfilename(initialdir='c:/',title='Select File')
                filetype=filepath.split('.')
                filetype=filetype[1]
                filename=os.path.basename(filepath)
                self.textarea.insert(END,f'\n{filename}\n')

        #settings
        def settings(self):
                def clear1():
                        fromEntryField.delete(0,END)
                        passwordEntryField.delete(0,END)

                def save():
                        if fromEntryField.get()=='' or passwordEntryField.get()=='':
                                 messagebox.showerror('Error','All Fields Are Required',parent=root1)

                        else:
                                f=open('credentials.txt','w')
                                f.write(fromEntryField.get()+','+passwordEntryField.get())
                                f.close()
                                messagebox.showinfo('Information','CREDENTIALS SAVED SUCCESSFULLY',parent=root1)

                root1=Toplevel()
                root1.title('Setting')
                root1.geometry('580x340+350+90')

                root1.config(bg='green')

                Label(root1,text='Credential Settings',image=self.newLOGO,compound=LEFT,font=('goudy old style',40,'bold'),
                        fg='white',bg='gray20').grid(padx=60)

                fromLabelFrame = LabelFrame(root1, text='From (Email Address)', font=('roboto', 16, 'bold'), bd=0, fg='white',
                                        bg='green')
                fromLabelFrame.grid(row=1, column=0,pady=20)

                fromEntryField = Entry(fromLabelFrame, font=('times new roman', 18, 'bold'), width=30)
                fromEntryField.grid(row=0, column=0)

                passwordLabelFrame = LabelFrame(root1, text='Password', font=('times new roman', 16, 'bold'), bd=0,
                                                fg='white',
                                                bg='green')
                passwordLabelFrame.grid(row=2, column=0, pady=20)

                passwordEntryField = Entry(passwordLabelFrame, font=('times new roman', 18, 'bold'), width=30,show='*')
                passwordEntryField.grid(row=0, column=0)

                Button(root1,text='Save',font=('roboto',16,'bold'),cursor='hand2',bg='gold2',fg='black'
                        ,command=save).place(x=200,y=280)
                Button(root1,text='Clear',font=('roboto',16,'bold'),cursor='hand2',bg='gold2',fg='black'
                        ,command=clear1).place(x=300,y=280)

                f=open('credentials.txt','r')
                for i in f:
                        credentials=i.split(',')

                fromEntryField.insert(0,credentials[0])
                passwordEntryField.insert(0,credentials[1])

                #send Email
        def send_email(self):
                        if self.toEntryField.get()=='' or self.subjectEntryField.get()=='' or self.textarea.get(1.0,END)=='\n':
                                messagebox.showerror('Error','All Fields Are Required',parent=self.email)

                        else:
                                if self.choice.get()=='single':
                                        result=self.sendingEmail(self.toEntryField.get(),self.subjectEntryField.get(),self.textarea.get(1.0,END))
                                        if result=='sent':
                                                messagebox.showinfo('Success','Email is sent successfulyy')

                                        if result=='failed':
                                                messagebox.showerror('Error','Email is not sent.')

                                if self.choice.get()=='multiple':
                                        sent=0
                                        failed=0
                                        for x in final_emails:
                                                result=self.sendingEmail(x,self.subjectEntryField.get(),self.textarea.get(1.0,END))
                                                if result=='sent':
                                                         sent+=1
                                                if result=='failed':
                                                        failed+=1

                                                self.totalLabel.config(text='')
                                                self.sentLabel.config(text='Sent:' + str(sent))
                                                self.leftLabel.config(text='Left:' + str(len(final_emails) - (sent + failed)))
                                                self.failedLabel.config(text='Failed:' + str(failed))

                                                self.totalLabel.update()
                                                self.sentLabel.update()
                                                self.leftLabel.update()
                                                self.failedLabel.update()

                                        messagebox.showinfo('Success','Emails are sent successfully')
        #sending Emails
        def sendingEmail(toAddress,subject,body):
                f=open('credentials.txt','r')
                for i in f:
                        credentials=i.split(',')

                message=EmailMessage()
                message['subject']=subject
                message['to']=toAddress
                message['from']=credentials[0]
                message.set_content(body)
                if check:
                        if filetype=='png' or filetype=='jpg' or filetype=='jpeg':
                                f=open(filepath,'rb')
                                file_data=f.read()
                                subtype=imghdr.what(filepath)


                                message.add_attachment(file_data,maintype='image',subtype=subtype,filename=filename)

                        else:
                                f = open(filepath, 'rb')
                                file_data = f.read()
                                message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=filename)


                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login(credentials[0],credentials[1])
                s.send_message(message)
                x=s.ehlo()
                if x[0]==250:
                        return 'sent'
                else:
                        return 'failed'

        #To automate time count  
        def tick(self):
                time=strftime('%I:%M:%S  %p')
                self.Time.config(text=time)
                self.Time.after(200,self.tick)  

              
 ########################################################################################################################## 
    

 ######################description of what the date should look like when called to be displayed on the screen#############      
ts=time()
date=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year=date.split('-')
mont={'01':'january', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July',
'08':'August', '09':'September', '10':'October', '11':'November', '12':'December',}
      
 ########################################################################################################################## 
        

if __name__=='__main__':
    main()