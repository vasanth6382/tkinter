import tkinter as tk

window=tk.Tk()

dishes=['salad', 'potato wedges', 'garlic bread', 'margherita Pizza', 'Vegatable Pizza', 'Chicken Pizza', 'Ice Cream', 'Cookie', 'Chocolate Cake']
prices = [6.25, 5.25, 7.75, 13.75, 14.25, 15.75, 9.25, 8.25, 8.75, ]

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



entry=tk.Entry(window, width=10)
entry.grid(row=1, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=2, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=3, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=4, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=5, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=6, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=7, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=8, column=2)

entry=tk.Entry(window, width=10)
entry.grid(row=9, column=2)

button=tk.Button(window, text='Order',)
button.grid(row=10, column=1)

window.mainloop()