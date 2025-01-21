import tkinter as tk
from PIL import Image, ImageTk
import config

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title('Budget App')
root.geometry('400x400')  # Set the window size to 300x300 pixels
root.configure(bg='#058E9D')  # Set the background color for the root window

# Load the image and resize it
image = Image.open("1.jpg")
image = image.resize((300, 120), Image.ANTIALIAS)  # Resize the image
photo = ImageTk.PhotoImage(image)

# Setting up the frames for each page with a background color
welcome_frame = tk.Frame(root, bg='#058E9D', width=400, height=400)
input_frame = tk.Frame(root, bg='#058E9D', width=400, height=400)
summary_frame = tk.Frame(root, bg='#058E9D', width=400, height=400)
new_expense_frame = tk.Frame(root, bg='#058E9D', width=400, height=400)
new_expense_frame.grid(row=0, column=0, sticky='news')

for frame in (welcome_frame, input_frame, summary_frame):
    frame.grid(row=0, column=0, sticky='news')

# Welcome Frame with Image
title_bg = tk.Label(welcome_frame, text="Budget", font=('Helvetica', 16), bg='#3FA9B5', fg='white', width=10, height=2)
title_bg.place(x=130, y=0)

wel_m = tk.Label(welcome_frame, text="Welcome to your Budget", font=('Helvetica', 16), fg='white', bg='#058E9D')
wel_m .place(x=80,y=70)
image_front = tk.Label(welcome_frame, image=photo, bg='#058E9D')  # Display the resized image
image_front.place(x=40,y=120)

# Buttons with specified sizes and colors
enter_button = tk.Button(welcome_frame, text="Enter", bg='#71B1CA', width=10, height=2, command=lambda: [show_frame(input_frame)])
enter_button.place(x=70, y=250)

view_button = tk.Button(welcome_frame, text="View", bg='#71B1CA', width=10, height=2, command=lambda: show_frame(summary_frame))
view_button.place(x=220, y=250)

close_button = tk.Button(welcome_frame, text="Close", bg='#71B1CA', width=10, height=2, command=root.quit)
close_button.place(x=144, y=300)

# Input Frame
wlcome_text = tk.Label(input_frame, text="Enter your Income and Expenses", font=('Helvetica', 18), bg='#058E9D')
wlcome_text.place(x=30, y=0)

income_text = tk.Label(input_frame, text="Income", bg='#058E9D')
income_text.place(x=30, y=50)
income_entry = tk.Entry(input_frame)
income_entry.place(x=100, y=50)

rent_text = tk.Label(input_frame, text="Rent", bg='#058E9D')
rent_text.place(x=30, y=80)
rent_entry = tk.Entry(input_frame)
rent_entry.place(x=100, y=80)

g_text = tk.Label(input_frame, text="Grocery", bg='#058E9D')
g_text.place(x=30, y=110)
grocery_entry = tk.Entry(input_frame)
grocery_entry.place(x=100, y=110)

enter_text = tk.Label(input_frame, text="Entertainment", bg='#058E9D')
enter_text.place(x=30, y=140)
entertainment_entry = tk.Entry(input_frame)
entertainment_entry.place(x=100, y=140)

utilities_text =  tk.Label(input_frame, text="Utilities", bg='#058E9D')
utilities_text.place(x=30, y=170)
utilities_entry = tk.Entry(input_frame)
utilities_entry.place(x=100, y=170)


# Modified Submit button with a new command
def submit_data():
    income = income_entry.get()
    config.update_monthly_income(income)
    config.budget_data.update({
        "monthly rent": rent_entry.get(),
        "monthly groceries": grocery_entry.get(),
        "monthly utilities": utilities_entry.get(),
        "monthly entertainment": entertainment_entry.get()
    })
    config.calculate_totals()  # Call the calculate totals from the main module
    update_summary()  # Update the summary frame with the new data
    show_frame(summary_frame)  # Show the summary frame

to_new_expense_frame_button = tk.Button(input_frame, text="Add New Expense",  bg='#71B1CA', width=15, height=2, command=lambda: show_frame(new_expense_frame))
to_new_expense_frame_button.place(x=145, y=200)  
s_button = tk.Button(input_frame, text="Submit",bg='#71B1CA', width=10, height=2, command=submit_data)
s_button.place(x=150, y=300)

