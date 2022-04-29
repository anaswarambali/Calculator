from tkinter import *
from tkinter import messagebox

class gui:
    def __init__(self):
        
        self.l=['','','']
        lb=[]
        self.f=True
        self.op=False

        root=Tk()
        root.title("Calculator")
        root.minsize(400, 600)

        #to dislpay the window int the center of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int(screen_width/2 -  400 / 2)
        y = int(screen_height/2 - 600 / 2)
        root.geometry('400x600+'+str(x)+'+'+str(y))

        
        #root.overrideredirect(True)
        root.configure(bg='#232323')
        root.attributes('-alpha',0.99)
    
        
        tf=Frame(root,height=100,bg='#232323')
        tf.pack(side='top',fill=BOTH,expand=False)
        
        bf=Frame(root,bg='#232323')
        bf.pack(side='bottom',fill=BOTH,expand=True,pady=3,padx=3)
        
        '''Grid.rowconfigure(bf,1,weight=1)
        Grid.columnconfigure(bf,0,weight=1)
        Grid.rowconfigure(bf,1,weight=1)'''
        
        #BUTTONS FOR THE CALC OF 1,2 ETC

                          
        '''b1 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='/' ,command=lambda :self.press('/','o'))
        b2 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text=''  ,command=lambda :self.press(' ',' '))
        b3 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='C' ,command=self.clear)
        b4 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='%' ,command=lambda :self.press('%','o'))
        b5 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='7' ,command=lambda :  self.press(7,'n'))
        b6 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='8' ,command=lambda :  self.press(8,'n'))
        b7 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='9' ,command=lambda :  self.press(9,'n'))
        b8 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='x' ,command=lambda :self.press('x','o'))
        b9 =Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='4' ,command=lambda :  self.press(4,'n'))
        b10=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='5' ,command=lambda :  self.press(5,'n'))
        b11=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='6' ,command=lambda :  self.press(6,'n'))
        b12=Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='-' ,command=lambda :self.press('-','o'))
        b13=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='1' ,command=lambda :  self.press(1,'n'))
        b14=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='2' ,command=lambda :  self.press(2,'n'))
        b15=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='3' ,command=lambda :  self.press(3,'n'))
        b16=Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='+' ,command=lambda :self.press('+','o'))
        b17=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='  ',command=lambda :self.press(' ',' '))
        b18=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text='0' ,command=lambda :  self.press(0,'n'))
        b19=Button(bf,font=('Helvetica',30),bd=0,width=4,bg= 'black', fg='white',text=' .',command=lambda :self.press('.','p'))
        b20=Button(bf,font=('Helvetica',30),bd=0,width=4,bg='#121212',fg='white',text='=' ,command=lambda :     self.compute())

        #TO ALIGN EACH BUTTON CORRECTLY IN PLACE    
        b1.grid(row=0,column=0,sticky='NEWS',pady=1,padx=1)
        b2.grid(row=0,column=1,sticky='NEWS',pady=1,padx=1)
        b3.grid(row=0,column=2,sticky='NSEW',pady=1,padx=1)
        b4.grid(row=0,column=3,sticky='NSEW',pady=1,padx=1)
        
        b5.grid(row=1,column=0,sticky='NSEW',pady=1,padx=1)
        b6.grid(row=1,column=1,sticky='NSEW',pady=1,padx=1)
        b7.grid(row=1,column=2,sticky='NSEW',pady=1,padx=1)
        b8.grid(row=1,column=3,sticky='NSEW',pady=1,padx=1)

        b9.grid( row=2,column=0,sticky='NSEW',pady=1,padx=1)
        b10.grid( row=2,column=1,sticky='NSEW',pady=1,padx=1)
        b11.grid (row=2,column=2,sticky='NSEW',pady=1,padx=1)
        b12.grid(row=2,column=3,sticky='NSEW',pady=1,padx=1)

        b13.grid( row=3,column=0,sticky='NSEW',pady=1,padx=1)
        b14.grid( row=3,column=1,sticky='NSEW',pady=1,padx=1)
        b15.grid( row=3,column=2,sticky='NSEW',pady=1,padx=1)
        b16.grid(row=3,column=3,sticky='NSEW',pady=1,padx=1)
        
        b17.grid( row=4,column=0,sticky='NSEW',pady=1,padx=1)
        b18.grid( row=4,column=1,sticky='NSEW',pady=1,padx=1)
        b19.grid( row=4,column=2,sticky='NSEW',pady=1,padx=1)
        b20.grid(row=4,column=3,sticky='NSEW',pady=1,padx=1)'''

        for i in range(20):
            s="b"+str(i+1)
            globals()[s]=Button(bf,font=('Helvetica',30),bd=0,width=4,fg='white',bg='#121212')
            
        lb=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]
            
        b1.config(text='/' ,command=lambda :self.press('/','o'))
        b2.config(text='pow'  ,command=lambda :self.press('^','o'))
        b4.config(text='C' ,command=self.clear)
        b3.config(text='%' ,command=lambda :self.press('%','o'))
        b5.config(text='7' ,command=lambda :  self.press(7,'n'),bg= 'black')
        b6.config(text='8' ,command=lambda :  self.press(8,'n'),bg= 'black')
        b7.config(text='9' ,command=lambda :  self.press(9,'n'),bg= 'black')
        b8.config(text='x' ,command=lambda :self.press('x','o'))
        b9.config(text='4' ,command=lambda :  self.press(4,'n'),bg= 'black')
        b10.config(text='5' ,command=lambda :  self.press(5,'n'),bg= 'black')
        b11.config(text='6' ,command=lambda :  self.press(6,'n'),bg= 'black')
        b12.config(text='-' ,command=lambda :self.press('-','o'))
        b13.config(text='1' ,command=lambda :  self.press(1,'n'),bg= 'black')
        b14.config(text='2' ,command=lambda :  self.press(2,'n'),bg= 'black')
        b15.config(text='3' ,command=lambda :  self.press(3,'n'),bg= 'black')
        b16.config(text='+' ,command=lambda :self.press('+','o'))
        b17.config(text='  ',command=lambda :self.press(' ',' '),bg= 'black')
        b18.config(text='0' ,command=lambda :  self.press(0,'n'),bg= 'black')
        b19.config(text=' .',command=lambda :self.press('.','p'),bg= 'black')
        b20.config(text='=' ,command=lambda :     self.compute())
           
        #LOOP STRUCTURE TO ALIGN EACH BUTTON CORRECTLY IN PLACE 
        c=0            
        for i in range(5):
            k=lb[c:c+4]
            for j in range(4):
                k[j].grid(row=i,column=j,sticky='NEWS',pady=1,padx=1)
                self.hover(k[j])
            c+=4
            
            
        #TO ALLOW EXPANSION OF BUTTONS IN THE WINDOWS
        for i in range(5):
            Grid.rowconfigure(bf,i,weight=1)
            if i>0:
                Grid.columnconfigure(bf,i-1,weight=1)


        #LABEL TO DISPLAY SMALL EXPRESSION ON TOP
        self.s=StringVar()
        entrys=Label(tf,textvariable=self.s,font=('Helvetica',20       ),bg='#232323',fg='white')
        entrys.pack(side='top',pady=10,padx=10,anchor=NE)
        
        #LABEL TO DISPLAY ENTERED EXPRESSION 
        self.t=StringVar()
        entry= Label(tf,textvariable=self.t,font=('Helvetica',50,'bold'),bg='#232323',fg='white')
        entry.pack(side='right',pady=10,padx=10)
        self.t.set(' ')

               
        root.mainloop()

    def hover(self,button,c1='#343434'):
        #FUNCTION TO CHANGE COLOUR ON HOVER
        button.bind("<Enter>", func=lambda e: button.config(background=c1))
        c2=button['background']
        button.bind("<Leave>", func=lambda e: button.config(background=c2))

    def compute(self):
        #FUNCTION TO COMPUTE RESULT
        exp=s=''
        r=lambda x,y: 1 if y==0 else x*r(x,y-1)
        result = {
            '^': lambda x,y: r(x,y),
            'x': lambda x,y: x*y,
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '/': lambda x,y: x/y,
            '%': lambda x,y: x%y
            }
        try:
            final=result[self.l[1]](self.l[0],self.l[2])
        except ZeroDivisionError:
            self.clear()
            messagebox.showinfo("Error","Division by Zero")
        else:
            self.t.set(final)
            for i in self.l:
                exp+=(str(i)+' ')   
            self.s.set((exp+" = "))
            self.clear('x')
            
    def clear(self,n=''):
        #FUNCTION TO CLEAR EXPRESSION
        self.l=['','','']
        self.f=True
        self.op=False
        if n!='x':
            self.s.set('')
            self.t.set("0")
        
    def press(self,n,w):
        exp=''
        if w=='n' and self.f:
            self.l[0]=str(self.l[0])
            self.l[0]+=str(n)
            self.l[0]=int(self.l[0])
            for i in self.l:
                exp+=str(i)
            self.op=True
            self.t.set(exp)
             
        elif w=='o' and self.op:
            self.l[1]=n
            self.f=False
            for i in self.l:
                exp+=(str(i)+' ')
            self.s.set(exp)
                
        elif w=='n' and not self.f:
            self.l[2]=str(self.l[2])
            self.l[2]+=str(n)
            self.l[2]=int(self.l[2])
            self.t.set(self.l[2])
            self.eq=True
            self.op=False
        else:
            pass

a=gui()
