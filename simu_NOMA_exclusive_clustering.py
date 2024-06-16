import math
def dot_product(v, half_1st, half_2nd):
    dot_product = sum(v[i] * v[j] for i, j in zip(half_1st, half_2nd))
    return dot_product

def ex_noma_power_opt(PRB, b, sigma, H, R):
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
        x[i] = (R[i] / abs(H[i]))

    sum_x = 0
    for i in range(0, n):
        sum_x += x[i]

    for i in range(0, n):
        if(i < n/2):
            v[i] = math.ceil(x[i] * 2 * PRB / sum_x)
        else:
            estimate = math.ceil(x[i] * 2 * PRB / sum_x)
            v[i] = estimate if (R[i]/estimate) >= b else math.floor(R[i]/b)
    

    # User Clustering
    sorted_indices = sorted(range(len(v)), key=lambda x: v[x])
    half_1st = list()
    half_2nd = list()
    for u in sorted_indices:
        if u < math.ceil(n / 2):
            half_1st.append(u)
        else:
            half_2nd.append(u)

    # print(f"{half_1st=}")
    # print(f"{half_2nd=}")
    # print(f"{v=}")

    r = PRB
    k = 0
    l = 0

    while r > 0 and dot_product(v, half_1st, half_2nd)!=0:
        
        while v[half_1st[k % math.ceil(n/2)]] == 0 or v[half_2nd[l % math.ceil(n/2)]] == 0:
            k += 1
            l += 1

        i = half_1st[k % math.ceil(n/2)]
        j = half_2nd[l % math.ceil(n/2)]

        association[i][j] += 1
        user_first[i] += 1
        user_second[j] += 1
        r -= 1
        v[i] -= 1
        v[j] -= 1
    
        k += 1
        l += 1


    # Power Allocation

    # Power Allocation - first user
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


    # Power Allocation - second user
    i = 0
    while i < n:
        if user_second[i] != 0:
            total_prb = user_second[i] + user_first[i]
            avg_rate = R[i] / total_prb
            j = 0
            while j < n:
                if association[j][i] != 0:
                    interfering_power_linear = 10 ** (power[j][i][0] / 10)
                    H_linear = 10 ** (H[i] / 10)
                    sigma_linear = 10 ** (sigma /10)
                    power[j][i][1] = round(
                        10 * math.log10((2 ** (avg_rate / b)) - 1)
                        + 10 * math.log10(interfering_power_linear * H_linear + sigma_linear * b)
                        - H[i],
                        2,
                    )
                j += 1
        i += 1

    return association, power

if __name__=='__main__':
    association, power = ex_noma_power_opt(11, 136, -145, [0.3, 0.9, 0.12, 0.5, 0.4, 0.8], [10, 20, 40, 10, 12, 1])
    print(f"{association=}")
    print(f"{power=}")