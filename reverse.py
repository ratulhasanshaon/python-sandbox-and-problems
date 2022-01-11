user_input = input()
rev =""
len1 =len(user_input)
for i in range(len1):
    rev += user_input[len1-1-i]
print(rev)

