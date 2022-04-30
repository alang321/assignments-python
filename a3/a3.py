import math
import matplotlib.pyplot as plt
import numpy as np

def exponential_growth(r, start_year, end_year):
    tao = 1 / math.log(1 + r)

    t_range = list(range(start_year, end_year + 1))
    growth_factor = [0] * len(t_range)

    for t in range(len(t_range)):
        growth_factor[t] = math.exp(t/tao)

    return t_range, growth_factor

def combined_exponential_growth(r, relative, start_year, end_year):
    tao = [1 / math.log(1 + r_n) for r_n in r]

    t_range = list(range(start_year, end_year + 1))
    growth_factors = [[0] * len(t_range) for _ in r]

    for r_n in range(len(r)):
        for t in range(len(t_range)):
            growth_factors[r_n][t] = math.exp(t/tao[r_n])

    combined = [0] * len(t_range)
    for t in range(len(t_range)):
        for idx in range(len(r)):
            combined[t] += growth_factors[idx][t] * relative[idx]

    return t_range, combined

# step 1
plt.figure()
plt.plot(*exponential_growth(0.044, 2005, 2100), label='Unimpeded growth', color="red")
plt.xlabel("Year")
plt.ylabel("Growth factor")
plt.legend()
plt.show()

# step2
r = [0.044, 1.044 * 0.99 - 1]
relative = [0.09, 0.91]
print(combined_exponential_growth(r, relative, 2005, 2100)[1][-1])
plt.figure()
plt.plot(*combined_exponential_growth(r, relative, 2005, 2100), label='Evolutionary growth', color="red")
plt.xlabel("Year")
plt.ylabel("Growth factor")
plt.legend()
plt.show()

