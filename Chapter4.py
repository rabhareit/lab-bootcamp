def printQNum(num):
    print("\n###########################")
    print("# Q{}.".format(num))
    print("###########################\n")

import re
###########################
# 31.
###########################

printQNum(31)


import requests
# https://stocks.finance.yahoo.co.jp/stocks/qi/?ids=9050
content = requests.get('https://stocks.finance.yahoo.co.jp/stocks/qi/?ids=9050')
print(content.text)


###########################
# 32.
###########################

printQNum(32)


from pyquery import PyQuery as pq

query = pq(content.text, parser='html')

code = query('.yjM'+'.center')("a[href *= '/stocks/detail/?code=']")
price = query('.yjM'+'.price')
for code, price in zip(code.text().split(), price.text().split()):
    print('({0},{1})'.format(code,price))



###########################
# 33.
###########################

printQNum(33)

print(query('.listNext').children().attr('href'))
# https://stocks.finance.yahoo.co.jp/stocks/qi/?ids=9050&p=2


###########################
# 34.
###########################

printQNum(34)

def getPrice():
    pair = {}
    BASE_URL = 'https://stocks.finance.yahoo.co.jp'
    target = 'https://stocks.finance.yahoo.co.jp/stocks/qi/?ids=9050'
    while(BASE_URL != target):
        print(target)
        cont = requests.get(target)
        lquery = pq(cont.text, parser='html')

        code = lquery('.yjM'+'.center')("a[href *= '/stocks/detail/?code=']")
        price = lquery('.yjM'+'.price')
        for code, price in zip(code.text().split(), price.text().split()):
            if price == '---':
                pair[code] = float(0)
            else:
                pair[code] = float(price.replace(',', ''))
        suffix = lquery('.listNext').children().attr('href')
        if suffix == None:
            break
        target = BASE_URL + suffix

    pair_sorted = sorted(pair.items(), reverse=True, key=lambda x:x[1])
        
    for p in pair_sorted:
        print(p)

# getPrice()

###########################
# 35.
###########################

printQNum(35)

BASE_URL = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code='
def get_stock_info(stock_code):
    try:
        c = requests.get(BASE_URL+stock_code)
    except Exception as e:
        return None
    q = pq(c.text, parser='html')
    company = q('th.symbol').children().text()
    current_stock_price = q('td.stoksPrice').text()
    last_close = q('.ymuiEditLink'+'.mar0').children().eq(0).text()
    result_dict = {
        'company':company,
        'current_stock_price':current_stock_price,
        'last_close':last_close
    }

    return result_dict

# print(get_stock_info('6058'))


###########################
# 36.
###########################

printQNum(36)


import json

CiNii_BASE_URL = 'http://ci.nii.ac.jp/books/opensearch/search?'

def getCiNiiSearchResult(q, f):
    qparam = '&q=' + q
    fparam = '&format=' + f
    requestUrl = CiNii_BASE_URL + qparam + fparam
    con = requests.get(requestUrl)

    if(f == 'html'):
        queryHtmtl = pq(con.text, parser=f)
        # クラス,od名,タグで検索
    elif(f == 'json'):
        queryJson = json.loads(con.text)
        titles = []
        for n in range(0,10):
            titles.append(queryJson['@graph'][0]['items'][n]['title'])
        return titles

for count, t in enumerate(getCiNiiSearchResult('お好み焼き', 'json')):
    print('{0}, {1}'.format(count+1, t))


###########################
# 37.
###########################

printQNum(37)

def getTitleNumberperYear():
    areaParam = '&area=22'
    pageParam = '&p=1'
    countParam = '&count=10000'
    fParam = '&format=json'
    requestUrl = CiNii_BASE_URL + areaParam + pageParam + countParam + fParam
    con = requests.get(requestUrl)
    queryJson = json.loads(con.text)

    with open('./shizuokalib.json', 'w') as tempf:
        tempf.write(json.dumps(queryJson, indent=2, ensure_ascii=False,))
        print('done')

    tempDict = {}
    for n in range(1,10000):
        try:
            pub = queryJson['@graph'][0]['items'][n]['prism:publicationDate']
        
            if re.match(r'.*-.*', pub):
                continue
            elif pub in tempDict:
                tempDict[pub] += 1
            else:
                tempDict.setdefault(pub, 1)
        except KeyError as ke:
            pass
    
    itemsPerYear = sorted(tempDict.items(), key = lambda x:x[0])
    print(itemsPerYear)

getTitleNumberperYear()