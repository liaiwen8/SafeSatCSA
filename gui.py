import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=600, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='SafeSat App')
label1.config(font=('helvetica', 14))
canvas1.create_window(250, 25, window=label1)

#label2 = tk.Label(root, text='What is your Perogee?:')
#label2.config(font=('helvetica', 10))
#canvas1.create_window(200, 100, window=label2)

#entry1 = tk.Entry(root) 
#canvas1.create_window(350, 100, window=entry1)


#label3 = tk.Label(root, text='What is your Apogee?:')
#label3.config(font=('helvetica', 10))
#canvas1.create_window(200, 160, window=label3)

#entry2 = tk.Entry(root) 
#canvas1.create_window(350, 160, window=entry2)

#label5 = tk.Label(root, text='What is your Inclination?:')
#label3.config(font=('helvetica', 10))
#canvas1.create_window(200, 200, window=label5)

#entry3 = tk.Entry(root) 
#canvas1.create_window(350, 200, window=entry3)

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

def get_check_collisions():
    x1 = entry4.get()
    x2 = entry5.get()

    label8 = tk.Label(root, text='working ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 120, window=label8)

    
button1 = tk.Button(text='Check for collisions', command=get_check_collisions, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 220, window=button1)

root.mainloop()
