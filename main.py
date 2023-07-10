import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

home_price = 120000
percent_year = 0.05 
years = 5
rate = 0.12
freq = 12

future_price = home_price * (1 + percent_year) ** years
print(f"Cena mieszkania za 5 lat będzie wynosiła: {future_price: .2f}zł")
#Kwota przyszłego mieszkania 153153.79zł

rate /= freq
nper = freq * years

deposit_amount = npf.pmt(rate, nper, 0, -future_price)
print(f"Miesięczna wymagana wpłata do banku wynosi: {deposit_amount: .2f}zł")
#Miesięcnza wymagana wpłata: 1875.28zł

plt.plot(future_price,label='Home price')
plt.plot(deposit_amount,label='Deposit value')
plt.xlabel('Months')
plt.ylabel('Value [zł]')
plt.legend()
plt.show()