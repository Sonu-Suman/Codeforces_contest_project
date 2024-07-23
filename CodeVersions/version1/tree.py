from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from result import Search


class Tree:
    def __init__(self, root):
        self.algorithm = False
        self.data_structure = False
        self.codeforces_contest = False
        self.optimal_search = Search()
        # self.root = Tk()
        self.new_window = Frame(root)
        self.new_window.pack()
        # self.new_window.title("problem result search Window")
        # self.new_window.maxsize(1200, 800)
        # self.new_window.minsize(1200, 800)


        self.btn_entry_frame = Frame(self.new_window, bg='lemon chiffon')
        self.btn_entry_frame.pack()

        # This is back to login image button ------------------------------------------------------------

        self.back = Image.open(r"images/back.png")
        self.back = ImageTk.PhotoImage(Image.open(
            "/codeforceProject/CodeVersions/version3/codeproject/images/back.png"))
        self.back_button1 = Button(self.btn_entry_frame, image=self.back, bg='lemon chiffon', relief='flat',
                                   command=self.back_to_login)
        self.back_button1.image = self.back
        self.back_button1.grid(row=0, column=0, pady=10, padx=(5, 140))

        # self.back_Btn = Button(self.btn_entry_frame, text="back", relief='flat',bg='lemon chiffon')
        # self.back_Btn.grid(row=0, column=0, pady=10, padx=(5, 140))

        # This is for main section -----------------------------------------------------------------------------------------

        self.select_main = ttk.Combobox(self.btn_entry_frame, height=4, takefocus=True, background='white',
                                                          font=('arial', 8, 'normal'), width=8, state='readonly')
        self.select_main['value'] = ('data structures', 'algorithm', 'contest', 'question')

        self.select_main.current()
        self.select_main.grid(row=0, column=1, padx=(0, 2), pady=10, sticky=E)
        self.select_main.bind('<<ComboboxSelected>>', self.callback)

        # For all data structure topic ------------------------------------------------------------------------------
        self.select_DSA_topic = ttk.Combobox(self.btn_entry_frame, height=4, takefocus=True, background='white',
                                                          font=('arial', 12, 'normal'), width=12, state='readonly')
        self.select_DSA_topic['value'] = (
                                            'data structures', 'chinese remainder theorem', 'number theory',
                                            'strings', 'trees', 'two pointers', 'sortings', 'ternary search'
                                            'matrices', 'probabilities', 'math', 'meet-in-the-middle', 'interactive',
                                            'binary search', 'bitmasks', 'brute force', 'schedules', 'shortest paths',
                                            'combinatorics', 'constructive algorithms', 'hashing',
                                            'dfs and similar', 'divide and conquer', 'dp', 'graphs', 'greedy',
                                            'dsu', 'expression parsing', 'fft', 'flows', 'games', 'geometry',
                                            'graph matching', 'implementation', 'string suffix structures',
                                        )

        # self.select_DSA_topic.current()
        self.select_DSA_topic.config(background='white')
        self.select_DSA_topic.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)

        self.text_entry = Entry(self.btn_entry_frame, width=47, relief='flat', font=('Times New Roman', 14, 'bold'), fg='red')
        self.text_entry.grid(row=0, column=3)

        # This is searching button ----------------------------------
        self.search = Image.open("images/loupe.png")
        self.search = ImageTk.PhotoImage(self.search)
        self.search_button2 = Button(self.btn_entry_frame, image=self.search, bg='lemon chiffon', relief='flat', command=self.search_to_page)
        self.search_button2.image = self.search
        self.search_button2.grid(row=0, column=4, pady=10, padx=(5, 170), sticky=W)

        # This is setting image button ----------------------------------------------------------------
        self.setting = Image.open("images/setting.png")
        self.setting = ImageTk.PhotoImage(self.setting)
        self.setting_button3 = Button(self.btn_entry_frame, image=self.setting, bg='lemon chiffon', relief='flat')
        self.setting_button3.image = self.setting
        self.setting_button3.grid(row=0, column=5, pady=10)


        self.v = IntVar()
        values = {"Starting": 1,
                "Intermediate": 2,
                "Hard": 3}

        i = 0
        for (text, value) in values.items():
            self.radio = tk.Radiobutton(self.btn_entry_frame, text=text, variable=self.v, value=value, command=self.selection)
            self.radio.config(bg='lemon chiffon', font=('arial', 12, 'normal'))
            self.radio.grid(row=1+i, column=5, padx=(5, 8*(12-len(text))))
            i += 1


        tree_frame = Frame(self.new_window, width=1200, bd=4)
        tree_frame.pack()


        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        yscrollcommand = tree_scroll.set

        self.style = ttk.Style()

        self.style.theme_use('default')


        self.tree = ttk.Treeview(tree_frame)
        self.tree['columns'] = ("A", "B", "C", "D", "E", "F")

        tree_scroll.config(command=self.tree.yview)

        # adding column
        # self.tree.column("#0",  width=0, minwidth=0)
        self.tree.column("A", width=300, minwidth=150)
        self.tree.column("B", width=300, minwidth=150)
        self.tree.column("C", width=300, minwidth=150)
        self.tree.column("D", width=300, minwidth=150)

        # Create headings
        # self.tree.heading("#0", text='Label', anchor=W)
        self.tree.heading("A", text="Section A", anchor=CENTER)
        self.tree.heading("B", text="Section B", anchor=CENTER)
        self.tree.heading("C", text="Extra Section", anchor=CENTER)
        self.tree.heading("D", text="Extra Section D", anchor=CENTER)

        self.tree['show'] = 'headings'
        self.tree.config(height=500)
        self.tree.pack(fill=BOTH, expand=1)


        # self.new_window.mainloop()


    def selection(self):
        dic = {1: "Starting problems", 2: "Intermediate problems", 3: "Hard problems"}
        messagebox.showinfo("Selection", f"You selected {dic[self.v.get()]}")
        # For matching right selection-------------------------------------------------


    def search_result(self, text):
        global l
        for item in self.tree.get_children():
            self.tree.delete(item)

        # For selecting topic
        # text = self.select_DSA_topic.get()

        self.text_entry.configure(state=NORMAL)
        self.text_entry.delete('0', tk.END)
        self.text_entry.insert('0', text)
        self.text_entry.configure(state=DISABLED)
        # =================================== Here we specifying our style for tree ==================================

        self.style.configure('Treeview',
            foreground='navajo white',
            background='navajo white',
            rowheight=30,
            fieldbackgroud='peach puff'
        )

        self.style.map('Treeview', background=[('selected', 'green')])
        self.style.theme_use('default')


        # We want to differentiate each row----------------------------
        self.tree.tag_configure('oddrow', background='white')
        self.tree.tag_configure('evenrow', background='Pale Turquoise1')

        # # For matching right selection-------------------------------------------------
        if self.v.get() == 2:
            l = ["C", "D"]
        elif self.v.get() == 3:
            l = ["E", 'F']
        else:
            l = ['A', 'B']


        # For better result =============================================================================================
        result = self.optimal_search.for_problem(text)
        # result = testing.for_problem(text)
        count = 0

        # l[0] = A and l[1]= f
        # I improved only first and last insert function      f'{j}'
        self.tree.heading("A", text=f'Section {l[0]}', anchor=CENTER)
        self.tree.heading("B", text=f"Section {l[1]}", anchor=CENTER)

        for a, f in zip(result[l[0]], result[l[1]]):
            if count % 2 == 0:
                # self.tree.insert(parent='', index='end',  text=[f'{str(a[1])}/{l[0]}', f'{str(f[1])}/{l[1]}'], values=(a[0], f[0], '', '', '', ''))
                self.tree.insert(parent='', index='end',  text=f'{str(a[1])}/{l[0]}', values=(f'🌟{a[0]}', '', '', '', '', ''), tags=('evenrow',))
            else:
                self.tree.insert('', 'end', text=f'{str(f[1])}/{l[1]}', values=('', f'🌟{f[0]}', '', '', '', ''), tags=('oddrow',))
            count += 1
            self.tree.bind("<Double-1>", self.link_tree)


        if len(result[l[0]]) > len(result[l[1]]):
            for a in result[l[0]][count:]:
                if count % 2 == 0:
                    self.tree.insert(parent='', index='end', text=f'{str(a[1])}/{l[0]}', values=(f'🌟{a[0]}', '', '', '', '', ''), tags=('evenrow',))
                else:
                    self.tree.insert(parent='', index='end', text=f'{str(a[1])}/{l[0]}', values=(f'🌟{a[0]}', '', '', '', '', ''), tags=('oddrow',))
                    self.tree.bind("<Double-1>", self.link_tree)
                count += 1
        elif len(result[l[1]]) > len(result[l[0]]):
            for f in result[l[1]][count:]:
                if count % 2 == 0:
                    self.tree.insert(parent='', index='end',  text=f'{str(f[1])}/{l[1]}', values=('', f'🌟{f[0]}', '', '', '', ''), tags=('evenrow',))
                else:
                    self.tree.insert(parent='', index='end',  text=f'{str(f[1])}/{l[1]}', values=('', f'🌟{f[0]}', '', '', '', ''), tags=('oddrow',))
                self.tree.bind("<Double-1>", self.link_tree)
                count += 1


    def link_tree(self,event):
        input_id = self.tree.selection()
        self.input_item = self.tree.item(input_id,"text")

        import webbrowser
        webbrowser.open('https://codeforces.com/problemset/problem/'+self.input_item)


    def back_to_login(self):
        # self.new_window.forget(self.new_window)
        self.new_window.forget()

    def callback(self, event):
        event = self.select_main.get()

        s = showinfo(
            title='Selection',
            message=f"you selected {event}"
        )
        if s == 'ok':
            if event == 'data structures':
                self.data_structure = True
                self.text_entry.configure(state='readonly')
                self.select_DSA_topic = ttk.Combobox(self.btn_entry_frame,
                                                          font=('arial', 12, 'bold'), width=12, state='readonly')
                self.select_DSA_topic['value'] = (
                                                    'data structures', 'chinese remainder theorem', 'number theory',
                                                    'strings', 'trees', 'two pointers',
                                                    'matrices', 'probabilities', 'math', 'meet-in-the-middle'
                                                    )

                self.select_DSA_topic.current()
                self.select_DSA_topic.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)

            elif event == 'algorithm':
                self.algorithm = True
                self.text_entry.configure(state=DISABLED)
                self.select_DSA_topic = ttk.Combobox(self.btn_entry_frame, font=('arial', 12, 'bold'), width=12,
                                                                  state='readonly')
                self.select_DSA_topic['value'] = (
                                                  'binary search', 'bitmasks', 'brute force',  'divide and conquer', 'dp',
                                                    'combinatorics', 'constructive algorithms', 'hashing',
                                                    'dfs and similar', 'string suffix structures',  'ternary search',
                                                    'dsu', 'expression parsing', 'schedules', 'shortest paths', 'sortings',
                                                    'fft', 'flows', 'games', 'geometry', 'graphs', 'greedy',
                                                    'graph matchings', 'implementation', 'interactive',
                                                )

                self.select_DSA_topic.current()
                self.select_DSA_topic.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)
                self.text_entry.configure(state=DISABLED)

            elif event in ['question', 'contest']:
                self.codeforces_contest = True
                self.text_entry.configure(state=NORMAL)
                self.select_DSA_topic = ttk.Combobox(self.btn_entry_frame, font=('arial', 12, 'bold'), width=12,
                                                                  state=DISABLED)
                self.select_DSA_topic['value'] = ()
                self.select_DSA_topic.current()
                self.select_DSA_topic.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)


    def search_to_page(self):

        search_list = []
        search_list.clear()

        section_of_search = self.select_main.get()
        types_of_search = self.select_DSA_topic.get()
        search_entry = self.text_entry.get()

        self.select_main.current()
        self.select_DSA_topic.current()
        self.text_entry.delete('0', tk.END)


        if self.data_structure:
            search_list.append(section_of_search)
            search_list.append(types_of_search)
            self.algorithm = False
            self.codeforces_contest = False
        elif self.algorithm:
            search_list.append(section_of_search)
            search_list.append(types_of_search)
            self.data_structure = False
            self.codeforces_contest = False
        elif self.codeforces_contest:
            search_list.append(section_of_search)
            search_list.append(search_entry)
            self.data_structure = False
            self.algorithm = False

        if search_list is not []:
            if len(search_list) == 2 and '' not in search_list:
                self.search_result(search_list[1])

            else:
                showinfo("Something Wrong", "You didn't you option properly ")
        else:
            messagebox.showwarning("Search Empty", "Actually your search list is empty")
        print(search_list)



