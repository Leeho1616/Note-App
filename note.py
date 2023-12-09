import tkinter as tk
from tkinter import messagebox
import json

class NoteApp:
    def __init__(self, master):
        # Initialize the NoteApp class
        self.master = master
        self.master.title("Note App")
        self.logged_in = False
        self.load_user_database()  # Load user database from file

        # Create login and register buttons
        self.login_button = tk.Button(self.master, text="Log In", command=self.show_login)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self.master, text="Register", command=self.show_register)
        self.register_button.pack(pady=5)

        # Create a listbox for displaying notes
        self.note_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=10, width=40)
        self.note_listbox.pack(pady=10)
        self.note_listbox.pack_forget()

        # Create a button to add new notes
        self.add_button = tk.Button(self.master, text="Add New", command=self.add_note)
        self.add_button.pack(pady=5)
        self.add_button.pack_forget()

        # Create a button to delete selected notes
        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_note)
        self.delete_button.pack(pady=5)
        self.delete_button.pack_forget()

        # Create a text widget for displaying and entering notes
        self.note_display = tk.Text(self.master, height=10, width=40)
        self.note_display.pack(pady=10)
        self.note_display.pack_forget()

    def show_login(self):
        # Create a login window
        login_window = tk.Toplevel(self.master)
        login_window.title("Log In")

        # Create entry widgets for user ID and password
        tk.Label(login_window, text="ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(login_window)
        self.id_entry.grid(row=0, column=1)

        tk.Label(login_window, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(login_window, show="*")
        self.password_entry.grid(row=1, column=1)

        # Create a button to initiate login check
        tk.Button(login_window, text="Log In", command=self.check_login).grid(row=2, columnspan=2)

    def show_register(self):
        # Create a registration window
        register_window = tk.Toplevel(self.master)
        register_window.title("Register")

        # Create entry widgets for user ID and password
        tk.Label(register_window, text="ID:").grid(row=0, column=0)
        self.register_id_entry = tk.Entry(register_window)
        self.register_id_entry.grid(row=0, column=1)

        tk.Label(register_window, text="Password:").grid(row=1, column=0)
        self.register_password_entry = tk.Entry(register_window, show="*")
        self.register_password_entry.grid(row=1, column=1)

        # Create a button to initiate registration
        tk.Button(register_window, text="Register", command=self.register_account).grid(row=2, columnspan=2)

    def check_login(self):
        # Check user login credentials
        user_id = self.id_entry.get()
        password = self.password_entry.get()

        if user_id in self.user_database and self.user_database[user_id] == password:
            messagebox.showinfo("Notification", "Log In Successful!")
            self.logged_in = True
            self.show_elements_after_login()
        else:
            messagebox.showerror("Error", "Login failed. Check ID and password.")

    def register_account(self):
        # Register a new user account
        user_id = self.register_id_entry.get()
        password = self.register_password_entry.get()

        if user_id and password:
            self.user_database[user_id] = password
            messagebox.showinfo("Notification", "Registration Successful!")
            self.save_user_database()  # Save updated user database to file
        else:
            messagebox.showerror("Error", "ID and password cannot be empty.")

    def show_elements_after_login(self):
        # Hide login and register buttons, show note-related elements
        self.login_button.pack_forget()
        self.register_button.pack_forget()
        self.note_listbox.pack()
        self.add_button.pack()
        self.delete_button.pack()
        self.note_display.pack()

    def add_note(self):
        # Add a new note to the listbox
        note_content = self.note_display.get("1.0", tk.END).strip()

        if note_content:
            self.note_listbox.insert(tk.END, note_content)
            self.clear_note_display()

    def delete_note(self):
        # Delete the selected note from the listbox
        selected_index = self.note_listbox.curselection()

        if selected_index:
            self.note_listbox.delete(selected_index)

    def save_user_database(self):
        # Save user database to a JSON file
        with open("user_database.json", "w") as file:
            json.dump(self.user_database, file)

    def load_user_database(self):
        # Load user database from a JSON file, create an empty one if not found
        try:
            with open("user_database.json", "r") as file:
                self.user_database = json.load(file)
        except FileNotFoundError:
            self.user_database = {}

    def clear_note_display(self):
        # Clear the note display text widget
        self.note_display.delete("1.0", tk.END)

# Create the main Tkinter window
root = tk.Tk()
app = NoteApp(root)  # Initialize the NoteApp
root.mainloop()  # Start the Tkinter event loop