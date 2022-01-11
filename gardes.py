scores = [77.51, 92.86, 98.01, 69.71, 78.52, 59.69, 60.49, 85.04, 87.33, 91.04]
grades = []


for s in scores:
    fl_sc = float(s)
    if fl_sc < 60:
        grades.append("F")
    elif fl_sc < 70:
        grades.append("D")
    elif fl_sc < 80:
        grades.append("C")
    elif fl_sc < 90:
        grades.append("B")
    else:
        grades.append("A")

print(grades)



