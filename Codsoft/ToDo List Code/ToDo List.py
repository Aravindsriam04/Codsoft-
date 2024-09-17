import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

tasks = []
task_status = []

def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, (task, status) in enumerate(zip(tasks, task_status)):
        status_str = "[Done]" if status else "[Not Done]"
        task_listbox.insert(tk.END, f"{status_str} {task}")

def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        tasks.append(task)
        task_status.append(False)
        update_task_list()

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        task_status.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Delete Task", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = simpledialog.askstring("Update Task", "Enter the new task description:")
        if new_task:
            tasks[selected_task_index] = new_task
            update_task_list()
    except IndexError:
        messagebox.showwarning("Update Task", "Please select a task to update.")

def toggle_task_status():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_status[selected_task_index] = not task_status[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Toggle Status", "Please select a task to mark as done or not done.")

task_listbox = tk.Listbox(root, height=15, width=50)
task_listbox.pack(pady=20)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", width=15, command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

toggle_status_button = tk.Button(root, text="Toggle Status", width=15, command=toggle_task_status)
toggle_status_button.pack(pady=5)

root.mainloop()
