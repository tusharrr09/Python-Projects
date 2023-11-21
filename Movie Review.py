from tkinter import *
import imdb                     #pip install imdbpy
from tkinter import messagebox 

######Functionality Part

def search():       #function is being called evertime we lick on search button
    
    if movieentry.get()=='':          #if nothing is entered by user
        messagebox.showerror('Error','Please type a Movie Name')

######GUI Second

    else:

        root1=Toplevel()     #class for everything present under tk class (title,resizable,label,geometry)
        root1.geometry('1000x620+200+50')
        root1.title('Movie Information')
        root1.config(bg='brown')       #using here for background color

        titlelabel=Label(root1,text='Title:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        titlelabel.place(x=60,y=30)

        titlenamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown')
        titlenamelabel.place(x=300,y=30)

        directorlabel=Label(root1,text='Director:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        directorlabel.place(x=60,y=100)

        directornamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown')
        directornamelabel.place(x=300,y=100)

        yearlabel=Label(root1,text='Year:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        yearlabel.place(x=60,y=170)

        yearnamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown')
        yearnamelabel.place(x=300,y=170)

        durationlabel=Label(root1,text='Duration:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        durationlabel.place(x=60,y=240)

        durationnamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown')
        durationnamelabel.place(x=300,y=240)

        genreslabel=Label(root1,text='Genres:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        genreslabel.place(x=60,y=310)

        genrenamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown')
        genrenamelabel.place(x=300,y=310)

        ratinglabel=Label(root1,text='Rating:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        ratinglabel.place(x=60,y=380)

        ratingnamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown')
        ratingnamelabel.place(x=300,y=380)

        castlabel=Label(root1,text='Cast:',font=('Old English Text MT',30,'bold'),fg='white',bg='brown')
        castlabel.place(x=60,y=450)

        castnamelabel=Label(root1,font=('felix titling',25,'bold'),fg='yellow',bg='brown',wraplength=650)          
                                                        #wraplength changes line after completing req pixels
        castnamelabel.place(x=300,y=450)


########fetching data

        imdbobject=imdb.IMDb()         #create object of imdb class        #object_variable=imdbobject 
        movie_name=movieentry.get()    #storing movie name typed
        movies=imdbobject.search_movie(movie_name)     #variable=movies
        
        index=movies[0].getID()              #returns 1st element INDEX of list
        movie=imdbobject.get_movie(index)    #variable=movie
        
        title=movie['title']
        titlenamelabel.config(text=title)     #to display title on movie window
        
        year=movie['year']
        yearnamelabel.config(text=year)       #to display year

        rating=movie['rating']
        ratingnamelabel.config(text=rating)

        genre=movie['genres']
        genrenamelabel.config(text=genre)

        director=movie['directors'][0]
        directornamelabel.config(text=director)

        duration=movie['runtime'][0]
        hours=int(duration)//60         #to show duration in hours & mins
        rem=int(duration)%60
        durationnamelabel.config(text=f'{hours} hours {rem} minutes')
                                    #f_string to concatenate variable with string{}

        cast=movie['cast']           #cast=list which we will return
        
        list_of_cast=list(map(str,cast))     #map function will take all names of list & keep it together                
        castlist=list_of_cast[:6]
        strr=''                             #variable   
        for item in castlist:
            if item==castlist[-1]:          #to add '.' after last element      #-1 is for last element
                strr=strr+item+'.'          
            else:
                strr=strr+item+','+' '          #to add ',' after every element

        castnamelabel.config(text=strr)



        root1.mainloop()


######GUI Part

root=Tk()     #object of tk class     #root=object variable
root.geometry('1057x650+100+30')
root.title('Movie Review')
root.resizable(False,False)     #disables maximise button

bgpic=PhotoImage(file='imdb pic.png')  #bgpic=object for Photoimage class

bglabel=Label(root,image=bgpic)   #creating a label
bglabel.place(x=0,y=0)            #placement of background

movielabel=Label(root,text='MoVie NamE:',font=('algerian',30,'bold'),fg='black',bg='yellow')    #creating text label
movielabel.place(x=550,y=300)         #placing label

movieentry=Entry(root,font=('FELIX TITLING',20,'bold'),bd=5,bg='yellow',justify=CENTER)            #creating entry field
movieentry.place(x=500,y=400)      #placing
movieentry.focus_set()             #cursor blinking

moviesearchbutton=Button(root,text='SEARCH',font=('Arial',10,'bold'),bd=5,bg='yellow', command=search)            #command functionality for everytime clicking on command
moviesearchbutton.place(x=640,y=470)

root.mainloop()