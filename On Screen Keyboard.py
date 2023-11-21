from tkinter import *
from tkinter import ttk
import ttkthemes 

def select(value):                  #select fuction to call out value
    
    if value=='Space':
        textarea.insert(INSERT,'  ')

    elif value=='Enter':
        textarea.insert(INSERT,'\n')    

    elif value=='Tab':
        textarea.insert(INSERT,'\t')

    elif value=='Delete':
        textarea.delete(1.0,END)    #delete from 1.0 till end


    elif value=='Backspace':
        i=textarea.get(1.0,END)     #i=function used to store
        newtext=i[:-2]              #string slicing    #will remove last 2 characters
        textarea.delete(1.0,END)    #Delete previous text start to end
        textarea.insert(INSERT,newtext)       #newtext is variable

    elif value=='CAPS':
        CAPSButton = ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace','Delete',
                      'Tab','Q','W','E','R','T','Y','U','I','O','P','[  ]','7','8','9',
                      'Caps','A','S','D','F','G','H','J','K','L',';','Enter','4','5','6',
                      'Shift','Z','X','C','V','B','N','M',',','.','/','Shift','1','2','3',
                      'Space']
        varRow=2
        varColumn=0
    
        for button in CAPSButton:                  #to create buttons
            command=lambda x=button: select(x)      #lambda is keyword used to create one line function  
                                                    #arguments:expression   #used for calling key function                     
            if button !='Space':
                ttk.Button(root,text=button,width=5,command=command).grid(row=varRow,column=varColumn) #to add buttons on our window   #command function
    
            else:
                ttk.Button(root,text=button,width=30).grid(row=6,column=0,columnspan=15)

            varColumn+=1                   #as buttons will overlap so increasing column numbers
            if varColumn>14:
                varColumn=0
                varRow+=1

    elif value=='Caps':
        CapsButton = ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace','Delete',
                      'Tab','q','w','e','r','t','y','u','i','o','p','{ }','7','8','9',
                      'Caps','a','s','d','f','g','h','j','k','l',':','Enter','4','5','6',
                      'Shift','z','x','c','v','b','n','m','<','>','?','Shift','1','2','3',
                      'Space']
        varRow=2
        varColumn=0
    
        for button in CapsButton:                  #to create buttons
            command=lambda x=button: select(x)      #lambda is keyword used to create one line function  
                                                    #arguments:expression   #used for calling key function                     
            if button !='Space':
                ttk.Button(root,text=button,width=5,command=command).grid(row=varRow,column=varColumn) #to add buttons on our window   #command function
    
            else:
                ttk.Button(root,text=button,width=30).grid(row=6,column=0,columnspan=15)

            varColumn+=1                   #as buttons will overlap so increasing column numbers
            if varColumn>14:
                varColumn=0
                varRow+=1


    elif value=='Shift':
        ShiftButton = ['~','!','@','#','$','%','^','&','*','(',')','_','+','Backspace','Delete',
                       'Tab','q','w','e','r','t','y','u','i','o','p','{ }','7','8','9',
                       'Caps','a','s','d','f','g','h','j','k','l',':','Enter','4','5','6',
                       'SHIFT','z','x','c','v','b','n','m','<','>','?','SHIFT','1','2','3',
                       'Space']
        varRow=2
        varColumn=0
    
        for button in ShiftButton:                  #to create buttons
            command=lambda x=button: select(x)      #lambda is keyword used to create one line function  
                                                    #arguments:expression   #used for calling key function                     
            if button !='Space':
                ttk.Button(root,text=button,width=5,command=command).grid(row=varRow,column=varColumn) #to add buttons on our window   #command function
    
            else:
                ttk.Button(root,text=button,width=30).grid(row=6,column=0,columnspan=15)

            varColumn+=1                   #as buttons will overlap so increasing column numbers
            if varColumn>14:
                varColumn=0
                varRow+=1
    
    elif value=='SHIFT':
        SHIFTButton = ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace','Delete',
                       'Tab','q','w','e','r','t','y','u','i','o','p','{ }','7','8','9',
                       'Caps','a','s','d','f','g','h','j','k','l',':','Enter','4','5','6',
                       'Shift','z','x','c','v','b','n','m',',','.','/','Shift','1','2','3',
                       'Space']
        varRow=2
        varColumn=0
    
        for button in SHIFTButton:                  #to create buttons
            command=lambda x=button: select(x)      #lambda is keyword used to create one line function  
                                                    #arguments:expression   #used for calling key function                     
            if button !='Space':
                ttk.Button(root,text=button,width=5,command=command).grid(row=varRow,column=varColumn) #to add buttons on our window   #command function
    
            else:
                ttk.Button(root,text=button,width=30).grid(row=6,column=0,columnspan=15)

            varColumn+=1                   #as buttons will overlap so increasing column numbers
            if varColumn>14:
                varColumn=0
                varRow+=1
    
    else:                                       #to print digits
        textarea.insert(INSERT,value)

    textarea.focus_set()         #to blink cursor


######GUI

root=ttkthemes.ThemedTk()        #object #creating instance of TK class

root.get_themes()
root.set_theme('radiance')

root.title('On Screen Keyboard')

titlelabel=Label(root,text='On Screen Keyboard',font=('felix titling', 30, 'bold'))  #variable=title  #object=titleLabel
titlelabel.grid(row=0,column=0,columnspan=15)

textarea=Text(root,font=('arial',15,'italic'),height=12,width=90,bd=5) #customisation
textarea.grid(row=1,column=0,columnspan=15)                             #where to use this
textarea.focus_set()            #cursor blinks wherever we r typing

varRow=2                        #variable #placement of buttons
varColumn=0

buttons = ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace','Delete',
           'Tab','q','w','e','r','t','y','u','i','o','p','[  ]','7','8','9',
           'CAPS','a','s','d','f','g','h','j','k','l',';','Enter','4','5','6',
           'Shift','z','x','c','v','b','n','m',',','.','/','Shift','1','2','3',
           'Space']

for button in buttons:          #to create buttons
    command=lambda x=button: select(x)       #lambda is keyword used to create one line function  
                                             #arguments:expression   #used for calling key function
    if button !='Space':
        ttk.Button(root,text=button,width=5,command=command).grid(row=varRow,column=varColumn) #to add buttons on our window   #command function
    
    else:
        ttk.Button(root,text=button,width=30).grid(row=6,column=0,columnspan=15)

    varColumn+=1                #as buttons will overlap so increasing column numbers
    if varColumn>14:
        varColumn=0
        varRow+=1

root.mainloop()