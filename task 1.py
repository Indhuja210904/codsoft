import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task_list():
    task_list.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        task_list.insert(tk.END, f"{index}. {task['task']} - {status}")

def mark_completed():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        tasks[selected_task_index]["completed"] = True
        update_task_list()

app = tk.Tk()
app.title("To do List App")
app.configure(bg='#f9b4a5') 

frame_input = tk.Frame(app, bg='#ECECEC')  
frame_input.pack(pady=20)

label_task = tk.Label(frame_input, text="Enter Task:", bg='#ead0d0')  
label_task.grid(row=0, column=0, pady=5)

entry_task = tk.Entry(frame_input, width=40)
entry_task.grid(row=0, column=1, pady=5)

button_add = tk.Button(frame_input, text="Add Task", command=add_task, bg='#b28d6e', fg='white')  
button_add.grid(row=1, column=0, columnspan=2, pady=10)

task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40, bg='#F5F5F5')  
task_list.pack(pady=10)

button_mark_completed = tk.Button(app, text="Mark Completed", command=mark_completed, bg='#b28d6e', fg='white')  
button_mark_completed.pack(pady=5)

app.mainloop()
