import math

# ищет длину вектора
def dlina(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

# вычитает второй вектор из первого
def raznost(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

# ищет скалярное произведение двух векторов
def skalar(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

# считает определенный интеграл
def integral(f, a, b, n=1000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

# приближенная дельта-функция
def delta(x, eps=1e-2):
    return math.exp(-(x * x) / (eps * eps)) / (eps * math.sqrt(math.pi))

# задача 1: четыре интеграла с дельта-функцией
def zadacha_1():
    i1 = integral(lambda x: (x * x - 5 * x + 6) * delta(2 * x), -1.0, 1.0, 2000)
    i2 = integral(lambda x: (x + 3) * delta(x + 5), -8.0, -1.0, 2000)
    i3 = integral(lambda x: (x + 3) * delta(x - 5), -8.0, -1.0, 2000)
    a = 0.5
    i4 = integral(lambda x: math.exp(-a * x) * delta(x * x + x - 2), -4.0, 4.0, 4000)
    print("1.а:", round(i1, 4))
    print("1.б:", round(i2, 4))
    print("1.в:", round(i3, 4))
    print("1.г:", round(i4, 4))

# задача 2: интеграл от exp(-x) * delta(cos x)
def zadacha_2():
    s = 0.0
    for k in range(30):
        xk = math.pi / 2.0 + math.pi * k
        s += math.exp(-xk) / abs(math.sin(xk))
    print("2:", round(s, 4))

# задача 3: интеграл от -inf до a от delta(x - x0)
def zadacha_3():
    x0 = 2.0
    v1 = round(integral(lambda x: delta(x - x0), -5.0, 0.0, 2000), 4)
    v2 = round(integral(lambda x: delta(x - x0), -5.0, 2.0, 2000), 4)
    v3 = round(integral(lambda x: delta(x - x0), -5.0, 4.0, 2000), 4)
    print(f"3: a<x0: {v1}, a=x0: {v2}, a>x0: {v3}")

# задача 4: трехмерный интеграл с дельта-функцией
def zadacha_4():
    a = [1.0, -2.0, 3.0]
    print("4:", 2 * skalar(a, a))

# задача 5: плотность заряда диполя
def zadacha_5():
    print("5: q*delta(r) - q*delta(r - a)")

# задача 6: плотность заряда сферической оболочки
def zadacha_6():
    Q, R = 5.0, 2.0
    q_int = integral(lambda r: 4 * math.pi * r * r * (Q / (4 * math.pi * R * R)) * delta(r - R), 0.0, 4.0, 2000)
    print("6: Q/(4*pi*R^2)*delta(r - R) | Q =", round(q_int, 4))

# задача 7: интеграл от лапласиана 1/r
def zadacha_7():
    eps = 0.05
    val = integral(lambda r: 4 * math.pi * r * r * (-3 * eps * eps / ((r * r + eps * eps) ** 2.5)), 0.0, 10.0, 3000)
    print("7:", round(val, 4))

# задача 8: потенциал элементарного диполя
def zadacha_8():
    p = [1.0, -2.0, 0.5]
    r0 = [0.5, 0.5, -0.5]
    r = [3.0, 1.0, 2.0]
    dr = raznost(r, r0)
    phi = skalar(p, dr) / (dlina(dr) ** 3)
    print("8:", round(phi, 4))

if __name__ == "__main__":
    zadacha_1()
    zadacha_2()
    zadacha_3()
    zadacha_4()
    zadacha_5()
    zadacha_6()
    zadacha_7()
    zadacha_8()