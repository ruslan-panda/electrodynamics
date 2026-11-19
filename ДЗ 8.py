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

# ищет скалярное произведение двух векторов
def skalar(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

# возвращает символ Кронекера
def kroneker(i, j):
    if i == j:
        return 1
    return 0

# считает тензор квадрупольного момента
def kvadrupol(zaryadi):
    Q = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    for q, r in zaryadi:
        r2 = skalar(r, r)
        for i in range(3):
            for j in range(3):
                Q[i][j] += q * (3 * r[i] * r[j] - r2 * kroneker(i, j))
    return Q

# считает потенциал на больших расстояниях до квадрупольного слагаемого
def potencial_daleko(zaryadi, tochka):
    r = dlina(tochka)
    q_poln = sum(q for q, _ in zaryadi)
    d = [0.0, 0.0, 0.0]
    for q, pos in zaryadi:
        d = slozhenie(d, umnozenie(pos, q))
    Q = kvadrupol(zaryadi)
    kvadr = 0.0
    for i in range(3):
        for j in range(3):
            kvadr += Q[i][j] * tochka[i] * tochka[j]
    return q_poln / r + skalar(d, tochka) / (r ** 3) + kvadr / (2 * r ** 5)

# задача 32: дипольный момент электронейтральной системы при сдвиге координат
def zadacha_32():
    zaryadi = [(2.0, [1.0, 0.0, 0.0]), (-1.0, [0.0, 2.0, 1.0]), (-1.0, [-1.0, 1.0, 3.0])]
    sdvig = [5.0, -3.0, 7.0]
    d1 = [0.0, 0.0, 0.0]
    d2 = [0.0, 0.0, 0.0]
    for q, r in zaryadi:
        d1 = slozhenie(d1, umnozenie(r, q))
        d2 = slozhenie(d2, umnozenie(raznost(r, sdvig), q))
    print("32:", d1, "==", d2)

# задача 33: квадрупольный момент при сдвиге координат
def zadacha_33():
    zaryadi = [(1.0, [1.0, 0.0, 0.0]), (1.0, [-1.0, 0.0, 0.0]), (-1.0, [0.0, 1.0, 0.0]), (-1.0, [0.0, -1.0, 0.0])]
    sdvig = [4.0, -2.0, 3.0]
    zaryadi2 = [(q, raznost(r, sdvig)) for q, r in zaryadi]
    print("33:", kvadrupol(zaryadi), "==", kvadrupol(zaryadi2))

# задача 34: потенциал тонкого диска на больших расстояниях
def zadacha_34():
    sigma = 1.0
    R = 1.0
    tochka = [6.0, 4.0, 8.0]
    nr = 25
    na = 40
    dr = R / nr
    da = 2 * math.pi / na
    zaryadi = []
    for i in range(nr):
        s = (i + 0.5) * dr
        for j in range(na):
            u = (j + 0.5) * da
            dq = sigma * s * dr * da
            zaryadi.append((dq, [s * math.cos(u), s * math.sin(u), 0.0]))
    print("34:", round(potencial_daleko(zaryadi, tochka), 5))

# задача 35: потенциал цилиндра на больших расстояниях
def zadacha_35():
    rho = 1.0
    R = 1.0
    H = 2.0
    tochka = [8.0, 5.0, 9.0]
    nr = 15
    na = 30
    nz = 15
    dr = R / nr
    da = 2 * math.pi / na
    dz = H / nz
    zaryadi = []
    for i in range(nr):
        s = (i + 0.5) * dr
        for j in range(na):
            u = (j + 0.5) * da
            x = s * math.cos(u)
            y = s * math.sin(u)
            for k in range(nz):
                z = -H / 2.0 + (k + 0.5) * dz
                dq = rho * s * dr * da * dz
                zaryadi.append((dq, [x, y, z]))
    print("35:", round(potencial_daleko(zaryadi, tochka), 5))

if __name__ == "__main__":
    zadacha_32()
    zadacha_33()
    zadacha_34()
    zadacha_35()