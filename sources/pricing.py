import numpy as np 
from scipy.stats import norm

def _d1_d2(S,K,T,r, sigma): #Black Scholes Formuals for d1 and d2
    d1= (np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2= d1-sigma*np.sqrt(T)
    return d1,d2

def call_price(S,K,T,r,sigma): #Price a European call option
    """
    S     : current spot price of the underlying
    K     : strike price
    T     : time to expiry, in years (e.g. 0.5 = 6 months)
    r     : risk-free interest rate (annualised, e.g. 0.05 = 5%)
    sigma : volatility of the underlying (annualised, e.g. 0.2 = 20%)
    """
    d1,d2=_d1_d2(S,K,T,r,sigma)
    CallPrice= (S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2))
    return CallPrice

def put_price(S,K,T,r,sigma):
    #Price a European put option 
    d1,d2=_d1_d2(S,K,T,r,sigma)
    PutPrice= K*np.exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
    return PutPrice

def delta_call(S,K,T,r,sigma):
    d1,d2= _d1_d2(S,K,T,r,sigma)
    return norm.cdf(d1)

def delta_put(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return norm.cdf(d1)-1

def gamma(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return norm.pdf(d1)/(S*sigma*np.sqrt(T))

def vega(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return S*norm.pdf(d1)*np.sqrt(T)/100

def theta_call(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return ((-S*norm.pdf(d1)*sigma)/(2*np.sqrt(T))-r*K*np.exp(-r*T)*norm.cdf(d2))/365

def theta_put(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return ((-S*norm.pdf(d1)*sigma)/(2*np.sqrt(T))-r*K*np.exp(-r*T)*norm.cdf(-d2))/365

def rho_call(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return K*T*np.exp(-r*T)*norm.cdf(d2)/100

def rho_put(S,K,T,r,sigma):
    d1,d2=_d1_d2(S,K,T,r,sigma)
    return -K*T*np.exp(-r*T)*norm.cdf(-d2)/100

S=100
K=100
T=1
r=0.05
sigma=0.2
if __name__=="__main__":
    print(delta_call(S,K,T,r,sigma))
    print(delta_put(S,K,T,r,sigma))
    print(gamma(S,K,T,r,sigma))
    print(vega(S,K,T,r,sigma))
    print(theta_call(S,K,T,r,sigma))
    print(theta_put(S,K,T,r,sigma))
    print(rho_call(S,K,T,r,sigma))
    print(rho_put(S,K,T,r,sigma))