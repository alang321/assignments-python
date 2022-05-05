import math
import matplotlib.pyplot as plt

correct_method = False

def unimpeded_growth(r, start_year=2005, end_year=2100):
    tao = 1 / math.log(1 + r)

    t_range = list(range(start_year, end_year + 1))
    growth_factor = [0] * len(t_range)

    for t in range(len(t_range)):
        growth_factor[t] = math.exp(t / tao)

    return t_range, growth_factor

def evolutionary_growth(r_list, market_share, start_year=2005, end_year=2100):
    tao = [1 / math.log(1 + r) for r in r_list]

    t_range = list(range(start_year, end_year + 1))
    growth_factors = [[0] * len(t_range) for _ in r_list]

    for category in range(len(r_list)):
        for t in range(len(t_range)):
            growth_factors[category][t] = math.exp(t / tao[category])

    combined_growth_fac = [0] * len(t_range)
    for t in range(len(t_range)):
        for idx in range(len(r_list)):
            combined_growth_fac[t] += growth_factors[idx][t] * market_share[idx]

    return t_range, combined_growth_fac

def revolutionary_growth(emission_reduction_list, revolution_year_list, r_list, market_share_list, t_L, start_year=2005, end_year=2100):
    tao = [1 / math.log(1 + r) for r in r_list]

    t_range = list(range(start_year, end_year + 1))
    growth_factor_list = [[0] * len(t_range) for _ in r_list]

    for category in range(len(r_list)):
        n_replaced = 0
        for t, year in enumerate(t_range):
            if year > revolution_year_list[category]:
                n_total = math.exp(t / tao[category])
                n_conv = max(growth_factor_list[category][t_range.index(revolution_year_list[category])] - n_replaced, 0)
                n_ng = n_total - n_conv
                growth_factor_list[category][t] = n_conv + (1-emission_reduction_list[category]) * n_ng
            else:
                growth_factor_list[category][t] = math.exp(t / tao[category])

            if year >= revolution_year_list[category]:
                n_replaced += n_replace(t, t_L, tao[category])


            if year == 2050:
                print(n_ng * market_share_list[category])

    combined_growth_fac = [0] * len(t_range)
    for t in range(len(t_range)):
        for category in range(len(r_list)):
            combined_growth_fac[t] += growth_factor_list[category][t] * market_share_list[category]

    return t_range, combined_growth_fac

def n_replace(t, t_L, tao, order=4):
    expansion = 0
    for i in range(1, order + 1):
        expansion += math.exp(-i * t_L / tao)

    return (1 - math.exp(-1/tao)) * math.exp(t/tao) * expansion

# step 1
# plt.figure()
# plt.plot(*unimpeded_growth(0.044), label='Unimpeded growth', color="red")
# plt.xlabel("Year")
# plt.ylabel("Growth factor")
# plt.legend()
# plt.show()

# step2
if correct_method:
    r_category = [0.044, 1.044 * 0.99 - 1, 1.044 * 0.99 - 1, 1.044 * 0.99 - 1]
else:
    r_category = [0.044, 0.034, 0.034, 0.034]
# category_distribution = [0.09, 0.24, 0.19, 0.48]
#
# plt.figure()
# plt.plot(*evolutionary_growth(r_category, category_distribution), label='Evolutionary growth', color="red")
# plt.xlabel("Year")
# plt.ylabel("Growth factor")
# plt.legend()
# plt.show()

# step3
lifetime = 20 # years
emission_red = [1, 0.8, 0.4, 0.3]
revolution_year = [2030, 2030, 2035, 2040]
distribution = [0.09, 0.24, 0.19, 0.48]
if correct_method:
    r = [0.044, 1.044 * 0.99 - 1, 1.044 * 0.99 - 1, 1.044 * 0.99 - 1]
else:
    r = [0.044, 0.034, 0.034, 0.034]

t_range, growth_fac_unimp = unimpeded_growth(0.044)
_, combined_growth_fac_ev = evolutionary_growth(r, distribution)
_, combined_growth_fac_rev = revolutionary_growth(emission_red, revolution_year, r, distribution, lifetime)

