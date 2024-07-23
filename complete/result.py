import requests
import time
import random
import hashlib
import Secerets

class Search:
    def __init__(self):
        self.base_url = 'https://codeforces.com/api/'
        self.api_key = Secerets.API_KEY
        self.secret_key = Secerets.SECRET_KEY

    # ===========================This is complete(for finding user information from codeforces) ==============================
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
            l = []
            for i in range(len(r.json()['result'])):
                for key, value in r.json()['result'][i].items():
                    if key in ['lastName', 'rating', 'friendOfCount', 'handle', 'firstName', 'contribution',
                               'organization', 'rank', 'maxRating', 'maxRank']:
                        # print(key, ": ", value)
                        l.append([str(key), str(value)])
        else:
            return r.json()['comment'].split(': ')
        return l

    # ======================================== for finding popular cp programming language =================================
    def contest_status(self, contest_id, end):
        d = dict()
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
                for key, value in r.json()['result'][i].items():
                    # if key not in ['problems', 'memoryConsumedBytes', '', 'timeConsumedMillis',
                    #                    'passedTestCount', 'testset', 'creationTimeSeconds',
                    #                    'relativeTimeSeconds', 'author', 'verdict', 'problem',
                    #                     'contestId', 'id']:
                    #     print(key, ": ", value)
                    if key == 'programmingLanguage':
                        if 'C++' in value:
                            value = 'C++'
                        elif 'Py' in value:
                            value = 'Python'
                        elif 'Java' in value:
                            value = 'Java'
                        else:
                            value = 'Others'

                        if value not in list(d.keys()):
                            d[value] = 1
                        else:
                            d[value] += 1
        else:
            return r.json()['comment']
        return d


    # ======================This is complete =========================================================================

    # ================================= for finding user rating and user contest list ================================
    def user_rating(self, handle):
        l_m = []
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
                l = []
                for key, value in r.json()['result'][i].items():
                    if key in ['contestId', 'contestName', 'rank', 'oldRating', 'newRating']:
                        l.append([key, value])
                        # print(str(key)+" : "+str(value))
                l_m.append(l)
        else:
            return r.json()['comment']
        return l_m

    # =========================== Contest Standing(And also for contest all question) ========================================
    def contest_standing(self, contestid):
        l = []
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
                l1 = []
                for key, value in r.json()['result']['problems'][i].items():
                    # if key not in ['type', '']:
                    #     print(key, ": ", value)
                    if key in ['contestId', "index", 'name', 'rating', 'tags']:
                        l1.append([key, value])
                l.append(l1)
            return l
        else:
            return r.json()['comment']

    # =====================================Now this is finished =====================================================

    # ========================================== for finding all contest list(international or codeforces)============
    def contest_list(self, gym):
        l = []
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
                    l1 = []
                    for key, value in r.json()['result'][i].items():
                        if key in ['name', 'type', 'phase']:
                            l1.append([key, value])
                    l.append(l1)

            if gym == 'false':
                for i in range(len(r.json()['result'])):
                    l1 = []
                    for key, value in r.json()['result'][i].items():
                        if key in ['id', 'name', 'type', 'phase']:
                            l1.append([key, value])

                    l.append(l1)
        else:
            return r.json()['comment']
        return l

    # ================================ for finding all problem list in any topic ======================================
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

            # ================================================================================================


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



    """
    # ====================================== For finding user programming language ==============================================
        #
        # url = 'https://codeforces.com/api/user.status?handle=Bharat_Chandravanshi&from=1&count=100'
        #
        # r = requests.get(url)
        # r = r.json()
        #
        # d = dict()
        # for i in range(len(r['result'])):
        #     print(r['result'][i]['programmingLanguage'])
        #     if r['result'][i]['programmingLanguage'] not in list(d.keys()):
        #         d[r['result'][i]['programmingLanguage']] = 1
        #     else:
        #         d[r['result'][i]['programmingLanguage']] += 1
        #
        # print(d)
        
        # ==============================================================================================================
    """


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
# print(c.contest_standing(contest_id))

# ============================ For Contest list ===========================================
# give = input("Enter true for specific region otherwise false: ")
# c.contest_list(give)

# ======================================= Question tag ==========================================================
# question_tag = input("Enter your question tag: ")
# c.for_problem(question_tag)

# ========================================= ALL RatedList =============================================================
# retire = input("Enter true or False value(worldwide): ")
# c.All_rated_list(retire)