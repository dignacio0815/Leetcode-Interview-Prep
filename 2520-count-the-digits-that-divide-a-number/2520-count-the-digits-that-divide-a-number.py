class Solution:
    def countDigits(self, num: int) -> int:
        counter = 0
        temp = num
        while temp > 0:
            divisor = temp % 10
            if (num % divisor == 0):
                counter += 1
            temp = temp // 10
        return counter