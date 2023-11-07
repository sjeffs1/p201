from tkinter import *

window = Tk()
window.title("interest Calculator")
window.geometry("400x400")
window.configure(bg = "lightcyan")

def calculateBMI():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round (i, 2)

app_label = Label(window, text="interest Calculator", fg="black", bg="lightcyan", font=("Algerian", 20), bd=5)
app_label.place(x = 50, y = 20)

principle_label = Label(window, text="Enter principle: ", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
principle_label.place(x = 20, y = 90)

principle = Entry(window, text="", bd = 2, width = 22)
principle.place(x = 150, y = 92)

rate_label = Label(window, text="Enter rate: ", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
rate_label.place(x = 20, y = 140)

rate = Entry(window, text="", bd = 2, width = 22)
rate.place(x = 150, y = 142)

time_label = Label(window, text="Enter time: ", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
time_label.place(x = 20, y = 185)

time = Entry(window, text="", bd = 2, width = 22)
time.place(x = 150, y = 187)


calculate_button = Button(window, text="Calculate", fg="black", bg="cyan", bd=4, command=calculateBMI)
calculate_button.place(x = 20, y = 250)

result_frame = LabelFrame(window, text="result: ", bg="lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x = 20, y = 300)

result_label = Label(window, text="", bg="lightcyan", font=("Calibri", 12), width = 33)
result_label.place(x = 20, y = 200)
result_label.pack()

window.mainloop()

