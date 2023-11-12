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

    codified = codified + exponentiation(numbers,e,n)

    return encryption(codified)

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
    
    return new_message


def obtain_key(dictionary, valueS): #Obtains key from value
    for key, value in dictionary.items():
        if value == valueS:
            return key
    return None