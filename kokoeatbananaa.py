import math
class solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
sol=solution()
print(sol.minEatingSpeed([3,6,7,11],8))

