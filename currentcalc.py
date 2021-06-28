from datetime import datetime


# Signatures:
# pmt(retirement_age, annual_yield, pv, fv)
# fv(retirement_age, annual_yield, pv, pmt)

birth_year = 1983

def pmt(retirement_age, annual_yield, pv, fv):
    # Compute PMT
    # cash flows: money received is positive, money paid out is negative

    years_to_invest = (birth_year + retirement_age) - datetime.now().year
    i = (1 + (annual_yield / 100)) ** (1/12) - 1
    j = 1 + i
    n = years_to_invest * 12

    jn = j ** (-n)

    pmt = (-fv * jn - pv) / ((1 - jn) / i)

    return round(pmt, 2)


def fv(retirement_age, annual_yield, pv, pmt):
    years_to_invest = (birth_year + retirement_age) - datetime.now().year

    i = (1 + (annual_yield / 100)) ** (1/12) - 1
    j = 1 + i
    n = years_to_invest * 12

    jn = j ** (-n)

    fv = (-pv - pmt * ((1 - jn) / i)) / jn

    return round(fv, 2)


def pv(retirement_age, annual_yield, fv, pmt):
    years_to_invest = (birth_year + retirement_age) - datetime.now().year

    i = (1 + (annual_yield / 100)) ** (1/12) - 1
    j = 1 + i
    n = years_to_invest * 12

    jn = j ** (-n)

    pv = -(j * pmt * ((1 - jn) / i) + fv * jn)

    return round(pv, 2)
