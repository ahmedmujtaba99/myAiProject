import tkinter as tk
from tkinter import ttk
from my_ai_project import predict

def calculate_price():
    # Retrieve the values from the entry fields and combobox
    age = int(age_entry.get())
    gender = gender_combobox.get()
    if gender == 'Male':
        gender = 0
    else:
        gender = 1
    bmi = float(bmi_entry.get())
    children = int(children_entry.get())
    smoker = smoker_var.get()

    region = region_combobox.get()
    if region == 'southeast':
        region = 0
    elif region == 'southwest':
        region = 1
    elif region == 'northeast':
        region = 2;
    else:
        region = 3
    # Perform any calculations or processing here to get the predicted price
    # Replace the following line with your own logic or machine learning model
  # Placeholder value

    # Display the predicted price
    price_label.config(text=f"Predicted Price: ${predict(age,gender,bmi,children,smoker,region)}")

# Create the main Tkinter window
window = tk.Tk()
window.title("Insurance Price Prediction")

# Create labels
labels = ["Age:", "Gender:", "BMI:", "No. of Children:", "Smoker:", "Region:"]
for i, label_text in enumerate(labels):
    label = tk.Label(window, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=10)

# Create entry fields
age_entry = tk.Entry(window)
age_entry.grid(row=0, column=1, padx=10, pady=10)

bmi_entry = tk.Entry(window)
bmi_entry.grid(row=2, column=1, padx=10, pady=10)

children_entry = tk.Entry(window)
children_entry.grid(row=3, column=1, padx=10, pady=10)

# Create gender combobox
gender_combobox = ttk.Combobox(window, values=["Male", "Female"])
gender_combobox.grid(row=1, column=1, padx=10, pady=10)

# Create smoker checkbox
smoker_var = tk.IntVar()
smoker_checkbox = tk.Checkbutton(window, text="Smoker", variable=smoker_var)
smoker_checkbox.grid(row=4, column=1, padx=10, pady=10)

# Create region combobox
# add here
region_combobox = ttk.Combobox(window, values=['southeast','southwest','northeast','northwest'])
region_combobox.grid(row=5, column=1, padx=10, pady=10)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_price)
calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create the predicted price label
price_label = tk.Label(window, text="Predicted Price: ")
price_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
