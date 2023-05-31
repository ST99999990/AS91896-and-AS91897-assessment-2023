#Tanav 
#This assesment is about creating a piece of code that's for a party hire company that'll sort out items hired from the company
#from there the outcome should provide the user with the recipt number and their order details 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random 
import re

def quit_app(): #defining the function that'll allow us to add a quit button 
    main_page.destroy()

def name_input(event): #function for name input
    name_entry_1.delete(0, "end")

def hire_item(event):#function for item hires
    item_hire.delete(0, "end")

def quantity_input(event):#function for the quantity amount 
    amount_input.delete(0, "end")

def recipt_thing(event):#function for the recipt input 
    recipt_input.delete(0, "end")

def append_details(): #function for appending the details z
    name = name_entry_1.get()
    item = item_hire.get()
    quantity = amount_input.get()
    receipt_number = recipt_input.get()

    if name != "" and item != "" and quantity != "" and receipt_number != "":#if the outputs where empty or like this
        hire_details.append([name, item, quantity, receipt_number])
        tree_view.insert("", "end", values=(name, item, quantity, receipt_number))
        name_entry_1.delete(0, 'end') 
        item_hire.delete(0, 'end')
        amount_input.delete(0, 'end')
        recipt_input.delete(0, 'end')
    else:
        messagebox.showerror("Error", "Please fill in all the fields.")#command/its text if the user does not input required information 

def submit(): #command for the sumbit button 
    name = name_entry_1.get()
    item = item_hire.get()
    quantity = amount_input.get()
    receipt_number = recipt_input.get()

    if name != "" and item != "" and quantity != "" and receipt_number != "":
        hire_details.append([name, item, quantity, receipt_number])
        tree_view.insert("", "end", values=(name, item, quantity, receipt_number))
        messagebox.showinfo("Success", "Details submitted successfully.")#this is a messgae to show that the purchase has be submitited
    else:
        messagebox.showerror("Error", "Please fill in all the fields.")

main_page = Tk()
main_page.title('JULIES PARTY HIRE')#tite of the site
main_page.geometry("850x400")#geometry ( size and shape ) of the site
main_page.configure(bg="LightSkyBlue2")#background colour 

Label(main_page, font=("impact", 20), text="JULIES PARTY HIRE", bg="LightSkyBlue2").grid(column=1, row=0)#
#spacing between the the title and name input 
Label(main_page, font="impact", bg="LightSkyBlue2").grid(column=0, row=1)
#button for name entry 
name_entry_1 = Entry(main_page, width=20, bg="white", font="helvetica")
name_entry_1.grid(ipadx=20, ipady=3, row=2, column=1)#the specs for the button 
name_entry_1.insert(0, "Please enter your name")
name_entry_1.bind("<FocusIn>", name_input)

#button for the item hire
item_hire = Entry(main_page, width=20, bg="white", font="sans")
item_hire.grid(ipadx=20, ipady=3, row=4, column=1)#specs for the button 
item_hire.insert(0, "What would you like to hire?")
item_hire.bind("<FocusIn>", hire_item)
#spacing between 
Label(main_page, font="imapct", bg="LightSkyBlue2").grid(column=1, row=3)
#amount 
amount_input = Entry(main_page, width=21, bg="white", font="helvetica")
amount_input.grid(ipadx=20, ipady=3, row=6, column=1)
amount_input.insert(0, "Item quantity")
amount_input.bind("<FocusIn>", quantity_input)
#this is to make sure only 1-500 items are hired 
def submit():
    name = name_entry_1.get()
    item = item_hire.get()
    quantity = amount_input.get()
    receipt_number = recipt_input.get()

    if name != "" and item != "" and quantity != "" and receipt_number != "":
        try:
            quantity = int(quantity)
            if 1 <= quantity <= 500:
                hire_details.append([name, item, quantity, receipt_number])
                tree_view.insert("", "end", values=(name, item, quantity, receipt_number))
                #These message boxes print out various outputs based on the users input 
                messagebox.showinfo("Success", "Details submitted successfully.")
            else:
                messagebox.showerror("Error", "Quantity must be between 1 and 500.")
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a valid number.")
    else:
        messagebox.showerror("Error", "Please fill in all the fields.")


  #if quanity is not blank then try converting it to an int

Label(main_page, font="imapct", bg="LightSkyBlue2").grid(column=1, row=5)

recipt_input = Entry(main_page, width=21, bg="white", font="helvetica")
recipt_input.grid(ipadx=20, ipady=3, row=8, column=1)
recipt_input.insert(0, "Enter your receipt number")
recipt_input.bind("<FocusIn>", recipt_thing)

Label(main_page, font="imapct", bg="LightSkyBlue2").grid(column=1, row=7)

Label(main_page, font="impact", bg="LightSkyBlue2").grid(column=1, row=9)

hire_details = []#the treeveiw, this will help us show the entries 
tree_view = ttk.Treeview(main_page, columns=("Name", "Item", "Quantity", "Receipt Number"), show="headings")
tree_view.grid(row=10, column=0, columnspan=4)

#heading names for the rows 
tree_view.heading("Name", text="Name")
tree_view.heading("Item", text="Item")
tree_view.heading("Quantity", text="Quantity")
tree_view.heading("Receipt Number", text="Receipt Number")
#sumbit button 
submit_button = Button(main_page, text="Submit", command=submit and append_details, font="helvetica", bg="SkyBlue2", fg="white")
submit_button.grid(column=0, row=8, ipadx=1, ipady=5)
#append details button 
append_button = Button(main_page, text="Append Details", command=append_details, font="helvetica", bg="SkyBlue2", fg="white")
append_button.grid(column=0, row=6, ipadx=1, ipady=5)
#quit button
quit_button = Button(main_page, text="QUIT", command=quit_app, font="sans", bg="SkyBlue2", fg="white")
quit_button.grid(column=0, row=1, ipadx=1, ipady=5)

#this is to delete the rows from the entries 
def delete_row():
    selected_item = tree_view.selection()
    if selected_item:
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this row?")#text to double check with user 
        if confirmed:
            tree_view.delete(selected_item)
            # Remove the corresponding entry from hire_details list
            for i, details in enumerate(hire_details):
                if details[0] == selected_item[0]:
                    hire_details.pop(i)
                    break
        else:
            messagebox.showinfo("Deletion Cancelled", "Row deletion has been cancelled.")
    else:
        messagebox.showerror("Error", "No row selected for deletion.")
#button for the row deleting
delete_button = Button(main_page, text="Delete Row", command=delete_row, font="helvetica", bg="SkyBlue2", fg="white")
delete_button.grid(column=2, row=8, ipadx=1, ipady=5)



main_page.mainloop()
