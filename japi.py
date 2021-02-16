import urllib.request, json

def getStockData(stocksymbol:str):
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + stocksymbol + '&apikey=DMPWZ2EB8PFCUYCJ'
    connection = urllib.request.urlopen(url)
    return connection.read().decode()

def main():

    stocksymbols = []

    while True:
        response = input('Enter a stock symbol: ')
        if (response == 'quit'):
            break
        stocksymbols.append(response)

    for symbol in stocksymbols:
        jsondata = getStockData(symbol)
        print(jsondata)
        pydata = json.loads(jsondata)
        print()
        print('The current price of ' + pydata['Global Quote']['01. symbol'] + ' is: ' + pydata['Global Quote']['05. price'])
        print()

    print("Stock Quotes retrieved successfully!")
    

if __name__ == '__main__':
    main()