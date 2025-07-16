#1 
s = "Python"
print("Reversed:", s[::-1])

#2
lst = [1,2,3,2,4,1,5]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print("Unique List:", unique)

#3
s = "programming"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)

#4
a=[1,2,3]; b=[3,4,5]
merged = list(set(a+b))
print("Merged List:", merged)

#5
s="madam"
print("Palindrome" if s==s[::-1] else "Not Palindrome")

