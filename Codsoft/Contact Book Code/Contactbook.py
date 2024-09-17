import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")

contacts = {}

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {details['phone']}")

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter the contact name:")
    if name:
        phone = simpledialog.askstring("Add Contact", "Enter the phone number:")
        email = simpledialog.askstring("Add Contact", "Enter the email address:")
        address = simpledialog.askstring("Add Contact", "Enter the address:")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()

def view_contact():
    try:
        selected_contact = contact_listbox.curselection()[0]
        name = list(contacts.keys())[selected_contact]
        details = contacts[name]
        messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
    except IndexError:
        messagebox.showwarning("View Contact", "Please select a contact to view.")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter the name or phone number to search:")
    if query:
        found = False
        for name, details in contacts.items():
            if query.lower() in name.lower() or query in details['phone']:
                messagebox.showinfo("Search Result", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                found = True
                break
        if not found:
            messagebox.showinfo("Search Result", "No contact found.")

def update_contact():
    try:
        selected_contact = contact_listbox.curselection()[0]
        name = list(contacts.keys())[selected_contact]
        new_name = simpledialog.askstring("Update Contact", "Enter the new contact name:", initialvalue=name)
        new_phone = simpledialog.askstring("Update Contact", "Enter the new phone number:", initialvalue=contacts[name]['phone'])
        new_email = simpledialog.askstring("Update Contact", "Enter the new email address:", initialvalue=contacts[name]['email'])
        new_address = simpledialog.askstring("Update Contact", "Enter the new address:", initialvalue=contacts[name]['address'])
        if new_name:
            contacts.pop(name)
            contacts[new_name] = {"phone": new_phone, "email": new_email, "address": new_address}
            update_contact_list()
    except IndexError:
        messagebox.showwarning("Update Contact", "Please select a contact to update.")
        
def delete_contact():
    try:
        selected_contact = contact_listbox.curselection()[0]
        name = list(contacts.keys())[selected_contact]
        if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {name}?"):
            contacts.pop(name)
            update_contact_list()
    except IndexError:
        messagebox.showwarning("Delete Contact", "Please select a contact to delete.")

contact_listbox = tk.Listbox(root, height=15, width=50)
contact_listbox.pack(pady=20)

add_button = tk.Button(root, text="Add Contact", width=20, command=add_contact)
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Contact", width=20, command=view_contact)
view_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", width=20, command=search_contact)
search_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", width=20, command=update_contact)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", width=20, command=delete_contact)
delete_button.pack(pady=5)

root.mainloop()
