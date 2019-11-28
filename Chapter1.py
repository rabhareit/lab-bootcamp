import collections


###############################################################
# 1.
# 1からNまでの整数和を求める関数sumを作成せよ。
#
###############################################################
def sum(num):
    result = 0
    for n in range(1, num + 1):
        result += n
    return result


###############################################################
# 2.
# 97の正の平方根をmathモジュールを使わずに
# 力づくで求めよ。なお、求める解は、その二乗と
# 97との差が0.001以内に収まるように求めよ。
#
###############################################################
print(97 ** 0.5)

###############################################################
# 3.
# 変数x, yを受け取り「xの価格はy円（税込）」という
# 文字列を返す関数を作成せよ
# （言語処理100本ノック2015 Q.7改題）。
#
###############################################################

def printXprice(x, y):
    return '{0}の値段は{1}円(税込)'.format(x, y)

###############################################################
# 4.
# 文字列"Rats live on no evil star"の
# 文字を逆に並べた文字列を表示せよ。
#
###############################################################
print("Rats live on no evil star"[::-1])

###############################################################
# 5.
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し、各単語の（アルファベットの）
# 文字数を先頭から出現順に並べたリストを作成せよ
# （言語処理100本ノック 2015 Q.3より）。
#
###############################################################

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
lists = str.split()
ans = ""
ans = lists.sort(key=len)
result = lists.join()
print(ans)

###############################################################
# 6.
# 任意の文字列に含まれる文字の出現頻度を求める
# 関数count_charを作成せよ。なお、返り値は、キーが文字、
# 値が出現頻度に対応した辞書オブジェクト形式にせよ
# （例："I have a pen" -> 
# {'I': 1, ' ': 3, 'h': 1, 'a': 2, 'v': 1, 'e': 2, 'p': 1, 'n': 1}）。
#
# （ヒント）
# ある文字列sが与えられたとき、list(s)はsを1文字ずつ分解したリストを返す。
#
###############################################################
print("\n" + "Q6." + "\n")


def count_char(s):
    listring = list(s)
    return collections.Counter(listring)


def count_char_new(s):
    l = list(s)
    freq = {}
    for ch in l:
        freq.setdefault(ch, 0)
        freq[ch] += 1
    return freq


print(count_char("aaabb"))

###################################################
# 7,
# data/introduction_assignmentディレクトリにある
# population-abstract2010-2015.csvを読み込み、
# その内容を一行ずつ表示せよ。
#
# （留意事項）
# 当該CSVファイルは「平成27年度国勢調査の
# 総人口・世帯数データ」の一部を抽出・加工したものです。
#
###################################################
print("\n" + "Q7." + "\n")
with open("./data/population-abstract2010-2015.csv")as pop:
    for line in pop:
        print(line)
#    while True:
#        line = pop.readline()
#        if not line:
#            break
#        print(line)
# print(population)


###################################################
# 8.
# Q7で用いたCSVファイルは、下記項目からなる人口統計データである。
# 当該CSVデータから、都道府県名をキー、2015年調査時と2010年調査時の
# 人口増減数を値とする辞書オブジェクトpopulationを作成せよ。
#
# id
# 都道府県名（area_name）
# 2015年度調査時の人口（population2015）
# 2010年度調査時の人口（population2010）
# 2015年度調査時の世帯数（household2015）
# 2015年度調査時の世帯数（household2010）
#
###################################################
print("\n" + "Q8." + "\n")
population = {}
with open("./data/population-abstract2010-2015.csv") as popu:
    header = popu.readline()
    while True:
        l = popu.readline()
        if not l:
            break
        column = l.split(",")
        population[column[1]] = int(column[2]) - int(column[3])
print(population)

###################################################
# 9.
# Q7で用いたCSVファイルを利用して、
# 2010年度調査から2015年度調査の間で人口増減数が大きかった
# 都道府県を増減数付で上位10件を表示せよ。
# 表示は「30位: 京都府（25739人）」という形式で行うこと。
#
###################################################
print("\n" + "Q9." + "\n")
population_sorted = sorted(population.items(), key=lambda x: abs(x[1]), reverse=True)

for count, t in enumerate(population_sorted):
    if count == 10:
        break
    print(str(count + 1) + "位:" + t[0] + "（" + str(abs(t[1])) + "人）")

###################################################
# 10.
# Q7,Q8,Q9で用いた2015年度の国勢調査データを用いて、
# 都道府県名、各都道府県の2010年度調査から2015年度調査の間で
# 人口増減数について、TSV形式でファイル保存せよ。
###################################################
print("\n" + "Q10." + "\n")
with open("./data/population-abstract2010-2015.tsv", "w") as out:
    for key, value in population.items():
        out.write(key + "\t" + str(value) + "\n")
    print("DONE!!")
