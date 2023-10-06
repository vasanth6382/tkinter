import tkinter as tk

window=tk.Tk()


dishes=['salad', 'potato wedges', 'garlic bread', 'margherita Pizza', 'Vegatable Pizza', 'Chicken Pizza', 'Ice Cream', 'Cookie', 'Chocolate Cake']
prices = [6.25, 5.25, 7.75, 13.75, 14.25, 15.75, 9.25, 8.25, 8.75, ]

global errorlabel
errorlabel = tk.Label(window, text="Please ensure that you use the correct data type", fg='red')

def submit():
    try:
        quantities=[dish1.get(), dish2.get(),dish3.get(),dish4.get(),dish5.get(),dish6.get(),dish7.get(),dish8.get(),dish9.get(),]
    except:
        errorlabel.grid(row=11, column=0, columnspan=3)
    else:
        errorlabel.grid_forget()
        bill = 0
        for x in range(len(quantities)):
            bill += prices[x] * quantities[x]
        label = tk.Label(window, text=f"The total bill is ${bill}", )
        label.grid(row=11, column=0, columnspan=3)

frame = tk.Frame(
    master=window, width=5,
    relief=tk.RAISED,
    borderwidth=1,
)
frame.grid(row=0, column=0)
label = tk.Label(master=frame, text=f"Dish", width=14, font=('Helvetica', 12, 'bold'))
label.pack()

frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame.grid(row=0, column=1)
label = tk.Label(master=frame, text=f"Price", width=4, font=('Helvetica', 12, 'bold'))
label.pack()

frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame.grid(row=0, column=2)
label = tk.Label(master=frame, text=f"Quantity", width=6, font=('Helvetica', 12, 'bold'))
label.pack()

for i in range(len(dishes)):
    frame = tk.Frame(
        master=window, width=5,
        relief=tk.RAISED,
        borderwidth=1,
    )
    frame.grid(row=i+1, column=0)
    label = tk.Label(master=frame, text=f"{dishes[i]}", width=20)
    label.pack()

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=i+1, column=1)
    label = tk.Label(master=frame, text=f"${prices[i]}", width=6)
    label.pack()


dish1=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish1)
entry.grid(row=1, column=2)

dish2=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish2)
entry.grid(row=2, column=2)

dish3=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish3)
entry.grid(row=3, column=2)

dish4=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish4)
entry.grid(row=4, column=2)

dish5=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish5)
entry.grid(row=5, column=2)

dish6=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish6)
entry.grid(row=6, column=2)

dish7=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish7)
entry.grid(row=7, column=2)

dish8=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish8)
entry.grid(row=8, column=2)

dish9=tk.IntVar()
entry=tk.Entry(window, width=10, textvariable=dish9)
entry.grid(row=9, column=2)

button=tk.Button(window, text='Order', command=submit)
button.grid(row=10, column=1)

window.mainloop()
