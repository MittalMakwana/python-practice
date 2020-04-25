def stock2(list):
    min_price = 1000000
    profit = 0
    for i in list:
        min_price = min(min_price, i)
        curr_profit = profit - min_price
        profit = max(curr_profit, profit)
        print(i, min_price, curr_profit, profit)
    return profit


def check_profit(stock_price):
    profit = 0

    for i in range(len(stock_price)):
        for j in range(i, len(stock_price)):
            buy_price = stock_price[i]
            sell_price = stock_price[j]
            curr_profit = sell_price - buy_price
            profit = max(profit, curr_profit)


    return profit

a=[7,1,5,3,6,4]
b = [7,6,4,3,1]
print(check_profit(a))
print(stock2(a))
print(stock2(b))
