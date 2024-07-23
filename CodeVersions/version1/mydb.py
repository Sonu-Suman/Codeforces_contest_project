import mysql.connector
import datetime


class Command:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', passwd='1234', user='root', database='customers')

        self.mycursor = self.conn.cursor()

    def execute(self, contest_id, url, Questions):
        date = datetime.date.today()
        Time = datetime.datetime.now().strftime("%I:%M")

        self.mycursor.execute(f"INSERT INTO contest(contest_name, url_tag, Questions, At_date, At_time) "
                              f"VALUES('{contest_id}', '{url}', {Questions}, '{date}', '{Time}')")

        print("Executed Successfully")
        self.mycursor.close()


# date = datetime.date.today()
# # strTime = datetime.datetime.now().strftime("%I:%M %p")
# print(date)
# print(strTime)

c = Command()
contest_id = input("Enter your contest id: ")
url_link = input("Enter your url : ")
Question = int(input("Enter your total number of Questions: "))
c.execute(contest_id, url_link, Question)