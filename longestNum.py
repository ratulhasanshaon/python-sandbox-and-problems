txt = input()

#your code goes here
res = txt.split(' ')
num = max(res,key = len)
print(num)