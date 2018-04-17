
def Multiply(a, b):
# Multiply numbers represented as array of digits.
    if(len(a) == 1 and len(b) == 1):
        return IntToDigits( a[0] * b[0] )
       
    return a

def Add(a, b):
# Add Numbers represented as array of digits.
    return 0

def IntToDigits(number):
# Convert number to array of digits.    
    if(number <= 0 ):
        return [0]
        
    a = number
    result = []
    while (a > 0):
        b = a % 10
        a = a // 10        
        result.append(b)
    result.reverse()    
    return result

def StringToDigits(st):
# Convert string to array of digits.
    return [int(d) for d in st]

if __name__== "__main__":
    print("=================== Integer multiplication ===============")
    a = '2'
    b = '6'
    print("{0} * {1} = {2}"
        .format(a, b,
            Multiply(
                StringToDigits(a),
                StringToDigits(b))))
    