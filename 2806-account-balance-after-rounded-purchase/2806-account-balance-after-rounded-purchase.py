class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        amount = purchaseAmount % 10
        if (amount >= 5):
            return 100 - (math.ceil(purchaseAmount) + 10 - amount)
        return 100 - (math.floor(purchaseAmount) - amount)