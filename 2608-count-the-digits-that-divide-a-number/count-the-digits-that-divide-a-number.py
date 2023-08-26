class Solution:
    def countDigits(self, num: int) -> int:
        return self.getCount(num)

        # return self.extractingDigits(num)

    def extractingDigits(self, num: int) -> int:
            
        return count

    def getDigits(self, num: int) -> int:
        temp = num
        # return [int(d) for d in str(num)]
        while temp > 0:
            # get right most digit
            digit = temp % 10
            
            yield digit

            # interger divide num
            temp //= 10



    def getCount(self, num: int) -> int:
        count = 0
        for d in self.getDigits(num):
            if (num % d == 0):
                count += 1

        return count