import sys
import math

class Number:

    def Clone(self):
        clon = Number()
        clon.digits = self.digits[:]
        clon.sign = self.sign
        return clon

    def _intToDigits(self, number):
        # Convert number to array of digits.
        if(number <= 0):
            return [0]

        a = number
        result = []
        while (a > 0):
            b = a % 10
            a = a // 10
            result.append(b)
        #result.reverse()
        return result

    def __init__(self):
        self.digits = [0]
        self.sign = 1

    def __getitem__(self, key):
        return self.digits[key]

    def __str__(self):
        self._trim()
        reversed = self.digits[:]
        reversed.reverse()
        s = "".join(map(str, reversed))
        if(self.sign < 0):
            s = "-" + s
        return s

    def __add__(self, other):
        self._trim()
        other._trim()
        if(self.sign == other.sign):
            length = max(len(self.digits), len(other.digits))
            self.digits = self.digits + [0] * (length - len(self.digits))
            other.digits = other.digits + [0] * (length - len(other.digits))
            resultArray = [0] * (length + 1)
            for i in range(length):
                sum = self[i] + other[i] + resultArray[i]
                sumDigits = self._intToDigits(sum)
                resultArray[i] = sumDigits[0]
                if (sum >= 10):
                    resultArray[i+1] = sumDigits[1]
            result = Number()
            result.FromDigits(resultArray, self.sign)

        elif(self.sign > 0 and other.sign < 0):
            b = other.Clone()
            b.sign = 1
            result = self - b
        elif(self.sign < 0 and other.sign > 0):
            a = self.Clone()
            a.sign = 1
            result = other - a

        result._trim()
        return result

    def _trim(self):
        trimming = True
        result = []
        reversed = self.digits[:]
        reversed.reverse()
        for d in reversed:
            if (trimming and d == 0):
                continue
            elif(d != 0):
                trimming = False
            result.append(d)
        result.reverse()
        self.digits = result

    def  __sub__(self, other):
        self._trim()
        other._trim()
        
        result = Number()
        
        if(self.sign<0 and other.sign>0):
            a = self.Clone()
            a.sign = 1
            result = a + other
            result.sign = - 1
            return result

        elif(self.sign<0 and other.sign<0):
            a = self.Clone()
            b = other.Clone()
            a.sign = 1
            b.sign = 1
            result = b - a
            return result

        elif(self.sign > 0 and other.sign < 0):
            b = other.Clone()
            b.sign = 1
            result = self + b
            return result

        elif(self.sign > 0 and other.sign > 0):
            isSignReversed = False
            a = self.digits[:]
            b = other.digits[:]

            
            length = max(len(a), len(b))
            a = a + [0] * (length - len(a) + 1)
            b = b + [0] * (length - len(b) + 1)
            resultArray = [0] * (length + 2)


            ra = a[:]
            ra.reverse()
            rb = b[:]
            rb.reverse()
            if( ra < rb):
                isSignReversed = True
                c = a[:]
                a = b[:]
                b = c[:]


            for i in range(length):
                m = a[i] - b[i]
                if(m >= 0):
                    resultArray[i] = m
                else:
                    resultArray[i] = 10 + m
                    a[i+1] = a[i+1] - 1
            result.FromDigits(resultArray, 1)
            if(isSignReversed):
                result.sign = -1
            result._trim()
        return result                

    def _toInt(self):
        result = 0;
        for p, val in enumerate(self.digits):
            result = result + val * math.pow(10 , p);
        return result

    def __mul__(self, other):
        #print("{0} * {1}".format(self, other))
        self._trim()
        other._trim()

        power = max(len(self.digits), len(other.digits))
        self.digits = self.digits + [0] * (power - len(self.digits))
        other.digits = other.digits + [0] * (power - len(other.digits))
        halfPower = power // 2

        if(power < 10):
            a = self._toInt()
            b = other._toInt()
            c = int(a*b)
            result = Number()
            # result.FromDigits(self._intToDigits(self[0] * other[0]))
            result.digits = self._intToDigits(c)
            return result

        a, b, c, d = Number(), Number(), Number(), Number()
        
        selfReversed = self.digits[:]
        #selfReversed.reverse()
        a.FromDigits(selfReversed[halfPower:])
        b.FromDigits(selfReversed[:halfPower])
        
        otherReversed = other.digits[:]
        #otherReversed.reverse()
        c.FromDigits(otherReversed[halfPower:])
        d.FromDigits(otherReversed[:halfPower])

        ac = a * c
        #print("ac = {0} * {1} = {2}".format(a, c, ac))
        bd = b * d
        #print("bd = {0} * {1} = {2}".format(b, d, bd))
        abcd = (a + b) * (c + d)
        #print("abcd = ({0} + {1}) * ({2} + {3}) = {4}".format(a, b, c, d, abcd))

        acPow = Number()
        acPow.FromDigits([0] * power + ac.digits, 1)
        #print("acˆ{0} = {1}".format(power, acPow))
        second = abcd - ac - bd
        second.digits = [0] * halfPower + second.digits

        result = acPow + second + bd
        #print("{0} * {1} = {2}".format(self, other, result))
        return result

    def FromString(self, st, sn = 1):
        inverted = [int(d) for d in st]
        inverted.reverse()
        self.digits = inverted
        self.sign = sn
    
    def FromInt(self, value):
        if(value < 0):
            self.sign = -1
            value *= -1
        self.digits = IntToDigits(value)
    
    def FromDigits(self, d, s = 1):
        self.digits = d[:]
        self.sign = s    

if __name__== "__main__":
    print("=================== Integer multiplication ===============")
    # a = Number()
    # a.FromString("123456789")
    # b = Number()
    # b.FromString("123456789")


# 8539734222673567065463550869546574495034888536086947207063018477067743144893212717960214626108649073011374895871952806582723184

    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(10000)
    print("=================== Integer multiplication ===============")
    a = Number()
    a.FromString(
        "3141592653589793238462643383279502884197169399375105820974944592")
    b = Number()
    b.FromString(
        "2718281828459045235360287471352662497757247093699959574966967627")

    # res = a - b
    # print("{0} - {1} = {2}" .format(a, b, res))

    # res = a + b
    # print("{0} + {1} = {2}" .format(a, b, res))

    res = a * b
    print("{0} * {1} = /n{2}" .format(a, b, res))

   

    
