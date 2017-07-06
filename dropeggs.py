import sys


#initialize a matrix with max floors Fmax that can be covered with D drops and B breaks,
# only calculating till B=32 and D= 100000(approximated for Fmax(D,2)  -1,  10000 < max-possible-D >100000, to optimize memory usage) because Fmax = -1 for all cases above
def initMatrix():

    #only one floor can be guaranteed to be solvable if only one drop is allowed
    x = 1
    while(x < 33): 
      fMatrix[1][x] = 1;
      x += 1


    #x floors can be guaranteed to be solvable if only x drops and one break is allowed
    x = 1
    while x <  100001:
        fMatrix[x][1] = x;
        x += 1


    maxFval = 2**32


    """for other cases, fMatrix[d][b] = 1  //one drop required to test a floor
                                        + fMatrix[d - 1][b]  //if the egg doesnt break, we can test floors above current with d-1 drops and b breaks left
                                        + fMatrix[d - 1][b - 1] //if the egg breaks, we can test floors below current with d-1 drops and b breaks left
                                        """
    id = 2
    while(id < 100001):
        ib = 2
        while (ib < 33):
            if (ib <= id):
                if fMatrix[id - 1][ib] == -1 or fMatrix[id - 1][ib - 1] == -1:
                    fMatrix[id][ib] = -1

                else:
                    fMatrix[id][ib] = 1 + fMatrix[id - 1][ib] + fMatrix[id - 1][ib - 1]

                    if fMatrix[id][ib] < 0 or fMatrix[id][ib] >= maxFval:
                        fMatrix[id][ib] = -1
            else:
                fMatrix[id][ib] = fMatrix[id][id];

            ib += 1
        id += 1


#gets F max for D drops and B breaks from the F matrix
def  Fmax(D, B):
    if D > 32 and  B > 32:
        fMax = -1

    elif B > D:
        fMax = fMatrix[D][D]

    elif B == 1:
        fMax = D

    else:
        fMax = fMatrix[D][B]

    return fMax


#gets min drops required by checking Fmax till F while incrementing the number drops for given number of breaks 
def Dmin(F, B):
    if (B > 32):
        B = 32;

    dMin = 1 
    while(fMatrix[dMin][B] < F):
        dMin += 1

    return dMin



#gets min breaks required by incrementally checking the number of breaks for given number of drops till  Fmax < F
def Bmin(F, D):
    if D >= F:
        bMin = 1

    else:
        if D > 100000:
            D = 100000

        bMin = 1
        while(fMatrix[D][bMin] < F and fMatrix[D][bMin] != -1):
            bMin += 1

    return bMin
    


fMatrix = [[0 for x in range(33)] for y in range(100001)] 
initMatrix()


filename = sys.argv[1]
infile = file(filename, 'r')
T = int(infile.readline().strip())

for caseNum in range(1, T+1):
    line = infile.readline().strip()
    f, d, b = map(int, line.split())

    fD = Fmax(d, b)
    dMin = Dmin(f,b)
    bMin = Bmin(f,d)
    
    print "Case #%d: %d %d %d" % (caseNum, fD, dMin, bMin)
