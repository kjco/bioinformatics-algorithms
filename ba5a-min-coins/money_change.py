
money = 8074
#money = 18705
#coin_list = [24,23,21,5,3,1]
coin_list = [24,13,12,7,5,3,1]

#coin_list = map(int, open('dataset_71_8.txt').read().split(','))

d = {0:0}

for m in range(1,money+1):
    min_coin = 1000000
    for coin in coin_list:
        if m >= coin:
            if d[m-coin]+1 < min_coin:
                min_coin = d[m-coin]+1
    d[m] = min_coin

#print d    

print d[money]
    
