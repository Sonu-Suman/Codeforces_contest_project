import string
from tkinter import *
from hello import RoundedButton
from tkinter import Scrollbar, scrolledtext
from tkinter import messagebox
from CredentailInfo import CredentialPage
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.messagebox import showinfo
from result import Search
import matplotlib.pyplot as plt
import numpy as np


class Window:
    def __init__(self, root, credential):
        self.credential = credential
        self.optimal_search = Search()
        self.data_structure = False
        self.Q_to_contest = False
        self.all_Question_from_contest = False
        self.root = root
        self.new_window = LabelFrame(self.root, bg='lemon chiffon')
        self.new_window.place(x=0, y=0)

        self.back = Image.open("images/back.png")
        self.search = Image.open("images/loupe.png")
        self.setting = Image.open("images/setting.png")

        self.back = ImageTk.PhotoImage(self.back)
        self.search = ImageTk.PhotoImage(self.search)
        self.setting = ImageTk.PhotoImage(self.setting)

        self.back_button1 = Button(self.new_window, image=self.back, bg='lemon chiffon', relief='flat',
                                            command=self.back_to_login)
        self.search_button2 = Button(self.new_window, image=self.search, bg='lemon chiffon', relief='flat',
                                                    command=self.search_to_page)
        self.setting_button3 = Button(self.new_window, image=self.setting, bg='lemon chiffon', relief='flat',
                                                    command=self.show_credential)

        self.back_button1.image = self.back
        self.search_button2.image = self.search
        self.setting_button3.image = self.setting

        self.back_button1.grid(row=1, column=0, pady=(5, 15), padx=(5, 10), sticky=W)
        self.search_button2.grid(row=1, column=3, pady=(5, 15), padx=(2, 150), sticky=W)
        self.setting_button3.grid(row=1, column=4, pady=(5, 15), padx=(140, 10), sticky=E)

        self.search_entry = StringVar()
        self.search_entry = Entry(self.new_window, font=('Times New Roman', 16, 'normal'), textvariable=self.search_entry,
                                  width=50, bg='lemon chiffon3', fg='blue')
        self.search_entry.grid(row=1, column=2, pady=(10, 10), sticky=W, padx=(210, 5))


        title2 = Label(self.new_window, text='Enter your Contest Id (Only INTEGER): ',
                       bg='lemon chiffon', width=50, font=('Times New Roman', 14, 'normal'), fg='blue')
        title2.grid(row=0, column=0, columnspan=6, pady=(10, 2))

        favorite_programming_language = RoundedButton(self.new_window, text='fav. programming \nlanguage', color='Sea Green1',
                                                      fg='blue', border_radius=5, font_size=14, padx=0, pady=35, command=self.display_graph)
        favorite_programming_language.grid(row=0, column=4, columnspan=5, pady=(5, 2))

        search_title = Label(self.new_window, text="Search Result -->", bd=5, bg='lemon chiffon', width=30,
                             font=('Times New Roman', 16, 'bold'))
        search_title.grid(row=2, column=0, columnspan=6)

        self.show_result_frame = Frame(self.new_window)
        self.show_result_frame.grid(row=2, column=0, columnspan=6)

        # This is for style--------------------------------------
        self.style = ttk.Style()
        self.style.theme_use('default')

        # =================================== Here we specifying our style for tree ==================================
        self.style.configure('Treeview',
                                foreground='navajo white',
                                background='white',
                                rowheight=30,
                                fieldbackgroud='peach puff',
                                highlightthickness=0,
                                bd=0,
                                font=('Calibri', 13, 'normal'))

        self.style.configure("Treeview.Heading",
                             font=('Calibri', 15, 'bold')
                             )  # Modify the font of the headings


        self.tree_view = ttk.Treeview(self.show_result_frame)
        self.tree_view['columns'] = ('A', 'B', 'C', 'D')

        scroll_y = Scrollbar(self.show_result_frame)
        scroll_y.pack(side=RIGHT, fill=Y)

        # defining columns
        self.tree_view.column("#0", anchor=W, width=40, minwidth=20)
        self.tree_view.column("A", width=125, minwidth=60, anchor=CENTER)
        self.tree_view.column("B", width=600, minwidth=600, anchor=CENTER)
        self.tree_view.column("C", width=100, minwidth=100, anchor=CENTER)
        self.tree_view.column("D", width=357, minwidth=120, anchor=CENTER)

        # define our headings
        self.tree_view.heading("#0", text='', anchor=W)
        self.tree_view.heading("A", text='Contest Id: ', anchor=CENTER)
        self.tree_view.heading("B", text="ALl Questions: ", anchor=CENTER)
        self.tree_view.heading("C", text='Rating', anchor=CENTER)
        self.tree_view.heading("D", text="Tags: ", anchor=CENTER)

        self.tree_view['show'] = 'headings'

        scroll_y.configure(command=self.tree_view.yview)

        self.tree_view.configure(height=22)
        self.tree_view.pack(fill=BOTH, expand=1)

    def show_credential(self):
        CredentialPage(self.root, credential=self.credential)


    def back_to_login(self):
        self.new_window.destroy()


    def search_to_page(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

        self.style.map('Treeview', background=[('selected', 'green')])
        self.style.theme_use('default')

        # We want to differentiate each row----------------------------
        self.tree_view.tag_configure('oddrow', background='white')
        self.tree_view.tag_configure('evenrow', background='Pale Turquoise1')

        search_entry = self.search_entry.get()
        # print(str(self.search_entry))
        if search_entry != '':
            if int(search_entry):
                try:
                    result = self.optimal_search.contest_standing(search_entry)
                    self.tree_view.insert(parent="", index='end', iid=0, text=f'{result[0][0][1]}', values=(f"Contest Id {result[0][0][1]}", '', '', ''))
                    self.tree_view.bind("<Double-1>", self.link_tree)
                    self.tree_view.bind('<<TreeviewSelect>>', self.show_child)
                    for i in range(1, len(result)):
                        if i % 2 == 0:
                            self.tree_view.insert(parent='0', index='end', iid=i+1, text=f"{result[i][1][1]}",
                                                  values=("", f"{result[i][2][1]}", f"{result[i][3][1]}", f"{', '.join(result[0][4][1])}"), tags=('evenrow',))
                        else:
                            self.tree_view.insert(parent='0', index='end', iid=i+1, text=f"{result[i][1][1]}",
                                                  values=("", f"{result[i][2][1]}", f"{result[i][3][1]}", f"{'  '.join(result[0][4][1])}"), tags=('oddrow',))
                        self.tree_view.bind("<Double-1>", self.link_tree)

                    self.visual = self.optimal_search.contest_status(search_entry, 1000)
                except Exception as e:
                    messagebox.showwarning("Bad Connection", 'Your connection is too slow.')
                    print(e)
            else:
                messagebox.showwarning("Invalid Contest Id", "Please Type contest id integer.")
        else:
            messagebox.showwarning("Empty Search bar", "You must first enter your contest id. \nthen after click on search button")


    def link_tree(self, event):
        input_id = self.tree_view.selection()
        self.input_item = self.tree_view.item(input_id, "text")
        id = self.search_entry.get()

        import webbrowser
        try:
            if int(self.input_item):
                webbrowser.open('https://codeforces.com/contest/'+self.input_item)
        except Exception as e:
            try:
                 webbrowser.open('https://codeforces.com/contest/'+str(id)+'/problem/'+str(self.input_item))
            except Exception as e:
                print(e)
                showinfo("Bad Connection", "Something went wrong!")


    def display_graph(self):
        try:
            asking = messagebox.askquestion("Types", 'Graphical type -> yes\nText type -> no')
            if asking == 'yes':
                try:
                    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

                    data = list(self.visual.values())
                    ingredients = list(self.visual.keys())

                    def func(pct, allvals):
                        absolute = int(np.round(pct/100.*np.sum(allvals)))
                        return "{:.1f}%".format(pct, absolute)


                    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                                      textprops=dict(color="w"))

                    ax.legend(wedges, ingredients,
                              title="Ingredients",
                              loc="center left",
                              bbox_to_anchor=(1, 0, 0.5, 1))

                    plt.setp(autotexts, size=8, weight="bold")
                    ax.set_title(f"Favorite language of programmer in {str(self.search_entry.get())} contest.")

                    plt.show()
                except Exception as e:
                    print(e)
                    messagebox.showinfo("SOMETHING WRONG", "Something went wrong.")
            else:
                # ============================= Currently I am working on this===================================
                showinfo("Under process",  "Currently I am working on this so please wait some days")
        except Exception as e:
            print(e)
            messagebox.showinfo("SORRY", "Something went wrong.")


    def show_child(self, event):
        self.open_children(self.tree_view.focus())

    def open_children(self, parent):
        self.tree_view.item(parent, open=True)  # open parent
        for child in self.tree_view.get_children(parent):
            self.open_children(child)
