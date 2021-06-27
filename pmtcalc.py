from datetime import datetime

from constants import birth_year, retirement_age, annual_yield

# Compute PMT
# cash flows: positive is investment, negative is withdrawal


pv = 140000
fv = -2000000

years_to_invest = (birth_year + retirement_age) - datetime.now().year
i = (1 + (annual_yield / 100)) ** (1/12) - 1
j = 1 + i
n = years_to_invest * 12

jn = j ** (-n)

pmt = (-fv * jn - pv) / ((1 - jn) / i)

print(f"PMT: {pmt:.2f}")

# -2415.75
