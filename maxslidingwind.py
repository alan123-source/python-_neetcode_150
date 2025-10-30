import collections

def maxslidwin(self, nums: list[int], k: int) -> list[int]:
    output = []
    q = collections.deque()   # stores indices, in decreasing order of nums[]
    l = r = 0

    while r < len(nums):
        # Maintain decreasing order in deque
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # Remove left index if it’s out of window
        if l > q[0]:
            q.popleft()

        # When window size is at least k, record max
        if (r + 1) >= k:
            output.append(nums[q[0]])  # q[0] is max in window
            l += 1                     # move left pointer
        r += 1

    return output
# main pattern to learn from this qyestion is mainitaining decreasing ordre of quue
