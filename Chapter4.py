def printQNum(num):
    print("\n###########################")
    print("# Q{}.".format(num))
    print("###########################\n")

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

code = query('.yjM .center')("a[href *= '/stocks/detail/?code=']")
price = query('.yjM .price')
for code, price in zip(code.text().split(), price.text().split()):
    print('({0},{1})'.format(code,price))