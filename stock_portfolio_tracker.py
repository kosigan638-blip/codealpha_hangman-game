stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

num = int(input("How many different stocks do you own? "))

total = 0
for i in range(num):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        total += stock_prices[stock] * quantity
    else:
        print("Stock not found!")

print("Total Investment Value: $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total}")

print("Result saved to portfolio.txt")