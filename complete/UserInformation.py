import string
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from result import Search
from PIL import Image, ImageTk
from CredentailInfo import CredentialPage
import os
import sys

class UserInfo:
    def __init__(self, root, credential):
        self.credential = credential
        self.optimal_search = Search()
        self.root = root

        self.Main_User_frame = LabelFrame(self.root, bg='lemon chiffon')
        self.Main_User_frame.place(x=0, y=0)

        self.back = Image.open(self.resource_path("images/back.png"))
        self.search = Image.open(self.resource_path("images/loupe.png"))
        self.setting = Image.open(self.resource_path("images/setting.png"))

        self.back = ImageTk.PhotoImage(self.back)
        self.search = ImageTk.PhotoImage(self.search)
        self.setting = ImageTk.PhotoImage(self.setting)

        self.back_button1 = Button(self.Main_User_frame, image=self.back, bg='lemon chiffon', relief='flat',
                                   command=self.back_to_login_from_user_info)
        self.search_button2 = Button(self.Main_User_frame, image=self.search, bg='lemon chiffon', relief='flat',
                                     command=self.search_user)
        self.setting_button3 = Button(self.Main_User_frame, image=self.setting, bg='lemon chiffon', relief='flat',
                                      command=self.show_credential)

        self.back_button1.image = self.back
        self.search_button2.image = self.search
        self.setting_button3.image = self.setting

        # self.back_button1.pack(side=LEFT, padx=20, pady=30)
        # self.search_button2.pack()
        # self.setting_button3.pack()

        self.back_button1.grid(row=1, column=0, pady=(5, 15), padx=(4, 10), sticky=W)
        self.search_button2.grid(row=1, column=3, pady=(5, 15), padx=(2, 150), sticky=W)
        self.setting_button3.grid(row=1, column=4, pady=(5, 15), padx=(130, 10), sticky=E)

        self.search_entry = StringVar()
        self.search_entry = Entry(self.Main_User_frame, font=('Times New Roman', 16, 'normal'), textvariable=self.search_entry,
                                  width=50, bg='lemon chiffon3', fg='blue')
        self.search_entry.grid(row=1, column=2, pady=(5, 15), sticky=W, padx=(210, 5))


        title2 = Label(self.Main_User_frame, text='Enter user handle name: 🚴‍👇',
                       bg='lemon chiffon', width=50, font=('Times New Roman', 14, 'normal'), fg='blue')
        title2.grid(row=0, column=0, columnspan=6, pady=(10, 2))

        search_title = Label(self.Main_User_frame, text="Search Result -->", bd=5, bg='lemon chiffon', width=30,
                             font=('Times New Roman', 16, 'bold'))
        search_title.grid(row=2, column=0, columnspan=6)

        self.show_result_frame = Frame(self.Main_User_frame)
        self.show_result_frame.grid(row=2, column=0, columnspan=6)

        # This is for style--------------------------------------
        self.style = ttk.Style()
        self.style.theme_use('default')


        self.style.configure('Treeview',
                                foreground='navajo white',
                                background='white',
                                rowheight=30,
                                fieldbackgroud='lemon chiffon',           # highlightthickness=0,
                                bd=0,
                                font=('Calibri', 13, 'normal'))

        self.style.configure("Treeview.Heading",
                             font=('Calibri', 15, 'bold')
                             )  # Modify the font of the headings

        self.style.layout("Treeview",
                          [('Treeview.treearea',
                            {'sticky': 'nswe'})]
                          )  # Remove the borders

        self.style.map('Treeview', background=[('selected', 'blue')])
        self.style.theme_use('default')


        scroll_y = Scrollbar(self.show_result_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.tree_view = ttk.Treeview(self.show_result_frame, yscrollcommand=scroll_y.set, style='Treeview')
        self.tree_view['columns'] = ('A', 'B', 'C', 'D')

        # defining columns
        self.tree_view.column("#0", width=50, minwidth=20)
        self.tree_view.column("A", width=255, minwidth=200, anchor=CENTER)
        self.tree_view.column("B", width=200, minwidth=150, anchor=CENTER)
        self.tree_view.column("C", width=562, minwidth=450, anchor=CENTER)
        self.tree_view.column("D", width=165, minwidth=120, anchor=CENTER)

        # define our headings
        self.tree_view.heading("#0", text='', anchor=W)
        self.tree_view.heading("A", text='User Name: ', anchor=CENTER)
        self.tree_view.heading("B", text="Other Details: ", anchor=CENTER)
        self.tree_view.heading("C", text='Contest Name: ', anchor=CENTER)
        self.tree_view.heading("D", text="New Rating: ", anchor=CENTER)

        self.tree_view['show'] = 'headings'
        scroll_y.config(command=self.tree_view.yview)

        self.tree_view.configure(height=23)
        self.tree_view.pack(fill=BOTH, expand=1)


    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def show_credential(self):
        CredentialPage(self.root, credential=self.credential)


    def back_to_login_from_user_info(self):
        self.Main_User_frame.destroy()


    def search_user(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

        # We want to differentiate each row----------------------------
        self.tree_view.tag_configure('oddrow', background='white')
        self.tree_view.tag_configure('evenrow', background='Pale Turquoise1')


        search_entry = self.search_entry.get()
        if search_entry != '':
            try:
                # user_info, user_rating = self.optimal_search.user_info(search_entry), self.optimal_search.user_rating(search_entry)
                selection = tk.Label(text="PLEASE WAIT.....\nFetching data........", bg='black', fg='white', width=20)
                selection.config(font=('cursive', 12, 'bold'))
                selection.place(x=500, y=400)
                user_info, user_rating = self.optimal_search.user_info(search_entry), self.optimal_search.user_rating(search_entry)
                selection.after(1000, selection.destroy)

                if user_info[0] == 'handles':
                    messagebox.showinfo("User not Found", f'{user_info[1]}')

                user_info_length = len(user_info)
                user_rating_length = len(user_rating)
                user_rating_first_length = len(user_rating[0])
                self.tree_view.insert(parent='', index='end', iid=0, text=f'{user_info[3][1]}',
                                      values=(f"{user_info[4][1]}: {user_info[0][1]}", f"{user_info[7][0]}: {user_info[7][1]}", "", ""),
                                      tags=('evenrow',))
                self.tree_view.bind("<Double-1>", self.callback)
                self.tree_view.bind('<<TreeviewOpen>>', self.show_child)
                count = 1
                for i in range(user_info_length):
                    if i in [0, 4, 7]:
                        continue

                    if count % 2 == 0:
                        self.tree_view.insert(parent='0', index='end', iid=count, text='',
                                      values=("", f"{user_info[i][0]}: {user_info[i][1]}", "", ""), tags=("evenrow",))

                    else:
                        self.tree_view.insert(parent='0', index='end', iid=count, text='',
                                      values=("", f"{user_info[i][0]}: {user_info[i][1]}", "", ""), tags=("oddrow",))
                    count += 1

                # print(user_rating_length)
                # print(user_rating)
                # print(user_rating_first_length)
                # print(user_rating[0])
                for j in range(user_rating_length):
                    s = 8+(3*j)
                    counter = 1
                    if s % 2 == 0:
                        self.tree_view.insert(parent='', index='end', iid=s, text=f'{user_rating[j][0][1]}',
                                              values=("", "", f"{user_rating[j][1][1]}", f"{user_rating[j][4][0]}: {user_rating[j][4][1]}"), tags=('evenrow',))
                    else:
                        self.tree_view.insert(parent='', index='end', iid=s, text=f'{user_rating[j][0][1]}',
                                              values=("", "", f"{user_rating[j][1][1]}", f"{user_rating[j][4][0]}: {user_rating[j][4][1]}"), tags=('oddrow',))
                    self.tree_view.bind("<Double-1>", self.callback)
                    self.tree_view.bind('<<TreeviewSelect>>', self.show_child)
                    for k in range(user_rating_first_length):
                        if k in [0, 1, 4]:
                            continue

                        if counter % 2 == 0:
                            self.tree_view.insert(parent=f'{s}', index='end', iid=s+counter, text='',
                                      values=("", "", "", f"{user_rating[j][k][0]}: {user_rating[j][k][1]}"), tags=("evenrow",))

                        else:
                            self.tree_view.insert(parent=f'{s}', index='end', iid=s+counter, text='',
                                      values=("", "", "", f"{user_rating[j][k][0]}: {user_rating[j][k][1]}"), tags=("oddrow",))
                        counter += 1
            except Exception as e:
                print(e)
                messagebox.showerror("Something Wrong", "Something Went wrong\nWe kindly suggest you Please check your own network connection")
        else:
            messagebox.showwarning("Empty Search field", "Don't search with empty search field!")


    def callback(self, event):
        input_id = self.tree_view.selection()
        self.input_item = self.tree_view.item(input_id, "text")

        if self.input_item == '':
            messagebox.showinfo("INFORMATION ROW", "Here is only display information")
        else:
            import webbrowser
            try:
                if int(self.input_item):
                    webbrowser.open('https://codeforces.com/contests/'+self.input_item)
            except Exception as e:
                try:
                    webbrowser.open('https://codeforces.com/profile/'+str(self.input_item))
                except Exception as e:
                    messagebox.showinfo("Bad Connection", "Something went wrong!")
                    print("1-- ", e)
                print("2-- ", e)


    def show_child(self, event):
        self.open_children(self.tree_view.focus())


    def open_children(self, parent):
        self.tree_view.item(parent, open=True)  # open parent
        for child in self.tree_view.get_children(parent):
            self.open_children(child)


# if __name__ == "__main__":
#     root = tk.Tk()
#     UserInfo(root)
#     root.mainloop()