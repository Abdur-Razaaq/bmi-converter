# Imports all toll from tkinter
from tkinter import *

# Initialization of window
root = Tk()

# Sets window size, title and colour
root.geometry("400x400")
root.title("Body Mass Index Calculator")
root.config(bg="Yellow")

# Setting values
mass_ans = IntVar()
height_ans = IntVar()
bmi_ans = IntVar()
age = IntVar()
gender = IntVar()


# Calculates the BMI and gives one of the three results if all values are added
# Also checks if entered values are not zero if zero display 0
def calculate_bmi():
    try:
        result = float(ans.get()) / (float(height.get()) * float(height.get()))
        bmi_ans.set(result)
    except ZeroDivisionError:
        mass_ans.set(0)
        height_ans.set(0)
        bmi_ans.set(0)
        return
    if result < 18.5:
        resLabelText.set("You are categorised as Underweight!")
    if 18.5 < result < 25:
        resLabelText.set("You are categorised as Normal!")
    if result > 25:
        resLabelText.set("You are categorised as Overweight!")
    return


# Labels and entry fields added and set using pack
# Age label
ageLabelText = StringVar()
ageLabelText.set("Age: ")
massLabel = Label(root, textvariable=ageLabelText)
massLabel.pack()

# Age entry field
ans = Entry(root, textvariable=age)
ans.pack()

# Gender label
genderLabelText = StringVar()
genderLabelText.set("Gender: ")
massLabel = Label(root, textvariable=genderLabelText)
massLabel.pack()

# Gender Entry field
ans = Entry(root, textvariable=gender)
ans.pack()

# mass label
mLabelText = StringVar()
mLabelText.set("Mass in kg: ")
massLabel = Label(root, textvariable=mLabelText)
massLabel.pack()

# mass entry field
ans = Entry(root, textvariable=mass_ans)
ans.pack()

# Label for height
hLabelText = StringVar()
hLabelText.set("Height in m: ")
heightLabel = Label(root, textvariable=hLabelText)
heightLabel.pack()

# height entry field
height = Entry(root, textvariable=height_ans)
height.pack()

# Button and label for BMI calculation
button = Button(root, text="Calculate BMI", command=calculate_bmi)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(root, textvariable=bmiLabelText)
bmiLabel.pack()

# answer field for BMI
bmi = Entry(root, textvariable=bmi_ans)
bmi.pack()

# result label text
resLabelText = StringVar()
resLabelText.set(" You are categorised as: ")
resLabel = Label(root, textvariable=resLabelText)
resLabel.pack()

# Ensures that the window remains open until terminated by the user
root.mainloop()
