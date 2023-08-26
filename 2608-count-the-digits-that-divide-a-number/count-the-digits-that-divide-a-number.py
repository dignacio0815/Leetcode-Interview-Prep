class Solution:
    def countDigits(self, num: int) -> int:
        return self.getCount(num)

        # return self.extractingDigits(num)

    def extractingDigits(self, num: int) -> int:
            
        return count

    def getDigits(self, num: int) -> int:
        # assume num is 3248
        # log_10(1) = 0
        # log_10(10) = 1
        # log_10(100) = 2
        # log_10(1000) = 3
        # log_10(3248) = 3.?
        # log_10(10000) = 4

        power = 10**int(math.log10(num))
        temp = num
        while power > 0:
            digit = temp // power
            yield digit

            temp %= power
            power //= 10



        # return [int(d) for d in str(num)]
        # while temp > 0:
        #     # get right most digit
        #     digit = temp % 10
        #     print("yielding digit ", digit)
        #     yield digit
        #     print("after yielding digit ", digit)
        #     # interger divide num
        #     temp //= 10



    def getCount(self, num: int) -> int:
        count = 0
        for d in self.getDigits(num):
            print("using digit ", d)
            if (num % d == 0):
                count += 1

        return count