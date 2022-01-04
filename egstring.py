str=input("Enter string")
words=str.split()
reversed_one_word=""
print(words)
for word in words:
    reversed_one_word+=" "+ (word[::-1])
    print(reversed_one_word)
print(reversed_one_word)


str=input("enter string")
print (" ".join(w[::-1] for w in str.split()))