from tkinter import *
import tkinter as tk
from tkinter import Scrollbar, scrolledtext
from tkinter import messagebox
from db import Searching
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.messagebox import showinfo
from result import Search


class Window:
    def __init__(self, root):
        self.optimal_search = Search()
        self.algorithm = False
        self.data_structure = False
        self.codeforces_contest = False
        self.new_window = Frame(root, bg='lemon chiffon')
        # new_window.grid_size()
        self.new_window.pack()

        self.back = Image.open("images/back.png")
        self.search = Image.open("images/loupe.png")
        self.setting = Image.open("images/setting.png")

        self.back = ImageTk.PhotoImage(self.back)
        self.search = ImageTk.PhotoImage(self.search)
        self.setting = ImageTk.PhotoImage(self.setting)

        self.back_button1 = Button(self.new_window, image=self.back, bg='lemon chiffon', relief='flat', command=self.back_to_login)
        self.search_button2 = Button(self.new_window, image=self.search, bg='lemon chiffon', relief='flat', command=self.search_to_page)
        self.setting_button3 = Button(self.new_window, image=self.setting, bg='lemon chiffon', relief='flat')

        self.back_button1.image = self.back
        self.search_button2.image = self.search
        self.setting_button3.image = self.setting

        # self.back_button1.pack(side=LEFT, padx=20, pady=30)
        # self.search_button2.pack()
        # self.setting_button3.pack()

        self.back_button1.grid(row=0, column=0, pady=10, padx=(5, 10))
        self.search_button2.grid(row=0, column=4, pady=10, padx=(5, 150), sticky=W)
        self.setting_button3.grid(row=0, column=5, pady=10)


        self.select_four_search_combo = ttk.Combobox(self.new_window,
                                                      font=('arial', 12, 'bold'), width=8, height=30, state='readonly')
        self.select_four_search_combo['value'] = ('ds', 'algo', 'contest', 'question')
        self.select_four_search_combo.current(0)
        self.select_four_search_combo.grid(row=0, column=1, padx=(20, 0), sticky=E)
        self.select_four_search_combo.bind('<<ComboboxSelected>>', self.callback)


        self.select_combo_dsa_search = StringVar()
        self.select_DSA_topic_search_combo = ttk.Combobox(self.new_window, textvariable=self.select_combo_dsa_search,
                                                          font=('arial', 13, 'bold'), width=12, state='readonly')
        self.select_DSA_topic_search_combo['value'] = (
                                                        'data structures', 'chinese remainder theorem', 'number theory',
                                                             'strings', 'trees', 'two pointers',
                                                            'matrices', 'probabilities', 'math', 'meet-in-the-middle',
                                                            'binary search', 'bitmasks', 'brute force',
                                                                'combinatorics', 'constructive algorithms', 'hashing',
                                                                 'dfs and similar', 'divide and conquer', 'dp',
                                                                 'dsu', 'expression parsing',
                                                                'fft', 'flows', 'games', 'geometry', 'graphs', 'greedy',
                                                                'graph matching', 'implementation', 'interactive',
                                                                 'schedules', 'shortest paths', 'sortings',
                                                                'string suffix structures',  'ternary search'
                                                        )

        self.select_DSA_topic_search_combo.current()
        self.select_DSA_topic_search_combo.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)


        self.entry = Entry(self.new_window, font=('Times New Roman', 16, 'bold'), width=45)
        self.entry.grid(row=0, column=3, pady=10, sticky=W)


        title2 = Label(self.new_window, bd=5, bg='lemon chiffon', width=30, font=('Times New Roman', 16, 'bold'))
        title2.grid(row=1, column=0, columnspan=6)

        search_title = Label(title2, text='Search by:->', bd=5, bg='lemon chiffon', font=('Times New Roman', 12, 'bold'))
        search_title.grid(row=0, column=0, padx=(0, 100))


        v = StringVar()

        values = {"Starting": "OK! I select started type problem for you",
                    "Intermediate": "OK! I select intermediate problem for you",
                  "Hard": 'OK! I select hard problem for you'}

        i = 0
        for (text, value) in values.items():
            r = tk.Radiobutton(title2, text=text, variable=v, value=value)
            r.config(bg='lemon chiffon', font=('arial', 12, 'bold'))
            r.grid(row=0, column=1+i, padx=(0, 10))
            i += 1

        search_title = Label(self.new_window, text="Search Result -->", bd=5, bg='lemon chiffon', width=30,
                             font=('Times New Roman', 16, 'bold'))
        search_title.grid(row=2, column=0, columnspan=6)
        #
        # result_frame = Frame(self.new_window, relief=RIDGE, bd=2, height=34)
        # result_frame.grid(row=3, column=0, columnspan=6)
        #
        # scroll_X = Scrollbar(result_frame, orient=HORIZONTAL)
        # scroll_Y = Scrollbar(result_frame, orient=VERTICAL)
        #
        # self.result_table = ttk.Treeview(result_frame,
        #                                  column=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
        #                                  xscrollcommand=scroll_X.set, yscrollcommand=scroll_Y.set
        #                                  )
        #
        # scroll_X.pack(side=BOTTOM, fill=X)
        # scroll_Y.pack(side=RIGHT, fill=Y)
        #
        # scroll_X.configure(command=self.result_table.xview)
        # scroll_Y.configure(command=self.result_table.yview)
        #
        # self.result_table.heading('A', text='Section A')
        # self.result_table.heading('B', text='Section B')
        # self.result_table.heading('C', text="Section C")
        # self.result_table.heading('D', text='Section D')
        # self.result_table.heading('E', text='Section E')
        # self.result_table.heading('F', text='Section F')
        # self.result_table.heading('G', text='Section G')
        # self.result_table.heading('H', text='Section H')
        #
        # self.result_table['show'] = 'headings'
        #
        # self.result_table.column('A', width=150)
        # self.result_table.column('B', width=150)
        # self.result_table.column('C', width=150)
        # self.result_table.column('D', width=150)
        # self.result_table.column('E', width=150)
        # self.result_table.column('F', width=150)
        # self.result_table.column('G', width=150)
        # self.result_table.column('H', width=150)
        #
        # self.result_table.pack(fill=BOTH, expand=1)
        self.search_result_window = scrolledtext.ScrolledText(self.new_window, font=('arial', 12, 'bold'), relief='flat', wrap=tk.WORD,
                                                        bd=2, fg='blue',  height=34, width=125, state=DISABLED)

        self.search_result_window.grid(row=3, column=0, columnspan=6, padx=(20, 20))


    def back_to_login(self):
        self.new_window.forget()


    def callback(self, event):
        event = self.select_four_search_combo.get()

        s = showinfo(
            title='Selection',
            message=f"you selected {event}"
        )
        if s == 'ok':
            if event == 'ds':
                self.data_structure = True
                self.entry.configure(state=DISABLED)
                self.select_DSA_topic_search_combo = ttk.Combobox(self.new_window,
                                                          font=('arial', 12, 'bold'), width=12, state='readonly')
                self.select_DSA_topic_search_combo['value'] = (
                                                            'data structures', 'chinese remainder theorem', 'number theory',
                                                             'strings', 'trees', 'two pointers',
                                                            'matrices', 'probabilities', 'math', 'meet-in-the-middle'
                                                            )

                self.select_DSA_topic_search_combo.current(0)
                self.select_DSA_topic_search_combo.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)

            elif event == 'algo':
                self.algorithm = True
                self.entry.configure(state=DISABLED)
                self.select_DSA_topic_search_combo = ttk.Combobox(self.new_window, font=('arial', 12, 'bold'), width=12,
                                                                  state='readonly')
                self.select_DSA_topic_search_combo['value'] = (
                                                                'binary search', 'bitmasks', 'brute force',
                                                                'combinatorics', 'constructive algorithms', 'hashing',
                                                                 'dfs and similar', 'divide and conquer', 'dp',
                                                                 'dsu', 'expression parsing',
                                                                'fft', 'flows', 'games', 'geometry', 'graphs', 'greedy',
                                                                'graph matchings', 'implementation', 'interactive',
                                                                 'schedules', 'shortest paths', 'sortings',
                                                                'string suffix structures',  'ternary search',
                                                            )

                self.select_DSA_topic_search_combo.current(0)
                self.select_DSA_topic_search_combo.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)
                self.entry.configure(state=DISABLED)

            elif event in ['question', 'contest']:
                self.codeforces_contest = True
                self.entry.configure(state=NORMAL)
                self.select_DSA_topic_search_combo = ttk.Combobox(self.new_window, font=('arial', 12, 'bold'), width=12,
                                                                  state=DISABLED)
                self.select_DSA_topic_search_combo['value'] = ()
                self.select_DSA_topic_search_combo.current()
                self.select_DSA_topic_search_combo.grid(row=0, column=2, padx=(0, 2), pady=10, sticky=E)

    def search_to_page(self):
        search_list = []
        search_list.clear()
        self.search_result_window.delete('1.0', tk.END)

        section_of_search = self.select_four_search_combo.get()
        types_of_search = self.select_DSA_topic_search_combo.get()
        search_entry = self.entry.get()

        # if not self.data_structure:
        #     yes = messagebox.askokcancel("Selection Warning", "Please select proper option!")
        #     if not yes:
        #         self.back_to_login()

        if self.data_structure:
            self.select_four_search_combo.current(0)
            self.select_DSA_topic_search_combo.current(0)
        if self.algorithm:
            self.select_four_search_combo.current(0)
            self.select_DSA_topic_search_combo.current(0)
        elif self.codeforces_contest:
            self.select_four_search_combo.current(0)
            self.entry.delete(0, tk.END)

        if self.data_structure:
            search_list.append(section_of_search)
            search_list.append(types_of_search)
        elif self.algorithm:
            search_list.append(section_of_search)
            search_list.append(types_of_search)
        elif self.codeforces_contest:
            search_list.append(section_of_search)
            search_list.append(search_entry)

        if search_list is not []:
            if len(search_list) == 2:
                self.search_result_window.configure(state=NORMAL)
                self.search_result_window.insert('1.0', self.optimal_search.for_problem(search_list[1]))
                # self.optimal_search.for_problem(search_list[1])
                # self.result_table.insert(tk.END, self.optimal_search.for_problem(search_list[1]))
            else:
                showinfo("Something Wrong", "You didn't you option properly ")
        else:
            messagebox.showwarning("Search Empty", "Actually your search list is empty")

        print(search_list[1])

#
# class Search:
#     def __init__(self):
#         self.dbs = Searching()
#
#     def efficient(self, search_list):
#         search1 = search_list[0]
#         search2 = search_list[1]
#
#         self.dbs.by_algo(search1, search2)


"""
def msg1():
    if str(v.get()) == 'agree with our terms and conditions':
        if messagebox.askyesno('MESSAGE', 'Hi!, \nYou agree with our term and conditions..') > 0:
            def next2():
                frame1.grid_forget()

                # THIS IS NEW PAGE -------------------------------------------------------------------------------------
                frame2.grid()

                # THIS IS PREVIOUS PAGE --------------------------------------------------------------------------------
                # frame3.grid()

            next2()

        # HERE is there something


    def sel():
    selection = tk.Label(text=("You are " + str(v.get())), bg='black', fg='white')
    selection.config(font=('cursive', 12, 'bold'))
    selection.grid(row=0, column=0)
    selection.after(1000, selection.destroy)
"""