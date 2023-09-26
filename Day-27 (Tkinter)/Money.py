from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 279.3713)
    Km_result_label.config(text=f"{km}")


window = Tk()
window.title("Paisaaa")
window.config(padx=20, pady=20)

miles_input = Entry(width=9)
miles_input.grid(column=1, row=0)

mile_label = Label(text="$Dollar")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=-0, row=1)

Km_result_label = Label(text="0")
Km_result_label.grid(column=1, row=1)

Km_label = Label(text="Rps")
Km_label.grid(column=3, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
