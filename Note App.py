import tkinter as tk
from tkinter import messagebox
import json

class Noteapp:
    #khởi tạo
    def __init__(self, master ):
        self.master = master    #Noteapp クラスを佐生精する
        self.master.title("Note App")   #đặt title cho app
        self.logged_in = False      #đặt trangj thái ko có người dùng nào đang đăng nhập
        self.load_user_database() #tải user database từ file
    
        #Tạo nút login và register
        self.login_button = tk.Button(self.master, text = "Log In", command= self.show_login)
        self.login_button.pack(pady = 5) 

        self.register_button = tk.Button(self.master, text = "Register", command= self.show_register)
        self.register_button.pack(pady = 5)

        #Tạo hộp danh sách để hiển thị ghi trú
        self.note_listbox = tk.Listbox(self.master, selectmode = tk.SINGLE, height= 15, width= 60)
        self.note_listbox.pack(pady = 10)
        self.note_listbox.pack_forget()

        #Tạo nút Add new notes
        self.add_button = tk.Button(self.master, text = "Add Note", command= self.add_note)
        self.add_button.pack(pady = 5)
        self.add_button.pack_forget()

        #Tạo nút xóa note
        self.delete_button = tk.Button(self.master, text = "Delete Note", command= self.delete_note)
        self.delete_button.pack(pady = 5)
        self.delete_button.pack_forget()

        #tạo ô để nhập note
        self.note_display = tk.Text(self.master, height=15, width=60)
        self.note_display.pack(pady = 10)
        self.note_display.pack_forget()

    def show_login(self):
        #Tạo ô login
        login_window = tk.Toplevel(self.master)
        login_window.title("Log In")

        #Tạo widgets nhập id và pass
        tk.Label(login_window, text = "ID:").grid(row = 1, column= 0)
        self.id_entry = tk.Entry(login_window)
        self.id_entry.grid(row = 0, column= 1)

        tk.Label(login_window, text="Password:").grid(row = 1, column= 0)
        self.password_entry = tk.Entry(login_window)
        self.password_entry.grid(row = 1, column= 1)

        #Tạo nút kiểm tra đăng nhập
        tk.Button(login_window, text= "Log In", command= self.check_login).grid(row= 2, columnspan= 2)
    
    def show_register(self):
        # Tạo ô đăng kí
        register_window = tk.Toplevel(self.master)
        register_window.title("Register")

        # Ưidgets id pass
        tk.Label(register_window, text="ID:").grid(row=0, column=0)
        self.register_id_entry = tk.Entry(register_window)
        self.register_id_entry.grid(row=0, column=1)

        tk.Label(register_window, text="Password:").grid(row=1, column=0)
        self.register_password_entry = tk.Entry(register_window, show="*")
        self.register_password_entry.grid(row=1, column=1)

        # tạo nick mới
        tk.Button(register_window, text="Register", command=self.register_account).grid(row=2, columnspan=2)
    
    def check_login(self):
        #kiểm tra user data
        user_id = self.id_entry.get()
        password = self.password_entry.get()

        if user_id in self.user_database and self.user_database[user_id] == password:
            messagebox.showinfo("Notification", "Log In Successful!")
            self.logged_in = True
            self.show_elements_after_login()
        else:
            messagebox.showinfo("Error", "Login Failed. Check your ID and password.")

    def register_account(self):
        #Tạo nick mới
        user_id = self.register_id_entry.get()
        password = self.register_password_entry.get()

        if user_id and password:
            self.user_database[user_id] = password
            messagebox.showinfo("Notification", "Registration Successful!")
            self.save_user_database()
        else:
            messagebox.showinfo("Error", "ID and password cannot be empty.")
    
    def show_elements_after_login(self):
        #hiển thị sau đăng nhập
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
        # Delete the selected note from the listbox
        selected_index = self.note_listbox.curselection()

        if selected_index:
            self.note_listbox.delete(selected_index)
    
    def save_user_database(self):
        #lưu user vào file json
        with open("user_database.json", "W") as file:
            json.dump(self.user_database, file)
    
    def load_user_database(self):
        #tải data từ file json
        try:
            with open("user_database.json", "r") as file:
                self.user_database = json.load(file)
        except FileNotFoundError:
            self.user_database = {}
    
    def clear_note_display(self):
        self.note_display.delete("1.0", tk.END)

#Tạo cửa sổ tkinter
root = tk.Tk()
app = Noteapp(root)
root.mainloop()









