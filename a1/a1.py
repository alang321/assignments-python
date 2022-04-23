import math


g_0 = 9.80665 #m/s
R = 287.0 #J/kgK
#seal level values
T_0 = 288.15 #K
p_0 = 101325.0 #Pa
rho_0 = 1.225 #kg/m3
#layers
altitude = [11000.0, 20000.0, 32000.0, 47000.0, 51000.0, 71000.0, 86000.0, 0.0]
a = [-0.0065, 0.0, 0.001, 0.0028, 0.0, -0.0028, -0.002]


def getHeight():
    print("1. Calcula the ISA for altitude in meters\n2. Calculate ISA for altitude in feet\n3. Calculate ISA for altitude in FL")
    while True:
        i = int(input("\nEnter your choice:"))
        if i==1:
            h = float(input("\nEnter altitude [m]:"))
            return h
        elif i==2:
            h = float(input("\nEnter altitude [ft]:"))
            return h * 0.3048
        elif i==3:
            h = float(input("\nEnter altitude [FL]:"))
            return (h * 100) * 0.3048


def getTemperaturePressure(h, t0, p0, layer=0):
    h1 = min(h, altitude[layer])
    t1 = t0 + a[layer]*(h1-altitude[layer-1])
    if a[layer] == 0:
        p1 = p0 * math.exp((-g_0/(R * t0))*(h1-altitude[layer-1]))
    else:
        p1 = p0 * (t1/t0)**(-g_0/(a[layer]*R))
    if h > altitude[layer]:
        return getTemperaturePressure(h, t1, p1, layer+1)
    else:
        return t1, p1

def getDensity(p, T):
    return p/(R*T)


while True:
    print("      *** ISA calculator ***")
    h = getHeight()

    optT = input("\nUse different seal level temperature in Celsius (Press enter to use standard 15 Celsius):")
    if optT != "":
        T_0 = float(optT)+273.15
    print(T_0)
    T, p = getTemperaturePressure(h, T_0, p_0)
    rho = getDensity(p, T)
    print("Temperature : ", round(T, 2), "K (", round((T-273.15), 2), " 'C)")
    print("Pressure : ", round(p, 2), " Pa ( ", round((p/p_0)*100, 1), "% SL)")
    print("Density : ", round(rho, 5), " kg/m3 ( ", round((rho/rho_0)*100, 1), "% SL)")

    print("\nReady")

    if input("\nPress Enter to continue or enter \"e\" to exit:") == "e":
        break






