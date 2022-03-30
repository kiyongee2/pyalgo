# 주식 최대 수익
# 입력 : 주식 가격의 변화값
# 출력 : 한 주를 한번 사고팔아 얻을 수 있는 최대 수익 값

def max_profit(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]  # 첫째날의 주가를 주가의 최솟값으로 기억

    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))