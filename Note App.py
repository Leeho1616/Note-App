import tkinter as tk
from tkinter import messagebox
import json

class Noteapp:
    def __init__(self, master):
        self.master = master
        self.master.title("Note App")
        self.logged_in = False
        self.load_user_database()

        self.master.configure(bg="#f0f0f0")

        frame_login = tk.Frame(self.master, bg="#f0f0f0")
        frame_login.pack(pady=20)

        self.login_button = tk.Button(frame_login, text="Log In", command=self.show_login, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.login_button.grid(row=0, column=0, pady=5, padx=10)

        self.register_button = tk.Button(frame_login, text="Register", command=self.show_register, bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.register_button.grid(row=0, column=1, pady=5, padx=10)

        self.note_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=15, width=60)
        self.note_listbox.pack(pady=10)
        self.note_listbox.pack_forget()

        self.add_button = tk.Button(self.master, text="Add Note", command=self.add_note, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.add_button.pack(pady=5)
        self.add_button.pack_forget()

        self.delete_button = tk.Button(self.master, text="Delete Note", command=self.delete_note, bg="#EF5350", fg="white", font=("Helvetica", 12))
        self.delete_button.pack(pady=5)
        self.delete_button.pack_forget()

        self.note_display = tk.Text(self.master, height=15, width=60)
        self.note_display.pack(pady=10)
        self.note_display.pack_forget()

    def show_login(self):
        login_window = tk.Toplevel(self.master, bg="#f0f0f0")
        login_window.title("Log In")

        tk.Label(login_window, text="ID:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0)
        self.id_entry = tk.Entry(login_window)
        self.id_entry.grid(row=0, column=1)

        tk.Label(login_window, text="Password:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0)
        self.password_entry = tk.Entry(login_window, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(login_window, text="Log In", command=self.check_login, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=2, columnspan=2)

    def show_register(self):
        register_window = tk.Toplevel(self.master, bg="#f0f0f0")
        register_window.title("Register")

        tk.Label(register_window, text="ID:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0)
        self.register_id_entry = tk.Entry(register_window)
        self.register_id_entry.grid(row=0, column=1)

        tk.Label(register_window, text="Password:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0)
        self.register_password_entry = tk.Entry(register_window, show="*")
        self.register_password_entry.grid(row=1, column=1)

        tk.Button(register_window, text="Register", command=self.register_account, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=2, columnspan=2)

    def check_login(self):
        user_id = self.id_entry.get()
        password = self.password_entry.get()

        if user_id in self.user_database and self.user_database[user_id] == password:
            messagebox.showinfo("Notification", "Log In Successful!")
            self.logged_in = True
            self.show_elements_after_login()
        else:
            messagebox.showinfo("Error", "Login Failed. Check your ID and password.")

    def register_account(self):
        user_id = self.register_id_entry.get()
        password = self.register_password_entry.get()

        if user_id and password:
            self.user_database[user_id] = password
            messagebox.showinfo("Notification", "Registration Successful!")
            self.save_user_database()
        else:
            messagebox.showinfo("Error", "ID and password cannot be empty.")

    def show_elements_after_login(self):
        self.login_button.pack_forget()
        self.register_button.pack_forget()
        self.note_listbox.pack()
        self.add_button.pack()
        self.delete_button.pack()
        self.note_display.pack()

    def add_note(self):
        note_content = self.note_display.get("1.0", tk.END).strip()

        if note_content:
            self.note_listbox.insert(tk.END, note_content)
            self.clear_note_display()

    def delete_note(self):
        selected_index = self.note_listbox.curselection()

        if selected_index:
            self.note_listbox.delete(selected_index)

    def save_user_database(self):
        with open("user_database.json", "w") as file:
            json.dump(self.user_database, file)

    def load_user_database(self):
        try:
            with open("user_database.json", "r") as file:
                self.user_database = json.load(file)
        except FileNotFoundError:
            self.user_database = {}

    def clear_note_display(self):
        self.note_display.delete("1.0", tk.END)

root = tk.Tk()
app = Noteapp(root)
root.mainloop()
