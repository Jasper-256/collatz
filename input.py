from sys import exit
import run

print("input a collatz seed or type exit to end program")
run.br()

while True:
    while True:
        inp = input("seed = ")

        if inp == "exit":
            exit(0)
        elif inp.lstrip('-').isdigit():
            seed = int(inp)
            break
        else:
            print(inp + " is not an integer, please try again")
            run.br()

    run.collatz(seed, True, False)
