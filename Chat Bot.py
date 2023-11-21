from tkinter import *               #importing classes & methods
from textblob import TextBlob
#from chatterbot import ChatBot


######FUNCTIONALITY

def botreply():
    question=questionField.get()        #will return everthing written on entry field   #VARIABLE=question
    textarea.insert(END,'You:'+question+'\n')   #insert on text area     #'+' will concatenate strings
    questionField.delete(0,END)         #delete everything from start to end to enter new question 



######GUI
root=Tk()                           #root=object of tk class

root.geometry('500x570+100+70')
root.title('ChatBot by Tushar')
root.config(bg='sky blue')

logoPic=PhotoImage(file='chatbot.png')         #creates object of image

logoPicLabel=Label(root,image=logoPic)       
logoPicLabel.pack(pady=5)           #placing the pic label with pack method

centerFrame=Frame(root)            #frame for displaying screen
centerFrame.pack()                 #placing with pack

scrollbar=Scrollbar(centerFrame)    #using scrollbar class
scrollbar.pack(side=RIGHT)          #placing at right side

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=9,    #styling of text area   #height of text area is 10
              yscrollcommand=scrollbar.set,wrap='word')                 #set scrollbar with text area       #wrap will move words together
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)        #for seeing yview of text area

questionField=Entry(root,font=('arial',20,'bold'))      #entry-field for writing question
questionField.pack(pady=15,fill=X)                  #placing it     #vertical-padding       #filled completely on x-axis

askPic=PhotoImage(file='robot-chatbot1.png')             #creating object of image
askButton=Button(root,image=askPic,bg='brown',command=botreply)    #creating ask button
askButton.pack()

root.mainloop()                     #window created & we can see it continuously