from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from db import Searching


class Access:
    def __init__(self, root):
        self.db_get = Searching()
        self.root = root

        self.access_data_frame = Frame(self.root, bg='SeaGreen1')
        self.access_data_frame.pack()

        self.main_label = Label(self.access_data_frame, text="Access your personal Data.", font=("Times New Roman", 40, 'bold'), bg="SeaGreen1")
        self.main_label.grid(row=0, column=0, columnspan=4, padx=(60, 60), pady=(20, 20))

        txt = "Here you can access your personal stored data."
        self.find_data = Label(self.access_data_frame, text=txt, font=("Times New Roman", 14, 'normal'), fg='blue', bg='SeaGreen1')
        self.find_data.grid(row=1, column=0, columnspan=4)

        self.see_questions = Button(self.access_data_frame, text='Questions', font=("Times New Roman", 18, 'bold'), width=15,
                                           relief='flat', bg='SeaGreen1', fg='red', command=self.see_Question_frm)
        self.see_questions.grid(row=2, column=1, pady=(80, 60), padx=(40, 70))

        self.contest_link = Button(self.access_data_frame, text='Access Links', font=("Times New Roman", 18, 'bold'),
                                   relief='flat', bg='SeaGreen1', fg='blue', command=self.get_Question_link, width=15)
        self.contest_link.grid(row=2, column=2, pady=(80, 60), padx=(60, 50))

        self.get_list = Button(self.access_data_frame, text="Find List", font=("Times New Roman", 18, 'bold'),
                                         relief='flat', bg='SeaGreen1', fg='white', width=15)
        self.get_list.grid(row=3, column=2, pady=(60, 60), padx=(40, 70))

        self.back_data_homepage = Button(self.access_data_frame, text="Home Page", font=("Times New Roman", 18, 'bold'), width=15,
                                         relief='flat', bg='SeaGreen1', fg='blue', command=self.access_data_frame.forget)
        self.back_data_homepage.grid(row=3, column=1, pady=(60, 60), padx=(45, 50))

        thanks_lbl = Label(self.access_data_frame, text='Thank You!', font=("Aparajita", 40, 'bold'), bg='SeaGreen1', fg='hot pink')
        thanks_lbl.grid(row=4, column=0, columnspan=3, pady=(20, 40))


    def go_to_question_page(self):
        user_name = self.user_name.get()
        question_tag = self.select_see_question_topic_search_combo.get()
        question_name = self.see_question_entry.get()

        try:
            self.db_get.question(user_name, question_tag, question_name)
        except Exception as e:
            messagebox.showerror("SOMETHING WRONG!", "Something went wrong!")
            print(e)


    def see_Question_frm(self):
        self.access_data_frame.forget()
        self.see_ques_main_frm = LabelFrame(self.root, bg='salmon')
        self.see_ques_main_frm.pack()

        see_question_label = Label(self.see_ques_main_frm, text="Go To Question!", font=("Times New Roman", 36, 'bold'),
                           bg="salmon", fg='blue')
        see_question_label.grid(row=0, column=0, columnspan=2, pady=10, padx=(150, 150))

        self.user_name_ques_lbl = Label(self.see_ques_main_frm, text='User Id', font=('Times New Roman', 16, 'bold'), fg='black', bg='salmon')
        self.user_name_ques_lbl.grid(row=1, column=0, pady=10)

        self.User_Name_f_see_question = StringVar()
        self.user_name = Entry(self.see_ques_main_frm, textvariable=self.User_Name_f_see_question, font=('Times New Roman', 12, 'bold'), width=25)
        self.user_name.grid(row=1, column=1, pady=10, padx=(20, 40))

        see_question_tag_label = Label(self.see_ques_main_frm, text="Select Question tag: ", font=("Times New Roman", 16, 'bold'),
                                    fg="blue", bg='salmon')
        see_question_tag_label.grid(row=2, column=0, pady=10)

        self.select_question_tag_combo = StringVar()
        self.select_see_question_topic_search_combo = ttk.Combobox(self.see_ques_main_frm, textvariable=self.select_question_tag_combo,
                                                        font=('arial', 12, 'bold'), width=20, state='readonly')
        self.select_see_question_topic_search_combo['value'] = (
                                                    'Array', 'Number theory', 'Linked List', 'Stack and Queue', 'Trie',
                                                    'Binary Heap Tree', 'Binary Tree', 'Binary Search Tree',
                                                    'Binary Search', 'Sorting', 'String Algo', "Greedy Algo", "Graph",
                                                    'BFS', 'DFS', 'Bit_Masking', 'Topological Sort', "Knapsack Algo",
                                                    'Dijkstra Algo', 'Bellman Ford Algo', 'Floyd warshall Algo',
                                                    "Kruskal's Algo", "Primes Algo", 'Recursion', 'Backtracking',
                                                    'Dynamic Programming', 'Divide & Conquer Algo', 'Disjoint Set'
                                                    )

        self.select_see_question_topic_search_combo.current(0)
        self.select_see_question_topic_search_combo.grid(row=2, column=1, padx=(20, 40))

        unique_label_a = Label(self.see_ques_main_frm, text="Question name exact same as saved name:-->",
                               font=('Times New Roman', 11, 'normal'), bg="indian red", fg='salmon')
        unique_label_a.grid(row=3, column=0, sticky=N)

        cloud_and_local_file_name_A = Label(self.see_ques_main_frm, text="Question name: ",
                                            font=("Times New Roman", 16, 'bold'), fg='blue', bg='salmon')
        cloud_and_local_file_name_A.grid(row=4, column=0, pady=2)

        self.see_question_entry = Entry(self.see_ques_main_frm, width=25, font=("Times New Roman", 12, 'bold'))
        self.see_question_entry.grid(row=4, column=1, padx=(20, 40))

        self.back_window_to_see_question_frame = Button(self.see_ques_main_frm, text='Back', font=("Times New Roman", 16, 'bold'),
                                                        relief='flat', fg='red', bg='salmon', command=self.revert_main, width=15)
        self.back_window_to_see_question_frame.grid(row=5, column=0, padx=(40, 30), pady=(20, 10))

        self.see_question_enter_btn = Button(self.see_ques_main_frm, text="Enter ", font=("Times New Roman", 16, 'bold'),
                                                relief='flat', fg='green', bg='salmon', width=15, command=self.go_to_question_page)
        self.see_question_enter_btn.grid(row=5, column=1, padx=(30, 40), pady=(20, 10))


    def revert_main(self):
        self.see_ques_main_frm.forget()
        Access(self.root)


    def go_to_link_page(self):
        user_name = self.user_name_get_link_label.get()
        link_name = self.get_link_name.get()

        try:
            self.db_get.get_link_page(user_name, link_name)
        except Exception as e:
            print(e)


    def get_Question_link(self):
        self.access_data_frame.forget()
        self.get_link_frame = Label(self.root, bg='hot pink')
        self.get_link_frame.pack()

        get_link_label_frame = Label(self.get_link_frame, text="Go to web url",
                                         font=('Times New Roman', 36, 'bold'), bg='hot pink', fg='OliveDrab1')
        get_link_label_frame.grid(row=0, column=0, columnspan=2, padx=(180, 180))

        self.user_name_link_lbl = Label(self.get_link_frame, text='User Id', font=('Times New Roman', 16, 'bold'), bg='hot pink', fg='OliveDrab1')
        self.user_name_link_lbl.grid(row=1, column=0, pady=(20, 10), padx=(20, 20))

        self.User_Name_glf_cont = StringVar()
        self.user_name_get_link_label = Entry(self.get_link_frame, textvariable=self.User_Name_glf_cont, font=('Times New Roman', 12, 'bold'), width=30)
        self.user_name_get_link_label.grid(row=1, column=1, pady=(10, 10), padx=(20, 40))

        self.get_link_name_lbl = Label(self.get_link_frame, text='Link Name: ', font=('Times New Roman', 16, 'bold'), bg='hot pink', fg='OliveDrab1')
        self.get_link_name_lbl.grid(row=2, column=0, pady=(10, 10), padx=(20, 20))

        self.get_Link_Name_f_cont = StringVar()
        self.get_link_name = Entry(self.get_link_frame, textvariable=self.get_Link_Name_f_cont, font=('Times New Roman', 12, 'bold'), width=30)
        self.get_link_name.grid(row=2, column=1, pady=(10, 10), padx=(20, 40))

        self.back_window_to_get_link_frame = Button(self.get_link_frame, text='Back', font=("Times New Roman", 16, 'bold'),
                                                        relief='flat', fg='red', bg='hot pink', width=15, command=self.revert)
        self.back_window_to_get_link_frame.grid(row=5, column=0, padx=(40, 30), pady=(20, 10))

        self.get_link_enter_btn = Button(self.get_link_frame, text="Enter ", font=("Times New Roman", 16, 'bold'),
                                                relief='flat', fg='green', bg='hot pink', width=15, command=self.go_to_link_page)
        self.get_link_enter_btn.grid(row=5, column=1, padx=(30, 40), pady=(20, 10))


    def revert(self):
        self.get_link_frame.forget()
        Access(self.root)