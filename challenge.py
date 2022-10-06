import random, time
from secret import SuperSecretFunction, flag
from pwn import log
from Crypto.Util.number import isPrime, bytes_to_long, long_to_bytes

def solve(ct, realN, realPhi, realE, realD, n, phi, e, d):
        try:
            if realN != n or realPhi != phi or realE != e or realD != d:
                Nope = int("Nope!")
            flag_dec = long_to_bytes(pow(ct, d, n))
            if flag_dec == flag:
                print("Complimenti ecco la tua flag:", flag_dec)
            else:
                Nope = int("Nope!")
        except:
            return log.critical("I dati inseriti non sono giusti.")

def signal(tempo):
    tempo_max = tempo + 15
    tempo_now = round(time.time())
    if tempo_now >= tempo_max: return exit()

def main():
    a, b, x, y = 0, 0, 0, 0

    while a == b or x == 0 or y == 0 or x == y:
        a = random.randint(5000, 100000)
        b = random.randint(5000, 100000)
        mcd, x, y = SuperSecretFunction(a, b)

    random.seed(y**x)

    sec = round(time.time())

    print(f"a = {a}\nb = {b}")

    print("Trova i valori di 'x' e 'y' tali che a*x + b*y = GCD(a, b)")
    x1 = int(input("x?: "))
    signal(sec)
    y1 = int(input("y?: "))
    signal(sec)
    if x1 != x or y1 != y: return log.critical("I valori x/y sono errati!")
    else: print("Corretto!\n\nOra dovrai indicarmi il valore delle variabili sotto indicate, sapendo come sono state calcolate nel codice.\n")

    p, q, e = 4, 4, 4

    while isPrime(p) == False:
        p = random.randint(5000, 100000)
    while isPrime(q) == False:
        q = random.randint(5000, 100000)
    while isPrime(e) == False:
        e = random.randint(5000, 100000)

    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    flag_enc = pow(bytes_to_long(flag), e, n)

    e1 = int(input("e?: "))
    signal(sec)

    n1 = int(input("n?: "))
    signal(sec)

    phi1 = int(input("phi?: "))
    signal(sec)

    d1 = int(input("d?: "))
    signal(sec)

    solve(flag_enc, n, phi, e, d, n1, phi1, e1, d1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()