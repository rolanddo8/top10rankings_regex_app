
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10570926
#    Student name: Le Hoang Minh Do (Jaymin Do)
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).  91023PT
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the specification document accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# You MAY NOT use any other module other than those supplied in this template.
# You may negotiate a change of this restriction with your client (Donna Kingsbury)s
# but be warned that non-standard modules such as 'Beautiful Soup' OR 'Pillow's
# will NOT be considered.

# You may need the following if there is a temporary SSL CERTIFICATE issue that iss
# beyond your control.  Only uncomment the following two lines if that is the case.s
##import ssl
##ssl._create_default_https_context = ssl._create_unverified_context

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution)
from urllib.request import urlopen

# Import the standard Tkinter functions.
# (You WILL need to use these functions in your s4olution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

##### DEVELOP YOUR SOLUTION HERE #####
#Import webbrowser module
import webbrowser
#Create a window
window = Tk()
topten = LabelFrame(window, bd = '7')
topten.grid()
#Give the window a title
window.title('Main menu')

#Varibles for url
imdb_previous_file = 'archieve/previousmovie.html'
imdb_current_html = 'https://www.imdb.com/chart/boxoffice'
bbc_current_html = 'https://www.bbc.co.uk/programmes/articles/TYv9MtpnqFRMPKP7QFcYfW/the-official-uk-top-40-singles-chart'
bbc_previous_file = 'archieve/bbc_previous_top10_song.html'
imdb_picture_html = 'https://static.amazon.jobs/teams/53/thumbnails/IMDb_Jobs_Header_Mobile.jpg?1501027253'
bbc_picture_html = 'https://ichef.bbci.co.uk/news/976/cpsprodpb/13FE0/production/_86288818_bbcmusic_logo_use.jpg'

#Local variables in order to recall many time
error_notification = 'ERROR: Do not have connection \nPlease check your network and try again'
bbc_local_image = 'Gif/bbc.gif'
imdb_local_image = 'Gif/imdb.gif'
previous_imdb_title = 'IMDB previous top 10 movie'
current_imdb_title = 'IMDB current top 10 movie'
previous_bbc_title = 'Previous BBC Top10 Singles chart'
current_bbc_title = 'Current BBC Top10 Singles chart'

#Create a image in main window
topten_image = PhotoImage(file = 'Gif/toptenimage.gif')

#Crate frame for the picture in main window
labelframe_picture = LabelFrame(topten, bd = '5')
labelframe_picture.grid(row = 1, column = 1, columnspan = 3, rowspan = 3, padx = 10, pady = 5)
#Create a picture and insert it into the frame
picture = Label(labelframe_picture, image = topten_image)
picture.grid(row = 0, column = 0)
#Create a title in main window
Label(topten, text = 'TOP 10 Movies and Songs', font = ('Times', 30, 'bold'), fg = 'Black', bg = 'Yellow').grid(row = 0, column = 1, columnspan = 7) 

#Create frame and title of top10 imdb movies
IMDB_frame = LabelFrame(topten, bd = '10', text = '      IMDB       ', font = ('Arial', 20))
IMDB_frame.grid(row = 1, column = 4, columnspan = 3)
movie_Top10 = Label(IMDB_frame, text = 'Movie Top10', font = ('Arial', 20))
movie_Top10.grid(row = 1, column = 4,columnspan = 6)

#Crate frame and title of top10 bbc songs
bbc_frame = LabelFrame(topten, bd = '10', text = '         TOP          ',font = ('Arial', 20))
bbc_frame.grid(row = 2, column = 4, columnspan = 3)
bbc_treding = Label(bbc_frame, text = 'BBC Singles Chart', font = ('Arial', 20))  
bbc_treding.grid(row = 1, column =4, columnspan = 6)


#Read a previous html file 
#Modified from supplied code of Donna Kingsbury
def read_current_html(url):
    #read the url
    webpage = urlopen(url)
    #read the text
    html_code = webpage.read().decode("UTF-8")
    #close the webpage
    webpage.close()
    return html_code

#Read a current html link
def read_previous_html(filename):
    #
    html_code = open(filename).read()
    return html_code

#Two functions below are created for get and list top10 things (movies or songs)
def gettop10_imdb(top10_things):
    templist = ''
    counter = 1 
    for i in range(10):  #Name of IMDB movies begin in first element of the list
        templist = templist + str(counter) + '.   ' + top10_things[i] + '\n' 
        counter = counter + 1
    return templist
def gettop10_bbc(top10_things):
    templist = ''
    counter = 1 
    for i in range(1,11):  #Name of BBC songs begin in second element of the list
        templist = templist + str(counter) + '.   ' + top10_things[i] + '\n' 
        counter = counter + 1
    return templist


