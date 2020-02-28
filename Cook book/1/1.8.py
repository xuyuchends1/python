# 与字典有关的操作
prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75
          }

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

min_value = min(prices, key=lambda k: prices[k])
print(min_value)
