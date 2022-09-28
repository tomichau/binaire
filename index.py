############
#    By    #
# TOMICHAU #
############
def db(dec):
    itsNull = 0
    numbers = []
    number = 0
    nbBoites = dec
    nbReste = 0
    while itsNull < 1 :
        nbReste = nbBoites % 2
        nbBoites = nbBoites // 2

        if nbReste > 0 :
            number = 1
        else:
            number = 0
        
        numbers.append(str(number))

        if nbBoites == 0:
            itsNull = 1
        else:
            itsNull = 0
    
    numbers.reverse()
    return("".join(numbers))
    
def bd(binaire):
    binaire = str(binaire)
    binaire = reverses(binaire)
    
    calculate = 0
    n = 0 
    for i in binaire:
        if i == '1':
           calculate = calculate + 2**n
        else:
            calculate = calculate + 0
        n += 1
    return calculate

def dh(dec):
    itsNull = 0
    numbers = []
    number = 0
    nbBoites = dec
    nbReste = 0
    while itsNull < 1 :
        nbReste = nbBoites % 16
        nbBoites = nbBoites // 16

        if nbReste ==  10:
            number = "A"
        elif nbReste == 11:
            number = "B"
        elif nbReste == 12:
            number = "C"
        elif nbReste == 13:
            number = "D"
        elif nbReste == 14:
            number = "E"
        elif nbReste == 15:
            number = "F"
        else:
            number = nbReste
        
        numbers.append(str(number))

        if nbBoites == 0:
            itsNull = 1
        else:
            itsNull = 0
    
    numbers.reverse()
    return("".join(numbers))

def hd(hex):
    hex= str(hex)
    hex = reverses(hex)
    
    calculate = 0
    n = 0 
    for i in hex:

        if hex[n] == "A" or hex[n] == "a":
           calculate = calculate + 10*16**n
        elif hex[n] == "B" or hex[n] == "b":
            calculate = calculate + 11*16**n
        elif hex[n] == "C" or hex[n] == "c":
            calculate = calculate + 12*16**n
        elif hex[n] == "D" or hex[n] == "d":
            calculate = calculate + 13*16**n
        elif hex[n] == "E" or hex[n] == "e":
            calculate = calculate + 14*16**n
        elif hex[n] == "F" or hex[n] == "f":
            calculate = calculate + 15*16**n
        else:
            calculate = calculate + int(hex[n])*16**n
        n += 1
    return calculate

def hb(hex):
    return db(hd(hex))

def bh(bin):
    return dh(bd(bin))

def reverses(s):
    new_string = ''
    index = len(s)
    while index:
        index -= 1                   
        new_string += s[index] 
    return new_string
