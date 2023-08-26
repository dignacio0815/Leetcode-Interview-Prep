class Solution:
    def countDigits(self, num: int) -> int:
        return self.extractingDigits(num)

    def extractingDigits(self, num: int) -> int:
        count = 0
        temp = num
        while temp > 0:
            # print(num)

            # get right most digit
            digit = temp % 10

            # print(digit)
            
            # check num mod digit equals to 0 -> increment count
            if num % digit == 0:
                count += 1

            # interger divide num
            temp //= 10
            
        return count