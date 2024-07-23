import requests
from pprint import pprint as pp
import time
import random
import hashlib
import json
import Secerets

class Search:
    def __init__(self):
        self.base_url = 'https://codeforces.com/api/'
        self.api_key = Secerets.API_KEY
        self.secret_key = Secerets.SECRET_KEY

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
            for i in range(len(r.json()['result'])):
                for key, value in r.json()['result'][i].items():
                    if key not in ['avatar', '', 'lastOnLineTimeSeconds', 'registrationTimeSeconds', 'titlePhoto']:
                        print(key, ": ", value)
        else:
            return r.json()['comment']


    def contest_status(self, contest_id, end):  # for finding popular cp programming language
        start = 1
        # ================== for time ====================================
        Time = str(int(time.time()))
        # ========================== for random six character ===========================================
        rand = random.randint(100000, 999999)
        # ============================= for hexadecimal number ===============================================
        hash = str(rand)+'/contest.standings?apiKey='+self.api_key+'&contestId='+contest_id+'&time='+Time+'#'+self.secret_key
        hash_code = str(hashlib.sha512(hash.encode("utf-8")).hexdigest())
        main_url = f'https://codeforces.com/api/contest.status?contestId={contest_id}&from={start}&count={end}&apiKey{self.api_key}&time={Time}&apiSig={rand}{hash_code}'
        r = requests.get(main_url)
        if r.json()['status'] == 'OK':
            for i in range(len(r.json()['result'])):
                print()
                for key, value in r.json()['result'][i].items():
                    if key not in ['problems', 'memoryConsumedBytes', '', 'timeConsumedMillis',
                                       'passedTestCount', 'testset', 'creationTimeSeconds',
                                       'relativeTimeSeconds', 'author', 'verdict', 'problem']:
                        print(key, ": ", value)
        else:
            return r.json()['comment']


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
            for i in range(len(r.json()['result'])):
                print()
                for key, value in r.json()['result'][i].items():
                    if key not in ['ratingUpdateTimeSeconds', '']:
                        print(key, ": ", value)
        else:
            return r.json()['comment']

    # ====================================== Contest Standing =========================================================
    def contest_standing(self, contestid):
        start = 1
        end = 2
        unofficial = True
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
            for i in range(len(r.json()['result']['problems'])):
                print()
                for key, value in r.json()['result']['problems'][i].items():
                    if key not in ['type', '']:
                        print(key, ": ", value)
        else:
            return r.json()['comment']


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
                for i in range(len(r.json()['result'])):
                    print()
                    for key, value in r.json()['result'][i].items():
                        if key not in ['frozen', '', 'durationSeconds', 'preparedBy', 'description', 'name',
                                           'startTimeSeconds', 'relativeTimeSeconds']:
                            print(key, ": ", value)

            if gym == 'false':
                for i in range(len(r.json()['result'])):
                    print()
                    for key, value in r.json()['result'][i].items():
                        if key not in ['frozen', '', 'durationSeconds', 'preparedBy', 'description', 'name',
                                           'startTimeSeconds', 'relativeTimeSeconds']:
                            print(key, ": ", value)
        else:
            return r.json()['comment']


    def for_problem(self, question_tag):
        problem_list = []
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
            r = r.json()
            dic = dict()
            l1 = []
            d = []

            for i in range(len(r['result']['problems'])):
                if r['result']['problems'][i]['index'] not in d:
                    d.append(r['result']['problems'][i]['index'])
                    dic[r['result']['problems'][i]['index']] = list()

                if r['result']['problems'][i]['index'] not in list(dic.keys()):
                    l1.append([r['result']['problems'][i]['name'], r['result']['problems'][i]['contestId']])
                    dic[r['result']['problems'][i]['index']] = l1
                else:
                    s = dic[r['result']['problems'][i]['index']]
                    s.append([r['result']['problems'][i]['name'], r['result']['problems'][i]['contestId']])
                    dic[r['result']['problems'][i]['index']] = s
                l1.clear()
            # return '\n'.join(dic['A'])
            return dic











            # for i in range(len(r.json()['result']['problems'])):
            #     # print()
            #     l = {}
            #     for key, value in r.json()['result']['problems'][i].items():
            #         if key not in ['type', '']:
            #             l[key] = value
            #             # print(key, ": ", value)
            #     problem_list.append(l)
            #
            # # for i in range(100):
            # #     print(problem_list)
            # pp(problem_list)
        else:
            return r.json()['comment']

    # =========================== I faced dome problem in this ========================================================
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
    #     pp(r.json())

    # =================================================Now this is Complete =============================================



# ==========================================================================================================================
c = Search()
# ==================================================================================================================
# handle = input("Enter user handle name: ")
# c.user_info(handle)

# =======================================================================================================================
# contest_id = input("Enter your contest id: ")
# end = int(input("Enter your ending point: "))
# c.contest_status(contest_id, end)

# =====================================For User rating(completed)😁😁😁😁 ++++===========================================
# name = input("Enter user name(in User rating): ")
# c.user_rating(name)

# ============================================== for contest standing(Completed now) ===================================
# contest_id = input("Enter your contest id: ")
# c.contest_standing(contest_id)

# ============================ For Contest list ===========================================
# give = input("Enter true for specific region otherwise false: ")
# c.contest_list(give)

# ======================================= Question tag ==========================================================
# question_tag = input("Enter your question tag: ")
# c.for_problem(question_tag)

# ========================================= ALL RatedList =============================================================
# retire = input("Enter true or False value(worldwide): ")
# c.All_rated_list(retire)