##https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        ori_a = a
        ori_b = b
        while a != 0:
            b,a = a, b % a
            
        gcd = b
        lcm =(ori_a * ori_b)//gcd
        
        return [lcm,gcd]
