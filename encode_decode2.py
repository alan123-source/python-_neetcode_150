class Solution:
    def encode(self,strs):
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
    def decode(self,str):
        res,i=[],0
        while i<len(str):
            j=i
            while str[j]!="#":
                j=j+1
            length=int(str[i:j])
            res.append(str[j+1:j+1+length])
            i=j+1+length

# 🔹 1️⃣ Length-Prefix Encoding
#
# Pattern: Store each string with its length first, then a delimiter, then the string itself.
#
# Use Case: When elements may contain special characters (like # or ,) that could conflict with simple join operations.
#
# Example: "leet" → "4#leet"
#
# Where seen:
#
# Serialize/deserialize strings, lists, or arrays
#
# Network protocols / message framing
#
# Custom file storage
#
# 🔹 2️⃣ Delimiter + Exact Length Extraction
#
# Pattern: Combine a delimiter (#) and length to extract elements unambiguously.
#
# Why: Even if the string itself contains the delimiter, you can still slice it correctly using the length.
#
# Where seen:
#
# Parsing CSV / custom formats
#
# 2D array / string serialization
#
# 🔹 3️⃣ Iterative Parsing with Index Pointers
#
# Pattern: Use pointers (i, j) to traverse a string without splitting.
#
# Steps:
#
# Find delimiter → know length of element
#
# Slice substring using start + length
#
# Move pointer to next element
#
# Where seen:
#
# Sliding window / parsing streams
#
# Online data processing
#
# 🔹 4️⃣ Hash-free / In-place Serialization
#
# Pattern: Avoid extra memory like dictionaries or sets; just encode the structure in the string itself.
#
# Why useful:
#
# Saves space
#
# Ensures deterministic decoding
#
# 🔹 5️⃣ Generalization / Serialization Pattern
#
# Pattern: This is a “serialize & deserialize” pattern — take structured data → encode into string → decode back.
#
# Where seen:
#
# JSON / XML parsing
#
# Tree serialization (LeetCode: Serialize/Deserialize Binary Tree)
#
# Custom network message formats