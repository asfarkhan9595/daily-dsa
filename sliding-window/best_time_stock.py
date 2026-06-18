# Day 7 - Best Time to Buy and Sell Stock
# LeetCode #121
# Maximum profit from buying and selling  stock

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Test
print(max_profit([7, 1, 5, 3, 6, 4]))  # 6
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([2, 4, 1]))           # 2