print("Growth Factor (2100): ", combined_growth_fac_rev[-1])
plt.figure()
plt.plot(t_range, growth_fac_unimp, label='Unimpeded growth', color="red")
plt.plot(t_range, combined_growth_fac_ev, label='Evolutionary', color="green")
plt.plot(t_range, combined_growth_fac_rev, label='Revolutionary', color="blue")
plt.ylim(0.8, 8)
plt.xlabel("Year")
plt.ylabel("Growth factor")
plt.legend()
plt.show()


# step 4
r_def = [0.044, 0.044, 0.044, 0.044]
lifetime_def = 20
emission_red_def = [1, 0.8, 0.4, 0.3]
revolution_year_def = [2030, 2030, 2035, 2040]
evolution_rate_def = [0.0, 0.01, 0.01, 0.01]
if correct_method:
    r_eff_def = [(r_def[i] + 1) * (1 - evolution_rate_def[i]) - 1 for i in range(len(r_def))]
else:
    r_eff_def = [r_def[i] - evolution_rate_def[i] for i in range(len(r_def))]

distribution = [0.09, 0.24, 0.19, 0.48]
lifetime = lifetime_def # years
emission_red = emission_red_def.copy()
revolution_year = revolution_year_def.copy()
evolution_rate = evolution_rate_def.copy()
r = r_def.copy()

category_names = ["<500 km", "500-1500 km", "1500-3000 km", ">3000 km"]
variables = [r, evolution_rate, emission_red, lifetime, revolution_year]
variables_def_vals = [r_def, evolution_rate_def, emission_red_def, lifetime_def, revolution_year_def]
variable_names = ["Growth rate", "Evolution rate", "Emission reduction factor", "Lifetime", "Year of Introduction"]
variable_type = [float, float, float, int, int]

while True:
    try:
        txt = "\n"
        for i, name in enumerate(variable_names):
            txt += str(i) + " - Change " + name + "\n"
        txt += f"{len(variable_names)} - Reset all\n{(len(variable_names) + 1)} - To show result\nPress anything else to exit\n"
        a = int(input(txt))

        if not 0 <= a <= (len(variable_names) + 1):
            raise ValueError

        if a == len(variable_names):
            for i in range(len(variable_names)):
                if type(variables[i]) == list:
                    variables[i] = variables_def_vals[i].copy()
                else:
                    variables[i] = variables_def_vals[i]
    except:
        break

    if 0 <= a < len(variable_names):
        if type(variables[a]) == list:
            for i in range(len(variables[a])):
                try:
                    b = variable_type[a](input(f"Change {variable_names[a]} (Category: {category_names[i]} value: {variables[a][i]}):"))
                    variables[a][i] = b
                except:
                    continue
        else:
            try:
                b = variable_type[a](input(f"Change {variable_names[a]} (value: {variables[a]}):"))
                variables[a] = b
            except:
                pass

    if correct_method:
        r_eff = [(r[i] + 1) * (1 - evolution_rate[i]) - 1 for i in range(len(r))]
    else:
        r_eff = [r[i] - evolution_rate[i] for i in range(len(r))]

    if a == (len(variable_names) + 1):
        print()
        print("Calculating Results with parameters:\n")
        for i, name in enumerate(variable_names):
            print(f"{name}: {variables[i]}")

        _, combined_growth_fac_rev_old = revolutionary_growth(emission_red_def, revolution_year_def, r_eff_def, distribution, lifetime_def)
        t_range, combined_growth_fac_rev_new = revolutionary_growth(emission_red, revolution_year, r_eff, distribution, lifetime)
        print("\nGrowth Factor (2100): ", combined_growth_fac_rev[-1])

        plt.figure()
        plt.plot(t_range, combined_growth_fac_rev_old, label='Original', color="blue")
        plt.plot(t_range, combined_growth_fac_rev_new, label='New', color="red")
        plt.xlabel("Year")
        plt.ylabel("Growth factor")
        plt.legend()
        plt.show()

# lifetime and year of introduction mostly dont alter final emission rate just total emissions
# growth factor huge effect
# emission reduction some effect
# evolution same as growth factor
