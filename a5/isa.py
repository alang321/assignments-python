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

def __getTemperaturePressure(h, t0, p0, layer=0):
    h1 = min(h, altitude[layer])
    t1 = t0 + a[layer]*(h1-altitude[layer-1])
    if a[layer] == 0:
        p1 = p0 * math.exp((-g_0/(R * t0))*(h1-altitude[layer-1]))
    else:
        p1 = p0 * (t1/t0)**(-g_0/(a[layer]*R))
    if h > altitude[layer]:
        return __getTemperaturePressure(h, t1, p1, layer+1)
    else:
        return t1, p1

def __getDensity(p, T):
    return p/(R*T)

def getIsa(h):
    T, p = __getTemperaturePressure(h, T_0, p_0)
    rho = __getDensity(p, T)
    return T, p, rho










