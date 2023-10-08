import tkinter as tk
from numpy import number
from skyfield.api import load, wgs84
from numpy.linalg import norm
from skyfield.api import EarthSatellite
from PIL import Image, ImageTk

# Function to input TLE data from the user

activeURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
analystURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=analyst&FORMAT=tle'
satellites = load.tle_file(activeURL, filename='sat.php')
analyst = load.tle_file(analystURL, filename='ana.php')
#print('Loaded', len(satellites), 'satellites')
#print('Loaded', len(analyst), 'A')

root= tk.Tk()

img = ImageTk.PhotoImage(Image.open("satellite.png"))
panel = tk.Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

canvas1 = tk.Canvas(root, width=600, height=600, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='SafeSat App')
label1.config(font=('helvetica', 14))
canvas1.create_window(250, 25, window=label1)

label6 = tk.Label(root, text='What is your Satellite Serial Number?:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label6)

entry4 = tk.Entry(root) 
canvas1.create_window(370, 100, window=entry4)

label7 = tk.Label(root, text='What is your 2nd Satellite Serial Number?:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 140, window=label7)

entry5 = tk.Entry(root) 
canvas1.create_window(370, 140, window=entry5)

#def get_user_tle_input():
    #label10 = tk.Label(root, text='Enter TLE Line 1: ')
    #label1.config(font=('helvetica', 10))
    #canvas1.create_window(25, 140, window=label10)
    #tle_line1 = tk.Entry(root) 
    #canvas1.create_window(100, 140, window=tle_line1)
    #label11 = tk.Label(root, text='Enter TLE Line 2: ')
    #label1.config(font=('helvetica', 10))
    #canvas1.create_window(25, 140, window=label11)
    #tle_line2 = tk.Entry(root) 
    #canvas1.create_window(100, 140, window=tle_line2)
    #return tle_line1, tle_line2

def get_check_collisions():
    inA = entry4.get()
    inB = entry5.get()

    label8 = tk.Label(root, text='working ' + inA + '+' +inB , font=('helvetica', 10))
    canvas1.create_window(200, 120, window=label8)

   # inA = int(input("serialA (Enter 0 to input your own TLE data): "))
#inB = int(input("serialB (Enter 0 to input your own TLE data): "))

    numactive = {sat.model.satnum: sat for sat in satellites}
    numanalyst = {sat.model.satnum: sat for sat in satellites}
    satellite = numactive[inA]
#print(satellite)
    debris = numanalyst[inB]
#print(debris)

    t = load.timescale(delta_t=0).now()

    for i in range(0, 1000, 10):
        t = load.timescale(delta_t=i).now()
        geoS = satellite.at(t)
        geoD = debris.at(t)
        #print(geoS.position.km)
        #print(geoD.position.km)

    # Calculate the position vectors and their difference
        position_S = geoS.position.km
        position_D = geoD.position.km
        position_difference = position_S - position_D

    # Calculate the distance between the objects
        distance_km = norm(position_difference)

        if distance_km < 5:
            label14 = tk.Label(root, text='Collision')
            label1.config(font=('helvetica', 10))
            canvas1.create_window(200, 200, window=label14)

            exit ()
        else:
            label14 = tk.Label(root, text='no Collision')
            label1.config(font=('helvetica', 10))
            canvas1.create_window(200, 200, window=label14)
            exit()

    
button1 = tk.Button(text='Check for collisions', command=get_check_collisions, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 220, window=button1)

root.mainloop()

