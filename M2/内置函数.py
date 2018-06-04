# -*- coding:utf-8 -*-

name=['alex','wupeiqi','yuanhao','nezha']

res = map(lambda  x: x + '_sb',name)
for i in res:
	print(i)
	
num = [1,3,5,6,7,8]

res_1 = filter(lambda x: x%2 == 0,num)
for i in res_1:
	print(i)


portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

list_por = []
for i in portfolio:
	shares = i['shares']
	price = i['price']
	all_sell = shares * price
	dic_1 = {}
	dic_1['name'] = i['name']
	dic_1['all'] = all_sell
	list_por.append(dic_1)

print(list_por)

filter_res = filter(lambda x : x['price']>100,portfolio)
print(list(filter_res))