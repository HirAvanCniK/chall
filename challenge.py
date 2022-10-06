import random, time
from secret import SuperSecretFunction, flag
from pwn import log
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def solve(ct, realK, k, realIv, iv):
        try:
            if realK != k or realIv != iv:
                Nope = int("Nope!")
            cipher = AES.new(k, AES.MODE_CBC, iv)
            flag_dec = cipher.decrypt(ct)
            if flag_dec[:-2] == flag:
                print("Complimenti ecco la tua flag:", flag)
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

    key = random.randbytes(16)
    iv = random.randbytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag_enc = cipher.encrypt(pad(flag, 16))

    k = input("key? (esadecimale): ")
    signal(sec)

    IV = input("iv? (esadecimale): ")
    signal(sec)

    solve(flag_enc, key, bytes.fromhex(k), iv, bytes.fromhex(IV))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()