#Two variables to store the list of name of top movies and songs of previous file
#The current url have a error "urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>" so that cannot be created over the funtion
top10_imdb_previous = findall('alt="(.*)"/>', read_previous_html(imdb_previous_file))
top10_bbc_previous = findall('<h2>(.*)</h2>', read_previous_html(bbc_previous_file)) 

#Create function for preview button
def preview_function():
    if var.get() == 1:
        imdb_subwindow1 = Toplevel() #Create subwindow
        #Create a title of subwindow  
        imdb_subwindow1.title(previous_imdb_title)
        Label(imdb_subwindow1, text = previous_imdb_title, font = ('Times', 30, 'bold'), bg = 'yellow').grid(row = 0, column = 1, columnspan = 10, ipadx = 240)
        #Create the frame and insert image imdb into
        labelframe_picture_imdb = LabelFrame(imdb_subwindow1, bd = '5')
        labelframe_picture_imdb.grid(row = 1, column = 1, pady = 7)
        imdb_image = PhotoImage(file = imdb_local_image)
        imdb_picture_previous = Label(labelframe_picture_imdb, image = imdb_image)
        imdb_picture_previous.image = imdb_image
        imdb_picture_previous.grid(row = 1, column = 0)
        #List the name of top10 imdb movies
        text_imdb = Label(imdb_subwindow1, text = gettop10_imdb(top10_imdb_previous) , font = ('Times', 20, 'bold'), justify = LEFT, bg = 'light sky blue')
        text_imdb.grid(row = 1, column = 2, padx = 5, ipady= 70)
    elif var.get() == 2:
          
        imdb_subwindow2 = Toplevel()#Create subwindow
        #Create a title of subwindow  
        imdb_subwindow2.title(current_imdb_title)
        Label(imdb_subwindow2, text = current_imdb_title, font = ('Times', 30, 'bold'), bg = 'yellow').grid(row = 0, column = 0, columnspan = 10, ipadx = 250)
        #create image frame and insert the image
        labelframe_image_imdb = LabelFrame(imdb_subwindow2, bd = '5')
        labelframe_image_imdb.grid(row = 1, column = 0, pady = 5)
        imdb_image_current = PhotoImage(file = imdb_local_image)
        imdb_picture_current = Label(labelframe_image_imdb, image = imdb_image_current)
        imdb_picture_current.image = imdb_image_current
        imdb_picture_current.grid(row = 1, column = 0)
        try: 
            #List the name of top10 bbc songs
            top10_imdb_current = findall('alt="(.*)"/>', read_current_html(imdb_current_html))
            text_imdb_current = Label(imdb_subwindow2, text = gettop10_imdb(top10_imdb_current), font = ('Times', 20, 'bold'), justify = LEFT, bg = 'light sky blue')
            text_imdb_current.grid(row = 1, column = 2, padx = 5, ipady = 70)
        except: #In case of no internet
            text_imdb_current = Label(imdb_subwindow2, text = error_notification , font = ('Times', 20, 'bold'), justify = LEFT, bg = 'red')
            text_imdb_current.grid(row = 1, column = 2, padx = 5, ipady = 150)
    elif var.get() == 3:
        bbc_subwindow1 = Toplevel()#Create subwindow
        #Create a title of subwindow 
        bbc_subwindow1.title(previous_bbc_title)
        Label(bbc_subwindow1, text = previous_bbc_title, font = ('Times', 30, 'bold'), bg = 'yellow').grid(row = 0, column = 0, columnspan = 10, ipadx = 94)
        #Create image frame and insert the image
        labelframe_image_bbc = LabelFrame(bbc_subwindow1, bd = '5')
        labelframe_image_bbc.grid(row = 1, column = 0, pady = 5, padx = 5)
        bbc_image = PhotoImage(file = bbc_local_image)
        bbc_image_previous = Label(labelframe_image_bbc, image = bbc_image)
        bbc_image_previous.image = bbc_image
        bbc_image_previous.grid(row = 0, column = 0, padx = 5)
        #List the name of top10 bbc songs
        text_bbc = Label(bbc_subwindow1, text = gettop10_bbc(top10_bbc_previous), font = ('Times', 17, 'bold'), justify = LEFT, wraplength = 500, bg = 'light sky blue')
        text_bbc.grid(row = 1, column = 2, padx = 5, pady= 5, ipady= 85)
    elif var.get() == 4:
            bbc_subwindow2 = Toplevel()#Create subwindow
            #Create a title of subwindow 
            bbc_subwindow2.title(current_bbc_title)
            Label(bbc_subwindow2, text = current_bbc_title, font = ('Times', 30, 'bold'), bg = 'yellow').grid(row = 0, column = 0, columnspan = 10, ipadx = 90)
            #Create image frame and insert the image
            labelframe_picture_bbc = LabelFrame(bbc_subwindow2, bd = '5')
            labelframe_picture_bbc.grid(row = 1, column = 0, pady = 5)
            bbc_image = PhotoImage(file = bbc_local_image)
            bbc_picture_current = Label(labelframe_picture_bbc, image = bbc_image)
            bbc_picture_current.image = bbc_image
            bbc_picture_current.grid(row = 1, column = 0, padx = 5)
            try:
                #List the name of top10 bbc songs
                top10_bbc_current = findall('<h2>(.*)</h2>', read_current_html(bbc_current_html))     
                text_bbc = Label(bbc_subwindow2, text = gettop10_bbc(top10_bbc_current), font = ('Times', 17, 'bold'), justify = LEFT, wraplength = 600, bg = 'light sky blue')
                text_bbc.grid(row = 1, column = 2, padx = 5, pady= 5, ipady= 50)
            except: #in case of no internet
                #Crate a notification for user
                text_bbc = Label(bbc_subwindow2, text = error_notification, font = ('Times', 17, 'bold'), justify = LEFT,  bg = 'red')
                text_bbc.grid(row = 1, column = 2, padx = 5, pady= 5,  ipady = 80)
