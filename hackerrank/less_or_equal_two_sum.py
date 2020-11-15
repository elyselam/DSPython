
def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    sorted_prices = list(reversed(sorted_prices))
    maxNumItems = 0
    sumOfPrices = 0
    for i in range(len(sorted_prices)):
        if sorted_prices[i] + sumOfPrices <= k:
            maxNumItems += 1
            sumOfPrices += sorted_prices[i]
            print("Sum of prices: ", sumOfPrices)
    return maxNumItems

lst = [1,12,5,111,200,1000,10]
print(maximumToys(lst,50))

