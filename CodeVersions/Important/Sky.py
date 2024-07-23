import hashlib
import requests
from pprint import pprint as pp
import random
import time


"""
1). Here we need types of algo and types of data structure
2). Search entry text
"""


class Search:
    def __init__(self):
        self.base_url = 'https://codeforces.com/api/'
        self.api_key = 'apiKey=ee72966bd403aee419adc7e99a7a19c010e76530'
        self.secret_key = 'd7cd8464c4433e0424978dc6eeadf26478d33247'

    # ==========================================This is complete ====================================================
    def user_info(self, handle):
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/user.info?'+self.api_key+'&handles='+handle+'&time='+Time+'#'+self.secret_key
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/user.info?handles={handle}&{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == "OK":
            # ==========================Saving in file==============================================================
            with open('../validationFile/user_info.txt', 'w', encoding='utf-8') as file:
                for i in range(len(r.json()['result'])):
                    file.write("\n")
                    for key, value in r.json()['result'][i].items():
                        file.write(str(key)+": "+str(value)+"\n")

            file.close()
            # =================== Displaying from file =======================================
            with open('../validationFile/user_info.txt', 'r') as file:
                for data in file.read().splitlines():
                    data = data.split(':')
                    # print(len(data))
                    # print(data)
                    if data[0] not in ['avatar', '', 'lastOnLineTimeSeconds', 'registrationTimeSeconds', 'titlePhoto']:
                        print(data[0], ": ", data[1])
            file.close()
            # return pp(r.json())
        else:
            return r.json()['comment']
    # ===================================Now This is completed ================================================

    # ======================This is complete =========================================================================
    def user_rating(self, handle):
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/user.rating?'+self.api_key+'&handle='+handle+'&time='+Time+'#'+self.secret_key
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/user.rating?handle={handle}&{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == "OK":
            # ============================Here is Value Error(Now Solved) ===============================================
            with open('../validationFile/user_rating.txt', 'w', encoding='utf-8') as file:
                for i in range(len(r.json()['result'])):
                    file.write("\n")
                    for key, value in r.json()['result'][i].items():
                        file.write(str(key)+": "+str(value)+"\n")

            file.close()

            with open('../validationFile/user_rating.txt', 'r', encoding='utf-8') as file:
                for data in file.read().splitlines():
                    data = data.split(':')
                    # print(len(data))
                    # print(data)
                    if data[0] == '':
                        print('\n')
                    if data[0] not in ['ratingUpdateTimeSeconds', '']:
                        print(data[0], ": ", data[1])
            file.close()
            # return pp(r.json())
        else:
            return r.json()['comment']

    # ==========================This is fully completed ==========================


    # def All_rated_list(self, retire):
    #     retire = retire.lower()
    #     # ================== for time ====================================
    #     Time = str(int(time.time()))
    #     # ========================== for random six character ===========================================
    #     rand = random.randint(100000, 999999)
    #     # ============================= for hexadecimal number ===============================================
    #     hash = str(rand)+'/user.ratedList?'+self.api_key+'&includeRetired='+retire+'&time='+Time+'#'+self.secret_key
    #     hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
    #     main_url = f'https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired={retire}&{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
    #     r = requests.get(main_url)
    #     return pp(r.json())

    # =================================================Now this is Complete =============================================


    def contest_status(self, contest_id, start, end):
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/contest.standings?apiKey='+self.api_key+'&contestId='+contest_id+'&time='+Time+'#'+self.secret_key
        # ========================== Encrypted with SHA512 algorithm ==================================================
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/contest.status?contestId={contest_id}&from={start}&count={end}&apiKey{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == 'OK':
            with open('../validationFile/contest_status.txt', 'w', encoding='utf-8') as file:
                for i in range(len(r.json()['result'])):
                    file.write("\n")
                    for key, value in r.json()['result'][i].items():
                        file.write(str(key)+": "+str(value)+"\n")

            file.close()

            with open('../validationFile/contest_status.txt', 'r', encoding='utf-8') as file:
                for data in file.read().splitlines():
                    data = data.split(':')
                    # print(len(data))
                    # print(data)
                    if data[0] == '':
                        print('\n')
                    if data[0] not in ['problems', 'memoryConsumedBytes', '', 'timeConsumedMillis',
                                       'passedTestCount', 'testset', 'creationTimeSeconds',
                                       'relativeTimeSeconds', 'author', 'verdict', 'problem']:
                        print(data[0], ": ", data[1], '\n')
            file.close()
            # return pp(r.json())
        else:
            return r.json()['comment']
    # ==================================Now this is completed ============================================================

    def contest_standing(self, contestid):
        start = 1
        end = 2
        unofficial=True
        unofficial = str(unofficial).lower()
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/contest.standings?apiKey='+self.api_key+'&contestId='+contestid+'&time='+Time+'#'+self.secret_key
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/contest.standings?contestId={contestid}&from={start}&count={end}&showUnofficial={unofficial}&apiKey{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == 'OK':
            with open('../validationFile/contest_standing.txt', 'w', encoding='utf-8') as file:
                for i in range(len(r.json()['result']['problems'])):
                    file.write("\n")
                    for key, value in r.json()['result']['problems'][i].items():
                        file.write(str(key)+": "+str(value)+"\n")

            file.close()

            with open('../validationFile/contest_standing.txt', 'r', encoding='utf-8') as file:
                for data in file.read().splitlines():
                    data = data.split(':')
                    # print(len(data))
                    # print(data)
                    if data[0] == '':
                        print('\n')
                    if data[0] not in ['type', '']:
                        print(data[0], ": ", data[1])
            file.close()
            # return pp(r.json())
        else:
            print(r.json()['comment'])

    # =====================================Now this is finished =====================================================
    def contest_list(self, gym):
        gym = str(gym).lower()
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/contest.list?'+self.api_key+'&gym='+gym+'&time='+Time+'#'+self.secret_key
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/contest.list?gym={gym}&{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == 'OK':
            if gym == 'true':
                with open('../validationFile/contestlistt.txt', 'w', encoding='utf-8') as file:
                    for i in range(10):
                        file.write("\n")
                        for key, value in r.json()['result'][i].items():
                            file.write(str(key)+": "+str(value)+"\n")
                file.close()

                with open('../validationFile/contestlistt.txt', 'r', encoding='utf-8') as file:
                    for data in file.read().splitlines():
                        data = data.split(':')
                        # print(len(data))
                        # print(data)
                        if data[0] == '':
                            print('\n')
                        if data[0] not in ['frozen', '', 'durationSeconds', 'preparedBy', 'description', 'name',
                                           'startTimeSeconds', 'relativeTimeSeconds']:
                            print(data[0], ": ", data[1])
                file.close()

            elif gym == 'false':
                with open('../validationFile/contestlistf.txt', 'w', encoding='utf-8') as file:
                    for i in range(10):
                        file.write("\n")
                        for key, value in r.json()['result'][i].items():
                            file.write(str(key)+": "+str(value)+"\n")
                file.close()

                with open('../validationFile/contestlistf.txt', 'r', encoding='utf-8') as file:
                    for data in file.read().splitlines():
                        data = data.split(':')
                        # print(len(data))
                        # print(data)
                        if data[0] == '':
                            print('\n')
                        if data[0] not in ['frozen', '', 'relativeTimeSeconds',
                                           'startTimeSeconds', 'durationSeconds']:
                            print(data[0], ": ", data[1])
                file.close()
            # return pp(r.json())
        else:
            print(r.json()['comment'])
    # =====================================This is completed ============================================================


    def for_problem(self, question_tag):
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/problemset.problems?'+self.api_key+'&tags='+question_tag+'&time='+Time+'#'+self.secret_key
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/problemset.problems?tags={question_tag}&{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == 'OK':
            with open('../validationFile/problems_list.txt', 'w', encoding='utf-8') as file:
                for i in range(len(r.json()['result']['problems'])):
                    file.write("\n")
                    for key, value in r.json()['result']['problems'][i].items():
                        file.write(str(key)+": "+str(value)+"\n")

            file.close()
            # return pp(r.json()['result']['problems'])

            with open('../validationFile/problems_list.txt', 'r', encoding='utf-8') as file:
                for data in file.read().splitlines():
                    data = data.split(':')
                    # print(len(data))
                    # print(data)
                    if data[0] == '':
                        print('\n')
                    if data[0] not in ['type', '']:
                        print(data[0], ": ", data[1])
            file.close()
        else:
            return r.json()['comment']






c = Search()

# ======================================= Here we specify method name and method tag (after)==========================
# question_tag = input("Enter your question tag: ")
# c.for_problem(question_tag)

# ============================ For Contest list ===========================================
give = input("Enter true for specific region otherwise false: ")
c.contest_list(give)

# ============================================== for contest standing(Completed now) ===================================
# contest_id = input("Enter your contest id: ")
# c.contest_standing(contest_id)

# ==================================== For Contest Status(Completed now) ================================================
# contest_id = input("Enter your contest id: ")
# start = int(input("Enter your start position: "))
# end = int(input("Enter your ending point: "))
# c.contest_status(contest_id, start, end)

# ========================================== User information(Completed now) =========================================
# handle = input("Enter user handle(User info): ")
# c.user_info(handle)

# =====================================For User rating(completed)😁😁😁😁 ++++===========================================
# name = input("Enter user name(in User rating): ")
# c.user_rating(name)
# ========================================= ALL RatedList =============================================================
# retire = input("Enter true or False value(worldwide): ")
# c.All_rated_list(retire)