#Two functions below are created for wirte the html webpage
def write_html_imdb(title, top10_things, picture_html, time, gross, bg_color, url_name):
    htmltitle = title    
    htmlname =  htmltitle +'.html'
    htmlfile = open(htmlname, 'w')
    htmlfile.write('''<!DOCTYPE>

    <html>
        <head>
            <title> ''' + htmltitle + '''(Previous) </title>
            <!-- Jaymin - N10570926 -->
        </head>
        <style>
            body
            {
                        background-color: ''' + bg_color + ''';
                    } 
        </style>
        <body>    
            
            <h1 align = "center"> ''' + title + ''' </h1>
            <p align = "center">
            <img src="''' + picture_html + '''",
                width=40%, height = 40%, align="middle">
            </p>
            <h3 align = "center">''' + time + '''</h3>
            <table align = "center",  border = "2", cellspacing="4">
                <tr>
                    <th>#</th>
                    <th>Movie Name</th>
                    <th>Gross</th>
                </tr> ''')
    for i in range(10):  
        htmlfile.write('<tr>')
        htmlfile.write('\n' + '<th> ' + str(i+1)  + ' </th>')        #Number will count from number 1 
        htmlfile.write('\n' + '<th>' + top10_things[i] + '</th>')    #Name of IMDB movies begin in first element of the list
        htmlfile.write('\n' + '<th>' + gross[i] + '</th>')           #Gross of each movie begin in first element of the list
        htmlfile.write('\n' + '</  tr>')
    htmlfile.write(''' 
            </table>
            <h4 align = "center"> <span style="color:blue"> <u>''' + url_name + ''' </u> </span> </h4>
        </body>
    </html>
    ''')    
    #open webpage direcly
    webbrowser.open(htmlname)

def write_html_bbc(title, top10_things, picture_html, time, time_in_chart, bg_color, url_name):
    htmltitle = title    
    htmlname =  htmltitle +'.html'
    htmlfile = open(htmlname, 'w')
    htmlfile.write('''<!DOCTYPE>

    <html>
        <head>
            <title> ''' + htmltitle + '''(Previous) </title>
            <!-- Jaymin - N10570926 -->
        </head>
        <style>
            body
            {
                        background-color: ''' + bg_color + ''';
                    } 
        </style>
        <body>    
            
            <h1 align = "center"> ''' + title + ''' </h1>
            <p align = "center">
            <img src="''' + picture_html + '''",
                width=40%, height = 40%, align="middle">
            </p>
            <h3 align = "center">''' + time + '''</h3>
            <table align = "center",  border = "2", cellspacing="4">
                <tr>
                    <th>#</th>
                    <th>Movie Name</th>
                    <th>Time in chart</th>
                </tr> ''')
    for i in range(10):  
        htmlfile.write('<tr>')
        htmlfile.write('\n' + '<th> ' + str(i + 1)  + ' </th>') #Number will count from number 1
        htmlfile.write('\n' + '<th>' + top10_things[i + 1] + '</th>') #Name of BBC songs begin in second element of the list
        htmlfile.write('\n' + '<th>' + time_in_chart[i + 1] + '</th>')  #Time in chart of each song begin in second element of the list 
        htmlfile.write('\n' + '</  tr>')
    htmlfile.write(''' 
            </table>
            <h4 align = "center"> <span style="color:blue"> <u>''' + url_name + ''' </u> </span> </h4>
        </body>
    </html>
    ''')    
    #Open webpage direcly
    webbrowser.open(htmlname)
