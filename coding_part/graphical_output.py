# Import Module
from tkinter import *
import matplotlib.pyplot as plt

def plot_graphs(speed_graph,accelaration_graph,fps) :
    # create root window
    root = Tk()

    # root window title and dimension
    root.title("Velocity And Accelaration Output")
    # Set geometry (widthxheight)
    root.geometry('350x200')

    heading = Label(root, text="Graphical Outputs  : ", font=("arial", 15, "bold"), fg="red").pack() #creates a heading of text

    def velocity_time():
        # Ploting the Graph
        for Y in speed_graph:
            X = []
            for i in range(len(Y)):
                X += [i+1]
            plt.plot(X,Y)
        t_unit = round(50 / fps,2)
        str1 =  "time( 1 unit = " + str(t_unit) + " sec )" + "----> "  
        plt.xlabel(str1)
        plt.ylabel('Speed in meter per seconds (mps)'+'---->')
        plt.title("Velocity Vs Time graph")
        plt.show()

    def accelaration_time():
        # Ploting the Graph
        for Y in accelaration_graph:
            X = []
            for i in range(len(Y)):
                X += [i+1]
            plt.plot(X,Y)
        t_unit = round(50 / fps,2)
        str1 =  "time( 1 unit = " + str(t_unit) + " sec )" + "----> "  
        plt.xlabel(str1)
        plt.ylabel('Acceleration in meter per seconds (mps2)'+'---->')
        plt.title('Acceleration Vs Time graph')
        plt.show()

    b1=Button(root,text="Velocity Vs Time Plot",font="Calibri 15 bold",width = 30,command=velocity_time)
    b1.place(x=20,y=30)  

    b1=Button(root,text="Accelaration Vs Time Plot",font="Calibri 15 bold",width = 30,command=accelaration_time)
    b1.place(x=20,y=90)  

    # all widgets will be here
    # Execute Tkinter
    root.mainloop()   