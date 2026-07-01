text = "banana"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts)