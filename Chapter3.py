
def printQNum(num):
    print("\n#######################################")
    print("# {}.".format(num))
    print("#######################################\n")

###############################################################
# 21.
###############################################################

printQNum(21)

import datetime

def str2Datetime(s):
    return datetime.datetime.strptime(s,"%Y年%m月%d日%H時%M分%S秒")


print(datetime.datetime.strptime("2017年12月8日 9時23分16秒", "%Y年%m月%d日 %H時%M分%S秒"))


###############################################################
# 22.
###############################################################

printQNum(22)

import re

# どれかのパラメータがない場合の分岐
# s = %H%M%S -> 2019-01-01 + s - 2019-01-01

def str2Datetime(s):
    return datetime.datetime.strptime(s,"%Y年%m月%d日%H時%M分%S秒")


def str2TimeDelta(s):
    dlt = {}
    s = re.sub(r"([0-9])日と", r"\1,日-",s)
    s = re.sub(r"([0-9])時間", r"\1,時間-",s)
    s = re.sub(r"([0-9])分", r"\1,分-",s)
    s = re.sub(r"([0-9])秒", r"\1,秒",s)
    for temp in s.split("-"):
        l = temp.split(",")
        dlt[l[1]] = int(l[0])
    return datetime.timedelta(days=dlt["日"],hours=dlt["時間"], minutes=dlt["分"], seconds=dlt["秒"])


n = "2017年12月8日9時23分16秒"
back = "12371日と23時間23分16秒"

mac = str2Datetime(n) - str2TimeDelta(back)
print(datetime.datetime.strftime(mac, "%Y年%m月%d日"))


###############################################################
# 23.
###############################################################

printQNum(23)

import json

def file2Json(title):
    k = open(title)
    return json.load(k)

json_kaken = file2Json("./data/kaken2017/17K17832.json")
# principal_investigator[name]
# project_name 
# budget
print("{}".format(json.dumps(json_kaken, indent=4)))
print(json_kaken["principal_investigator"]["name"])
print(json_kaken["project_name"])
print("¥"+"{:,}".format(json_kaken["budget"]))


###############################################################
# 24.
###############################################################
printQNum(24)


import os

fileList = os.listdir("./data/kaken2017/")
budgetDict = {}
for fileName in fileList:
    k = file2Json("./data/kaken2017/"+fileName)
    affiliation = k["principal_investigator"]["affiliation"]
    budgetDict.setdefault(affiliation,0)
    budgetDict[affiliation] += int(k["budget"])
# print(budgetDict)
budgetDict_sorted = sorted(budgetDict.items(), key=lambda x: (x[1], x[0]), reverse=True)
# print(budgetDict_sorted)
n = 0
for id, budget in budgetDict_sorted:
    if n < 20:
        print(id)
        print("¥"+"{:,}".format(budget))
        n += 1
    else:
        break


###############################################################
# 25.
###############################################################
printQNum(25)


from pyquery import PyQuery as pq

# with open('./data/big-cities-pageviews.xml') as cities:
#     content = pq(cities)


###############################################################
# 27.
###############################################################
printQNum(27)

with open('./data/hamamatsu.txt') as ham:
    hamamatsu = ham.read()
    print(re.findall(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', hamamatsu))


###############################################################
# 28.
###############################################################
    printQNum(28)

    categories = re.findall(r'Category:[^\|\*\]\[]*',hamamatsu)
    for category in categories:
        print(category.replace('Category:', ''))


###############################################################
# 29.
###############################################################
    printQNum(29)
    highlow = re.findall(r'[^\|]?....high\sC\s=\s....?|[^\|]?....low\sC\s=\s....?', hamamatsu)
    with open('./data/hamamatsuResult.tsv', 'w') as wr:
        wr.write('type\tmonth\ttemperature\n')
        for s in highlow:
            sp = s.split()
            if sp[0] == 'year':
                continue
            elif sp[1] == 'high':
                wr.write('最高\t'+sp[0]+'\t'+sp[4]+'\n')
            elif sp[1] == 'low':
                wr.write('最低\t'+sp[0]+'\t'+sp[4]+'\n')
            else:
                print(sp[1])


###############################################################
# 30.
###############################################################
printQNum(30)

sen = 'Herzlichen Glückwunsch zum Erreichen der zwanzig Aufgaben! Nächsten Aufgaben sind praktischer für Ihre Forschungsaktivitäten. Habe Spaß!'.lower()

with open('./data/dictionary.csv') as dic:
    for c in dic:
        cor = c.split(',')
        sen = sen.replace(cor[0], cor[1])

    print(sen.replace('\n',''))