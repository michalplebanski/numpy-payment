import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

home_price = 120000
percent_year = 0.05 
years = 5
rate = 0.12
freq = 12

#Home price for 5 years

future_price = home_price * (1 + percent_year) ** years
print(f"Cena mieszkania za 5 lat będzie wynosiła: {future_price: .2f}zł")