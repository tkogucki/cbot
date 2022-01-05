import ccxt
from datetime import datetime
import calendar

# print(ccxt.exchanges)
def crypto_values():
    binance = ccxt.binance()
    symbol = "BTC/USDT"

    ticker = binance.fetch_ticker(symbol)
    #print(ticker)
    currBitcoinPrice = ticker["close"]
    print(f"${currBitcoinPrice}")


    fetchStrut = {
        "time" : 0,
        "close" : 4
    }
    # recieving current utc time and converting to unix time
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    # calculating back 1 week to set start time
    since = (unixtime - 60*60*24*7) * 1000 # UTC timestamp in milliseconds

    # fetching ohlcv at spacing = timeframe, starting with since
    output = binance.fetch_ohlcv(symbol, timeframe = '1h', since = since)

    # taking the first and last time frames and pulling out there human readable time
    StartTime = datetime.fromtimestamp(output[0][fetchStrut["time"]]/1000)
    EndTime = datetime.fromtimestamp(output[-1][fetchStrut["time"]]/1000)
    print(f"Start Date: {StartTime}")
    print(f"End Date: {EndTime}")

    # calculting value and percentage change
    StartPrice = output[0][fetchStrut["close"]]
    EndPrice =  output[-1][fetchStrut["close"]]
    CashDelta = EndPrice - StartPrice
    PercChange = (EndPrice - StartPrice) / StartPrice * 100

    # formatting strings for return value
    PercChangeStr = f"Bitcoin Wk Percentage Change: {PercChange:.3f}%"
    CashDeltaStr = f"Bitcoin Wk Cash Delta = {CashDelta:.2f}"

    return CashDeltaStr, PercChangeStr

