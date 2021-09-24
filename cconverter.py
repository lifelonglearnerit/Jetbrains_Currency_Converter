import requests

usr_curr = input().lower()  # currency which user has and want to exchange
r = requests.get(f'http://www.floatrates.com/daily/{usr_curr}.json')
curr_dict = r.json()

#  adding usd and eur to cache
cache_dict = {}
if usr_curr == 'usd':
    cache_dict.update({'eur': curr_dict['eur']['rate']})
elif usr_curr == 'eur':
    cache_dict.update({'usd': curr_dict['usd']['rate']})
else:
    cache_dict.update({'eur': curr_dict['eur']['rate'],
                       'usd': curr_dict['usd']['rate']})
while True:
    exch_curr = input().lower()  # currency to which user want to exchange
    if exch_curr == "": break  # end of program when empty input
    am_money = float(input())  # amount of money which user has
    #  cache_chek(exch_curr)
    print('Checking the cache...')
    if exch_curr in cache_dict:
        print('Oh! It is in the cache!')
        exchange = am_money * cache_dict[exch_curr]
        print(f'You received {round(exchange, 2)} {exch_curr.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        exchange = am_money * curr_dict[f'{exch_curr}']['rate']
        print(f'You received {round(exchange, 2)} {exch_curr.upper()}.')
        cache_dict.update({f'{exch_curr}': curr_dict[f'{exch_curr}']['rate']})

