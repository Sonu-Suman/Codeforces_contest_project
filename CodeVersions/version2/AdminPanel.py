from tkinter import ttk
from tkinter import *
import tkinter as tk
from db import Store
from tkinter import messagebox


class Admin:
    def __init__(self):
        self.dbc = Store()
        self.root = tk.Tk()
        self.root.minsize(600, 400)
        self.root.maxsize(600, 400)
        self.root.title("Admin Panel")
        self.root.configure(bg="SeaGreen1")

        main_label = Label(self.root, text="Welcome Back Sir", font=("Times New Roman", 24, 'bold'), bg="SeaGreen1")
        main_label.place(x=180, y=20)

        generating = "Here you can access your database so that you can add any question in any folder,\n " \
                     "and you can also modified and delete."

        discription_label = Label(self.root, text=generating, font=("Times New Roman", 12, 'normal'), bg="SeaGreen1",
                                  fg='blue')
        discription_label.place(x=40, y=60)

        self.Algorithm = Button(self.root, text='Algorithm Que', font=("Times New Roman", 18, 'bold'), bg='SeaGreen1',
                                relief='flat', width=18, fg='violetRed1', command=self.Algo)
        self.Algorithm.place(x=20, y=140)

        self.Contest = Button(self.root, text='Contest', font=("Times New Roman", 18, 'bold'), bg='SeaGreen1',
                              relief='flat', width=18, fg='deep pink', command=self.contest)
        self.Contest.place(x=310, y=140)

        self.Que_to_Contest = Button(self.root, text='Que to Contest', font=("Times New Roman", 18, 'bold'),
                                     bg='SeaGreen1',
                                     relief='flat', width=18, fg='firebrick1', command=self.Que_Contest)
        self.Que_to_Contest.place(x=20, y=220)

        self.Data_Structure = Button(self.root, text='Data Structure', font=("Times New Roman", 18, 'bold'),
                                     bg='SeaGreen1',
                                     relief='flat', width=18, fg='gold', command=self.Datas)
        self.Data_Structure.place(x=310, y=220)

        main_label = Label(self.root, text="THANK YOU!", font=("Times New Roman", 24, 'bold'), bg="SeaGreen1", fg='red')
        main_label.place(x=200, y=300)

        self.root.mainloop()

    # ============================================ For Question adding Algo section storage ==============================


    def algo_file(self):
        cloud_folder_name = self.on_cloud_and_local_filename_a.get()
        cloudfilename = self.select_combo_a_search.get()
        filename = self.on_cloud_and_local_filename_a.get()

        try:
            self.dbc.algo(cloud_folder_name, cloudfilename, filename)
            # self.dbc.algo(cloud_folder_name, filename)
            messagebox.showinfo("Successfully add", f"Your file {filename} successfully added in cloud storage.")
        except Exception as e:
            confirm = messagebox.askretrycancel("Crash", f'Your file {filename} didn\'t added in the cloud storage!')
            print("This is from Algorithm folder: ", e)
            if confirm == 1:
                self.algo_file()

    def Algo(self):
        self.algo_label = LabelFrame(self.root, bg="indian red")
        self.algo_label.pack()

        main_label = Label(self.algo_label, text="Adding Algorithm Question!", font=("Times New Roman", 24, 'bold'),
                           bg="indian red", fg='SeaGreen1')
        main_label.grid(row=0, column=0, columnspan=2, pady=10)

        cloudfilename_label = Label(self.algo_label, text="Cloud Folder name: ", font=("Times New Roman", 16, 'bold'),
                                    bg="indian red", fg='SeaGreen1')
        cloudfilename_label.grid(row=1, column=0, pady=10)

        self.select_combo_a_search = StringVar()
        self.select_A_topic_search_combo = ttk.Combobox(self.algo_label, textvariable=self.select_combo_a_search,
                                                        font=('arial', 12, 'bold'), width=20, state='readonly')
        self.select_A_topic_search_combo['value'] = (
                                                    'Binary Search', 'Sorting', 'String Algo', "Greedy Algo", "Graph",
                                                    'BFS', 'DFS', 'Bit-Masking', 'Topological Sort', "Knapsack Algo",
                                                    'Dijkstra Algo', 'Bellman Ford Algo', 'Floyd warshall Algo',
                                                    "Kruskal's Algo", "Primes Algo", 'Recursion', 'Backtracking',
                                                    'Dynamic Programming', 'Divide & Conquer Algo', 'Disjoint Set'
                                                    )

        self.select_A_topic_search_combo.current(0)
        self.select_A_topic_search_combo.grid(row=1, column=1)

        unique_label_a = Label(self.algo_label, text="File name must be unique:-->",
                               font=('Times New Roman', 11, 'normal'), fg='black', bg='indian red')
        unique_label_a.grid(row=2, column=0, sticky=N)

        cloud_and_local_file_name_A = Label(self.algo_label, text="Cloud/Local file name: ",
                                            font=("Times New Roman", 16, 'bold'), bg="indian red", fg='SeaGreen1')
        cloud_and_local_file_name_A.grid(row=3, column=0, pady=2)

        self.on_cloud_and_local_filename_a = Entry(self.algo_label, width=25)
        self.on_cloud_and_local_filename_a.grid(row=3, column=1, padx=(5, 20))

        # filename_label = Label(self.algo_label, text="File you want to save: ", font=("Times New Roman", 16, 'bold'),
        #                                                          bg="indian red", fg='SeaGreen1')
        # filename_label.grid(row=4, column=0, pady=10)
        #
        # self.filename_algo = Entry(self.algo_label, width=30)
        # self.filename_algo.grid(row=4, column=1, padx=(5, 20))

        self.algo_back_button = Button(self.algo_label, text='Home Page ', font=("Times New Roman", 18, 'bold'),
                                       bg='indian red',
                                       relief='flat', width=18, fg='gold', command=self.algo_label.forget)
        self.algo_back_button.grid(row=4, column=0, pady=4)

        self.algo_register_button = Button(self.algo_label, text='Enter ', font=("Times New Roman", 18, 'bold'),
                                           bg='indian red',
                                           relief='flat', width=18, fg='gold', command=self.algo_file)
        self.algo_register_button.grid(row=4, column=1, pady=4)


    # =================================== For Question adding data structure storage Backend ================================


    def data_section_save(self):
        cloud_folder_name = self.select_combo_ds_search.get()
        cloud_file_name = self.question_name_on_cloud_d.get()
        local_filename = self.question_name_on_cloud_d.get()

        try:
            self.dbc.data_str(cloud_folder_name, cloud_file_name, local_filename)
            messagebox.showinfo("Successfully add", f"Your file {local_filename} successfully added in cloud storage.")
        except Exception as e:
            confirm = messagebox.askretrycancel("Crash",
                                                f'Your file {local_filename} didn\'t added in the cloud storage!')
            print("This is from Data structure folder: ", e)
            if confirm == 1:
                self.data_section_save()

    def Datas(self):
        self.data_label = LabelFrame(self.root, bg='aquamarine')
        self.data_label.pack()

        main_label = Label(self.data_label, text="Adding Data Structure Question!",
                           font=("Times New Roman", 24, 'bold'), bg='aquamarine', fg='light cyan')
        main_label.grid(row=0, column=0, columnspan=2, pady=10)

        cloudfilename_label = Label(self.data_label, text="Cloud Folder name: ", font=("Times New Roman", 16, 'bold'),
                                    bg='aquamarine', fg='light cyan')
        cloudfilename_label.grid(row=1, column=0, pady=10)

        self.select_combo_ds_search = StringVar()
        self.select_DS_topic_search_combo = ttk.Combobox(self.data_label, textvariable=self.select_combo_ds_search,
                                                         font=('arial', 12, 'bold'), width=20, state='readonly')
        self.select_DS_topic_search_combo['value'] = ('Array', 'Number theory', 'Linked List', 'Stack and Queue', 'Trie',
                                                      'Binary Heap Tree', 'Binary Tree', 'Binary Search Tree')

        self.select_DS_topic_search_combo.current(0)
        self.select_DS_topic_search_combo.grid(row=1, column=1)

        unique_label_d = Label(self.data_label, text="File name must be unique:-->",
                               font=('Times New Roman', 11, 'normal'), fg='black', bg='aquamarine')
        unique_label_d.grid(row=2, column=0, sticky=S)

        tag_label = Label(self.data_label, text="cloud/local file name: ", font=("Times New Roman", 16, 'bold'),
                          bg='aquamarine', fg='light cyan')
        tag_label.grid(row=3, column=0, pady=2)

        self.question_name_on_cloud_d = Entry(self.data_label, width=25)
        self.question_name_on_cloud_d.grid(row=3, column=1)

        # filename_label = Label(self.data_label, text="File you want to save: ", font=("Times New Roman", 16, 'bold'), bg='aquamarine', fg='light cyan')
        # filename_label.grid(row=3, column=0, pady=10)
        #
        # self.filename_data = Entry(self.data_label, width=30)
        # self.filename_data.grid(row=3, column=1)

        self.data_back_button = Button(self.data_label, text='Home Page ', font=("Times New Roman", 18, 'bold'),
                                       bg='aquamarine', fg='blue',
                                       relief='flat', width=18, command=self.data_label.forget)
        self.data_back_button.grid(row=4, column=0, pady=4)

        self.data_register_button = Button(self.data_label, text='Save ', font=("Times New Roman", 18, 'bold'),
                                           bg='aquamarine', fg='green',
                                           relief='flat', width=18, command=self.data_section_save)
        self.data_register_button.grid(row=4, column=1, pady=4)


    # ============================================ For Contest Question adding Backend ===================================


    def for_contest(self):
        contest_cloud_folder_name = self.contest_cloud_folder_name.get()
        total_no_of_question = self.select_no_of_question_contest.get()
        question_tag = self.select_contest_question_tag.get()
        on_cloud_file_name = self.on_cloud_and_local_filename_contest.get()
        local_file_name = self.on_cloud_and_local_filename_contest.get()

        try:
            self.dbc.data_str(contest_cloud_folder_name, on_cloud_file_name, local_file_name)
            messagebox.showinfo("Successfully add", f"Your file {local_file_name} successfully added in cloud storage.")
        except Exception as e:
            confirm = messagebox.askretrycancel("Crash",
                                                f'Your file {local_file_name} didn\'t added in the cloud storage!')
            print(e)
            if confirm == 1:
                self.for_contest()

    def contest(self):
        self.contest_frame = LabelFrame(self.root, bg='Sienna1')
        self.contest_frame.pack()

        main_label = Label(self.contest_frame, text="Adding About Contest", font=("Times New Roman", 24, 'bold'),
                           bg='Sienna1', fg='blue')
        main_label.grid(row=0, column=0, columnspan=2, pady=10)

        cloudfilename_label = Label(self.contest_frame, text="Contest Id: ", font=("Times New Roman", 16, 'bold'),
                                    bg='Sienna1', fg='blue')  # This is also for cloud folder name in contest storage
        cloudfilename_label.grid(row=1, column=0, pady=10, padx=(10, 20))

        self.contest_cloud_folder_name = Entry(self.contest_frame, width=25)
        self.contest_cloud_folder_name.grid(row=1, column=1, padx=(10, 40))

        total_question_label_in_contest = Label(self.contest_frame, text="Total no of questions ",
                                                font=("Times New Roman", 16, 'bold'), bg='Sienna1', fg='blue')
        total_question_label_in_contest.grid(row=2, column=0, pady=10, padx=(10, 20))

        self.select_no_of_question_contest = StringVar()
        self.select_no_of_question_search_combo = ttk.Combobox(self.contest_frame,
                                                               textvariable=self.select_no_of_question_contest,
                                                               font=('arial', 12, 'bold'), width=20, state='readonly')
        self.select_no_of_question_search_combo['value'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        self.select_no_of_question_search_combo.current(0)
        self.select_no_of_question_search_combo.grid(row=2, column=1, padx=(10, 40))

        tag_label = Label(self.contest_frame, text="Question tag", font=("Times New Roman", 16, 'bold'), bg='Sienna1',
                          fg='blue')
        tag_label.grid(row=3, column=0, pady=10, padx=(10, 20))

        self.select_contest_question_tag = StringVar()
        self.select_question_tag_combo = ttk.Combobox(self.contest_frame, textvariable=self.select_contest_question_tag,
                                                      font=('arial', 12, 'bold'), width=20, state='readonly')
        self.select_question_tag_combo['value'] = ('Array', 'Number theory', 'Linked List', 'Stack', 'Queue', 'Trie',
                                                   'Binary Heap Tree', 'Binary Tree', 'Binary Search Tree',
                                                   'Binary Search',
                                                   'Sorting', 'String Algo', "Greedy Algo", "Graph", 'BFS', 'DFS',
                                                   'Topological Sort', "Knapsack Algo", 'Dijkstra Algo',
                                                   'Bellman Ford Algo',
                                                   'Floyd warshall Algo', "Kruskal's Algo", "Primes Algo", 'Recursion',
                                                   'Backtracking', 'Dynamic Programming',
                                                   'Divide & Conquer Algo', 'Disjoint Set')

        self.select_question_tag_combo.current(0)
        self.select_question_tag_combo.grid(row=3, column=1, padx=(10, 40))

        unique_label_c = Label(self.contest_frame, text="File name must be unique:-->",
                               font=('Times New Roman', 11, 'normal'), fg='black', bg='indian red')
        unique_label_c.grid(row=4, column=0, sticky=N)

        cloud_file_name = Label(self.contest_frame, text="on cloud/local file name: ",
                                font=("Times New Roman", 16, 'bold'), bg='Sienna1', fg='blue')
        cloud_file_name.grid(row=5, column=0, pady=2, padx=(10, 20))

        self.on_cloud_and_local_filename_contest = Entry(self.contest_frame, width=25)
        self.on_cloud_and_local_filename_contest.grid(row=5, column=1, padx=(10, 40))

        # local_file_name_contest = Label(self.contest_frame, text="local file name: ", font=("Times New Roman", 16, 'bold'), bg='Sienna1', fg='blue')
        # local_file_name_contest.grid(row=5, column=0, pady=10, padx=(10, 20))
        #
        # self.contest_local_file_name = Entry(self.contest_frame, width=25)
        # self.contest_local_file_name.grid(row=5, column=1, padx=(10, 40))

        self.contest_back_button = Button(self.contest_frame, text='Home Page ', font=("Times New Roman", 16, 'bold'),
                                          bg='Sienna1', fg='black',
                                          relief='flat', width=18, command=self.contest_frame.forget)
        self.contest_back_button.grid(row=6, column=0, pady=4)

        self.Question_to_save_contest_button = Button(self.contest_frame, text='Save ',
                                                      font=("Times New Roman", 16, 'bold'), bg='Sienna1', fg='green',
                                                      relief='flat', width=18, command=self.for_contest)
        self.Question_to_save_contest_button.grid(row=6, column=1, pady=4)

    # ============================================ For Question to Contest Backend ========================================
    def for_question_to_contest(self):
        pass

    def Que_Contest(self):
        self.Q_to_contest_main_frame = Label(self.root, bg='hot pink')
        self.Q_to_contest_main_frame.pack()

        Q_to_contest_label_frame = Label(self.Q_to_contest_main_frame, text="Adding Link Window",
                                         font=('Times New Roman', 24, 'bold'), bg='hot pink', fg='OliveDrab1')
        Q_to_contest_label_frame.grid(row=0, column=0, columnspan=2)

        Q_type_link = Label(self.Q_to_contest_main_frame, text="Paste your link here: ",
                            font=('Times New Roman', 16, 'normal'),
                            bg='hot pink', fg='OliveDrab1')
        Q_type_link.grid(row=1, column=0, padx=(20, 5))

        self.Link_to_Question = Entry(self.Q_to_contest_main_frame, width=25)
        self.Link_to_Question.grid(row=1, column=1, padx=(5, 20))

        self.question_to_link_back_button = Button(self.Q_to_contest_main_frame, text='Home Page ',
                                                   font=("Times New Roman", 16, 'bold'),
                                                   bg='hot pink', fg='blue', relief='flat', width=18,
                                                   command=self.Q_to_contest_main_frame.forget)
        self.question_to_link_back_button.grid(row=2, column=0, pady=4)

        self.contest_to_link_button = Button(self.Q_to_contest_main_frame, text='Save ',
                                             font=("Times New Roman", 16, 'bold'),
                                             bg='hot pink', fg='green', relief='flat', width=18)
        self.contest_to_link_button.grid(row=2, column=1, pady=4)


if __name__ == "__main__":
    Admin()