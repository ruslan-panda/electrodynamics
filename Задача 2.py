import math

# складывает два вектора
def slozhenie(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

# ищет векторное произведение двух векторов
def vektor_proizv(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

# ищет дивергенцию 2D поля
def div_2d(f, x, y, h=1e-5):
    ux = (f(x + h, y)[0] - f(x - h, y)[0]) / (2 * h)
    uy = (f(x, y + h)[1] - f(x, y - h)[1]) / (2 * h)
    return ux + uy

# ищет ротор 2D поля
def rot_2d(f, x, y, h=1e-5):
    uy = (f(x + h, y)[1] - f(x - h, y)[1]) / (2 * h)
    ux = (f(x, y + h)[0] - f(x, y - h)[0]) / (2 * h)
    return uy - ux

# строит матрицу бесконечно малого поворота
def matrica_povorota(dphi):
    dx, dy, dz = dphi
    return [
        [1.0, dz, -dy],
        [-dz, 1.0, dx],
        [dy, -dx, 1.0]
    ]

# определяет тип вектора по знаку при инверсии
def tip_vektora(znak):
    if znak == -1:
        return "полярный"
    return "аксиальный"

# определяет тип скаляра по знаку при инверсии
def tip_skalara(znak):
    if znak == 1:
        return "скаляр"
    return "псевдоскаляр"

# задача 8: матрица бесконечно малого поворота
def zadacha_8():
    m = matrica_povorota([0.001, -0.002, 0.003])
    print("8:", m)

# задача 9: тип вектора набла
def zadacha_9():
    print("9:", tip_vektora(-1))

# задача 10: тип градиента
def zadacha_10():
    print("10:", tip_vektora(-1 * 1), "|", tip_vektora(-1 * -1))

# задача 11: тип div и rot
def zadacha_11():
    print("11: div=" + tip_skalara(-1 * -1), "rot=" + tip_vektora(-1 * -1))
    print("11: div=" + tip_skalara(-1 * 1), "rot=" + tip_vektora(-1 * 1))

# задача 12: скаляры и псевдоскаляры
def zadacha_12():
    ist = -1
    aks = 1
    print("12:",
          tip_skalara(ist * ist),
          tip_skalara(ist * aks),
          tip_skalara(ist * ist * ist),
          tip_skalara(ist * aks * aks),
          tip_skalara(aks * aks * aks))

# задает шесть двумерных полей
def polya():
    return [
        ("a", lambda x, y: [-(y + 3.5) / (x * x + (y + 3.5) ** 2), x / (x * x + (y + 3.5) ** 2)]),
        ("b", lambda x, y: [0.0, math.exp(-x * x / 4.0)]),
        ("c", lambda x, y: [x / math.sqrt(x * x + y * y), y / math.sqrt(x * x + y * y)]),
        ("d", lambda x, y: [-x, -y]),
        ("e", lambda x, y: [-(y + 3.5) / math.sqrt(x * x + (y + 3.5) ** 2), x / math.sqrt(x * x + (y + 3.5) ** 2)]),
        ("f", lambda x, y: [-y, x])
    ]

# задача 2: проверяет div и rot для каждого поля
def zadacha_2():
    for name, f in polya():
        d = round(div_2d(f, 1.0, 1.0), 4)
        r = round(rot_2d(f, 1.0, 1.0), 4)
        print(f"2.{name}: div={d} rot={r}")

if __name__ == "__main__":
    zadacha_8()
    zadacha_9()
    zadacha_10()
    zadacha_11()
    zadacha_12()
    zadacha_2()