import unittest

def algEv(a, b):
    if a < b:
        (a, b) = (b, a)
    
    if b == 0:
        return a
    else:
        return algEv(b, a % b)


class Evklid_gcd_test(unittest.TestCase):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
                  67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 
                  139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
                   
    def test_primes(self):
        for i in range(10, 150):
            for k in Evklid_gcd_test.prime_numbers:
                if algEv(i, k) != 1:
                    return False
        return True
                
    def test_n(self):
        for n in range(1, 20):
            for i in range(1, 150):
                if algEv(n, i) % n != 0 or algEv(n, i) % i != 0: 
                    return False
                else:
                    return True