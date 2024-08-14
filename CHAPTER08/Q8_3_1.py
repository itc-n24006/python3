from collections import Counter

text = "すもももももももものうち"
counter = Counter(text)  
unique_chars = [ch for ch, cnt in counter.items() if cnt == 1]
print(unique_chars)

