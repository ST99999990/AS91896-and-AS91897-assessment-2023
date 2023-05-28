#Tanav 
#This assesment is about creating a piece of code that's for a party hire company that'll sort out items hired from the company
#from there the outcome should provide the user with the recipt number and their order details 
from tkinter import * 
import tkinter as ttk  
main_page = ttk.Tk() 
main_page.title('JULIES PARTY HIRE')
main_page.geometry("850x400")
main_page.configure(bg="LightSkyBlue2")

#Main window
main_page.columnconfigure((0,5), weight=5)#allows for even spacing 
Label(main_page, font=("impact", 20), text="JULIES PARTY HIRE", bg = "LightSkyBlue2").grid(column=1, row=0)#allows for our gui to have a title\

#Extra spacing between the title and entry box
Label(main_page, font = "impact", bg = "LightSkyBlue2").grid(column = 0, row = 1)

#Entry boxes for name entry 
def name_thing(event):
    name_entry_1.delete(0, "end")
name_entry_1 = Entry(main_page, width= 20, bg= "white" , font = "helvetica")#creates the enrty box
name_entry_1.grid(ipadx =20, ipady =3,  row = 2,column=1)#adjusts the placement and size 
name_entry_1.columnconfigure((0,15), weight = 2)#adjust the placement of the box
name_entry_1.insert(0, "Please enter your name")#insetrs the message or question into the box
name_entry_1.bind("<FocusIn>", name_thing)#Makes it so that the text is temporary 

#entry box for the items needed for hiring 
def hire_thing(event):
    item_hire.delete(0, "end")
item_hire = Entry(main_page, width = 20,bg = "white", font ="helvetica")#creates the entry box
item_hire.grid(ipadx = 20,ipady=3, row = 4,column = 1)
item_hire.columnconfigure((0,15), weight = 2)
item_hire.insert(0, "What would you like to hire?")#the text thats on the box
item_hire.bind("<FocusIn>", hire_thing) #makes the text temporary

#extra labels that will help with spacing inbetween name entry and item hire
Label(main_page, font = "imapct", bg = "LightSkyBlue2").grid(column = 1, row = 3)

#Entry box for the amount input 
def quanity_thing(event):
    amount_input.delete(0,"end")
amount_input = int()
amount_input = Entry(main_page, width = 21, bg = "white", font = "helvetica")#creates the entry box
amount_input.grid(ipadx = 20, ipady =3, row = 6, column = 1)#helps adjust the width and length of the box 
amount_input.columnconfigure((0,15), weight = 5)
amount_input.insert(0, "Item quantity")#The text in the entry box
amount_input.bind("<FocusIn>", quanity_thing)#makes the text tempopary 
if amount_input < 500 or amount_input > 1:#applying limits to the input
    print("Item hire is only from 1 - 500")



   


#Spacing for the item hire and the adress input 
Label(main_page, font= "imapct", bg = "LightSkyBlue2" ).grid(column =1, row = 5 )

#Entry box for the costumer email adress
def recipt_thing(event):
    recipt_input.delete(0,"end")
recipt_input = IntVar()
recipt_input = Entry(main_page, width = 21, bg = "white", font = "helvetica")#creates the entry box
recipt_input.grid(ipadx = 20, ipady =3, row = 8, column = 1)#helps adjust the width and length of the box 
recipt_input.columnconfigure((0,15), weight = 5)
recipt_input.insert(0, "Enter your recipt number")#The text in the entry box
recipt_input.bind("<FocusIn>", recipt_thing)#makes the text tempopary 

#Spacing between the adress and email input
Label(main_page, font= "imapct", bg = "LightSkyBlue2" ).grid(column =1, row = 7 )

#Spacing between the textbox and button
Label(main_page, font = "impact", bg = "LightSkyBlue2" ).grid(column =1, row = 9 )

#button for entrying all the entries 
def setup_buttons(): 
    global item_hire, recipt_input, amount_input, name_entry_1
Button(main_page, text = "submit").grid(column = 1, row = 10)

main_page.mainloop()
