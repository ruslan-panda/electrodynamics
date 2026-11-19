import math

# ищет длину вектора
def dlina(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

# ищет скалярное произведение двух векторов
def skalar(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

# ищет лапласиан скалярного поля
def laplas(f, x, y, z, h=1e-3):
    f0 = f(x, y, z)
    d2x = (f(x + h, y, z) - 2 * f0 + f(x - h, y, z)) / (h * h)
    d2y = (f(x, y + h, z) - 2 * f0 + f(x, y - h, z)) / (h * h)
    d2z = (f(x, y, z + h) - 2 * f0 + f(x, y, z - h)) / (h * h)
    return d2x + d2y + d2z

# возвращает символ Кронекера
def kroneker(i, j):
    if i == j:
        return 1
    return 0

# возвращает тензор Леви-Чивиты
def levi_chivita(i, j, k):
    if (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
        return 1
    if (i, j, k) in [(3, 2, 1), (1, 3, 2), (2, 1, 3)]:
        return -1
    return 0

# задача 1: точки параллельности и перпендикулярности градиента оси Ox
def zadacha_1():
    print("1: параллелен Ox: x=0, y=0 | перпендикулярен Ox: z=2x+1")

# задача 2: поток поля через сферу
def zadacha_2():
    R = 3.0
    a = [1.0, 0.0, -1.0]
    nt, np = 40, 80
    dt, dp = math.pi / nt, 2 * math.pi / np
    potok = 0.0
    for i in range(nt):
        th = (i + 0.5) * dt
        for j in range(np):
            ph = (j + 0.5) * dp
            n = [math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)]
            potok += skalar(a, n) * R * R * math.sin(th) * dt * dp
    print("2:", round(potok, 4))

# задача 3: циркуляция поля по окружности радиуса 2
def zadacha_3():
    R = 2.0
    n = 1000
    dt = 2 * math.pi / n
    s = 0.0
    for i in range(n):
        t = (i + 0.5) * dt
        x, y = R * math.cos(t), R * math.sin(t)
        a = [x, x - y, x]
        dr = [-R * math.sin(t) * dt, R * math.cos(t) * dt, 0.0]
        s += skalar(a, dr)
    print("3:", round(s, 4))

# задача 4: двойной лапласиан от r^n
def zadacha_4():
    x, y, z = 1.2, -0.9, 1.5
    otveti = []
    for n in [4, 5, 6]:
        f = lambda xx, yy, zz, nn=n: dlina([xx, yy, zz]) ** nn
        fl = lambda xx, yy, zz: laplas(f, xx, yy, zz, h=1e-2)
        otveti.append(round(laplas(fl, x, y, z, h=1e-2), 2))
    print("4:", otveti)

# задача 5: смена знака при перестановке индексов
def zadacha_5():
    print("5: меняет знак на противоположный (-eps_ijk)")

# задача 6: четыре тензорные суммы
def zadacha_6():
    s1 = [sum(kroneker(i, j) * levi_chivita(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3]) for k in [1, 2, 3]]
    s2 = sum(kroneker(i, j) * kroneker(j, k) * kroneker(k, i) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3])
    s3 = [[sum(levi_chivita(i, j, k) * levi_chivita(i, j, m) for i in [1, 2, 3] for j in [1, 2, 3]) for m in [1, 2, 3]] for k in [1, 2, 3]]
    s4_ok = all(
        sum(levi_chivita(i, j, k) * levi_chivita(k, l, m) * levi_chivita(m, n, i)
            for i in [1, 2, 3] for k in [1, 2, 3] for m in [1, 2, 3]) == -levi_chivita(j, l, n)
        for j in [1, 2, 3] for l in [1, 2, 3] for n in [1, 2, 3]
    )
    print("6.1:", s1)
    print("6.2:", s2)
    print("6.3:", s3)
    print("6.4:", "-eps_jln" if s4_ok else "ошибка")

if __name__ == "__main__":
    zadacha_1()
    zadacha_2()
    zadacha_3()
    zadacha_4()
    zadacha_5()
    zadacha_6()