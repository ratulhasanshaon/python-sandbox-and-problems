
# initializing list
test_list = [1,7,90,0,8,0,59,0,0,0,7,11]
  
# printing original list
print("The original list : " + str(test_list))
  
# using list comprehension + isinstance()
# Shift zeroes at end of list
temp = [ele for ele in test_list if ele or 
        ele is None or isinstance(ele, bool)]
res = temp + [0] * (len(test_list) - len(temp))
  
# print result
print("The list after shifting 0's to end : " + str(res))