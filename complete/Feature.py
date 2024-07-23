import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from hello import RoundedButton
from Question import Window
from contestList import ContestList
from UserInformation import UserInfo
from AdminPanel import Admin
from tree import Tree
from CredentailInfo import CredentialPage
import os
import sys


class FeatureAPP:
    def __init__(self, root, credential):
        # root = tk.Tk()
        # root.minsize(1200, 800)
        # root.maxsize(1200, 800)
        # root.title("CODEFORCES APPLICATIONS")
        # root.configure(bg='lemon chiffon')
        self.credential = credential
        self.feature_root = root
        self.feature_frame_main = Frame(self.feature_root, bg='lemon chiffon')
        self.feature_frame_main.pack()

        self.header_label = Frame(self.feature_frame_main, bg='lemon chiffon')
        # self.header_label.pack()
        self.header_label.grid(row=0, column=0, columnspan=1)

        signup_frame_label = Label(self.header_label, text="Features Page", font=('Times New Roman', 42, 'bold'), fg='blue', bg='lemon chiffon')
        signup_frame_label.grid(row=0, column=0, columnspan=4)

        txt = 'This is the feature page.\nHere all available feature in this application is listed.'
        discription_label = Label(self.header_label, text=txt, font=("Times New Roman", 12, 'bold'), bg='lemon chiffon', fg='black')
        discription_label.grid(row=1, column=0, columnspan=4, padx=(200, 200), pady=(20, 10))


        self.back = Image.open(self.resource_path("images/back.png"))
        self.back = ImageTk.PhotoImage(self.back)
        self.back_button1 = Button(self.header_label, image=self.back, bg='lemon chiffon', relief='flat',
                                   command=self.back_to_login_from_feature)
        self.back_button1.image = self.back
        self.back_button1.grid(row=0, column=0, padx=(0, 280))


        # This is setting image button ----------------------------------------------------------------
        self.setting = Image.open(self.resource_path("images/setting.png"))
        self.setting = ImageTk.PhotoImage(self.setting)
        self.setting_button3 = Button(self.header_label, image=self.setting, bg='lemon chiffon', relief='flat',
                                                command=self.show_credential)
        self.setting_button3.image = self.setting
        self.setting_button3.grid(row=0, column=3, padx=(820, 10))


        self.feature_frame = Frame(self.feature_frame_main, width=1200, bd=4, bg='lemon chiffon')
        # self.feature_frame.pack()
        self.feature_frame.grid(row=1, column=0, columnspan=1)
        # =================================================================
        self.user_information_btn = RoundedButton(self.feature_frame, text="Users \nInformation", border_radius=30, font_size=20,
                                                fg='white', color='SeaGreen1', padx=0, pady=80, command=self.user_information_page)
        self.user_information_btn.grid(row=2, column=3, pady=(10, 10), padx=(0, 0))

        self.data_structure_btn = RoundedButton(self.feature_frame, text="Data Structure \nQuestions", border_radius=30, font_size=20,
                                                fg='blue', color='hot pink', padx=0, pady=70, command=self.data_structure_page)
        self.data_structure_btn.grid(row=3, column=1, pady=(40, 40), padx=(110, 100))

        self.algorithm_btn = RoundedButton(self.feature_frame, text="Algorithms \nQuestions", border_radius=30, font_size=20,
                                           fg='white', color='tomato', padx=10, pady=70, command=self.algorithm_page)
        self.algorithm_btn.grid(row=3, column=2, pady=(40, 40), padx=(200, 15))

        # self.user_information = RoundedButton(self.feature_frame, text="Popular Programming\n Language", border_radius=30, font_size=20,
        #                                         fg='white', color='firebrick2', padx=10, pady=80, command=self.personal_space_page)
        # self.user_information.grid(row=4, column=0, pady=(10, 10), padx=(0, 200))

        self.user_information = RoundedButton(self.feature_frame, text="Personal \nSpace", border_radius=30, font_size=20,
                                                fg='white', color='firebrick2', padx=20, pady=80, command=self.personal_space_page)
        self.user_information.grid(row=4, column=3, pady=(10, 10), padx=(0, 0))

        self.question_btn = RoundedButton(self.feature_frame, text="Questions", border_radius=30, font_size=20, fg='white',
                                          color='tomato', padx=180, pady=70, command=self.question_page)
        self.question_btn.grid(row=5, column=1, padx=(70, 50), pady=(40, 80))

        self.contest_btn = RoundedButton(self.feature_frame, text="All Contest", border_radius=30, font_size=20, fg='blue',
                                         color='hot pink', padx=155, pady=70, command=self.contest_page)
        self.contest_btn.grid(row=5, column=2, padx=(200, 15), pady=(40, 80))

        self.feature_root.mainloop()


    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def show_credential(self):
        CredentialPage(self.feature_root, credential=self.credential)


    def question_page(self):
        # self.feature_frame_main.forget()
        Window(self.feature_root, credential=self.credential)


    def algorithm_page(self):
        Tree(self.feature_root, true_false='algo', credential=self.credential)


    def data_structure_page(self):
        Tree(self.feature_root, true_false="data_structure", credential=self.credential)
    

    def contest_page(self):
        # if self.contest_to:
        #     ContestList(self.root)
        # else:
        #     messagebox.showwarning("Invalid Access", "First you Log in!")
        ContestList(self.feature_root, credential=self.credential)


    def user_information_page(self):
        UserInfo(self.feature_root, credential=self.credential)


    def personal_space_page(self):
        Admin()


    def back_to_login_from_feature(self):
        self.feature_frame_main.forget()
        # self.feature_root.forget(self.feature_root)


# if __name__ == "__main__":
#     FeatureAPP()