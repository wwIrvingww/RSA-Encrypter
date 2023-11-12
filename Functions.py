#Diccionario letras
codigo = {"A" : "00",
          "B" : "01",
          "C" : "02",
          "D" : "03",
          "E" : "04",
          "F" : "05",
          "G" : "06",
          "H" : "07",
          "I" : "08",
          "J" : "09",
          "K" : "10",
          "L" : "11",
          "M" : "12",
          "N" : "13",
          "O" : "14",
          "P" : "15",
          "Q" : "16",
          "R" : "17",
          "S" : "18",
          "T" : "19",
          "U" : "20",
          "V" : "21",
          "W" : "22",
          "X" : "23",
          "Y" : "24",
          "Z" : "25"}

mensajes = {}

#===================================================
#General
#===================================================

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

def extended_gcd(a,b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x,x

def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception("El inverso modular no existe")
    else:
        return x % m

def factorizar(n):
    factores = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1

    return factores

def exponentiation(numbers,e,n): #Calculate module for power
    if numbers[0] == "0":
        numbers = numbers[1:]
    
    value = mpower2(int(numbers), int(e), int(n))
    if len(str(value)) == 4:
        return str(value)
    elif len(str(value)) == 3:
        return "0"+str(value)
    elif len(str(value)) == 2:
        return "00"+str(value)
    elif len(str(value)) == 1:
        return "000"+str(value)
    

def mpower2(b,n,m): #b -> base, n -> exponente, m -> modulo
    if n == 0:
        return 1
    if n % 2 == 0:
        return mpower2(b,n/2,m)**2 % m
    if n % 2 != 0:
        return (b*mpower2(b,(n-1)/2,m)**2 % m)
    
def obtain_key(dictionary, valueS): #Obtains key from value
    for key, value in dictionary.items():
        if value == valueS:
            return key
    return None

#=========================================================
#Encriptación
#=========================================================

def mensaje(message,e,n): #Encodes the message and returns the message encoded 
    message = message.upper()
    if len(message) % 2 == 0:
        message = message.upper() + "H"
    codified = ""
    numbers = ""
    for i in message:
        if len(numbers) % 4 != 0 and numbers != "":
            numbers = numbers + codigo[i]
        elif len(numbers) % 4 == 0 and numbers != "":
            codified = codified + exponentiation(numbers,e,n)
            if i != " ":
                numbers = codigo[i]

        elif numbers == "" and i != " ":
            numbers = codigo[i]
        
        
        if i == " ":
            codified = codified + " "
            numbers = ""

    codified = codified + exponentiation(numbers,e,n)

    return encryption(codified)

    
def encryption(codified): #Write the codified message from the gotten numbers
    new_message = ""
    message_number = ""
    for i in codified:
        if (len(message_number) % 2 != 0 and message_number != "") or (i == "0" and len(message_number) % 2 != 0):
            message_number = message_number + i
        elif len(message_number) % 2 == 0 and message_number != "":
            if int(message_number) > 25:
                value = str(int(message_number) % 26)

                if len(value) == 1:
                    message_number = "0" + value

                else: 
                    message_number = value

            new_message = new_message + obtain_key(codigo,message_number)
            if i != " ":
                message_number = i
            else:
                message_number = ""

        elif message_number == "" and i != " ":
            message_number = i

        
        if i == " ":
            new_message = new_message + " "

    if int(message_number) > 25:
                value = str(int(message_number) % 26)
                if len(value) == 1:
                    message_number = "0" + value
                else: 
                    message_number = value
    new_message = new_message + obtain_key(codigo,message_number)
    
    mensajes[new_message] = codified

    return new_message

#========================================================
#Desencriptación
#========================================================

#Private key
def privateKey(e,n):
    factors = factorizar(n)
    phi = phiValue(factors[0],factors[1])
    return modinv(e, phi)

def mensajeC(message, e, n): #Write the message from the gotten numbers
    d = privateKey(e,n)
    if message in mensajes:
        message = mensajes[message]
        new_message = ""
        message_number = ""
        for i in message:
            if (len(message_number) % 4 != 0 and message_number != "") or (i == "0" and len(message_number) % 2 != 0):
                message_number = message_number + i
            elif len(message_number) % 4 == 0 and message_number != "":
                if int(message_number) > 25:
                    value = str(int(message_number))

                    if len(value) == 3:
                        message_number = "0" + value

                    else: 
                        message_number = value

                new_message = new_message + exponentiation(message_number,d,n)
                if i != " ":
                    message_number = i
                else:
                    message_number = ""

            elif message_number == "" and i != " ":
                message_number = i

            
            if i == " ":
                new_message = new_message + " "

        if int(message_number) > 25:
                    value = str(int(message_number))
                    if len(value) == 1:
                        message_number = "0" + value
                    else: 
                        message_number = value
        new_message = new_message + exponentiation(message_number,d,n)

        return desencryption(new_message)
    else:
        return "El mensaje no se puede decodificar"
    
def desencryption(codified): #Write the codified message from the gotten numbers
    new_message = ""
    message_number = ""
    for i in codified:
        if (len(message_number) % 2 != 0 and message_number != "") or (i == "0" and len(message_number) % 2 != 0):
            message_number = message_number + i
        elif len(message_number) % 2 == 0 and message_number != "":
            if int(message_number) > 25:
                value = str(int(message_number) % 26)

                if len(value) == 1:
                    message_number = "0" + value

                else: 
                    message_number = value

            new_message = new_message + obtain_key(codigo,message_number)
            if i != " ":
                message_number = i
            else:
                message_number = ""

        elif message_number == "" and i != " ":
            message_number = i

        
        if i == " ":
            new_message = new_message + " "

    if int(message_number) > 25:
                value = str(int(message_number) % 26)
                if len(value) == 1:
                    message_number = "0" + value
                else: 
                    message_number = value
    new_message = new_message + obtain_key(codigo,message_number)

    if new_message[len(new_message)-1] == "H":
        new_message = new_message[:-1]

    return new_message