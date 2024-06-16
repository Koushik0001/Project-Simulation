def check_noma_possible(power, height, no_of_users):
    for i in range(len(power)):
        for j in range(len(power[i])):

            if power[i][j][1] <= power[i][j][0] and power[i][j][0]!=0:
                print(f"NOMA not possible for {height=} and {no_of_users=}")
                return
    
    # print(f"NOMA possible for {height=} and {no_of_users=}")