#Calculating n
def nValue(p, q):
    return p*q

#Calculating phi
def phiValue(p, q):
    return (p-1)*(q-1)

#Euclides Algorithm for mcd = 1
def euclides(e, phi): #phi > e
    if (phi % e) != 0:
        if e == 1:
            return True
        else:
            return False
    else:
        mod = phi % e
        euclides(mod, e)
    