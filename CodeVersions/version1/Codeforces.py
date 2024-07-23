import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from db import SignInAndSignUp
from hello import RoundedButton
from tree import Tree



class Graphics:

    def __init__(self):
        self.db = SignInAndSignUp()
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

        self.logo_label2.place(x=240, y=125)
        self.logo_label.place(x=600, y=125)

        title = Label(self.root, text="Codeforces Coding Contest", font=('Times New Roman', 48, 'bold'), bg='lemon chiffon', fg='red4')
        title.place(x=200, y=20)

        self.learn_about = Button(self.root, text="Learn About", font=('Times New Roman', 8, 'bold'), bg='lemon chiffon', fg='red4', relief='flat')
        self.learn_about.place(x=900, y=100)

        self.learn_policy = Button(self.root, text="Privacy Policy", font=('Times New Roman', 8, 'bold'), bg='lemon chiffon', fg='red4', relief='flat')
        self.learn_policy.place(x=20, y=750)

        login_credential_label = Label(self.root, text="Log in credential: ", bg='lemon chiffon', font=("Times New Roman", 32, 'bold'), fg='SeaGreen1')
        login_credential_label.place(x=430, y=420)

        name_label = Label(self.root, text="Email : ", bg='lemon chiffon', font=("lucida calligraphy", 22, 'bold'))
        name_label.place(x=240, y=500)

        self.user_email = Entry(self.root, bg='lemon chiffon', font=('lucida calligraphy', 16, 'bold'), width=30)
        self.user_email.place(x=480, y=500)

        name_label = Label(self.root, text="Password : ", bg='lemon chiffon', font=("lucida calligraphy", 22, 'bold'))
        name_label.place(x=240, y=560)

        self.user_password = Entry(self.root, show='*', bg='lemon chiffon',  font=('lucida calligraphy', 16, 'bold'), width=30)
        self.user_password.place(x=480, y=560)

        self.forgot_password = RoundedButton(self.root, text="Forgot password", border_radius=4, font_size=14, fg='red', command=self.forgot_password, color='lemon chiffon', padx=36, pady=18)
        self.forgot_password.place(x=800, y=610)

        # self.Login = CustomButton(self.root, text='Log in', bg='lemon chiffon', font=('Times New Roman', 18, 'bold'), padx=20)
        self.Login = RoundedButton(self.root, text="Log in", border_radius=4, font_size=20, command=self.Login, fg='black', color='cornflower blue', padx=64, pady=24)
        self.Login.place(x=800, y=680)

        self.SignUp = RoundedButton(self.root, text="Sign Up", border_radius=4, font_size=20, command=self.Signup_frame, fg='black', color='cornflower blue', padx=64, pady=24)
        self.SignUp.place(x=400, y=680)

        notification_label = Label(self.root, text='Get notification: ', fg='ivory3', bg='lemon chiffon', font=('lucida calligraphy', 10, 'bold'))
        notification_label.place(x=820, y=760)

        self.notification_email = Entry(self.root,  bg='lemon chiffon', font=('lucida calligraphy', 8, 'normal'), width=24)
        self.notification_email.place(x=960, y=760)

        self.forward_logo = Image.open('images/right-arrow.png')
        self.forward_logo = ImageTk.PhotoImage(self.forward_logo)
        self.forward_label = Button(self.root, image=self.forward_logo, bg='lemon chiffon', relief='flat', fg='lemon chiffon')

        self.forward_label.image = self.logo

        self.forward_label.place(x=1160, y=760)



        self.root.mainloop()

    def back_to_login_from_password(self):
        self.password_frame.forget()

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

        self.password_back_toLogin = RoundedButton(self.password_frame, text="Login page", border_radius=4, font_size=16, fg='black', color='cornflower blue', padx=64, pady=24, command=self.back_to_login_from_password)
        self.password_back_toLogin.grid(row=2, column=1, columnspan=2, padx=10, pady=20)

        self.Register = RoundedButton(self.password_frame, text="Enter ", border_radius=4, font_size=18, fg='black', color='cornflower blue', padx=64, pady=24, command=self.access_password)
        self.Register.grid(row=2, column=2, columnspan=3, padx=40, pady=20)

        get_password = Label(self.password_frame, text="Your Password: ", font=('lucida calligraphy', 14, 'bold'), bg='gray63')
        get_password.grid(row=3, column=0, pady=10, padx=10)



    def Login(self):
        email = self.user_email.get()
        password = self.user_password.get()
        print(email, password)
        # Window(self.root)
        # Tree(self.root)
        try:
            self.db.login(email, password)
            messagebox.showinfo("Successful", "Successfully logged in")
            # self.root.forget(self.root)
            self.user_email.delete(0, tk.END)
            self.user_password.delete(0, tk.END)
            # Window(self.root)
            Tree(self.root)
        except:
            messagebox.showerror("Invalid", "Your enter credential is invalid!")

        self.user_email.delete(0, tk.END)
        self.user_password.delete(0, tk.END)




    def Signup_frame(self):
        self.signup_frame = Frame(self.root, bg='papaya whip')
        self.signup_frame.pack()

        signup_frame_label = Label(self.signup_frame, text="Sign Up Page", font=('arial', 24, 'bold'), fg='chocolate3', bg='papaya whip')
        signup_frame_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        user_name = Label(self.signup_frame, text='Name: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        user_name.grid(row=1, column=0, padx=20)

        self.signup_user_name = Entry(self.signup_frame, bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), width=25)
        self.signup_user_name.grid(row=1, column=1, padx=20, pady=10)

        signup_user_email = Label(self.signup_frame, text='Email: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        signup_user_email.grid(row=2, column=0, padx=20, pady=10)

        self.signup_user_email = Entry(self.signup_frame, bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), relief='groove', width=25)
        self.signup_user_email.grid(row=2, column=1, padx=20, pady=10)

        signup_user_password = Label(self.signup_frame, text='Enter Password: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        signup_user_password.grid(row=3, column=0, padx=20, pady=10)

        self.signup_user_password = Entry(self.signup_frame, show='*', bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), relief='groove', width=25)
        self.signup_user_password.grid(row=3, column=1, padx=20, pady=10)

        signup_user_re_enter_password = Label(self.signup_frame, text='Re-enter Password: ', font=("lucida calligraphy", 18, 'bold'), bg='papaya whip')
        signup_user_re_enter_password.grid(row=4, column=0, padx=20, pady=10)

        self.signup_user_re_enter_password = Entry(self.signup_frame, show='*', bg='lemon chiffon', font=('lucida calligraphy', 14, 'bold'), relief='groove', width=25)
        self.signup_user_re_enter_password.grid(row=4, column=1, padx=20, pady=10)

        self.have_account = RoundedButton(self.signup_frame, text="Already have a account:", border_radius=4, font_size=14,
                                          fg='red', command=self.back_to_login, color='papaya whip', padx=36, pady=18)
        self.have_account.grid(row=5, column=1, padx=100)

        # self.Login = CustomButton(self.root, text='Log in', bg='lemon chiffon', font=('Times New Roman', 18, 'bold'), padx=20)
        self.back_login = RoundedButton(self.signup_frame, text="Back to Login", border_radius=4, font_size=16, fg='black', color='cornflower blue', padx=64, pady=24, command=self.back_to_login)
        self.back_login.grid(row=6, column=0, columnspan=1, padx=10)

        self.Register = RoundedButton(self.signup_frame, text="Register", border_radius=4, font_size=18, fg='black', color='cornflower blue', padx=64, pady=24, command=self.Signup)
        self.Register.grid(row=6, column=1, columnspan=2, padx=10, pady=10)



    def back_to_login(self):
        self.signup_frame.forget()

    def Signup(self):
        email = self.signup_user_email.get()
        password = self.signup_user_password.get()
        re_enter = self.signup_user_re_enter_password.get()
        if password == '' or re_enter == '' or email == '':
            if re_enter == password:
                print(email, password)
                try:
                    self.db.signin(email, password)
                    messagebox.showinfo("Welcome!", "You successfully registered")
                    self.signup_frame.forget()
                except Exception as e:
                    print(e.__cause__)
                    messagebox.showerror("Invalid", "Your email already registered!")
            else:
                messagebox.showwarning("Invalid Password", "Double check your password!")
        else:
            messagebox.showerror("Error", "Please enter value in field!")

        self.signup_user_email.delete(0, tk.END)
        self.signup_user_password.delete(0, tk.END)
        self.signup_user_name.delete(0, tk.END)
        self.signup_user_re_enter_password.delete(0, tk.END)


    def new_window(self):
        self.window = Frame(self.root, bg="gray")
        self.window.pack()
        self.root.forget(self.root)

        self.entry = Entry(self.window, font=("Times New ROman", 24, 'bold'))
        self.entry.grid(row=0, column=0)



if __name__ == "__main__":
    Graphics()