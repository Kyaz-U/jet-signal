# api_client.py

import random

def get_latest_coefficients():
    """
    Bu funksiya hozircha test maqsadida random koeffitsiyentlar qaytaradi.
    Keyinchalik bu yerga real API dan web scraping yoki API chaqiriqlar qo‘shiladi.
    """
    k1 = round(random.uniform(1.0, 5.0), 2)
    k2 = round(random.uniform(1.0, 5.0), 2)
    k3 = round(random.uniform(1.0, 5.0), 2)
    return k1, k2, k3
