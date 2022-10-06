flag = b"flag{WH4t_gR4d3_d0_y0U_h4v3_1N_CrYp70M47H!?!?}"

def SuperSecretFunction(a, b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = SuperSecretFunction(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
