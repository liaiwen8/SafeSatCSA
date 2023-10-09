import tkinter as tk
from skyfield.api import load, EarthSatellite
from numpy.linalg import norm


def create_window2():
    window1.destroy()
    window2 = tk.Tk()
    window2.title("Enter Satellite Catalog Number")
    window2.geometry("400x200") 
    
    label = tk.Label(window2, text="Satellite Catalog Number:")
    label.pack()
    
    entry = tk.Entry(window2)
    entry.pack()
    
    def show_text():
        global satcat
        satcat = int(entry.get())
        window2.destroy()
        window3 = tk.Tk()
        window3.title("Test Window")
        window3.geometry("300x100")  
        
        label = tk.Label(window3, text="SEE TERMINAL")
        label.pack()

        print(satcat)

        compute_collisions(25544)
        
        window3.mainloop()
    
    button = tk.Button(window2, text="ENTER DATA", command=show_text)
    button.pack()
    
    window2.mainloop()

def create_window3():
    window1.destroy()
    window3 = tk.Tk()
    window3.title("Enter TLE Data")
    window3.geometry("400x250")  
    
    label1 = tk.Label(window3, text="TLE line one:")
    label1.pack()
    
    entry1 = tk.Entry(window3)
    entry1.pack()
    
    label2 = tk.Label(window3, text="TLE line two:")
    label2.pack()
    
    entry2 = tk.Entry(window3)
    entry2.pack()
    
    def show_text():
        global tle1, tle2
        tle1 = entry1.get()
        tle2 = entry2.get()
        window3.destroy()
        window4 = tk.Tk()
        window4.title("Test Window")
        window4.geometry("300x100")  
        
        label = tk.Label(window4, text="SEE TERMINAL")
        label.pack()

        collision_debris, collision_distances = compute_collisionsTLE(tle1, tle2)
        print(collision_debris)
        print(collision_distances)
        
        window4.mainloop()
    
    button = tk.Button(window3, text="ENTER DATA", command=show_text)
    button.pack()
    
    window3.mainloop()




def compute_collisions(catnum):
  names = []
  distances = []

  activeURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
  satellites = load.tle_file(activeURL, filename='sat.php')
  print('Loaded', len(satellites), 'satellites')

  num = {sat.model.satnum: sat for sat in satellites}
  satellite = num.get(catnum)

  if satellite is None:
    print("Invalid satellite serial number or TLE data.")
  else:
    t = load.timescale(delta_t=0).now()

  print("LOADED ", satellite.name)

  for i in range(10):
    t = load.timescale(delta_t=i).now()
    geoS = satellite.at(t)
    print(f"Position of Satellite at {t.utc_datetime()}: {geoS.position.km}")

    for debris in satellites:
      if debris != satellite:
        geoD = debris.at(t)
        position_S = geoS.position.km
        position_D = geoD.position.km
        position_difference = position_S - position_D

        distance_km = norm(position_difference)

        if distance_km < 5:
            print("COLLISION/NEAR MISS with", debris.name)
            print("Distance between satellite and debris:", distance_km, "km")
            names.append(debris.name)
            distances.append(distance_km)

  return names, distances






def compute_collisionsTLE(line1, line2):
  names = []
  distances = []

  activeURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
  satellites = load.tle_file(activeURL, filename='sat.php')
  print('Loaded', len(satellites), 'satellites')

  ts = load.timescale()
  satellite = EarthSatellite(line1, line2, "Custom Satellite", ts)
  print(satellite)

  if satellite is None:
    print("Invalid satellite serial number or TLE data.")
  else:
    t = load.timescale(delta_t=0).now()

  print("LOADED ", satellite.name)

  for i in range(10):
    t = load.timescale(delta_t=i).now()
    geoS = satellite.at(t)
    print(f"Position of Satellite at {t.utc_datetime()}: {geoS.position.km}")

    for debris in satellites:
      if debris != satellite:
        geoD = debris.at(t)
        position_S = geoS.position.km
        position_D = geoD.position.km
        position_difference = position_S - position_D

        distance_km = norm(position_difference)

        if distance_km < 5:
            print("COLLISION/NEAR MISS with", debris.name)
            print("Distance between satellite and debris:", distance_km, "km")
            names.append(debris.name)
            distances.append(distance_km)

  return names, distances







#main window
window1 = tk.Tk()
window1.title("SAFESAT CSA")
window1.geometry("400x150")  

button1 = tk.Button(window1, text="No Technical Experience", command=create_window2)
button1.pack()

button2 = tk.Button(window1, text="Technical Experience with TLEs", command=create_window3)
button2.pack()

window1.mainloop()