#Create a nitification for user in case of no internet
def error_html():
    htmltitle = error_notification   
    htmlname =  'no_internet.html'
    htmlfile = open(htmlname, 'w')
    htmlfile.write('''<!DOCTYPE>
                <html>
                    <head>
                        <title> ''' + htmltitle + '''(Previous) </title>
                        <!-- Jaymin - N10570926 -->
                    <head>
                    <style>
                        body
                        {
                                    background-color: red;
                                } 
                    </style>
                    <body>    
                        
                        <h1 align = "center"> ''' + htmltitle + ''' </h1>
                    </body>
                </html>
                ''')   
    #Open webpage direcly
    webbrowser.open(htmlname)

#Create a export function
def export_function():
    global imdb_picture_html, bbc_picture_html, top10_bbc_current, top10_bbc_previous, top10_imdb_previous
    if var.get() == 1:
        time_imdb_previous = findall('<h4>(.*)</h4>', read_previous_html(imdb_previous_file))[0]
        gross_imdb_previous = findall('"secondaryInfo">(.*)</span>', read_previous_html(imdb_previous_file))
        imdb_bgcolor = '#F5DEB3'
        write_html_imdb(previous_imdb_title, top10_imdb_previous, imdb_picture_html, time_imdb_previous, gross_imdb_previous, imdb_bgcolor, imdb_previous_file)
       
    elif var.get() == 2:
        try:
            top10_imdb_current = findall('alt="(.*)"/>', read_current_html(imdb_current_html))
            time_imdb_current = findall('<h4>(.*)</h4>', read_current_html(imdb_current_html))[0]
            gross_imdb_current = findall('"secondaryInfo">(.*)</span>', read_current_html(imdb_current_html))
            imdb_bgcolor = '#F5DEB3'
            write_html_imdb(current_imdb_title, top10_imdb_current, imdb_picture_html, time_imdb_current, gross_imdb_current, imdb_bgcolor, imdb_current_html)
        except OSError: #In case of no internet
            error_html()   
    elif var.get() == 3:
        time_bbc_previous = findall('<em>(.*)</em>', read_previous_html(bbc_previous_file))[0]
        time_song_inchart_previous = findall('<p>(.*)</p>', read_previous_html(bbc_previous_file))
        bbc_bgcolor = 'grey'
        write_html_bbc(previous_bbc_title, top10_bbc_previous, bbc_picture_html, time_bbc_previous, time_song_inchart_previous, bbc_bgcolor, bbc_previous_file)
    elif var.get() == 4:
        try:
            top10_bbc_current = findall('<h2>(.*)</h2>', read_current_html(bbc_current_html)) 
            time_bbc_current = findall('<em>(.*)</em>', read_current_html(bbc_current_html))[0]
            time_song_inchart_current = findall('<p>(.*)</p>', read_current_html(bbc_current_html))
            bbc_bgcolor = 'grey'
            write_html_bbc(current_bbc_title, top10_bbc_current, bbc_picture_html, time_bbc_current, time_song_inchart_current, bbc_bgcolor, bbc_current_html)
        except OSError: #In case of no internet
            error_html()

#Create previous and current radiobuttons
var = IntVar() #Create a varible of buttons
#Previous radio button of IMDB top10 movies
previous_buttons1 = Radiobutton(IMDB_frame, text = 'Previous', 
                                font = ('Times', 13), variable = var, value = 1, selectcolor = 'grey') 
previous_buttons1.grid(row = 2, column = 3, rowspan = 3, columnspan = 3)
#Previous radio button of BBC top10 songs
current_buttons1 = Radiobutton(IMDB_frame, text = 'Current', 
                               font = ('Times', 13), variable = var, value = 2, selectcolor = 'grey') 
current_buttons1.grid(row = 2, column = 7, columnspan = 3, rowspan = 3)

#Current radio button of IMDB top10 movie
previous_buttons2 = Radiobutton(bbc_frame, text = 'Previous', 
                                font = ('Times', 13), variable = var, value = 3, selectcolor ='grey') 
previous_buttons2.grid(row = 2, column = 2, rowspan = 3, columnspan = 4)
#Current radio button of BBC top10 songs
current_buttons2 = Radiobutton(bbc_frame, text = 'Current', 
                                font = ('Times', 13), variable = var, value = 4, selectcolor = 'grey') 
current_buttons2.grid(row = 2, column = 6, columnspan = 4, rowspan = 3)

#Create a frame in the bottom of main window
bottom_frame = LabelFrame(topten, bd = '15')
bottom_frame.grid(row = 4, column = 0, rowspan = 3, columnspan=10, pady = 10)

#Create the buttons preview and export button

preview = Button(bottom_frame, text = 'Preview', font = ('Arial', 20), bg = 'white', command = preview_function)
preview.grid(row = 0, column = 10, padx =50)
export = Button(bottom_frame, text = 'Export' ,font = ('Arial', 20), bg = 'white', command = export_function)
export.grid(row = 0, column = 20, padx = 55)


#END
mainloop()
