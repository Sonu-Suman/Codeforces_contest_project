from tkinter import *


class CredentialPage:
    def __init__(self, root, credential):
        self.root = root
        User_Name = credential[3]
        User_Id = credential[1]
        Email = credential[2]

        self.credential_main_frm = LabelFrame(self.root)
        self.credential_main_frm.place(x=750, y=50)

        self.credential_frm = Frame(self.credential_main_frm, bg='black')
        self.credential_frm.pack()

        credential_page_cancel_btn = Button(self.credential_frm, text="X", font=("Times New Roman", 12, 'bold'), fg='red', relief='flat',
                                    bg='black', command=self.credential_main_frm.destroy)
        credential_page_cancel_btn.grid(row=0, column=3)

        credential_main_label = Label(self.credential_frm, text="User Credential Page", font=('cursive', 24, 'bold'), fg='white', bg='black')
        credential_main_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        credential_user_name_lbl = Label(self.credential_frm, text="Your Name: ", font=("Times New Roman", 18, 'bold'), fg='SeaGreen1', bg='black')
        credential_user_name_lbl.grid(row=2, column=0, padx=(20, 20), pady=(10, 10))

        credential_user_name = Label(self.credential_frm, text=User_Name, font=("Times New Roman", 18, 'bold'), fg='DarkOrange1', bg='black')
        credential_user_name.grid(row=2, column=1, padx=(20, 20), pady=(10, 10))

        credential_user_id_lbl = Label(self.credential_frm, text=" Your Id: ", font=("Times New Roman", 18, 'bold'), fg='salmon', bg='black')
        credential_user_id_lbl.grid(row=3, column=0, padx=(20, 20), pady=(10, 10))

        credential_user_id = Label(self.credential_frm, text=User_Id, font=("Times New Roman", 18, 'bold'), fg='blue', bg='black')
        credential_user_id.grid(row=3, column=1, padx=(20, 20), pady=(10, 10))

        credential_user_email_lbl = Label(self.credential_frm, text=" Your Email: ", font=("Times New Roman", 18, 'bold'), fg='blue', bg='black')
        credential_user_email_lbl.grid(row=4, column=0, padx=(20, 20), pady=(10, 2))

        credential_user_email = Label(self.credential_frm, text=Email, font=("Times New Roman", 18, 'bold'), fg='green yellow', bg='black')
        credential_user_email.grid(row=5, column=0, columnspan=2, padx=(50, 20), pady=(2, 10))


# if __name__ == "__main__":
#     root = tk.Tk()
#     CredentialPage(root, credential="hello")
#     root.mainloop()