import numpy as np 
import plotly.graph_objects as go
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from pricing import call_price, put_price, delta_call, gamma, vega
import matplotlib.pyplot as plt


##How does the Price curve do when spot price changes
spot_range=np.linspace(50,150,100)
prices = []

K = 100
T=1
r=0.05
sigma= 0.2

for S in spot_range:
    price = call_price(S,K,T,r,sigma)
    prices.append (price)


plt.plot(spot_range,prices)
plt.xlabel("Spot Price")
plt.ylabel("Call Prices")
plt.title("Call Options vs Stock Price")
plt.savefig("images/call_price_vs_spot.png")
plt.show()

plt.clf()
#Delta vs Spot Price

deltas = []
for S in spot_range:
    d = delta_call(S,K,T,r,sigma)
    deltas.append(d)

plt.plot(spot_range,deltas)
plt.xlabel("Spot Price")
plt.ylabel("Delta Value")
plt.title("Call Option Delta vs Spot Price" )
plt.savefig("images/delta_vs_spot.png")
plt.show()
plt.clf()

S=100
T_range = np.linspace(0.01,2,100)
vegas = []
for T in T_range:
    v=vega(S,K,T,r,sigma)
    vegas.append(v)


plt.plot(T_range,vegas)
plt.xlabel("Time to Expiry")
plt.ylabel("Vega Value")
plt.title("Vega vs Time to Expiry" )
plt.savefig("images/vega_vs_time.png")
plt.show()