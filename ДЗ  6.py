import math

# ищет длину вектора
def dlina(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

# складывает два вектора
def slozhenie(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

# вычитает второй вектор из первого
def raznost(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

# умножает вектор на число
def umnozenie(v, k):
    return [v[0] * k, v[1] * k, v[2] * k]

# считает определенный интеграл
def integral(f, a, b, n=1000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

# считает потенциал и поле системы зарядов
def pole_sistemi(zaryadi, tochka):
    phi = 0.0
    e_vec = [0.0, 0.0, 0.0]
    for q, pos in zaryadi:
        dr = raznost(tochka, pos)
        r = dlina(dr)
        if r < 0.05:
            r = 0.05
        phi += q / r
        e_vec = slozhenie(e_vec, umnozenie(dr, q / (r ** 3)))
    return phi, e_vec

# задача 15: потенциал и поле в центре правильного шестиугольника
def zadacha_15():
    a = 2.0
    q = 1.0
    zaryadi = []
    for i in range(6):
        u = math.pi * i / 3.0
        znak = 1.0 if i % 2 == 0 else -1.0
        zaryadi.append((znak * q, [a * math.cos(u), a * math.sin(u), 0.0]))
    phi, e = pole_sistemi(zaryadi, [0.0, 0.0, 0.0])
    print(f"15: phi={round(phi, 4)} E={round(dlina(e), 4)}")

# задача 16: потенциал и поле на оси кольца из двух разных половин
def zadacha_16():
    a = 2.0
    z = 1.5
    t1 = 3.0
    t2 = 1.0
    n = 1000
    du = 2 * math.pi / n
    zaryadi = []
    for i in range(n):
        u = (i + 0.5) * du
        tau = t1 if u < math.pi else t2
        dq = tau * a * du
        zaryadi.append((dq, [a * math.cos(u), a * math.sin(u), 0.0]))
    phi, e = pole_sistemi(zaryadi, [0.0, 0.0, z])
    print(f"16: phi={round(phi, 4)} E={round(dlina(e), 4)}")

# задача 17: потенциал и поле в центре заряженной дуги
def zadacha_17():
    a = 2.0
    tau = 1.5
    gamma = math.pi / 2.0
    n = 1000
    du = gamma / n
    zaryadi = []
    for i in range(n):
        u = -gamma / 2.0 + (i + 0.5) * du
        dq = tau * a * du
        zaryadi.append((dq, [a * math.cos(u), a * math.sin(u), 0.0]))
    phi, e = pole_sistemi(zaryadi, [0.0, 0.0, 0.0])
    print(f"17: phi={round(phi, 4)} E={round(dlina(e), 4)}")

# задача 18: поле на оси круглого отверстия в заряженной плоскости
def zadacha_18():
    sigma = 1.0
    R = 2.0
    z = 3.0
    e_plosk = 2 * math.pi * sigma
    e_disk = 2 * math.pi * sigma * z * integral(lambda s: s / ((s * s + z * z) ** 1.5), 0.0, R)
    print("18:", round(e_plosk - e_disk, 4))

if __name__ == "__main__":
    zadacha_15()
    zadacha_16()
    zadacha_17()
    zadacha_18()