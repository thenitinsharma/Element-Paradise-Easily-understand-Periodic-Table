from tkinter import*
from tkinter import font 
from tkinter.ttk import Progressbar
from tkinter import ttk
from PIL import Image,ImageTk
from KEEpydb import KEEpydb
import tkinter as tk
import Periodictable
import pygame
import random
import time
import PIL
import webbrowser
from tkinter import PhotoImage
from getdata import get
from getdata import getno
from tkinter import messagebox


# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

win=Tk()


width_of_window = 427
height_of_window = 250
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
win.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


win.overrideredirect(1)

'''
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='green') #4f4f4f'''
progress=Progressbar(win,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

def new_win():

    # setting root window:
    root =Tk()
    root.title("Element Paradise")
    #root.iconbitmap("periodic-table.ico")
    #root.geometry("1395x700+0+0")
    root.state("zoomed")
    #root.configure(bg='white')

    
    # loading Navbar icon image:
    navIcon =ImageTk.PhotoImage(Image.open("open1.png").resize((30,30),Image.ANTIALIAS))
    closeIcon =ImageTk.PhotoImage(Image.open("close.png").resize((30,30),Image.ANTIALIAS))

    # setting switch function:
    # top Navigation bar:
    topFrame =Frame(root, bg=color["orange"])
    topFrame =Frame(root, bg=color["orange"])
    topFrame.pack(side="top", fill= X)


    # Header label text:
    homeLabel = Label(topFrame, text="Element Paradise", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
    homeLabel.pack(side="right")

    # Main label :

    ##########################################  Placing background image  #################################################
    
    photo=ImageTk.PhotoImage(Image.open("background7.jpg").resize((1363,500),Image.ANTIALIAS))

    background_label=Label(root,image=photo)
    background_label.place(x=0,y=200)

    welcome_frame=Frame(root,bg="white",height=200,highlightthickness=5,highlightbackground="Blue",width=1370,cursor="hand2").place(x=0,y=45)
    welcome=ImageTk.PhotoImage(Image.open("intro1.png").resize((1356,110),Image.ANTIALIAS))
    banner_label=Label(welcome_frame,image=welcome)
    banner_label.place(x=5,y=51)
        
    ####################################### Main window of Searching Element Info ######################################


    def search():
        """This function is used to create Window for Searching element Information"""
        #search_root.iconbitmap("periodic-table.ico")
        f2=Frame(root,width=1395,height=700,bg='#12c4c0')
        f2.place(x=0,y=0)

        
        def destroy():
            f2.destroy()
        def callback(url):
            webbrowser.open_new_tab(url)
        def searchbyname():
                f3=Frame(f2,width=1395,height=700,bg='#12c4c0')
                f3.place(x=590,y=50)
                Label(f3,text=" Search🔎Using Element Name ",fg="White",bg="#12c4c0",font=" verdana 18 ",padx=200,pady=10).place(x=0,y=0)
                ExampleEntry=StringVar()
                ExampleEntry.set("Enter Element Name")
                entry=Entry(f3,textvariable=ExampleEntry,bg='White',highlightthickness=5,highlightbackground="Blue",highlightcolor="green",width=50,font=("cascadiacode  12 "))
                entry.place(x=100,y=150,height=50)
                entry.bind('<Button-1>',lambda e:ExampleEntry.set(""))
                name_var=StringVar()
                root.bind('<Return>',lambda e:submit())
                def submit():
                    name=ExampleEntry.get()
                    try:
                        data=get(name)
                        data['Element Symbol ']
                    except:
                        data={'Element Symbol ':'NotFound',
                        'Element Name':'NotFound',
                        'Atomic No.':'NotFound',
                        'Atomic Weight':'NotFound',
                        'State':'NotFound',
                        'Category':'NotFound'
                        }
                    Label(f3,bg='#12c4c0',text='Element Symbol : '+str(data['Element Symbol '])+'                ',font="Arial 10 bold").place(x=100,y=200)
                    Label(f3,bg='#12c4c0',text='Element Name : '+str(data['Element Name'])+'                ',font="Arial 10 bold").place(x=100,y=220)
                    Label(f3,bg='#12c4c0',text='Atomic No : '+str(data['Atomic No.'])+'                ',font="Arial 10 bold").place(x=100,y=240)
                    Label(f3,bg='#12c4c0',text='Atomic Weight : '+str(data['Atomic Weight'])+'                ',font="Arial 10 bold").place(x=100,y=260)
                    Label(f3,bg='#12c4c0',text='State : '+str(data['State'])+'                ',font="Arial 10 bold").place(x=100,y=280)
                    Label(f3,bg='#12c4c0',text='Category : '+str(data['Category'])+'                ',font="Arial 10 bold").place(x=100,y=300)
                sub=Button(f3,text="Submit",command=submit,bg='white',fg='Blue',font='verdana 18 bold',padx=18).place(x=600,y=150)

        def searchbynumber():
                    """This Function is used to Create Window for Search Element By Element Atmic Number """
                    #top1.iconbitmap("periodic-table.ico")
                    f4=Frame(f2,width=1395,height=700,bg='#12c4c0')
                    f4.place(x=590,y=50)
                    Label(f4,text=" Search🔎Using Atomic Number ",fg="White",bg="#12c4c0",font=" verdana 18 ",padx=200,pady=10).place(x=0,y=0)

                    ExampleEntry=StringVar()
                    ExampleEntry.set("Enter atomic number")
                    entry=Entry(f4,bg='White',highlightthickness=5,highlightbackground="Blue",highlightcolor="green",textvariable=ExampleEntry,width=50,font=("cascadiacode 12"))
                    entry.place(x=100,y=150,height=50)
                    entry.bind('<Button-1>',lambda e:ExampleEntry.set(""))
                    root.bind('<Return>',lambda e:submit())
                    def submit():
                        atomic_number=ExampleEntry.get()
                        try:
                            data=getno(int(atomic_number))
                            data['Element Symbol ']
                        except:
                            data={'Element Symbol ':'NotFound',
                            'Element Name':'NotFound',
                            'Atomic No.':'NotFound',
                            'Atomic Weight':'NotFound',
                            'State':'NotFound',
                            'Category':'NotFound'
                            }
                        

                        Label(f4,bg='#12c4c0',text='Element Symbol : '+str(data['Element Symbol '])+'                ',font="Arial 10 bold").place(x=100,y=200)
                        Label(f4,bg='#12c4c0',text='Element Name : '+str(data['Element Name'])+'                ',font="Arial 10 bold").place(x=100,y=220)
                        Label(f4,bg='#12c4c0',text='Atomic No : '+str(data['Atomic No.'])+'                ',font="Arial 10 bold").place(x=100,y=240)
                        Label(f4,bg='#12c4c0',text='Atomic Weight : '+str(data['Atomic Weight'])+'                ',font="Arial 10 bold").place(x=100,y=260)
                        Label(f4,bg='#12c4c0',text='State : '+str(data['State'])+'                ',font="Arial 10 bold").place(x=100,y=280)
                        Label(f4,bg='#12c4c0',text='Category : '+str(data['Category'])+'                ',font="Arial 10 bold").place(x=100,y=300)
                        
                    sub=Button(f4,text="Submit",command=submit,bg='white',fg='Blue',font='verdana 18 bold',padx=18).place(x=600,y=150)
    
      
        Label(f2,text="Search Element to get its information",fg="White",bg="blue",font="Forte 18 ",padx=650,pady=10).place(x=0,y=0)
        link=Label(f2,text="For More Information about Periodic Table Click Here",fg="purple",font="Arial 13 ",bg="white")
        link.bind("<Button-1>",lambda e:
        callback("https://en.wikipedia.org/wiki/Periodic_table"))
        link.place (x=900,y=670)
        Button(f2,text='Search using Element Name 🔎',borderwidth=5,font="verdana 18 ",fg="blue",command=searchbyname,cursor="hand2",bg="white",padx=10,pady=10).place(x=100,y=100)
        
        atm=Button(f2,text='Search using Atomic Number 🔎',borderwidth=5,font="verdana 18 ",fg="blue",command=searchbynumber,cursor="hand2",bg="white",padx=10,pady=10)
        atm.place(x=100,y=200)

        Button(f2,text='Back ⪻',fg='Purple',borderwidth=5,bg='white',command=destroy,font='verdana 18 ',padx=18).place(x=50,y=630)

    def about():
        """This function is used to create about window of Element Paradise App"""
        about=Tk()
        about.iconbitmap("periodic-table.ico")
        about.geometry("1400x700+0+0")
        about.title("About")
        about.configure(bg='white')
        
        def back():
            w=about.destroy()


        label=Label(about,text="About Element Paradise App",fg="White",bg="blue",font="Verdana 20 ",padx=550,pady=10,anchor=CENTER)
        label.grid(row=0,column=0)
        text_label=Label(about,text='''Element Paradise App is made to help student 
        so that they can better understand 
        chemistry by learning element
        information and remember it to become 
        asset in the modern era of science
        And we our creating app for making 
        education or learning chemistry and science easier.....''',fg="white",bg='blue',font="forte 30 ")
        text_label.place(x=200,y=150)
        creator=Label(about,text='Created By-: ',fg='blue',bg='white',font="arial 18 ")
        creator.place(x=850,y=550)
        name=Label(about,text='''Nitin Kumar Sharma
Rohit Sharma''',bg='white',font='verdana 18 ',fg='purple')
        name.place(x=1000,y=550)
        Button(about,text='Back ⪻',borderwidth=5,command=lambda:[back(),about()],font='verdana 12 ',padx=18,bg='white',fg='blue').place(x=50,y=600)

    ############################################## History of Periodic Table ##################################################
    def feedback():
        feed=Toplevel()
        frame_header = ttk.Frame(feed)
        frame_header.pack()
        headerlabel = Label(frame_header, text='Give your FEEDBACK ', foreground='White',background="purple",
                                font=('Verdana 20'),padx=50,pady=10)
        headerlabel.grid(row=0, column=1)
        messagelabel = ttk.Label(frame_header,
                                text='PLEASE TELL US WHAT YOU THINK',
                                foreground='green', font=('Arial', 10))
        messagelabel.grid(row=1, column=1)

        frame_content = ttk.Frame(feed)
        frame_content.pack()
        myvar = StringVar()
        var = StringVar()
        namelabel = ttk.Label(frame_content, text='Name')
        namelabel.grid(row=0, column=0, padx=5, sticky='sw')
        entry_name = Entry(frame_content,highlightthickness=3,highlightbackground="Blue",highlightcolor="green", width=18, font=('Arial', 14), textvariable=myvar)
        entry_name.grid(row=1, column=0)

        emaillabel = ttk.Label(frame_content, text='Email')
        emaillabel.grid(row=0, column=1, sticky='sw')
        entry_email =Entry(frame_content,highlightthickness=3,highlightbackground="Blue",highlightcolor="green", width=20, font=('Arial', 14), textvariable=var)
        entry_email.grid(row=1, column=1)

        commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
        commentlabel.grid(row=2, column=0, sticky='sw')
        textcomment = Text(frame_content, width=55, height=10)
        textcomment.grid(row=3, column=0, columnspan=2)


        textcomment.config(wrap ='word')
        def clear():
            messagebox.showinfo(title='clear', message='Do you want to clear?')
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            textcomment.delete(1.0, END)
            


        def submit():
            print('Name:{}'.format(myvar.get()))
            print('Email:{}'.format(var.get()))
            print('Comment:{}'.format(textcomment.get(1.0, END)))
            messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            textcomment.delete(1.0, END)

        
        submitbutton = ttk.Button(frame_content, text='Submit', command=lambda:[submit(),root.destroy()]).grid(row=4, column=0, sticky='e')
        clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')





    open_button=Button(text='Open Periodic table',borderwidth=5,font="verdana 18 ",command=Periodictable.main,cursor="hand2",fg="white",bg="green",padx=10,pady=10,width=17)
    open_button.place(x=100,y=460)


    search_button=Button(text='Search Element',borderwidth=5,font="verdana 18 ",command=search,cursor="hand2",bg="green",fg="white",padx=10,pady=10,width=17)
    search_button.place(x=100,y=300)


    Button(text='Play Trick song',font="verdana 18 ",borderwidth=5,cursor="hand2",command=lambda:play("Trick song.mp3"),fg="white",bg="green",padx=10,pady=10,width=17).place(x=100,y=380)


    def toggle_win():
        f1=Frame(root,width=300,height=700,bg='#12c4c0')
        f1.place(x=0,y=0)
        

        def bttn(x,y,text,bcolor,fcolor,cmd):
        
            def on_entera(e):
                myButton1['background'] = bcolor #ffcc66
                myButton1['foreground']= '#262626'  #000d33

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground']= '#262626'

            myButton1 = Button(f1,text=text,
                        width=42,
                        height=2,
                        fg='#262626',
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,            
                            command=cmd)
                        
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x,y=y)
        def dele():
            f1.destroy()
            

        bttn(0,154,'A B O U T','#0f9d9a','#12c4c0',lambda:[dele(),about()])
        #bttn(0,117,'C O N T A C T  U S','#0f9d9a','#12c4c0',None)
        bttn(0,190,'F E E D B A C K','#0f9d9a','#12c4c0',feedback)
        #bttn(0,191,'H E L P','#0f9d9a','#12c4c0',None)
        #bttn(0,228,'A C E R','#0f9d9a','#12c4c0',None)
        #bttn(0,265,'A C E R','#0f9d9a','#12c4c0',None)
        
        
        global img2
        img2 = ImageTk.PhotoImage(Image.open("close.png"))

        Button(f1,
            image=img2,
            border=0,
            command=dele, 
            bg='#12c4c0',
            activebackground='#12c4c0').place(x=5,y=10)
    def quiz1():  
         global f2
         f2=Frame(root,width=1395,height=700,bg='#12c4c0')
         f2.place(x=0,y=0)

         wel=Label(f2,text='  W E L C O M E  T O  E L E M E N T  P A R A D I S E  Q U I Z   ',fg="white",bg="#101357") 
         wel.config(font=('Broadway 22'))
         wel.place(relx=0.2,rely=0.02)

         
         wel=Label(f2,text="""  It's
                  A
                                    Quiz
                                                            Time  """,fg="white",bg='#12c4c0') 
         wel.config(font=('Broadway 30'))
         wel.place(x=220,y=250)

         

         start_button=Button(f2,text=" Start Quiz ",command=menu,font="verdana ",width=90,bg="blue",fg="white")
         start_button.place(x=435,y=660)

         back=Button(f2,command=lambda:(f2.destroy(),root()),width=35,text='Back ⪪',font="verdana",bg='blue',fg='white')
         back.place(x=4,y=660)

         

    def menu():
        global f2
        frame=Frame(f2,width=1395,height=700,bg='blue')     
        frame.place(x=0,y=0)
        wel=Label(frame,text='  W E L C O M E  T O  E L E M E N T  P A R A D I S E  Q U I Z   ',fg="white",bg="#101357") 
        wel.config(font=('Broadway 22'))
        wel.place(relx=0.2,rely=0.02)
        f3=Frame(frame,width=1000,height=500)
        f3.place(anchor="c",relx=0.5,rely=0.5)
        f3.config(bg="white")
        level = Label(f3,text='Select your Difficulty Level !!',bg="white",font="verdana 30")
        level.place(relx=0.25,rely=0.1)
        easy_bt=Button(f3,text="Easy Level",command=easy,font='verdana',width=50)
        easy_bt.place(x=300,y=200)
        medium_bt=Button(f3,text="Medium Level",command=medium,font='verdana',width=50)
        medium_bt.place(x=300,y=250)
        Hard_bt=Button(f3,text="Hard Level",command=difficult,font='verdana',width=50)
        Hard_bt.place(x=300,y=300)
        back=Button(f3,command=lambda:(frame.destroy(),quiz1(),root()),text='Back ⪪',font="verdana",bg='blue',fg='white')
        back.place(relx=0.2,rely=0.80)
    
    def easy():
        easy_frame=Frame(root,width=1393,height=700,bg="blue")
        easy_frame.place(x=0,y=0)
        f3=Frame(easy_frame,width=1000,height=500,bg="white")
        f3.place(anchor='c',relx=0.5,rely=0.5)

        def countDown():
            check = 0
            for k in range(20, 0, -1):
            
                if k == 1:
                    check=-1
                timer.configure(text="Time left:"+str(k),font="verdana")
                easy_frame.update()
                time.sleep(1)
            
            timer.configure(text="Times up!")
            if check==-1:
                return (-1)
            else:
                return 0
        global score
        score = 0
    
        easyQ = [
                    [
                        "What is the group atomic number of Carbon ?",
                         "2",
                         "6",
                         "7",
                         "15"
                    ],
                    [
                        "In which group of the modern periodic table are halogens placed?",
                        "16",
                        "18",
                        "1",
                        "17"
                    ],
                    [
                        "The most electropositive halogen is?",
                        "F",
                        "Cl",
                        "Br",
                        "I"
                    ],
                    [
                        "Modern Periodic Law was given by:",
                        "Dalton",
                        "Mendeleev",
                        "Dobereiner",
                        "Mosley"
                    ],
                    [
                        "While going up in a going up in Periodic table .the metallic charater ",
                        "increases",
                        "remains same",
                        "decreases",
                        "first increases then decreases"
                    ], 
                ]
        answer =[
                    "6",
                    "17",
                    "I",
                    "Mosley",
                    "decreases"
                ]
    
        lis=['',0,1,2,3,4]
        x=random.choice(lis[1:])

        ques=Label(f3,text=easyQ[x][0],font="verdana 20",bg="white")
        ques.place(relx=0.5,rely=0.2,anchor=CENTER)

        var=StringVar()

        a=Radiobutton(f3,text=easyQ[x][1],value=easyQ[x][1],variable = var,font="verdana 15",bg="white")
        a.place(relx=0.5,rely=0.42,anchor=CENTER)

        b=Radiobutton(f3,text=easyQ[x][2],value=easyQ[x][2],variable = var,font="verdana 15",bg="white")
        b.place(relx=0.5,rely=0.52,anchor=CENTER)

        c=Radiobutton(f3,text=easyQ[x][3],value=easyQ[x][3],variable = var,font="verdana 15",bg="white")
        c.place(relx=0.5,rely=0.62,anchor=CENTER)

        d=Radiobutton(f3,text=easyQ[x][4],value=easyQ[x][4],variable = var,font="verdana 15",bg="white")
        d.place(relx=0.5,rely=0.72,anchor=CENTER)

        lis.remove(x)

        timer=Label(f3)
        timer.place(relx=0.8,rely=0.82,anchor=CENTER)

        def display():
        
            if len(lis) == 1:
                    easy_frame.destroy()
                    showMark(score)
            if len(lis) == 2:
                 nextQuestion.configure(text='End',command=calc,font="verdana 10")
                
            if lis:
                x = random.choice(lis[1:])
                ques.configure(text =easyQ[x][0])
            
                a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
                b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
                c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
                d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
                lis.remove(x)
                print(lis)
                y = countDown()
                if y == -1:
                    display()

            
        def calc():
            global score
            if (var.get() in answer):
                score+=1
            display()
    
        submit = Button(f3,command=calc,text="Submit",font="verdana",width=20)
        submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
        nextQuestion = Button(f3,command=display,text="Next",font="verdana",width=5)
        nextQuestion.place(relx=0.90,rely=0.82,anchor=CENTER)

        back=Button(f3,command=lambda:(menu(),easy_frame.destroy(),root()),text='Back ⪪',font="verdana",bg='blue',fg='white')
        back.place(relx=0.2,rely=0.80)
    
    
        y = countDown()
        if y == -1:
            display()

            
    def medium():
        global f2
        medium_frame=Frame(f2,width=1393,height=700,bg="blue")
        medium_frame.place(x=0,y=0)
        #easy_frame.configure(bg="blue")
        f3=Frame(medium_frame,width=1000,height=500,bg="white")
        f3.place(anchor='c',relx=0.5,rely=0.5)
        def countDown():
            check = 0
            for k in range(20, 0, -1):
                
                if k == 1:
                    check=-1
                timer.configure(text="Time left:"+str(k),font="verdana")
                medium_frame.update()
                time.sleep(1)
                
            timer.configure(text="Times up!")
            if check==-1:
                return (-1)
            else:
                return 0
        global score
        score = 0
    
        mediumQ = [
                    [
                        "How many elements are present in the sixth period of the modern periodic table?",
                         "18",
                         "22",
                         "32",
                         "36"
                    ],
                    [
                        "Which non-metal exist in liquid state at room temperature?",
                        "Mercury",
                        "Iodine",
                        "Bromine",
                        "Chlorine"
                    ],
                    [
                        "The valency of noble gas elements is?",
                        "3",
                        "2",
                        "1",
                        "0"
                    ],
                    [
                        "Which of the following element has zero valency?",
                        "Lithium",
                        "Beryllium",
                        "Helium",
                        "Fluorine"
                    ],
                    [
                        "Elements on the right side of Periodic Table are__",
                        "Metals",
                        "Non-Metals",
                        "Semi Metals",
                        "Non-Metals"
                    ], 
                ]
        answer =[
                "32",
                "Bromine",
                "1",
                "Helium",
                "Non-Metals"
                ]
    
        lis=['',0,1,2,3,4]
        x=random.choice(lis[1:])

        ques=Label(f3,text=mediumQ[x][0],font="verdana 20",bg="white")
        ques.place(relx=0.5,rely=0.2,anchor=CENTER)

        var=StringVar()

        a=Radiobutton(f3,text=mediumQ[x][1],value=mediumQ[x][1],variable = var,font="verdana 15",bg="white")
        a.place(relx=0.5,rely=0.42,anchor=CENTER)

        b=Radiobutton(f3,text=mediumQ[x][2],value=mediumQ[x][2],variable = var,font="verdana 15",bg="white")
        b.place(relx=0.5,rely=0.52,anchor=CENTER)

        c=Radiobutton(f3,text=mediumQ[x][3],value=mediumQ[x][3],variable = var,font="verdana 15",bg="white")
        c.place(relx=0.5,rely=0.62,anchor=CENTER)

        d=Radiobutton(f3,text=mediumQ[x][4],value=mediumQ[x][4],variable = var,font="verdana 15",bg="white")
        d.place(relx=0.5,rely=0.72,anchor=CENTER)

        lis.remove(x)

        timer=Label(f3)
        timer.place(relx=0.8,rely=0.82,anchor=CENTER)

        def display():
        
            if len(lis) == 1:
                    medium_frame.destroy()
                    showMark(score)
            if len(lis) == 2:
                nextQuestion.configure(text='End',command=calc,font="verdana 10")
                
            if lis:
                x = random.choice(lis[1:])
                ques.configure(text =mediumQ[x][0])
            
                a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
                b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
                c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
                d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
                lis.remove(x)
                print(lis)
                y = countDown()
                if y == -1:
                     display()

            
        def calc():
            global score
            if (var.get() in answer):
                score+=1
            display()
    
        submit = Button(f3,command=calc,text="Submit",font="verdana",width=20)
        submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
        nextQuestion = Button(f3,command=display,text="Next",font="verdana",width=5)
        nextQuestion.place(relx=0.90,rely=0.82,anchor=CENTER)

        back=Button(f3,command=lambda:(menu(),medium_frame.destroy()),text='Back ⪪',font="verdana",bg='blue',fg='white')
        back.place(relx=0.2,rely=0.80)
    
    
        y = countDown()
        if y == -1:

            display()

    def difficult():
        global f2
        difficult_frame=Frame(f2,width=1393,height=700,bg="blue")
        difficult_frame.place(x=0,y=0)
        f3=Frame(difficult_frame,width=1000,height=500,bg="white")
        f3.place(anchor='c',relx=0.5,rely=0.5)

        def countDown():
            check = 0
            for k in range(20, 0, -1):
                
                if k == 1:
                    check=-1
                timer.configure(text="Time left:"+str(k),font="verdana")
                difficult_frame.update()
                time.sleep(1)
                
            timer.configure(text="Times up!")
            if check==-1:
                return (-1)
            else:
                return 0
        global score
        score = 0

        difficultQ = [
                    [
                         "Lanthanides and Actinides are also called __",
                         "Noble gases",
                         "Normal elements",
                         "Inner-Transition elements",
                         "Transition elements"
                    ],
                    [
                        "Maximum no. of electrons that can be placed in K shell?",
                        "18",
                        "32",
                        "2",
                        "8"
                    ],
                    [
                        "How many groups and periods are there in the Modern Periodic Table?",
                        "16 Groups and 9 Periods",
                        "18 Groups and 7 Periods",
                        "14 Groups and 9 Periods",
                        "18 Groups and 9 Periods"
                    ],
                    [
                        "Which elements has three shells which are comopletely filled with elctrons?",
                        "Argon",
                        "Neon",
                        "Krypton",
                        "Aluminium"
                    ],
                    [
                        "Which one is Metalloid?",
                        "Carbon",
                        "Silicon",
                        "Mercury",
                        "Chlorine"
                    ], 
                ]
        answer =[
                "Inner-Transition elements",
                "2",
                "18 Groups and 7 Periods",
                "Argon",
                "Silicon"
                ]
    
        lis=['',0,1,2,3,4]
        x=random.choice(lis[1:])

        ques=Label(f3,text=difficultQ[x][0],font="verdana 20",bg="white")
        ques.place(relx=0.5,rely=0.2,anchor=CENTER)

        var=StringVar()

        a=Radiobutton(f3,text=difficultQ[x][1],value=difficultQ[x][1],variable = var,font="verdana 15",bg="white")
        a.place(relx=0.5,rely=0.42,anchor=CENTER)

        b=Radiobutton(f3,text=difficultQ[x][2],value=difficultQ[x][2],variable = var,font="verdana 15",bg="white")
        b.place(relx=0.5,rely=0.52,anchor=CENTER)

        c=Radiobutton(f3,text=difficultQ[x][3],value=difficultQ[x][3],variable = var,font="verdana 15",bg="white")
        c.place(relx=0.5,rely=0.62,anchor=CENTER)

        d=Radiobutton(f3,text=difficultQ[x][4],value=difficultQ[x][4],variable = var,font="verdana 15",bg="white")
        d.place(relx=0.5,rely=0.72,anchor=CENTER)

        lis.remove(x)

        timer=Label(f3)
        timer.place(relx=0.8,rely=0.82,anchor=CENTER)

        def display():
        
            if len(lis) == 1:
                    difficult_frame.destroy()
                    showMark(score)
            if len(lis) == 2:
                nextQuestion.configure(text='End',command=calc,font="verdana")
                
            if lis:
                x = random.choice(lis[1:])
                ques.configure(text =difficultQ[x][0])
            
                a.configure(text=difficultQ[x][1],value=difficultQ[x][1])
      
                b.configure(text=difficultQ[x][2],value=difficultQ[x][2])
      
                c.configure(text=difficultQ[x][3],value=difficultQ[x][3])
      
                d.configure(text=difficultQ[x][4],value=difficultQ[x][4])
            
                lis.remove(x)
                print(lis)
                y = countDown()
                if y == -1:
                    display()

            
        def calc():
            global score
            if (var.get() in answer):
                score+=1
            display()
    
        submit = Button(f3,command=calc,text="Submit",font="verdana",width=20)
        submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
        nextQuestion = Button(f3,command=display,text="Next",font="verdana",width=5)
        nextQuestion.place(relx=0.90,rely=0.82,anchor=CENTER)
        back=Button(f3,command=lambda:(menu(),difficult_frame.destroy()),text='Back ⪪',font="verdana",bg='blue',fg='white')
        back.place(relx=0.2,rely=0.80)
    
        y = countDown()
        if y == -1:
            display()

    def showMark(mark):
        showMark_frame=Frame(f2,width=1393,height=700,bg="blue")
        showMark_frame.place(x=0,y=0)
        f3=Frame(showMark_frame,width=1000,height=500,bg="white")
        f3.place(anchor='c',relx=0.5,rely=0.5)

        st = "Your score is "+str(mark)
        mlabel = Label(f3,text=st,fg="black",font="verdana 30 bold")
        mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)

        back=Button(f3,command=lambda:(menu(),showMark_frame.destroy()),text='Back ⪪',font="verdana",bg='blue',fg='white')
        back.place(relx=0.2,rely=0.80)
    



    play_quiz_button=Button(text="Play Quiz",borderwidth=5,command=quiz1 ,font="verdana 18 ",bg="red",fg="white",cursor="hand2",padx=10,pady=10,width=17)
    play_quiz_button.place(x=100,y=540)

    navbarBtn =Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=toggle_win)
    navbarBtn.place(x=10, y=10)

    #########################################  defining animation  #################################################
    colors=['red','green','blue','purple']
    def color_changer():
        fg=random.choice(colors)
        label.config(fg=fg)
        label.after(700,color_changer)
        labels=['Created by👉- Nitin Kumar Sharma','Hey 😎 You are using Element Paradise']
        text=random.choice(labels)
        label.config(text=text)
    label=Label(root,font=('Forte',20,''),bg="white")
    label.place(x=500,y=155)
    color_changer()

    title2_label=Label(text="Class-12 PCM A1  📚  Roll no.-31",fg="red",font="verdana 18 ",bg="white")
    title2_label.place(x=550,y=195)

    root.mainloop()
    ################################################# code for playing song  ###########################################
    
    
pygame.init()
_playing=False
def play(path):
    global _playing
    if _playing==False:
        _playing=True
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.pause()
        _playing=False


# window in mainloop
def bar():

    l4=Label(win,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    r=0
    for i in range(100):
        progress['value']=r
        win.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    win.destroy()
    new_win()
        
    
progress.place(x=-10,y=235)


a='#249794'#BLUE COLOR
Frame(win,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(win,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)


###################################################  Label of Splash Window #############################################################

l1=Label(win,text='ELEMENT',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(win,text='PARADISE',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=175,y=82)

l3=Label(win,text='LEARNING MADE EASY',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)

  


win.mainloop()

############################################## Thanks For Using ###################################################