# if __name__ == "__main__":
#     Tree()  # If you run this code from here then you must to remove root from constructor and initialize main root


"""
# ================================================================================================================

        #
        # # For only one column of problem
        # count = 1
        # with open('testing.txt', 'w', encoding='utf-8') as file:
        #     for i in testing.for_problem(text):
        #         file.write(i)
        #         count += 1
        # file.close()
        # with open('testing.txt', 'r', encoding='utf-8') as file:
        #     # result = testing.for_problem()
        #     i = 0
        #     for j in file.read().splitlines():
        #         if i % 2 == 0:
        #             self.tree.insert(parent='', index='end', iid=i, text=f'{j}', values=('', '', '', '', '', j), tags=('even',))
        #             # self.tree.insert(parent='', index='end', iid=count+i, text="", values=('', '', '', '', '', 'https://codeforces.com/problems'), tags=('even',))
        #             # self.tree.move(count+i, i, i)
        #             self.tree.bind("<Double-1>", self.link_tree)
        #         else:
        #             self.tree.insert(parent='', index='end', iid=i, text=f'{j}', values=('', '', '', '', '', j), tags=('odd',))
        #             # self.tree.insert(parent='', index='end', iid=count+i, text="", values=('', '', '', '', '', 'https://codeforces.com/problems'), tags=('odd',))
        #             # self.tree.move(count+i, i, i)
        #             self.tree.bind("<Double-1>", self.link_tree)
        #         i += 1
        #
        # file.close()
"""