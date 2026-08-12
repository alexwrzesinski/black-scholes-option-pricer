import sys
import os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..","sources"))

from pricing import call_price, put_price, delta_call, delta_put, gamma, vega, theta_call, rho_call

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

def test_delta_call_known_value():
    d = delta_call(100, 100, 1, 0.05, 0.2)
    assert np.isclose(d, 0.6368, atol=0.01)


def test_delta_put_known_value():
    d = delta_put(100, 100, 1, 0.05, 0.2)
    assert np.isclose(d, -0.3632, atol=0.01)


def test_gamma_known_value():
    g = gamma(100, 100, 1, 0.05, 0.2)
    assert np.isclose(g, 0.0188, atol=0.001)


def test_vega_known_value():
    v = vega(100, 100, 1, 0.05, 0.2)
    assert np.isclose(v, 0.3752, atol=0.01)


def test_theta_call_known_value():
    t = theta_call(100, 100, 1, 0.05, 0.2)
    assert np.isclose(t, -0.0176, atol=0.001)


def test_rho_call_known_value():
    r = rho_call(100, 100, 1, 0.05, 0.2)
    assert np.isclose(r, 0.5323, atol=0.01)


def test_delta_put_call_relationship():
    # delta_put should always equal delta_call - 1, for any inputs
    dc = delta_call(100, 100, 1, 0.05, 0.2)
    dp = delta_put(100, 100, 1, 0.05, 0.2)
    assert np.isclose(dp, dc - 1, atol=0.0001)