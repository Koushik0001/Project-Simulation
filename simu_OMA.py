import math


def oma_power_opt(PRB, b, sigma, H, R):
    """
    PRB:int         # number of PRBs
    b:int           # PRB bandwidth
    sigma:float     # noise density
    H:list          # list of channel gains
    R:list          # list of minimum threshhold data rates
    """
    n = len(H)

    power = [0 for _ in range(0, n)]
    v = math.floor(PRB / n)
    if v == 0:
        print(f"OMA-Error: Number of PRBs is not enough to support {n} users!")
        return 0, None
    else:
        i = 0
        while i < n:
            avg_rate = R[i] / v
            power[i] = round(
                10 * math.log10((2 ** (avg_rate / b)) - 1)
                - H[i]
                + sigma
                + 10 * math.log10(b),
                2,
            )
            i += 1

        return v, power

