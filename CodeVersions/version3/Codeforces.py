import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from db import SignInAndSignUp
from hello import RoundedButton
from Feature import FeatureAPP
from tkinter import scrolledtext
from random import *
import string as s


class Graphics:
    def __init__(self):
        self.db = SignInAndSignUp()
        # self.command = Command()
        # flags for future-------------------------------------
        # self.data_structure_to = False
        # self.algorithm_to = False
        # self.question_to = False
        # self.contest_to = False
        # -------------------------------------------------------
        self.root = tk.Tk()
        self.root.title("Codeforces Contest Question finding Window")
        self.root.minsize(1200, 800)
        self.root.maxsize(1200, 800)
        self.root.configure(bg='lemon chiffon')

        # self.Main_frame = Frame(self.root, bg="#E5E5D6")
        self.logo = Image.open('images/code.png')
        self.logo2 = Image.open("images/coding-language.png")

        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo2 = ImageTk.PhotoImage(self.logo2)

        self.logo_label = Label(self.root, image=self.logo, bg='lemon chiffon')
        self.logo_label2 = Label(self.root, image=self.logo2, bg='lemon chiffon')

        self.logo_label.image = self.logo
        self.logo_label2.image = self.logo2

        # self.logo_label.grid(row=1, column=1, pady=20)
        # self.logo_label2.grid(row=1, column=0, padx=200, pady=20)
        # self.logo_label.pack(padx=200, pady=80, side=tk.LEFT)
        # self.logo_label2.pack(padx=200, pady=80)

        self.logo_label2.place(x=190, y=125)
        self.logo_label.place(x=550, y=125)

        title = Label(self.root, text="Codeforces Coding Contest", font=('Times New Roman', 48, 'bold'), bg='lemon chiffon', fg='red4')
        title.place(x=200, y=20)

        self.learn_about = Button(self.root, text="Learn About", font=('Times New Roman', 8, 'bold'), bg='lemon chiffon', fg='red4', relief='flat')
        self.learn_about.place(x=850, y=100)

        self.learn_policy = Button(self.root, text="Privacy Policy", font=('Times New Roman', 8, 'bold'), bg='lemon chiffon', fg='red4', relief='flat')
        self.learn_policy.place(x=20, y=750)

        login_credential_label = Label(self.root, text="Log in credential: ", bg='lemon chiffon', font=("Times New Roman", 32, 'bold'), fg='SeaGreen1')
        login_credential_label.place(x=380, y=420)

        name_label = Label(self.root, text="Email : ", bg='lemon chiffon', font=("lucida calligraphy", 22, 'bold'))
        name_label.place(x=190, y=500)

        self.user_email = Entry(self.root, bg='lemon chiffon', font=('lucida calligraphy', 16, 'bold'), width=30)
        self.user_email.place(x=380, y=505)

        name_label = Label(self.root, text="Password : ", bg='lemon chiffon', font=("lucida calligraphy", 22, 'bold'))
        name_label.place(x=190, y=560)

        self.user_password = Entry(self.root, show='*', bg='lemon chiffon',  font=('lucida calligraphy', 16, 'bold'), width=30)
        self.user_password.place(x=380, y=565)

        self.forgot_password = RoundedButton(self.root, text="Forgot password", border_radius=4, font_size=14, fg='red',
                                             command=self.forgot_password, color='lemon chiffon', padx=36, pady=18)
        self.forgot_password.place(x=720, y=610)

        self.SignUp = RoundedButton(self.root, text="Sign Up", border_radius=4, font_size=20, command=self.Signup_frame,
                                    fg='black', color='cornflower blue', padx=64, pady=24)
        self.SignUp.place(x=350, y=680)

        self.Login = RoundedButton(self.root, text="Log in", border_radius=4, font_size=20, command=self.Login, fg='black',
                                   color='cornflower blue', padx=64, pady=24)
        self.Login.place(x=750, y=680)

        self.data_structure_btn = RoundedButton(self.root, text="Data Structure \nQuestions", border_radius=30, font_size=20,
                                                fg='blue', color='hot pink', padx=0, pady=70)
        self.data_structure_btn.place(x=960, y=120)

        self.algorithm_btn = RoundedButton(self.root, text="Algorithms \nQuestions", border_radius=30, font_size=20,
                                           fg='white', color='tomato', padx=10, pady=70)
        self.algorithm_btn.place(x=960, y=240)

        self.question_btn = RoundedButton(self.root, text="Questions", border_radius=30, font_size=20, fg='blue',
                                          color='Sea Green1', padx=160, pady=70)
        self.question_btn.place(x=960, y=360)

        self.contest_btn = RoundedButton(self.root, text="All Contest", border_radius=30, font_size=20, fg='white',
                                         color='gold', padx=160, pady=70)
        self.contest_btn.place(x=960, y=480)

        self.personal_space_show = RoundedButton(self.root, text="Personal \nSpace", border_radius=30, font_size=20, fg='blue',
                                         color='deep sky blue', padx=100, pady=70)
        self.personal_space_show.place(x=960, y=600)

        notification_label = Label(self.root, text='Get notification: ', fg='ivory4', bg='lemon chiffon', font=('lucida calligraphy', 10, 'bold'))
        notification_label.place(x=820, y=760)

        self.notification_email = Entry(self.root,  bg='lemon chiffon', font=('lucida calligraphy', 8, 'normal'), width=24)
        self.notification_email.place(x=960, y=760)

        self.forward_logo = Image.open('images/right-arrow.png')
        self.forward_logo = ImageTk.PhotoImage(self.forward_logo)
        self.forward_label = Button(self.root, image=self.forward_logo, bg='lemon chiffon', relief='flat', fg='lemon chiffon',
                                    width=30, command=self.get_notification)
        self.forward_label.image = self.logo

        self.forward_label.place(x=1140, y=760)

        self.root.mainloop()

    def get_notification(self):
        res = self.notification_email.get()
        if res != '':
            try:
                self.db.saving_email(res)
                # self.command.execute(res)
            except Exception as e:
                messagebox.showinfo("SOMETHING WRONG", "Something went wrong.")
                print(e)
        else:
            messagebox.showwarning("ENTER EMAIL", 'first you enter email.')


    def access_password(self):
        email = self.password_forgot_email.get()


    def forgot_password(self):
        self.password_frame = LabelFrame(self.root, bg='gray63')
        self.password_frame.pack()

        password_frame_label = Label(self.password_frame, text="Re-access your password", font=('arial', 24, 'bold'), fg='#ffd700', bg='gray63')
        password_frame_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        password_frame_email = Label(self.password_frame, text="Email: ", font=('lucida calligraphy', 14, 'bold'), bg='gray63')
        password_frame_email.grid(row=1, column=0, padx=20)

        self.password_forgot_email = Entry(self.password_frame, bg='lemon chiffon', font=('lucida calligraphy', 16, 'bold'), width=25)
        self.password_forgot_email.grid(row=1, column=1, columnspan=3, padx=10)

        self.password_back_toLogin = RoundedButton(self.password_frame, text="Login page", border_radius=4, font_size=16,
                                                   fg='black', color='cornflower blue', padx=64, pady=24, command=self.back_to_login_from_password)
        self.password_back_toLogin.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

        self.click_forgot_btn = RoundedButton(self.password_frame, text="Enter ", border_radius=4, font_size=18, fg='black',
                                              color='cornflower blue', padx=64, pady=24, command=self.access_password)
        self.click_forgot_btn.grid(row=2, column=2, columnspan=3, padx=40, pady=20)

        get_password = Label(self.password_frame, text="Your Password: ", font=('lucida calligraphy', 14, 'bold'), bg='gray63')
        get_password.grid(row=3, column=0, pady=10, padx=10)


    def back_to_login_from_password(self):
        self.password_frame.forget()


    def Login(self):
        email = self.user_email.get()
        password = self.user_password.get()
        # print(email, password)
        # FeatureAPP(self.root, credential=["f", "ds", "suman@gmail.com", "Aparajita Suman"])
        if email != '' and password != '':
            try:
                done = self.db.login(email, password)
                # print("at login time : ===========", done)
                credential = self.db.get_user_id(done)

                selection = tk.Label(text="Logging.................\nPLEASE WAIT. ", bg='black', fg='white')
                selection.config(font=('cursive', 12, 'bold'))
                selection.place(x=500, y=400)
                selection.after(2000, selection.destroy)
                messagebox.showinfo("Successful", "Successfully logged in\nNow you can access these features")
                self.user_email.delete(0, tk.END)
                self.user_password.delete(0, tk.END)

                # flags for future used --------------------------------------
                # self.data_structure_to = True
                # self.contest_to = True
                # self.algorithm_to = True
                # self.question_to = True
                # # self.data_structure_page()
                # -----------------------------------
                # self.Feature_page()
                FeatureAPP(self.root, credential)
            except Exception as e:
                messagebox.showerror(f"SOMETHING WRONG", "May be network error. \nor may be cross check your filled information\n")
                print(e)
                self.user_email.delete(0, tk.END)
                self.user_password.delete(0, tk.END)
        else:
            messagebox.showwarning("FILL INFORMATION", "First fill up all information in the field.")


    def Signup_frame(self):
        self.signup_frame = Frame(self.root, bg='papaya whip')
        self.signup_frame.pack()

        signup_frame_label = Label(self.signup_frame, text="Sign Up Page", font=('cursive', 40, 'bold'), fg='chocolate3',
                                                    bg='papaya whip')
        signup_frame_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        user_name = Label(self.signup_frame, text='Name: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        user_name.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.signup_user_name = Entry(self.signup_frame, bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), width=25)
        self.signup_user_name.grid(row=1, column=1, padx=(20, 40), pady=(20, 10))

        signup_user_email = Label(self.signup_frame, text='Email: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        signup_user_email.grid(row=2, column=0, padx=20, pady=10)

        self.signup_user_email = Entry(self.signup_frame, bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), relief='groove', width=25)
        self.signup_user_email.grid(row=2, column=1, padx=(20, 40), pady=10)

        signup_user_password = Label(self.signup_frame, text='Enter Password: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        signup_user_password.grid(row=3, column=0, padx=20, pady=10)

        self.signup_user_password = Entry(self.signup_frame, show='*', bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), relief='groove', width=25)
        self.signup_user_password.grid(row=3, column=1, padx=(20, 40), pady=10)

        signup_user_re_enter_password = Label(self.signup_frame, text='Re-enter Password: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        signup_user_re_enter_password.grid(row=4, column=0, padx=20, pady=10)

        self.signup_user_re_enter_password = Entry(self.signup_frame, show='*', bg='lemon chiffon',
                                                   font=('lucida calligraphy', 14, 'bold'), relief='groove', width=25)
        self.signup_user_re_enter_password.grid(row=4, column=1, padx=(20, 40), pady=10)

        self.have_account = RoundedButton(self.signup_frame, text="Already have a account:", border_radius=4, font_size=14,
                                          fg='red', command=self.back_to_login, color='papaya whip', padx=36, pady=18)
        self.have_account.grid(row=5, column=1, padx=100, pady=(10, 10))

        # self.Login = CustomButton(self.root, text='Log in', bg='lemon chiffon', font=('Times New Roman', 18, 'bold'), padx=20)
        self.back_login = RoundedButton(self.signup_frame, text="Back to Login", border_radius=4, font_size=16, fg='black',
                                        color='cornflower blue', padx=64, pady=24, command=self.back_to_login)
        self.back_login.grid(row=6, column=0, columnspan=1, padx=10)

        self.Register = RoundedButton(self.signup_frame, text="Register", border_radius=4, font_size=18, fg='black',
                                      color='cornflower blue', padx=64, pady=24, command=self.Signup_Confirmation)
        self.Register.grid(row=6, column=1, columnspan=5, padx=10, pady=10)


    def Signup_Confirmation(self):
        self.signup_frame.forget()
        self.signup_confirm = Frame(self.root)
        self.signup_confirm.pack()

        signup_confirmation_label = Label(self.signup_confirm, text="Required Permission!", font=('arial', 18, 'bold'), fg='red')
        signup_confirmation_label.grid(row=0, column=0, columnspan=2, padx=(60, 20), pady=10)

        permission_txt = scrolledtext.ScrolledText(self.signup_confirm, font=('arial', 10, 'bold'), wrap=tk.WORD,
                                                        bd=2, fg='black', height=22, width=50)
        permission_txt.grid(row=1, column=0, columnspan=2, padx=(10, 10), pady=(10, 20))

        with open('permission.txt', 'r') as file:
            for line in file.readlines():
                permission_txt.insert(tk.END, line)

        file.close()

        self.v = tk.IntVar()
        values = {"I accept terms and conditions": 1,
                  "I don't accept terms and conditions": 2}

        i = 0
        for (text, value) in values.items():
            self.r = tk.Radiobutton(self.signup_confirm, text=text, variable=self.v, value=value, command=self.confirm_selection)
            self.r.config(fg='green', font=('arial', 12, 'bold'))
            self.r.grid(row=2 + i, column=0, padx=(40, 0))
            i += 1

        cancel_btn = Button(self.signup_confirm, text=' Back  ', font=("Times New Roman", 12, 'bold'), fg='red',
                                command=self.back_from_confirm, relief='flat')
        cancel_btn.grid(row=4, column=0, padx=(0, 150), pady=(5, 10))

        self.confirm_btn = Button(self.signup_confirm, text='Accepted', font=('Times New Roman', 12, 'bold'),
                             fg='green', relief='flat', state=DISABLED)
        self.confirm_btn.grid(row=4, column=1, padx=(0, 20), pady=(5, 10))


    def confirm_selection(self):
        if self.v.get() == 1:
            self.confirm_btn.configure(state=NORMAL, command=self.Signup)
            # self.Signup()
        else:
            print("No")

    def back_from_confirm(self):
        self.signup_confirm.forget()
        self.Signup_frame()

    def back_to_login(self):
        self.signup_frame.forget()

    def Signup(self):
        # for creating random user id ---------------------------------------
        user_name = self.signup_user_name.get()
        creating_id = s.ascii_letters + str(randint(1000000, 1000000000))
        user_id = "".join(choice(creating_id) for i in range(randint(10, 14)))
        # ------------------------------------------------------

        email = self.signup_user_email.get()
        password = self.signup_user_password.get()
        re_enter = self.signup_user_re_enter_password.get()
        if password != '' and re_enter != '' and email != '':
            if re_enter == password:
                print(email, password)
                try:
                    self.db.signin(email, password)
                    # For creating user id-------------------------------------
                    done = self.db.login(email, password)
                    self.db.save_random_id(done, user_name, user_id, email)
                    # ----------------------------------------------------------------
                    messagebox.showinfo("Welcome!", "You successfully registered")
                    self.signup_confirm.forget()
                except Exception as e:
                    print(e)
                    messagebox.showerror("Invalid", "Your email already registered!")
            else:
                messagebox.showwarning("Invalid Password", "Double check your password!")
        else:
            messagebox.showerror("Error", "Please enter value in all field!")

        self.signup_user_email.delete(0, tk.END)
        self.signup_user_password.delete(0, tk.END)
        self.signup_user_name.delete(0, tk.END)
        self.signup_user_re_enter_password.delete(0, tk.END)


# class ReTrackWindow:
#     def tracking_window(self):
#         self.root = tk.Tk()
#         self.root = tk.Tk()
#         self.root.title("Codeforces Contest Question finding Window")
#         self.root.minsize(1200, 800)
#         self.root.maxsize(1200, 800)
#         self.root.configure(bg='lemon chiffon')
#         FeatureAPP(self.root)
#         self.root.mainloop()

if __name__ == "__main__":
    Graphics()