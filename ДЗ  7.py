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

# задача 1: проводящая сфера
def zadacha_1():
    R, Q = 2.0, 10.0
    e_in = 0.0
    e_out = Q / (4.0 * 4.0)
    print(f"1: r<R: E={e_in} | r>R: E={round(e_out, 4)}")

# задача 2: проводящий цилиндр
def zadacha_2():
    R, sigma = 2.0, 1.5
    e_in = 0.0
    e_out = 4 * math.pi * sigma * R / 4.0
    print(f"2: a<R: E={e_in} | a>R: E={round(e_out, 4)}")

# задача 3: цилиндр с объемной плотностью и нить
def zadacha_3():
    R, rho = 2.0, 1.0
    e_in = 2 * math.pi * rho * 1.0
    e_out = 2 * math.pi * rho * R * R / 4.0
    tau = math.pi * R * R * rho
    e_nit = 2 * tau / 4.0
    print(f"3: a<=R: E={round(e_in, 4)} | a>R: E={round(e_out, 4)} | нить: E={round(e_nit, 4)}")

# задача 4: шаровой слой
def zadacha_4():
    R1, R2, rho = 1.0, 3.0, 1.0
    e1 = 0.0
    e2 = (4.0 / 3.0) * math.pi * rho * (2.0 ** 3 - R1 ** 3) / (2.0 ** 2)
    e3 = (4.0 / 3.0) * math.pi * rho * (R2 ** 3 - R1 ** 3) / (4.0 ** 2)
    print(f"4: r<=R1: E={e1} | R1<r<=R2: E={round(e2, 4)} | r>R2: E={round(e3, 4)}")

# задача 5: цилиндрический слой
def zadacha_5():
    R1, R2, rho = 1.0, 3.0, 1.0
    e1 = 0.0
    e2 = 2 * math.pi * rho * (2.0 ** 2 - R1 ** 2) / 2.0
    e3 = 2 * math.pi * rho * (R2 ** 2 - R1 ** 2) / 4.0
    print(f"5: a<=R1: E={e1} | R1<a<=R2: E={round(e2, 4)} | a>R2: E={round(e3, 4)}")

# строит список зарядов в вершинах правильного N-угольника
def mnogougolnik(N):
    spisok = []
    for k in range(N):
        u = 2 * math.pi * k / N
        q = 1.0 if k % 2 == 0 else -1.0
        spisok.append((q, [math.cos(u), math.sin(u), 0.0]))
    return spisok

# задача 6: потенциал и напряженность N-угольника для N=8 и N=32
def zadacha_6():
    for N in [8, 32]:
        z = mnogougolnik(N)
        phi, e = pole_sistemi(z, [0.5, 0.2, 0.0])
        print(f"6 (N={N}): phi={round(phi, 4)} E={round(dlina(e), 4)}")

# ищет угол отклонения нити методом деления пополам
def nayti_ugol(A):
    lev, prav = 0.0, 100.0
    for _ in range(80):
        ser = 0.5 * (lev + prav)
        if ser ** 3 - A * (ser + 1.0) > 0:
            prav = ser
        else:
            lev = ser
    return math.degrees(math.atan(0.5 * (lev + prav)))

# задача 7: зависимость угла от заряда
def zadacha_7():
    m, g, L = 1.0, 980.0, 10.0
    for q in [100, 300, 500, 800, 1000]:
        A = (q * q) / (4.0 * m * g * L * L)
        print(f"7 (q={q}): alpha={round(nayti_ugol(A), 2)}")

if __name__ == "__main__":
    zadacha_1()
    zadacha_2()
    zadacha_3()
    zadacha_4()
    zadacha_5()
    zadacha_6()
    zadacha_7()