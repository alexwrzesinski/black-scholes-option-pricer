import yfinance as yf
from datetime import datetime
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from pricing import call_price, put_price
ticker = yf.Ticker("SPY")
current_price=ticker.history(period="1d")["Close"].iloc[-1]
print(current_price)

expiries = ticker.options
chain = ticker.option_chain(expiries[3])
calls = chain.calls

#print(calls[["strike", "bid", "ask", "volume", "openInterest", "impliedVolatility"]])

liquid_calls = calls[(calls["openInterest"] > 50) & (calls["impliedVolatility"] > 0.01)]
liquid_calls["strike_diff"] = abs(liquid_calls["strike"] - current_price)
closest_row = liquid_calls.loc[liquid_calls["strike_diff"].idxmin()]
#print(closest_row)

from datetime import datetime

expiry_date = datetime.strptime("2026-08-17", "%Y-%m-%d")
T = (expiry_date - datetime.now()).days / 365
if T <= 0:
    T = 1 / 365  # floor to avoid division by zero for same-day/near-expiry contracts

r = 0.04
strike = closest_row["strike"]
market_price = closest_row["lastPrice"]
implied_vol = closest_row["impliedVolatility"]

model_price = call_price(current_price, strike, T, r, implied_vol)

print(f"Strike: {strike}")
print(f"Market price: {market_price}")
print(f"Model price: {model_price}")
print(f"Difference: {model_price - market_price}")

##model_price=call_price(current_price,strike,T,r, implied_vol)

model_price_test = call_price(current_price, strike, T, r, 0.12)
print(f"Model price with sigma=0.12: {model_price_test}")