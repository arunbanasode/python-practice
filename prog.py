name = "Arun"
marks = [80, 70, 90]

total = sum(marks)
average = total / len(marks)

if average >= 40:
    print(name, "Passed")
else:
    print(name, "Failed")