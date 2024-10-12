getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def vind_grootste_getal():
    grootste = 0
    for i in range(len(getallen)):
        if(getallen[i] > grootste):
            grootste = getallen[i]

    print(grootste)
vind_grootste_getal()