from tkinter import *
import sqlite3
#from PIL import ImageTk, Image
import numpy as np
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
style.use('ggplot')
import csv

root = Tk()
root.title("Bunnisher's Matplotlib")


def PlotIt():

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    x = np.random.randint(1,6,6)
    print("This is Poopy",x)
    y = np.random.randint(1,6,6)
    print("This is McDoopy",y)
    z = np.zeros(6)
    print("This is Haloopy",z)

    dx = np.ones(6)
    dy = np.ones(6)
    dz = [1,2,3,4,5,6]

    ax1.bar3d(x,y,z,dx,dy,dz)
    ax1.set_xlabel('Poopy')
    ax1.set_ylabel('McDoopy')
    ax1.set_zlabel('Haloopy')
    plt.show()

submit_btn = Button(root, text="Plot the information", command=PlotIt())
submit_btn.grid(row=8, column=1, pady=10)

button4 = Button(root, text="Shut er Down", command=root.destroy)
button4.grid(row=15, column=1, pady=10)

root.mainloop()
