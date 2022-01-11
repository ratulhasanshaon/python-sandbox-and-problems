years = [1967, 1900, 1400, 1628, 1701, 1217, 1359, 1300, 2000, 1054,
1724, 1000, 1800, 1100, 2100, 1023, 1600, 1500, 1358, 1160,
1700, 1744, 2009, 1200]
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