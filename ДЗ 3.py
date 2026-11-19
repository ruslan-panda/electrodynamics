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

# ищет векторное произведение двух векторов
def vektor_proizv(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

# ищет градиент скалярного поля
def grad(f, x, y, z, h=1e-5):
    dx = (f(x + h, y, z) - f(x - h, y, z)) / (2 * h)
    dy = (f(x, y + h, z) - f(x, y - h, z)) / (2 * h)
    dz = (f(x, y, z + h) - f(x, y, z - h)) / (2 * h)
    return [dx, dy, dz]

# ищет дивергенцию векторного поля
def div(f, x, y, z, h=1e-5):
    dx = (f(x + h, y, z)[0] - f(x - h, y, z)[0]) / (2 * h)
    dy = (f(x, y + h, z)[1] - f(x, y - h, z)[1]) / (2 * h)
    dz = (f(x, y, z + h)[2] - f(x, y, z - h)[2]) / (2 * h)
    return dx + dy + dz

# ищет ротор векторного поля
def rot(f, x, y, z, h=1e-5):
    daz_dy = (f(x, y + h, z)[2] - f(x, y - h, z)[2]) / (2 * h)
    day_dz = (f(x, y, z + h)[1] - f(x, y, z - h)[1]) / (2 * h)
    dax_dz = (f(x, y, z + h)[0] - f(x, y, z - h)[0]) / (2 * h)
    daz_dx = (f(x + h, y, z)[2] - f(x - h, y, z)[2]) / (2 * h)
    day_dx = (f(x + h, y, z)[1] - f(x - h, y, z)[1]) / (2 * h)
    dax_dy = (f(x, y + h, z)[0] - f(x, y - h, z)[0]) / (2 * h)
    return [daz_dy - day_dz, dax_dz - daz_dx, day_dx - dax_dy]

# ищет производную по направлению
def naprav_proizv(a, b_func, x, y, z, h=1e-5):
    dx = umnozenie(raznost(b_func(x + h, y, z), b_func(x - h, y, z)), 1.0 / (2 * h))
    dy = umnozenie(raznost(b_func(x, y + h, z), b_func(x, y - h, z)), 1.0 / (2 * h))
    dz = umnozenie(raznost(b_func(x, y, z + h), b_func(x, y, z - h)), 1.0 / (2 * h))
    return slozhenie(slozhenie(umnozenie(dx, a[0]), umnozenie(dy, a[1])), umnozenie(dz, a[2]))

# округляет числа в векторе
def okrug(v):
    return [round(c, 4) for c in v]

# считает объемный интеграл по кубу [0, 1]^3
def integral_kub(f, n=10):
    h = 1.0 / n
    dv = h * h * h
    s = [0.0, 0.0, 0.0]
    for i in range(n):
        x = (i + 0.5) * h
        for j in range(n):
            y = (j + 0.5) * h
            for k in range(n):
                z = (k + 0.5) * h
                s = slozhenie(s, umnozenie(f(x, y, z), dv))
    return s

# считает поверхностный интеграл по граням куба [0, 1]^3
def integral_grani(f, n=10):
    h = 1.0 / n
    ds = h * h
    s = [0.0, 0.0, 0.0]
    for i in range(n):
        u = (i + 0.5) * h
        for j in range(n):
            v = (j + 0.5) * h
            s = slozhenie(s, umnozenie(f(1.0, u, v, [1, 0, 0]), ds))
            s = slozhenie(s, umnozenie(f(0.0, u, v, [-1, 0, 0]), ds))
            s = slozhenie(s, umnozenie(f(u, 1.0, v, [0, 1, 0]), ds))
            s = slozhenie(s, umnozenie(f(u, 0.0, v, [0, -1, 0]), ds))
            s = slozhenie(s, umnozenie(f(u, v, 1.0, [0, 0, 1]), ds))
            s = slozhenie(s, umnozenie(f(u, v, 0.0, [0, 0, -1]), ds))
    return s

# считает оператор [[a x nabla] x b]
def dvoyn_nabla(a_vec, b_func, x, y, z):
    g = grad(lambda xx, yy, zz: skalar(a_vec, b_func(xx, yy, zz)), x, y, z)
    return raznost(g, umnozenie(a_vec, div(b_func, x, y, z)))

# задача 1: div r, rot r, grad(a*r), (a*nabla)r
def zadacha_1():
    x, y, z = 1.5, -2.0, 0.8
    a = [2.0, -1.0, 3.0]
    r = lambda x, y, z: [x, y, z]
    print("1:",
          f"div={round(div(r, x, y, z), 4)}",
          f"rot={okrug(rot(r, x, y, z))}",
          f"grad={okrug(grad(lambda x, y, z: skalar(a, [x, y, z]), x, y, z))}",
          f"(a*nabla)r={okrug(naprav_proizv(a, r, x, y, z))}")

# задача 2: операции с phi(r)
def zadacha_2():
    x, y, z = 1.2, 0.7, -1.5
    a = [1.0, 2.0, -1.0]
    f1 = lambda x, y, z: math.sin(dlina([x, y, z]))
    f2 = lambda x, y, z: umnozenie([x, y, z], math.sin(dlina([x, y, z])))
    print("2:",
          f"grad={okrug(grad(f1, x, y, z))}",
          f"div={round(div(f2, x, y, z), 4)}",
          f"rot={okrug(rot(f2, x, y, z))}",
          f"(a*nabla)={okrug(naprav_proizv(a, f2, x, y, z))}")

# задача 3: div и rot пяти векторов
def zadacha_3():
    x, y, z = 1.0, 2.0, -1.5
    a = [2.0, -1.0, 0.5]
    b = [-1.0, 3.0, 2.0]
    polya = [
        lambda x, y, z: umnozenie(b, skalar(a, [x, y, z])),
        lambda x, y, z: umnozenie([x, y, z], skalar(a, [x, y, z])),
        lambda x, y, z: vektor_proizv(a, [x, y, z]),
        lambda x, y, z: umnozenie(vektor_proizv(a, [x, y, z]), dlina([x, y, z]) ** 2),
        lambda x, y, z: vektor_proizv([x, y, z], vektor_proizv(a, [x, y, z]))
    ]
    for i, f in enumerate(polya, 1):
        print(f"3.{i}: div={round(div(f, x, y, z), 4)} rot={okrug(rot(f, x, y, z))}")

# задача 4: операции с полями A, B и phi
def zadacha_4():
    x, y, z = 1.1, -0.8, 1.4
    a = [1.0, -2.0, 0.5]
    A = lambda x, y, z: [x * y, y * z + x, z * z - y]
    B = lambda x, y, z: [x + z, x * y, y * z]
    phi = lambda x, y, z: x * x + y * y + z * z
    phiA = lambda x, y, z: umnozenie(A(x, y, z), phi(x, y, z))
    print("4.1:", okrug(grad(lambda x, y, z: skalar(A(x, y, z), [x, y, z]), x, y, z)))
    print("4.2:", okrug(grad(lambda x, y, z: skalar(A(x, y, z), B(x, y, z)), x, y, z)))
    print("4.3:", round(div(phiA, x, y, z), 4))
    print("4.4:", okrug(rot(phiA, x, y, z)))
    print("4.5:", okrug(naprav_proizv(a, phiA, x, y, z)))

# задача 5: grad((a*r)/r^3) и rot([a x r]/r^3)
def zadacha_5():
    x, y, z = 1.2, -1.5, 2.0
    a = [2.0, 1.0, -3.0]
    f1 = lambda x, y, z: skalar(a, [x, y, z]) / (dlina([x, y, z]) ** 3)
    f2 = lambda x, y, z: umnozenie(vektor_proizv(a, [x, y, z]), 1.0 / (dlina([x, y, z]) ** 3))
    print(f"5: grad={okrug(grad(f1, x, y, z))} rot={okrug(rot(f2, x, y, z))}")

# задача 6: первое интегральное равенство
def zadacha_6():
    a = lambda x, y, z: [x * x + y, y * z, z + x]
    b = lambda x, y, z: [y + 1.0, x * z, x + y]
    lev = lambda x, y, z: slozhenie(umnozenie(b(x, y, z), div(a, x, y, z)), naprav_proizv(a(x, y, z), b, x, y, z))
    prav = lambda x, y, z, n: umnozenie(b(x, y, z), skalar(n, a(x, y, z)))
    print("6:", okrug(integral_kub(lev)), "==", okrug(integral_grani(prav)))

# задача 7: второе интегральное равенство
def zadacha_7():
    a = lambda x, y, z: [x * y, y * y + z, x * z]
    b = lambda x, y, z: [x + z, y * x, z * z + 1.0]
    lev = lambda x, y, z: slozhenie(vektor_proizv(b(x, y, z), rot(a, x, y, z)), dvoyn_nabla(a(x, y, z), b, x, y, z))
    prav = lambda x, y, z, n: umnozenie(vektor_proizv(vektor_proizv(n, a(x, y, z)), b(x, y, z)), -1.0)
    print("7:", okrug(integral_kub(lev)), "==", okrug(integral_grani(prav)))

# задача 8: [[M x nabla] x r] = -2M
def zadacha_8():
    M = [2.0, -3.0, 5.0]
    r = lambda x, y, z: [x, y, z]
    print("8:", okrug(dvoyn_nabla(M, r, 1.0, 2.0, 3.0)), "==", okrug(umnozenie(M, -2.0)))

# задача 9: rot Pi и rot rot Pi
def zadacha_9():
    c, t = 2.0, 5.0
    x, y, z = 1.5, -1.0, 2.0
    d = lambda tau: [math.sin(tau), math.cos(tau), 0.1 * tau * tau]
    pi = lambda xx, yy, zz: umnozenie(d(t - dlina([xx, yy, zz]) / c), 1.0 / dlina([xx, yy, zz]))
    rot_pi = lambda xx, yy, zz: rot(pi, xx, yy, zz, h=1e-4)
    print("9:", f"rot={okrug(rot(pi, x, y, z))} rot_rot={okrug(rot(rot_pi, x, y, z, h=1e-4))}")

if __name__ == "__main__":
    zadacha_1()
    zadacha_2()
    zadacha_3()
    zadacha_4()
    zadacha_5()
    zadacha_6()
    zadacha_7()
    zadacha_8()
    zadacha_9()