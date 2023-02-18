#Using psycopg2 in order to communicate with the database
#Using tkinter to build background_image
#Using pandas to store the results of the queries appropriately
#Using PIL (pillow) to display images
from DB_info import *

usr,password,db_name = DB_info()                    #DB connection before GUI's creation
conn = psycopg2.connect( database= db_name,
                         user= usr,
                         password = password,
                         host='localhost',
                         port= '5432')
cursor = conn.cursor()                              #create cursor to execute queries & get results



#--------------------------------QUERIES AS FUNCTIONS#--------------------------------

def searchForArtwork():
    clear_frame()                                                               #clear frame
    frame.pack()                                                                #add frame

    entryBox = Entry(frame,width=100,relief = 'solid')                          #create entryBox
    imgFrame = Frame(frame,bg = 'indianred4')                                   #create image frame
    labeledImg = Label( imgFrame)                                               #image's label

    def getEntryData():                                                         #on "get" click:
        title = entryBox.get()                                                  #save user's imput
        title = title.rstrip()                                                  #alter input appropriately
        title = title.lstrip()

        query = " select * from art  where title = "                            #form query
        query += "'"
        query += title
        query += "'"
        cursor.execute(query)                                                   #execute query
        res = cursor.fetchall()                                                 #get results and
                                                                                #store them in dataframe
        info = pd.DataFrame(res,columns = ["title","creator","info","genre","image"])

        imgPath =  info["image"][0]                                             #get image path from DB
        imgPath = imgPath + ".png"                                              #alter path appropriately
        img = PhotoImage(file = imgPath)                                        #create an image
        labeledImg.config(image = img)                                          #image is now a label
        labeledImg.image = img                                                  #create instance of image

        imgFrame.pack()                                                         #display frame and image
        labeledImg.pack()


    query = " select title from art  order by title asc"                        #display the artworks
    cursor.execute(query)
    res = cursor.fetchall()
    artworks = pd.DataFrame(res,columns= ['Artworks'])

    label = Label(frame,text = artworks,justify = 'left',relief = 'solid')
    label.pack()

    entryBox.pack()                                                             #display the entry box

    b = Button(frame,                                                           #create a button to get input
               text = "get",
               command = getEntryData,
               bg = "antiquewhite1",
               justify='left')
    b.pack()                                                                    #display button

def showArtists():
    clear_frame()                                         #clear frame
    frame.pack()                                          #add frame


    query = " select name from artist  order by name asc" #query formation
    cursor.execute(query)                                 #execute query
    res = cursor.fetchall()                               #get results

    artists = pd.DataFrame(res,columns= ['Artists'])      #store results in a dataframe

    label = Label(frame,                                  #create a Label in frame
                  text = artists,                         #containing the results
                  justify = 'left',
                  relief = 'solid')
    label.pack()                                          #display results

def showMovements():
    #this function works in the same way
    #as the function showArtists

    clear_frame()
    frame.pack()

    query = " select name from genre  order by name asc"
    cursor.execute(query)
    res = cursor.fetchall()

    movements = pd.DataFrame(res,columns= ['Movements'])

    label = Label(frame,
                  text = movements,
                  justify = 'left',
                  relief = 'solid')
    label.pack()

def showArtworks():
    #this function works in the same way
    #as the function showArtists
    clear_frame()
    frame.pack()

    query = " select title from art  order by title asc"
    cursor.execute(query)
    res = cursor.fetchall()
    artworks = pd.DataFrame(res,columns= ['Artworks'])

    label = Label(frame,text = artworks,justify = 'left',relief = 'solid')
    label.pack()

def getArtistInfo():
    clear_frame()                                   #clear frame
    frame.pack()                                    #add frame

    entryBox = Entry(frame,                         #Create an entry box
                     width=100,
                     relief = 'solid')
    infoLabel = Label(frame,                        #create a label for info
                      text = '',
                      justify = 'left',
                      relief = 'solid',
                      wraplength=300)



    def getEntryData():                                         #on "get" button's click:

        artists_name = entryBox.get()                           #get artists name
        artists_name = artists_name.rstrip()                    #alter name appropriately
        artists_name = artists_name.lstrip()

        query = " select info from artist  where name = "       #form query
        query += "'"
        query += artists_name
        query += "'"
        cursor.execute(query)                                    #execute query
        res = cursor.fetchall()                                  #get results
        info = pd.DataFrame(res,columns = [artists_name])        #store them in dataframe

        infoLabel.config(text = info[artists_name][0])           #display results in already placed label



    query = " select name from artist  order by name asc"        #show all artists
    cursor.execute(query)                                        #execute query
    res = cursor.fetchall()                                      #get results

    artists = pd.DataFrame(res,columns= ['Artists'])             #store results in a dataframe

    label = Label(frame,                                         #create a label containing the results
                  text = artists,
                  justify = 'left',
                  relief = 'solid')
    label.pack()                                                 #display the results

    entryBox.pack()                                              #display the entry box

    b = Button(frame,                                            #create a button to get input from entry box
               text = "get",
               command = getEntryData,
               bg = "antiquewhite1",
               justify='left')
    b.pack()                                                     #display button
    infoLabel.pack()                                             #place the empty info label

