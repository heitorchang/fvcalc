from datetime import datetime

from constants import birth_year, retirement_age, annual_yield

# Compute FV
# cash flows: positive is investment, negative is withdrawal

pv = 72139
pmt = 0


years_to_invest = (birth_year + retirement_age) - datetime.now().year

i = (1 + (annual_yield / 100)) ** (1/12) - 1
j = 1 + i
n = years_to_invest * 12

jn = j ** (-n)

fv = (-pv - pmt * ((1 - jn) / i)) / jn

print(n, i, pv, pmt, fv)
print(f"FV: {fv:.2f}")
