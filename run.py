brText = "--------------------------------------------------------------------------------------------------------------------------------"

def br():
    print(brText)

def collatz(seed: int, verbose: bool, log: bool):
    originalSeed = seed
    iterations = 0
    fileName = "log.txt"
    seq = 404

    if log:
        f1 = open(fileName, "a")
        f1.write("seed = " + str(originalSeed) + "\n")
        f1.close()

    while True:
        if verbose:
            print(seed)

        if (seed == 1):
            seq = 1
            break
        if (seed == 0):
            seq = 0
            break
        if (seed == -1):
            seq = -1
            break
        if (seed == -5):
            seq = -5
            break
        if (seed == -17):
            seq = -17
            break

        if (seed % 2) == 0:
            seed = seed // 2
        else:
            seed = (seed * 3) + 1
        
        iterations += 1

    if verbose:
        print("seed = " + str(originalSeed))
        print("iterations = " + str(iterations))
        print("seq = " + str(seq))
        br()
    
    if log:
        f2 = open(fileName, "a")
        f2.write("iterations = " + str(iterations) + "\n")
        f2.write("seq = " + str(seq) + "\n")
        f2.write(brText + "\n")
        f2.close()
    
    return iterations