def getMovementInfo():
    #this function works in the same way
    #as the getArtistInfo
    clear_frame()
    frame.pack()

    entryBox = Entry(frame,width=100,relief = 'solid')
    infoLabel = Label(frame,
                      text = '',
                      justify = 'left',
                      relief = 'solid',
                      wraplength=300)

    def getEntryData():

        movements_name = entryBox.get()
        movements_name = movements_name.rstrip()
        movements_name = movements_name.lstrip()

        query = " select info from genre  where name = "
        query += "'"
        query += movements_name
        query += "'"
        cursor.execute(query)
        res = cursor.fetchall()
        info = pd.DataFrame(res,columns = [movements_name])

        infoLabel.config(text = info[movements_name][0])

    query = " select name from genre  order by name asc"
    cursor.execute(query)
    res = cursor.fetchall()
    movements = pd.DataFrame(res,columns= ['Movements'])

    label = Label(frame,text = movements,justify = 'left',relief = 'solid')
    label.pack()

    entryBox.pack()

    b = Button(frame,
               text = "get",
               command = getEntryData,
               bg = "antiquewhite1",
               justify='left')
    b.pack()

    infoLabel.pack()

def getArtworkInfo():
    #this function works in the same way
    #as the getArtistInfo
    clear_frame()
    frame.pack()

    entryBox = Entry(frame,width=100,relief = 'solid')
    infoLabel = Label(frame,
                      text = '',
                      justify = 'left',
                      relief = 'solid',
                      wraplength=300)
    def getEntryData():

        artwork_name = entryBox.get()
        artwork_name = artwork_name.rstrip()
        artwork_name = artwork_name.lstrip()

        query = " select info from art  where title = "
        query += "'"
        query += artwork_name
        query += "'"
        cursor.execute(query)
        res = cursor.fetchall()
        info = pd.DataFrame(res,columns = [artwork_name])

        infoLabel.config(text = info[artwork_name][0])

    query = " select title from art  order by title asc"
    cursor.execute(query)
    res = cursor.fetchall()
    artworks = pd.DataFrame(res,columns= ['Artworks'])

    label = Label(frame,text = artworks,justify = 'left',relief = 'solid')
    label.pack()

    entryBox.pack()                                                           #3:display the empty info label

    b = Button(frame,
               text = "get",
               command = getEntryData,
               bg = "antiquewhite1",
               justify='left')
    b.pack()

    infoLabel.pack()

def clear_frame():
    for widgets in frame.winfo_children():  #clear every widget belonging to a frame
        widgets.destroy()
    frame.forget()


#--------------------------------Create GUI--------------------------------
root = Tk()                                                                     #create main window
root.geometry("600x250")                                                        #initial window size

mainBackgroundPath = "background_image.png" #add background image
img = PhotoImage(file = mainBackgroundPath)
backgroundLabel = Label( root, image = img)
backgroundLabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)

frame = Frame(root,bg = 'indianred4')                                           #create a frame,useful
                                                                                #useful for displaying
                                                                                #the results of the queries

rootLabel = Label(root,                                                         #welcome user
                  text = "Welcome to the mini Gallery app!",
                  font='Helvetica 16 bold underline')
rootLabel.place(x = 1420,y = 500)




b1 = Button(root,                                                               #add buttons
            text = "Artists",                                                   #each button initiates
            command = showArtists,                                              #the execution of a query
            bg = "antiquewhite1",                                               #see below about the
            justify='left')                                                     #button's arguements
b1.place(x=0, y=100)

b2 = Button(root,
            text = "Movements",
            command = showMovements,
            bg = "antiquewhite2",
            justify='left')
b2.place(x=0, y=150)

b3 = Button(root,
            text = "Artworks",
            command = showArtworks,
            bg = "antiquewhite3",
            justify='left')
b3.place(x=0, y=200)

b4 = Button(root,
            text = "Artist Info",
            command = getArtistInfo,
            bg = "indianred4",
            justify = 'left')
b4.place(x=0, y=250)

b5 = Button(root,                                                               #where the button is placed
            text = "Movements Info",                                            #button description ( a text)
            command = getMovementInfo,                                          #function executed on click
            bg = "salmon4",                                                     #button colour
            justify = 'left')                                                   #text position
b5.place(x=0, y=300)                                                            #place button in
                                                                                #appropriate grid coordinates

b6 = Button(root,
            text = "Artwork Info",
            command = getArtworkInfo,
            bg = "lightsalmon4",
            justify = 'left')
b6.place(x=0, y=350)

b7 = Button(root,
            text = "Search for Artwork",
            command = searchForArtwork,
            bg = "lightsalmon4",
            justify = 'left')
b7.place(x=0, y=400)

clearButton = Button(root,                                                      #special button
                     text = "Clear",                                            #that clears the frame
                     command = clear_frame,
                     bg = 'red',
                     justify = 'left')
clearButton.place(x=0, y=600)


root.mainloop()                                                                 #main loop of the GUI
                                                                                #creates GUI
                                                                                #if "X" button clicked
                                                                                #destroys GUI

conn.close()                                                                    #close  connection to the DB
                                                                                #on app's exit
