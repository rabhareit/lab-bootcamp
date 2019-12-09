# import Chapter4 as c

def printQNum(num):
    print("\n#######################################")
    print("# Q{}.".format(num))
    print("#######################################\n")

###########################
# 41.
###########################

import MeCab
import re
from collections import Counter

with open('./data/Cha.txt') as cha:
    doc = cha.read()


tokenizer = MeCab.Tagger()
tokenizer.parse('')

parse = tokenizer.parse(doc)
lines = parse.split('\n')
items = [re.split('[\t,]', line) for line in lines]

######################################
# [内包表記] ： リスト式内包表記
# {内包表記} : 集合(set)式内包表記
# {キー:値の内包表記} : 辞書式内法表記
# (内包表記) : ジェネレーター式内法表記
# ジェネレーター：
# 1要素を取り出そうとするたびに処理を行い,
# 要素を「ジェネレート」する (search : yield文)
# 一度for文などで要素を生成すると再度生成されなくなる.
######################################

words = [item[0] for item in items
    if (item[0] not in ('EOS', '', 't', 'ー')
        and item[1] == '名詞'
        and item[2] == '一般'
    )
]

counter = Counter(words)
with open('resultQ41.txt', 'w') as rslt:
    for word, count in counter.most_common():
        rslt.write(f"{word}: {count}\n")


###########################
# 42.
###########################

saWords = [item[0] for item in items
    if (item[0] not in ('EOS', '', 't', '——')
        and item[1] == '名詞'
        and item[2] == 'サ変接続'
    )
]

ct = Counter(saWords)
with open('resultQ42.txt', 'w') as rslt:
    for word, count in ct.most_common():
        rslt.write(f"{word}: {count}\n")


###########################
# 43.
###########################

shiftedItems = items.copy()

temp = shiftedItems[0]
shiftedItems.remove(temp)

adjAndNoun = [i[0] + s[0] for (i, s) in zip(items, shiftedItems)
    if (i[0] not in ('EOS', '', 't', '——') and i[1] == '形容詞')
        and (s[0] not in ('EOS', '', 't', '——') and s[1] == '名詞')
]

with open('resultQ43.txt', 'w') as rslt:
    for aan in adjAndNoun:
        rslt.write(aan+'\n')


###########################
# 44.
###########################
printQNum(44)

allKiindsOfWords = [ (item[0], item[1]) for item in items
    if (item[0] not in ('EOS', '', 't', 'ー'))
]

c = Counter(allKiindsOfWords)
for count, tp in enumerate(c.most_common()):
    print('%s(%s)\t:\t%d回' % (tp[0][0], tp[0][1], tp[1]))
    if count == 20:
        break


###########################
# 45.
###########################
printQNum(45)

from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plot

tn = Tokenizer()

# wordList = [token.surface for token in tn.tokenize(doc)]

# for w, f in frec.items():
#     print(w+':'+str(f))

# plot.hist(wordList)
# plot.show()


###########################
# 46.
###########################
printQNum(46)

xAxis = []
yAxis = []

frec = {}
# for token in tn.tokenize(doc):
#     frec.setdefault(token.surface, 0)
#     frec[token.surface] += 1

# for w, f in frec.items():
#     xAxis.append(w)
#     yAxis.append(f)

# plot.scatter(xAxis,yAxis)
# plot.xlabel('word')
# plot.ylabel('frec')
# plot.show()


###########################
# 47.
###########################
printQNum(47)

doc = re.sub(r'[「」｜一]', '', doc)
sentences = re.split('[\n。]', doc)

for s in sentences:
    print(s.strip())
print(len(sentences))


###########################
# 48.
###########################
printQNum(48)

sentenceFrequency = {}

for w in words:
    count = 0
    for sentence in sentences:
        if w in sentence:
            count += 1
    sentenceFrequency[w] = count

for w, f in sentenceFrequency.items():
    print('%s:%s回' % (w, str(f)))