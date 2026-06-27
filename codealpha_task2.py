# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

num_stocks = int(input("Enter the number of stocks you own: "))

for i in range(num_stocks):
    print(f"\nStock #{i + 1}")

    stock_name = input("Enter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment_value = stock_prices[stock_name] * quantity
        total_investment += investment_value

        print("Stock Price:", stock_prices[stock_name])
        print("Investment Value:", investment_value)

    else:
        print("Stock not found in the portfolio database.")

print("\n" + "=" * 40)
print("TOTAL INVESTMENT VALUE: $", total_investment)
print("=" * 40)

save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Stock Portfolio Tracker\n")
    file.write("=======================\n")
    file.write("Total Investment Value: $" + str(total_investment))
    file.close()

    print("Result saved successfully in portfolio.txt")

print("\nThank you for using the Stock Portfolio Tracker!")