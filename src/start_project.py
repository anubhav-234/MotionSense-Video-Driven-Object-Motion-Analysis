from tkinter import * #imports the entire tkinter library
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from detect_objects import main

# ******************************************GUI OF THE PROGRAM***********************
root=Tk() #blank window called 'root'
root.title(" Velocity Estimation Project ")
root.geometry("700x500+0+0") #size of root window

heading = Label(root, text="Please enter the following information : ", font=("arial", 15, "bold"), fg="red").pack() #creates a heading of text
label_path = Label(root, text="Video File    : ", font=("arial", 12, "bold"), fg="green").place(x=10, y=100)
label_fov = Label(root, text="Field of View (m)  : ", font=("arial", 12, "bold"), fg="green").place(x=10, y=200)
label_minArea = Label(root, text="Min Area (50-2000) : ", font=("arial", 12, "bold"), fg="green").place(x=10, y=300)


# pathEntry_box = Entry(root, width=25, bg="white") #creates the name entry box

pathEntry_box=Entry(root,width=40, bg="white",font="Calibri 15 bold")
pathEntry_box.place(x=170, y=100) #defines the size of the entry box

def browsefunc():
    filename = askopenfilename(filetypes=(("mp4 file  ",'*.mp4'),))
    pathEntry_box.insert(END, filename) # add this

b1=Button(root,text="choose",font="Calibri 15 bold",width = 10,command=browsefunc)
b1.place(x=580,y=93)       

fovEntry_box = Entry(root, width=40, bg="white",font = "Calibri 15 bold")
fovEntry_box.place(x=170, y=200)

minAreaEntry_box = Entry(root, width=40, bg="white",font = "Calibri 15 bold")
minAreaEntry_box.place(x=170, y=300)


def execute(): #creates the function to be called once the button is pressed
    if (str(pathEntry_box.get()) != ""):
        video_path = str(pathEntry_box.get() or "hello")
        fov = float(fovEntry_box.get() or 1)
        min_area = int(minAreaEntry_box.get() or 1200)
        root.destroy()
        main(video_path,fov,min_area) # Main file execution  
        
    else:
        messagebox.showerror("Error","Select Video Path")

check = Button(root, text="Submit", width=10, height=2, bg="black", command= execute,font=('calibri', 13, 'bold'),foreground = 'white').place(x=320, y=400) #creates the button and calls the function to be executed

root.mainloop() #mainloop creates an inf loop of the open window so it stays open


