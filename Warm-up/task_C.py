import math


def move_to_center(x, y, delta):
    if x == 0 and y == 0:
        return x, y

    if x == 0:
        if y > 0:
            return x, y - delta
        else:
            return x, y + delta

    if y == 0:
        if x > 0:
            return x - delta, y
        else:
            return x + delta, y

    k = y / x
    x_delta = delta / math.sqrt(1 + k ** 2)

    if x > 0:
        return x - x_delta, (x - x_delta) * k
    else:
        return x + x_delta, (x + x_delta) * k


def shortest_path(xa, ya, xb, yb):
    rad_a = math.sqrt(xa ** 2 + ya ** 2)
    rad_b = math.sqrt(xb ** 2 + yb ** 2)

    if xa * yb == xb * ya:
        if xa * xb < 0 or ya * yb < 0:
            return rad_a + rad_b
        else:
            return abs(rad_b - rad_a)

    way_1 = rad_a + rad_b

    alpha = math.atan2(ya, xa)
    beta = math.atan2(yb, xb)

    if alpha * beta < 0:
        if abs(alpha) + abs(beta) < math.pi:
            phi = abs(alpha) + abs(beta)
        else:
            phi = math.pi * 2 - (abs(alpha) + abs(beta))
    else:
        phi = abs(alpha - beta)

    way_2 = abs(rad_b - rad_a)
    way_2 += rad_b * phi if rad_b < rad_a else rad_a * phi

    if way_2 < way_1:
        return way_2
    else:
        return way_1


def main():
    xa, ya, xb, yb = map(int, input().split(' '))
    print(f"{shortest_path(xa, ya, xb, yb):.6f}")


if __name__ == '__main__':
    main()