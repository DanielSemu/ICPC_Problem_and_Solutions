# x=float(input())
# count=0
# i=1
# while(i<= 100000000):
#     str1=str(i)
#     str1=str1[1:]+str1[0]
#     if i*x == int(str1):
#         count+=1
#         print(i)
#     i=i+1
# if(count==0):
#     print("No solution")


from math import gcd

class Fraction:
    @staticmethod
    def construct_from_decimal_string(string):
        a,b = string.split('.')
        return Fraction(int(a+b), 10**len(b))

    def __init__(self, a, b):
        g = gcd(a,b)
        self.a = a//g
        self.b = b//g

class TrickNumbers:

    @staticmethod
    def is_trick_number(f,k):
        d,m = divmod(f.a*k,f.b)
        return m == 0 and k == int(f'{d % 10}{str(d)[:-1]}')

    @staticmethod
    def generate_all_tricks(f):
        # Constructed in ascending order so no need for sorting
        for n in range(8):
            for last in range(1,10):
                _n = f.b * last * (10**(n+1) - 1)
                _d = (10 * f.b - f.a)
                if _d == 0:
                    break
                k,rem = divmod(_n,_d)
                if rem != 0:
                    continue
                if TrickNumbers.is_trick_number(f,k):
                    yield k

def main():
    f = Fraction.construct_from_decimal_string(input())
    #print(f.b)
    numbs = [tn for tn in TrickNumbers.generate_all_tricks(f)]
    if not numbs:
        print('No solution')
    else:
        for numb in numbs:
            print(numb)

if __name__ == "__main__":
    main()