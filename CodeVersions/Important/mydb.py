import mysql.connector
import smtplib



class Command:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', passwd='1234', user='root', database='customers')
        self.mycursor = self.conn.cursor()


    def execute(self, email):
        self.mycursor.execute(f"INSERT INTO SaveEmail(email) VALUES('{email}')")
        self.conn.commit()

        content = "Hello\n\nHi I'm Aparajita Suman.\nThank you for subscribing us.\nThis email is a confirmation email from Codeforces Problem Application."
        self.send_Email(f'{email}', content)

        self.mycursor.close()
        print("Executed Successfully")


    def send_Email(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('sk8282544@gmail.com', f'{Secerets.EMAIL_PASSWORD}')
        server.sendmail('sk8282544@gmail.com', to, content)
        server.close()




# date = datetime.date.today()
# # strTime = datetime.datetime.now().strftime("%I:%M %p")

# c = Command()
# contest_id = input("Enter your contest id: ")
# url_link = input("Enter your url : ")
# Question = int(input("Enter your total number of Questions: "))
# c.execute(contest_id, url_link, Question)