# New Expense Frame
update1_text = tk.Label(new_expense_frame, text="Name of expenses", bg='#058E9D')
update1_text.place(x=30, y=50)
new_expense_name_entry = tk.Entry(new_expense_frame)
new_expense_name_entry.place(x=160, y=50)

update2_text = tk.Label(new_expense_frame, text="Number of expenses", bg='#058E9D')
update2_text.place(x=30, y=100)
new_expense_amount_entry = tk.Entry(new_expense_frame)
new_expense_amount_entry.place(x=160, y=100)

def add_new_expense():
    expense_name = new_expense_name_entry.get()
    expense_amount = new_expense_amount_entry.get()
    if expense_name and expense_amount.isdigit():
        config.budget_data[expense_name] = expense_amount
        config.calculate_totals()  # Recalculate totals with new expense
        show_frame(summary_frame)  # Show updated summary

add_expense_button = tk.Button(new_expense_frame, text="Add Expense", bg='#71B1CA', width=10, height=2, command=lambda: [add_new_expense(), show_frame(input_frame)])
add_expense_button.place(x=150, y=150)


def update_summary():
    budget_details = config.print_budget_details()
    # Reset existing dynamic labels (destroy old labels to prevent overlap and memory leaks)
    for label in dynamic_labels.values():
        label.destroy()
    dynamic_labels.clear()  # Clear the dictionary to start fresh

    income_var.set(f"Income: {budget_details.get('monthly income', 'N/A')}")
    rent_var.set(f"Rent: {budget_details.get('monthly rent', 'N/A')}")
    grocery_var.set(f"Grocery: {budget_details.get('monthly groceries', 'N/A')}")
    entertainment_var.set(f"Entertainment: {budget_details.get('monthly entertainment', 'N/A')}")
    utilities_var.set(f"Utilities: {budget_details.get('monthly utilities', 'N/A')}")
    expenses_var.set(f"Total Expenses: {budget_details.get('total expenses', 'N/A')}")
    savings_var.set(f"Total Savings: {budget_details.get('total savings', 'N/A')}")

   # Dynamically display all other expenses
    y_position = 200  # Start position for dynamic labels
    for key, value in budget_details.items():
        if key not in ['monthly income', 'monthly rent', 'monthly groceries', 'monthly entertainment', 'monthly utilities', 'total expenses', 'total savings']:
            # Create a StringVar and Label for each dynamic expense
            var = tk.StringVar(value=f"{key}: {value}")
            label = tk.Label(summary_frame, textvariable=var, bg='#058E9D')
            label.place(x=30, y=y_position)
            dynamic_labels[key] = label  
            y_position += 30  # Increase the position for the next label

# Initialize a dictionary to store references to dynamically created labels
dynamic_labels = {}     
        

# Tkinter StringVars for dynamic label updates
income_var = tk.StringVar()
rent_var = tk.StringVar()
grocery_var = tk.StringVar()
entertainment_var = tk.StringVar()
utilities_var = tk.StringVar()
expenses_var = tk.StringVar()
savings_var = tk.StringVar()

# Summary Frame - Update with additional labels for each budget detail
tk.Label(summary_frame, text="Your Budget Summary", font=('Helvetica', 18), bg='#058E9D').pack(pady=20)
tk.Label(summary_frame, textvariable=income_var, bg='#058E9D').place(x=30, y=50)
tk.Label(summary_frame, textvariable=rent_var, bg='#058E9D').place(x=30, y=80)
tk.Label(summary_frame, textvariable=grocery_var, bg='#058E9D').place(x=30, y=110)
tk.Label(summary_frame, textvariable=entertainment_var, bg='#058E9D').place(x=30, y=140)
tk.Label(summary_frame, textvariable=utilities_var, bg='#058E9D').place(x=30, y=170)
tk.Label(summary_frame, textvariable=expenses_var, bg='#058E9D').place(x=30, y=230)
tk.Label(summary_frame, textvariable=savings_var, bg='#058E9D').place(x=30, y=260)
tk.Button(summary_frame, text="Home",bg='#71B1CA', width=10, height=2, command=lambda: show_frame(welcome_frame)).place(x=150, y=300)



show_frame(welcome_frame)
root.mainloop()
