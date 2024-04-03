import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            gender = gender_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course info
            customer_status = reg_status_var.get()
            numorders = numorders_spinbox.get()
            amountpaid = amountpaid_spinbox.get()
            
            print("Firstname: ", firstname, "Lastname: ", lastname)
            print("Gender: ", gender, "Age: ", age, "Nationality: ", nationality)
            print("# Orders: ", numorders, "Total paid: ", amountpaid)
            print("Customer status", customer_status)
            print("------------------------------------------")
            
            filepath = r"C:\Users\selim\Desktop\py\Excel data entry form\data.xlsx"
            
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["Firstname", "Lastname", "Gender", "Age", "Nationality",
                           "# Orders", "Total paid", "Customer status"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, gender, age, nationality, numorders,
                          amountpaid, customer_status])
            workbook.save(filepath)
                
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Firstname")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Lastname")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms."])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

customer_label = tkinter.Label(courses_frame, text="Customer Status")

reg_status_var = tkinter.StringVar(value="Not Premium")
customer_check = tkinter.Checkbutton(courses_frame, text="Currently Premium",
                                       variable=reg_status_var, onvalue="Premium", offvalue="Not Premium")

customer_label.grid(row=0, column=0)
customer_check.grid(row=1, column=0)

numorders_label = tkinter.Label(courses_frame, text= "# Orders")
numorders_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numorders_label.grid(row=0, column=1)
numorders_spinbox.grid(row=1, column=1)

amountpaid_label = tkinter.Label(courses_frame, text="Total paid")
amountpaid_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
amountpaid_label.grid(row=0, column=2)
amountpaid_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()