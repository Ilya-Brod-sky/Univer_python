import unittest

def prime(a):
    # 1 and 2 are strange numbers, so let's think they are prime
    
    if a == 2:
        return True
    p = 1
    
    while p <= a**0.5:
        p += 1
        if a % p == 0:
            return False
   
    return True

class prime_numbers_test(unittest.TestCase):

    def test_1(self):
        if prime(1) != True: return False #let's think 1 is a prime number
    
    def test_2(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        for i in range(2, 211):
            if i in prime_list:
                if prime(i) != True: return False
            else:
                if prime(i) != False: return False
        return True

