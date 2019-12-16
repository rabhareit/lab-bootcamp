# import Chapter4 as c

def printQNum(num):
    print("\n#######################################")
    print("# Q{}.".format(num))
    print("#######################################\n")

###########################
# 41.
###########################
printQNum(41)

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

nouns = [item[0] for item in items
    if (item[0] not in ('EOS', '', 't', 'ー')
        and item[1] == '名詞'
        and item[2] == '一般'
    )
]

counter = Counter(nouns)
sortedNounsFreq = counter.most_common()
nounsFreqDic = {}
with open('resultQ41.txt', 'w') as rslt:
    for word, count in sortedNounsFreq:
        nounsFreqDic[word] = count
        rslt.write(f"{word}: {count}\n")


###########################
# 42.
###########################
printQNum(42)
saNouns = [item[0] for item in items
    if (item[0] not in ('EOS', '', 't', '——')
        and item[1] == '名詞'
        and item[2] == 'サ変接続'
    )
]

ct = Counter(saNouns)
saNounsFreq = ct.most_common()
saNounsFreqDic = {}
with open('resultQ42.txt', 'w') as rslt:
    for word, count in saNounsFreq:
        saNounsFreqDic[word] = count
        rslt.write(f"{word}: {count}\n")


###########################
# 43.
###########################
printQNum(43)
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

from janome.tokenizer import Tokenizer
tn = Tokenizer()

termPosFreqDic = {}
for token in tn.tokenize(doc):
    pos = token.part_of_speech.split(',')[0]
    termPosFreqDic.setdefault((token.base_form, pos), 0)
    termPosFreqDic[(token.base_form, pos)] += 1

sortedTermFreq = sorted(termPosFreqDic.items(), key=lambda x:x[1], reverse=True)

for count, tp in enumerate(sortedTermFreq):
    print('%s(%s)\t:\t%d回' % (tp[0][0], tp[0][1], tp[1]))
    if count == 20:
        break


###########################
# 45.
###########################
printQNum(45)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot

def plotNounFreqHist():
    plot.hist(nounsFreqDic.values(), bins=50)
    plot.savefig('Q45.png')

# plotNounFreqHist()


###########################
# 46.
###########################
printQNum(46)

xAxis = []
yAxis = []

for count, f in enumerate(sortedTermFreq):
    xAxis.append(count+1)
    yAxis.append(f[1])

def plotRankAndFreqScater():
    plot.scatter(xAxis,yAxis)
    plot.xscale('log')
    plot.yscale('log')
    plot.xlabel('Rank')
    plot.ylabel('freq')
    plot.savefig('Q46.png')

# plotRankAndFreqScater()


###########################
# 47.
###########################
printQNum(47)

sentences = []
text = re.sub(r'[「」｜一\n]', '', doc)
for sent in re.split('[。！]', text):
    if sent != '':
        sentences.append(sent.strip())

print(len(sentences))


###########################
# 48.
###########################
printQNum(48)

sentenceFrequency = {}
tempNouns = []

for sentence in sentences:
    tokens = tn.tokenize(sentence)
    tempNouns.clear()

    for token in tokens:
        if '名詞' in token.part_of_speech:
            tempNouns.append(token.base_form)

    for w in nouns:
        if w in tempNouns:
            sentenceFrequency.setdefault(w,0)
            sentenceFrequency[w] += 1

sortedSF = sorted(sentenceFrequency.items(), key=lambda x:x[1], reverse=True)

with open('resultQ48.txt', 'w') as rslt:
    for l in sortedSF:
        rslt.write('%s:%s回\n' % (l[0], str(l[1])))


###########################
# 49.
###########################
printQNum(49)

def getCooccurredTerms(term):
    cooccurrence = {}
    for sentence in sentences:
        tokenList = tn.tokenize(sentence)

        chasen = False
        for token in tokenList:
            if term in token.base_form:
                chasen = True
        if chasen:
            for token in tokenList:
                pos = token.part_of_speech.split(',')
                if pos[0] == '名詞' and pos[1] in ('一般', '固有名詞', 'サ変接続', '形容動詞語幹') and term not in token.base_form:
                    cooccurrence.setdefault(token.surface, 0)
                    cooccurrence[token.surface] += 1

    return sorted(cooccurrence.items(), key=lambda x:x[1], reverse=True)

with open('resultQ49.txt', 'w') as rslt:
    for s in getCooccurredTerms('茶'):
        rslt.write('%s\t:\t%s回\n' % (s[0], s[1]))


###########################
# 50.
###########################
printQNum(50)

import itertools
import math

def sentenceFreq(term):
    count = 0
    for sentence in sentences:
        tokenList = tn.tokenize(sentence)
        nouns = [token.base_form for token in tokenList if "名詞" in token.part_of_speech]
        for noun in nouns:
            if term == noun:
                count += 1
    return count


def cooccurrence(term1, term2):
    term1 = "茶"
    n = len(sentences)

    i = 0
    for sentence in sentences:
        if term1 in sentence and term2 in sentence:
            i += 1
    
    freq1 = sentenceFreq(term1)
    freq2 = sentenceFreq(term2)

    return math.log((n*i)/(freq1*freq2))


targets = [sf[0] for sf in sortedSF if sf[1] > 2]

for terms in itertools.permutations(targets, r=2):
    print(cooccurrence(terms[0], terms[1]))