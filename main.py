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

months = np.arange(0, nper + 1)
home_value = home_price * (1 + percent_year/12) ** months
deposit_value = npf.fv(rate, months, -deposit_amount, 0)

plt.plot(months, home_value, label='Home price')
plt.plot(months, deposit_value, label='Deposit value')
plt.xlabel('Months')
plt.ylabel('Value [zł]')
plt.legend()
plt.show()