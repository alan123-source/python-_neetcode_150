from _collections import defaultdict


class Solution:
    def groupAnangrams(self,strs:list[str]) -> list[list[str]]:
        res=defaultdict(list)#mapping charcount to list of anagrams
        for s in strs:
            count=[0]*26 #a.....z
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return res.values()
sol=Solution();
print(sol.groupAnangrams(["tea","eat","ate","sure","urse"]))

# Step-by-step with the example ["tea", "eat", "ate", "sure", "urse"]
# 1️⃣ First string: "tea"
# count = [0]*26 → [0, 0, 0, ..., 0]
#
# Loop through each char:
#
# 't' → index = ord('t') - ord('a') = 19 → count[19] += 1
#
# 'e' → index = 4 → count[4] += 1
#
# 'a' → index = 0 → count[0] += 1
#
# Now count = [1, 0, 0, 0, 1, 0, ..., 1 (at index 19), 0, ..., 0]
#
# Convert to tuple → tuple(count) (so it can be a dictionary key)
#
# Store in res:
#
# arduino
# Copy code
# res[(1,0,0,0,1,0,...,1,...)] = ["tea"]
# 2️⃣ Second string: "eat"
# Same letters as "tea", just in different order.
#
# After processing, count will be exactly the same tuple as "tea".
#
# So res[(1,0,0,0,1,0,...,1,...)] now becomes:
#
# css
# Copy code
# ["tea", "eat"]
# 3️⃣ Third string: "ate"
# Same tuple again (because anagrams have the same letter counts).
#
# Now:
#
# css
# Copy code
# ["tea", "eat", "ate"]
# 4️⃣ Fourth string: "sure"
# Count will be different:
#
# 's' → index 18 → count[18] += 1
#
# 'u' → index 20 → count[20] += 1
#
# 'r' → index 17 → count[17] += 1
#
# 'e' → index 4 → count[4] += 1
#
# This tuple is different from the first one, so we get:
#
# perl
# Copy code
# res[(..., 1 at index 4, ..., 1 at index 17, ..., 1 at index 18, ..., 1 at index 20)] = ["sure"]
# 5️⃣ Fifth string: "urse"
# Same letters as "sure", so it matches the second key and is added:
#
# css
# Copy code
# ["sure", "urse"]
# Final res dictionary looks like:
# css
# Copy code
# {
#   (1,0,0,0,1,0,...,1,...): ["tea", "eat", "ate"],
#   (...): ["sure", "urse"]
