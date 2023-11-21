from tkinter import *
import os                   #os module to add functionality & interact with os

root=Tk()                   #root=object of main window

root.title('Computer Manager')
root.config(bg='gray20')
root.geometry('450x620+30+30')

titleImage=PhotoImage(file='Control Manager Images/title.png')

titleLabel=Label(root,text=' Control Manager',font=('felix titling','25','bold'),fg='WHITE',bg='gray20',image=titleImage,compound=LEFT)    #compound keyword is used to show both image and text
titleLabel.grid()           #add label to our window    

frame=Frame(root,bd=2,bg='GRAY20')      #for placing icons
frame.grid(row=1)


taskImage=PhotoImage(file='Control Manager Images/task.png')
Button(frame,text=' Task Manager',font=('FELIX TITLING',17,'bold'),image=taskImage,compound=LEFT,fg='YELLOW',bg='GRAY20',       #for creating buttons
       cursor='hand2',bd=0,command=lambda : os.system('taskmgr')).grid(padx=10,sticky='w',pady=10)                          #cursor keyword for changing to hand symbol     

controlImage=PhotoImage(file='Control Manager Images/controlpanel.png')
Button(frame,text=' Control panel',font=('FELIX TITLING',17,'bold'),image=controlImage,compound=LEFT,fg='PINK',bg='GRAY20',     #padx & pady for spacing btw buttons 
       cursor='hand2',bd=0,command=lambda : os.system('control')).grid(row=5,column=0,padx=10,sticky='w',pady=10)               #sticky keyword for indentation & w is for west

datetimeImage=PhotoImage(file='Control Manager Images/datetime.png')
Button(frame,text=' Date and Time',font=('FELIX TITLING',17,'bold'),image=datetimeImage,compound=LEFT,fg='RED',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('timedate.cpl')).grid(row=1,column=0,padx=10,sticky='w',pady=10)

deviceImage=PhotoImage(file='Control Manager Images/device.png')
Button(frame,text=' Device Manager',font=('FELIX TITLING',17,'bold'),image=deviceImage,compound=LEFT,fg='WHITE',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('devmgmt.msc')).grid(row=2,column=0,padx=10,sticky='w',pady=10)           #os.system to add functionality

updateImage=PhotoImage(file='Control Manager Images/update.png')
Button(frame,text=' Windows Update',font=('FELIX TITLING',17,'bold'),image=updateImage,compound=LEFT,fg='SKY BLUE',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('control update')).grid(row=7,column=0,padx=10,sticky='w',pady=10)

mouseImage=PhotoImage(file='Control Manager Images/mouse.png')
Button(frame,text=' Mouse Properties',font=('FELIX TITLING',17,'bold'),image=mouseImage,compound=LEFT,fg='DEEP PINK',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('main.cpl')).grid(row=3,column=0,padx=10,sticky='w',pady=10)

propertiesImage=PhotoImage(file='Control Manager Images/properties.png')
Button(frame,text=' System properties',font=('FELIX TITLING',17,'bold'),image=propertiesImage,compound=LEFT,fg='BLUE2',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('sysdm.cpl')).grid(row=8,column=0,padx=10,sticky='w',pady=10)

removeImage=PhotoImage(file='Control Manager Images/remove.png')
Button(frame,text=' Uninstall Softwares',font=('FELIX TITLING',17,'bold'),image=removeImage,compound=LEFT,fg='ORANGE',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('appwiz.cpl')).grid(row=4,column=0,padx=10,sticky='w',pady=10)

networkImage=PhotoImage(file='Control Manager Images/network.png')
Button(frame,text=' Network Connections',font=('FELIX TITLING',17,'bold'),image=networkImage,compound=LEFT,fg='LIGHT GREEN',bg='GRAY20',
       cursor='hand2',bd=0,command=lambda : os.system('ncpa.cpl')).grid(row=9,column=0,padx=10,sticky='w',pady=10)

root.mainloop()