years = [2012]
output = []

for y in  years:
    if y % 400 == 0:
        output.append("True")
    elif y%100==0:
        output.append("False")
    elif y%4==0:
        output.append("True")
    else:
        output.append("False")
print(output)