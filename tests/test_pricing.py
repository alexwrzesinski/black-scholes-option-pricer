import sys
import os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..","sources"))

from pricing import call_price, put_price

def test_call_price_known_val():
    Cprice=call_price(100,100,1,0.05,0.2)
    assert np.isclose(Cprice, 10.4506,atol=0.01),f"Expected near 10.4506, got {Cprice}"

def test_put_price_known_val():
    Pprice=put_price(100,100,1,0.05,0.2)
    assert np.isclose(Pprice,5.5735,atol=0.01),f"Expected near 5.5735, got {Cprice}"

def test_put_call_parity():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)
    
    lhs = call - put
    rhs = S - K * np.exp(-r * T)
    
    assert np.isclose(lhs, rhs, atol=0.01), f"Parity failed: {lhs} != {rhs}"