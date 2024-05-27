import math


def noma_power_opt(PRB, b, sigma, H, R):
    """
    PRB:int         # number of PRBs
    b:int           # PRB bandwidth
    sigma:float     # noise density
    H:list          # list of channel gains
    R:list          # list of minimum threshhold data rates
    """
    n = len(H)
    users = [f"u_{i}" for i in range(1, n + 1)]

    x = [0 for _ in range(0, n)]
    v = [0 for _ in range(0, n)]
    association = [[0 for _ in range(0, n)] for _ in range(0, n)]
    power = [[[0, 0] for _ in range(0, n)] for _ in range(0, n)]
    user_first = [0 for _ in range(0, n)]
    user_second = [0 for _ in range(0, n)]

    H, R, users = zip(*sorted(zip(H, R, users)))

    for i in range(0, n):
        x[i] = (R[i] / math.log10(abs(H[i])))

    sum_x = 0
    for i in range(0, n):
        sum_x += x[i]

    for i in range(0, n):
        v[i] = math.ceil(x[i] * 2 * PRB / sum_x)
    

    r = PRB
    k = 0
    l = math.ceil(n / 2)
    count = n

    while r > 0 and count >= 2:
        while v[k % n] == 0:
            k += 1
        while v[l % n] == 0:
            l += 1
        i = min(k % n, l % n)
        j = max(l % n, k % n)
        if i != j:
            association[i][j] += 1
            user_first[i] += 1
            user_second[j] += 1
            r -= 1
            v[i] -= 1
            v[j] -= 1
        else:
            l = k + math.ceil(n / 2)
        count = len(list(filter(lambda x: x != 0, v)))
        k += 1
        l += 1

    i = 0
    while i < n:
        if user_first[i] != 0:
            total_prb = user_first[i] + user_second[i]
            avg_rate = R[i] / total_prb
            power_first = round(
                10 * math.log10((2 ** (avg_rate / b)) - 1)
                - H[i]
                + sigma
                + 10 * math.log10(b),
                2,
            )
            j = 0
            while j < n:
                if association[i][j] != 0:
                    power[i][j][0] = power_first
                j += 1
        i += 1

    i = 0
    while i < n:
        if user_second[i] != 0:
            total_prb = user_second[i] + user_first[i]
            avg_rate = R[i] / total_prb
            j = 0
            while j < n:
                if association[j][i] != 0:
                    power[j][i][1] = round(
                        10 * math.log10((2 ** (avg_rate / b)) - 1)
                        + power[j][i][0]
                        + sigma
                        + 10 * math.log10(b),
                        2,
                    )
                j += 1
        i += 1

    return association, power


if __name__ == "__main__":
    n = 6
    association, power = noma_power_opt(
        183,
        180000,
        -174,
        [
            -6.48906303e-02,
            -4.20153889e-02,
            -9.34773156e-02,
            -5.06082728e-02,
            -1.81410630e-08,
            -1.04016670e-01,
        ],
        [200, 120, 240, 120, 290, 124],
    )
    total_power = 0
    for i in range(0, n):
        for j in range(0, n):
            total_power += association[i][j] * (
                (10 ** (power[i][j][0] / 10)) + (10 ** (power[i][j][1] / 10))
            )
    print(f"Association Matrix: {association}\n")
    print(f"Power Matrix: {power}\n")
    print(f"Total Power consumed is: {total_power} mW")
