from tkinter import messagebox
import customtkinter
from tkinter import *

# Initialize the main application window
app = customtkinter.CTk()
app.title('BMI CALCULATOR')
app.geometry("300x350")
app.config(bg="#000000")  


font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        
        if variable2.get() == "ft":
            height *= 30.48  # Convert feet to cm
        if variable1.get() == "ibs":
            weight *= 0.453592  # Convert pounds to kg

        bmi = weight / ((height / 100) ** 2)
        result_label.configure(text="Your BMI is : {:.1f}".format(bmi))
        
        # Interpret the BMI value
        if bmi < 18.5:
            interpretation = "You need to be on a diet so bad.You are Underweight"
        elif 18.5 <= bmi < 24.9:
            interpretation = "Your are healthy, Stay fit"
        elif 25 <= bmi < 29.9:
            interpretation = "You are Overweight, Exercise more"
        else:
            interpretation = "Obesity, Consult  a doctor"
        
        result_label.configure(text="Your BMI is : {:.1f}\n{}".format(bmi, interpretation))

    except ValueError:
        messagebox.showerror('Error', 'Enter a valid number!')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Your height cannot be zero')



title_label = customtkinter.CTkLabel(
    app, 
    font=font1, 
    text='BMI CALCULATOR',
    text_color='#ffffff',  
    fg_color='#000000'    
)
title_label.place(x=20, y=20)


weight_label = customtkinter.CTkLabel(
    app, 
    font=font2, 
    text='Weight',
    text_color='#ffffff', 
    fg_color='#000000'
)
weight_label.place(x=20, y=80)

height_label = customtkinter.CTkLabel(
    app, 
    font=font2, 
    text='Height',
    text_color='#ffffff',  
    fg_color='#000000'     
)
height_label.place(x=20, y=150)

weight_entry = customtkinter.CTkEntry(
    app, 
    font=font2,
    text_color='#ffffff',
    fg_color = '#000'
)
weight_entry.place(x = 20, y=110)


height_entry = customtkinter.CTkEntry(
    app, 
    font=font2,
    text_color='#ffffff',
    fg_color = '#000'
)
height_entry.place(x = 20, y=180)


weight_options = ['kg', 'ibs']
height_options = ['cm', 'ft']

variable1 = StringVar()
variable2 = StringVar()

weight_option = customtkinter.CTkComboBox (
    app,
    font=font2,
    text_color = '#ffffff', 
    dropdown_hover_color = '#06911f',
    values = weight_options,
    variable = variable1 , 
    width = 80,
    state = 'readonly'
)

weight_option.place(x = 180 , y = 110)
weight_option.set('kg')


heigth_option = customtkinter.CTkComboBox (
    app,
    font=font2,
    text_color = '#ffffff', 
    dropdown_hover_color = '#06911f',
    values = height_options,
    variable = variable2     , 
    width = 80,
    state = 'readonly'
)

heigth_option.place(x = 180 , y = 180)
heigth_option.set('cm')

calculate_button = customtkinter.CTkButton (
    app,
    font=font2,
    text_color = '#ffffff',
    text = 'Calculate BMI',
    fg_color = '#06911f', 
    hover_color = '#06911f',
    bg_color = '#000000',
    cursor = 'hand2',
    corner_radius = 5,
    width = 200,
    command = calculate_bmi
)

calculate_button.place(x = 50 , y = 230)

result_label = customtkinter.CTkLabel (
    app,
    text = '',
    font = font2, 
    text_color = '#ffffff',
    bg_color = '#000000'
)

result_label.place (x = 20 , y = 280)

app.mainloop() 

 


