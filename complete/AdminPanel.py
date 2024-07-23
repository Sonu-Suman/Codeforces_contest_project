from tkinter import ttk
from tkinter import *
import tkinter as tk
from db import Store
from AccessData import Access
from tkinter import messagebox


class Admin:
    def __init__(self):
        self.dbc = Store()
        self.root = tk.Tk()
        self.root.minsize(800, 600)
        self.root.maxsize(800, 600)
        self.root.title("Personal Space Page")
        self.root.configure(bg="SeaGreen1")
        # self.root = root

        self.main_label = Label(self.root, text="Store your personal data.", font=("Times New Roman", 40, 'bold'), bg="SeaGreen1")
        self.main_label.place(x=105, y=20)

        generating = "Here you can access your store your personal data like any type questions and \nany contest link." \
                     "with your user id so that you can't loose your personal data"

        discription_label = Label(self.root, text=generating, font=("Times New Roman", 14, 'normal'), bg="SeaGreen1",
                                  fg='blue')
        discription_label.place(x=110, y=100)

        self.Algorithm = Button(self.root, text='Save Question', font=("Times New Roman", 18, 'bold'), bg='SeaGreen1',
                                relief='flat', width=18, fg='violetRed1', command=self.Save_Questions)
        self.Algorithm.place(x=80, y=220)

        self.Que_to_Contest = Button(self.root, text='Save Link', font=("Times New Roman", 18, 'bold'), bg='SeaGreen1',
                                     relief='flat', width=18, fg='firebrick1', command=self.Save_Link)
        self.Que_to_Contest.place(x=410, y=220)

        self.exit_btn = Button(self.root, text='Exit', font=("Times New Roman", 18, 'bold'),
                                     bg='SeaGreen1', relief='flat', width=18, fg='red', command=self.root.destroy)
        self.exit_btn.place(x=80, y=350)

        self.Contest = Button(self.root, text='Access Stored Files', font=("Times New Roman", 18, 'bold'), bg='SeaGreen1',
                              relief='flat', width=18, fg='deep pink', command=self.access_cloud_storage)
        self.Contest.place(x=410, y=340)

        main_label = Label(self.root, text="THANK YOU!", font=("Times New Roman", 24, 'bold'), bg="SeaGreen1", fg='red')
        main_label.place(x=290, y=480)

        self.root.mainloop()

    # ============================================ For Question adding Algo section storage ==============================


    def question_save(self):
        cloud_question_name = self.on_cloud_and_local_filename_a.get()
        # personal_user_name = self.User_Name_f_algo.get()
        personal_user_name = self.user_name.get()
        # cloudfilename = self.select_combo_a_search.get()
        cloudfilename = self.select_dsa_topic_combo.get()
        filename = self.on_cloud_and_local_filename_a.get()

        try:
            self.dbc.save_questions(personal_user_name, cloudfilename, cloud_question_name, filename)

            messagebox.showinfo("Successfully add", f"Your file {filename} successfully added in cloud storage.")
        except Exception as e:
            confirm = messagebox.askretrycancel("Crash", f"Your file {filename} didn't added in the cloud storage!")
            print("This is from Question adding folder: ", e)
            if confirm == 1:
                self.question_save()

    def Save_Questions(self):
        self.save_question_lbl_frm = LabelFrame(self.root, bg="indian red")
        self.save_question_lbl_frm.pack()

        main_label = Label(self.save_question_lbl_frm, text="Save Important Question!", font=("Times New Roman", 36, 'bold'),
                           bg="indian red", fg='SeaGreen1')
        main_label.grid(row=0, column=0, columnspan=2, pady=20, padx=(50, 50))

        self.user_name_lbl = Label(self.save_question_lbl_frm, text='User Id', font=('Times New Roman', 18, 'bold'), bg='indian red', fg='SeaGreen1')
        self.user_name_lbl.grid(row=1, column=0, pady=10, padx=(30, 20))

        self.User_Name_f_algo = StringVar()
        self.user_name = Entry(self.save_question_lbl_frm, textvariable=self.User_Name_f_algo, font=('Times New Roman', 12, 'bold'), width=25)
        self.user_name.grid(row=1, column=1, pady=10)

        cloudfilename_label = Label(self.save_question_lbl_frm, text="Cloud Folder name: ", font=("Times New Roman", 16, 'bold'),
                                    bg="indian red", fg='SeaGreen1')
        cloudfilename_label.grid(row=2, column=0, pady=10)

        self.select_combo_a_search = StringVar()
        self.select_dsa_topic_combo = ttk.Combobox(self.save_question_lbl_frm, textvariable=self.select_combo_a_search,
                                                        font=('arial', 12, 'bold'), width=20, state='readonly')
        self.select_dsa_topic_combo['value'] = ('Array', 'Number_theory', 'Linked_List', 'Stack_and_Queue', 'Trie',
                                                      'Binary_Heap Tree', 'Binary_Tree', 'Binary Search Tree',
                                                    'Binary Search', 'Sorting', 'String Algo', "Greedy Algo", "Graph",
                                                    'BFS', 'DFS', 'Bit_Masking', 'Topological Sort', "Knapsack Algo",
                                                    'Dijkstra Algo', 'Bellman Ford Algo', 'Floyd warshall Algo',
                                                    "Kruskal's Algo", "Primes Algo", 'Recursion', 'Backtracking',
                                                    'Dynamic Programming', 'Divide & Conquer Algo', 'Disjoint Set'
                                                    )

        self.select_dsa_topic_combo.current(0)
        self.select_dsa_topic_combo.grid(row=2, column=1)

        unique_label_a = Label(self.save_question_lbl_frm, text="File name must be unique:-->",
                               font=('Times New Roman', 11, 'normal'), fg='black', bg='indian red')
        unique_label_a.grid(row=3, column=0, sticky=N)

        cloud_and_local_file_name_A = Label(self.save_question_lbl_frm, text="Cloud/Local file name: ",
                                            font=("Times New Roman", 16, 'bold'), bg="indian red", fg='SeaGreen1')
        cloud_and_local_file_name_A.grid(row=4, column=0, pady=2)

        self.on_cloud_and_local_filename_a = Entry(self.save_question_lbl_frm, width=25, font=("Times New Roman", 12, 'bold'))
        self.on_cloud_and_local_filename_a.grid(row=4, column=1, padx=(5, 20))

        self.algo_back_button = Button(self.save_question_lbl_frm, text='Home Page ', font=("Times New Roman", 18, 'bold'),
                                       bg='indian red',
                                       relief='flat', width=18, fg='gold', command=self.save_question_lbl_frm.forget)
        self.algo_back_button.grid(row=5, column=0, pady=(20, 10))

        self.algo_register_button = Button(self.save_question_lbl_frm, text='Enter ', font=("Times New Roman", 18, 'bold'),
                                           bg='indian red',
                                           relief='flat', width=18, fg='gold', command=self.question_save)
        self.algo_register_button.grid(row=5, column=1, pady=(20, 10))
    # ============================================ For Saving Important questions ======================================

    def save_link_contest(self):
        # personal_user_id = self.User_Name_f_cont.get()
        # link_name = self.Link_Name_f_cont.get()
        # link = self.link.get()
        personal_user_id = self.user_name.get()
        link_name = self.Link_name.get()
        link = self.save_important_link.get()

        try:
            self.dbc.save_imp_link(personal_user_id, link_name, link)

            messagebox.showinfo("Successfully add", f"Your file {link_name} successfully added in cloud storage.")
        except Exception as e:
            confirm = messagebox.askretrycancel("Crash", f'Your file {link_name} didn\'t added in the cloud storage!')
            print("This is from Link folder: ", e)
            if confirm == 1:
                self.save_link_contest()


    def Save_Link(self):
        self.save_link_frame = Label(self.root, bg='hot pink')
        self.save_link_frame.pack()

        Q_to_contest_label_frame = Label(self.save_link_frame, text="Save Important Link",
                                         font=('Times New Roman', 36, 'bold'), bg='hot pink', fg='OliveDrab1')
        Q_to_contest_label_frame.grid(row=0, column=0, columnspan=2, padx=(50, 50), pady=(20, 10))

        self.user_name_lbl = Label(self.save_link_frame, text='User Id', font=('Times New Roman', 16, 'bold'), bg='hot pink', fg='OliveDrab1')
        self.user_name_lbl.grid(row=1, column=0, pady=10)

        self.User_Name_f_cont = StringVar()
        self.user_name = Entry(self.save_link_frame, textvariable=self.User_Name_f_cont, font=('Times New Roman', 12, 'bold'), width=28)
        self.user_name.grid(row=1, column=1, pady=10)

        self.link_name_lbl = Label(self.save_link_frame, text='Link Name: ', font=('Times New Roman', 16, 'bold'), bg='hot pink', fg='OliveDrab1')
        self.link_name_lbl.grid(row=2, column=0, pady=10)

        self.Link_Name_f_cont = StringVar()
        self.Link_name = Entry(self.save_link_frame, textvariable=self.Link_Name_f_cont, font=('Times New Roman', 12, 'bold'), width=28)
        self.Link_name.grid(row=2, column=1, pady=10)

        Q_type_link = Label(self.save_link_frame, text="Paste your link here: ",
                            font=('Times New Roman', 16, 'normal'), bg='hot pink', fg='OliveDrab1')
        Q_type_link.grid(row=3, column=0, padx=(20, 10), pady=10)

        self.link = StringVar()
        self.save_important_link = Entry(self.save_link_frame, textvariable=self.link, width=28, font=('Times New Roman', 12, 'bold'))
        self.save_important_link.grid(row=3, column=1, padx=(10, 15), pady=10)

        self.link_back_button = Button(self.save_link_frame, text='Home Page ', font=("Times New Roman", 16, 'bold'),
                                                   bg='hot pink', fg='blue', relief='flat', width=20,
                                                   command=self.save_link_frame.forget)
        self.link_back_button.grid(row=4, column=0, pady=(20, 10))

        self.contest_to_link_button = Button(self.save_link_frame, text='Save ',
                                             font=("Times New Roman", 17, 'bold'),
                                             bg='hot pink', fg='green', relief='flat', width=20, command=self.save_link_contest)
        self.contest_to_link_button.grid(row=4, column=1, pady=(20, 10))


    def access_cloud_storage(self):
        Access(self.root)

    # def cut_out_from_admin(self):
    #     self.main_label.destroy()

# if __name__ == "__main__":
#     Admin()
