import tkinter as tk

def create_window2():
    window1.destroy()
    window2 = tk.Tk()
    window2.title("Enter Satellite Catalog Number")
    window2.geometry("400x200")  # Set the initial window size
    
    label = tk.Label(window2, text="Satellite Catalog Number:")
    label.pack()
    
    entry = tk.Entry(window2)
    entry.pack()
    
    def show_text():
        data = entry.get()
        window2.destroy()
        window3 = tk.Tk()
        window3.title("Test Window")
        window3.geometry("400x200")  # Set the initial window size
        
        label = tk.Label(window3, text="TEST")
        label.pack()
        
        window3.mainloop()
    
    button = tk.Button(window2, text="ENTER DATA", command=show_text)
    button.pack()
    
    window2.mainloop()

def create_window3():
    window1.destroy()
    window3 = tk.Tk()
    window3.title("Enter TLE Data")
    window3.geometry("400x250")  # Set the initial window size
    
    label1 = tk.Label(window3, text="TLE line one:")
    label1.pack()
    
    entry1 = tk.Entry(window3)
    entry1.pack()
    
    label2 = tk.Label(window3, text="TLE line two:")
    label2.pack()
    
    entry2 = tk.Entry(window3)
    entry2.pack()
    
    def show_text():
        tle1 = entry1.get()
        tle2 = entry2.get()
        window3.destroy()
        window4 = tk.Tk()
        window4.title("Test Window")
        window4.geometry("400x200")  # Set the initial window size
        
        label = tk.Label(window4, text="TEST")
        label.pack()
        
        window4.mainloop()
    
    button = tk.Button(window3, text="ENTER DATA", command=show_text)
    button.pack()
    
    window3.mainloop()

# Create the main window
window1 = tk.Tk()
window1.title("Main Window")
window1.geometry("400x150")  # Set the initial window size for the main window

button1 = tk.Button(window1, text="No Technical Experience", command=create_window2)
button1.pack()

button2 = tk.Button(window1, text="Technical Experience with TLEs", command=create_window3)
button2.pack()

window1.mainloop()
