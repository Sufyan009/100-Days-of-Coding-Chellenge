from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("Millage Converter")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "Text"


def clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=clicked)
button.pack()

# Enter
input = Entry()
input.pack()
print(input.get())


window.mainloop()
