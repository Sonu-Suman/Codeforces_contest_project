from tkinter import ttk
from CredentailInfo import CredentialPage
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from result import Search
import sys
import os


class ContestList:

    def __init__(self, root, credential):
        self.credential = credential
        self.optimal_search = Search()
        self.root = root

        self.Contest_frame = LabelFrame(self.root)
        self.Contest_frame.place(x=0, y=0)

        self.selection_and_btn_frame = Frame(self.Contest_frame, bg='lemon chiffon')
        self.selection_and_btn_frame.pack()

        main_label = Label(self.selection_and_btn_frame, text="Select type of Contest", bg='lemon chiffon',
                           font=("Times New Roman", 36, 'bold'), fg='red')
        main_label.grid(row=0, column=0, columnspan=5, pady=(10, 10), padx=(390, 390))

        self.back_contestlist = Image.open(self.resource_path("images/back.png"))
        self.back_contestlist = ImageTk.PhotoImage(self.back_contestlist)
        self.back_button1_contestlist = Button(self.selection_and_btn_frame, image=self.back_contestlist, bg='lemon chiffon', relief='flat',
                                   command=self.back_to_login)
        self.back_button1_contestlist.image = self.back_contestlist
        self.back_button1_contestlist.grid(row=1, column=0, pady=10, padx=(10, 10), sticky=W)

        self.v = IntVar()
        values = {"International": 1,
                  "Codeforces": 2}

        i = 0
        for key, values in values.items():
            self.radio = Radiobutton(self.selection_and_btn_frame, value=values, variable=self.v, text=key,
                                     bg='lemon chiffon', fg='blue', command=self.selection)
            self.radio.configure(font=('Times New Roman', 18, 'bold'))
            if i == 0:
                self.radio.grid(row=1, column=2, padx=(100, 20))
            else:
                self.radio.grid(row=1, column=2+i)
            i += 1


        self.setting_contestlist = Image.open(self.resource_path("images/setting.png"))
        self.setting_contestlist = ImageTk.PhotoImage(self.setting_contestlist)
        self.setting_btn_contestlist = Button(self.selection_and_btn_frame, image=self.setting_contestlist, bg='lemon chiffon', relief='flat',
                                        command=self.show_credential)
        self.setting_btn_contestlist.image = self.setting_contestlist
        self.setting_btn_contestlist.grid(row=1, column=4, padx=(0, 40), pady=10, sticky=E)

        self.tree_view = Frame(self.Contest_frame, width=1300, bd=0)
        self.tree_view.pack(padx=(0, 30))

        # ============================ Here we are specify our result window style =========================
        self.style = ttk.Style()
        self.style.theme_use('default')

        self.style.configure('Treeview',
                                foreground='navajo white',
                                background='white',
                                rowheight=30,                           # fieldbackgroud='peach puff',
                                highlightthickness=0,
                                bd=0,
                                font=('Calibri', 13, 'normal'))

        self.style.configure("Treeview.Heading",
                             font=('Calibri', 15, 'bold')
                             )  # Modify the font of the headings

        self.style.layout("Treeview",
                          [('Treeview.treearea',
                            {'sticky': 'nswe'})]
                          )  # Remove the borders

        tree_scroll = ttk.Scrollbar(self.tree_view, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.tree_bar = ttk.Treeview(self.tree_view, yscrollcommand=tree_scroll.set)
        self.tree_bar['columns'] = ("A", "B", "C")

        # self.tree_bar.column("#0", width=50, minwidth=25)
        self.tree_bar.column("A", width=750, minwidth=350, anchor=CENTER)
        self.tree_bar.column("B", width=141, minwidth=100, anchor=CENTER)
        self.tree_bar.column("C", width=290, minwidth=100, anchor=CENTER)


        # self.tree_bar.heading("#0", text="Label", anchor=W)
        self.tree_bar.heading("A", text="Contest Name")
        self.tree_bar.heading("B", text="Type", anchor=CENTER)
        self.tree_bar.heading("C", text="Phase", anchor=CENTER)

        tree_scroll.config(command=self.tree_bar.yview)
        self.tree_bar['show'] = 'headings'

        self.tree_bar.configure(height=21)
        self.tree_bar.pack(fill=BOTH, expand=1)


    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def show_credential(self):
        CredentialPage(self.root, credential=self.credential)


    def selection(self):
        self.style.map('Treeview', background=[('selected', 'green')])

        # We want to differentiate each row----------------------------
        self.tree_bar.tag_configure('oddrow', background='white')
        self.tree_bar.tag_configure('evenrow', background='Pale Turquoise1')

        self.types_of_searching = self.v.get()
        self.confirm = messagebox.askyesno("Selection", f"You selected {'International' if self.types_of_searching==1 else 'Codeforces'}, Contest List for searching.")
        if self.confirm:
            for item in self.tree_bar.get_children():
                self.tree_bar.delete(item)

            type = 'true' if self.types_of_searching == 1 else 'false'
            result = self.optimal_search.contest_list(type)
            for i in range(len(result)):
                if i % 2 == 0:
                    if type == 'true':
                        self.tree_bar.insert(parent="", index='end', iid=i, text='', values=(result[i][0][1], result[i][1][1], result[i][2][1]), tags=('evenrow',))
                    else:
                        self.tree_bar.insert(parent='', index='end', iid=i, text=f'{result[i][0][1]}',
                                             values=(f'✅{result[i][1][1]}', result[i][2][1], result[i][3][1]), tags=('evenrow',))
                else:
                    if type == 'true':
                        self.tree_bar.insert(parent="", index='end', iid=i, text='', values=(result[i][0][1], result[i][1][1], result[i][2][1]), tags=('oddrow',))
                    else:
                        self.tree_bar.insert(parent='', index='end', iid=i, text=f'{result[i][0][1]}',
                                             values=(f'✅{result[i][1][1]}', result[i][2][1], result[i][3][1]), tags=('oddrow',))
                self.tree_bar.bind("<Double-1>", self.link_tree)


    def link_tree(self, event):
        if self.types_of_searching == 2:
            input_id = self.tree_bar.selection()

            check = self.tree_bar.item(input_id, 'values')[2]
            if check == "FINISHED":
                self.input_item = self.tree_bar.item(input_id, "text")

                import webbrowser
                webbrowser.open('https://codeforces.com/contest/'+self.input_item)
            elif check == "BEFORE":
                showinfo("NOT STARTED", "This contest not started currently")
        else:
            showinfo("Not Available", "For finding this contest go for it's official website.")


    def back_to_login(self):
        # import Codeforces
        # Codeforces.Graphics().tracking_window()
        self.Contest_frame.destroy()


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.maxsize(1200, 800)
#     root.minsize(1200, 800)
#     root.title("Contest List Window")
#     ContestList(root)
#     root.mainloop()