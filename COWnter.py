def countCows(years):
    try:
        int(years)
    except:
        return None

    booming_cows = 0;
    cows_4 = 1;
    cows_3 = 0;
    cows_2 = 0;
    cows_1 = 0;

    for year in range(int(years)):
        booming_cows+=cows_2
        cows_2 = cows_3
        cows_3 = cows_4
        cows_4 = booming_cows

    return cows_1+cows_2+cows_3+cows_4+booming_cows

while(True):
    print("how many years?")
    print("cows left: " + str(countCows(input())))