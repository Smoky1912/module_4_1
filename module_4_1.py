from fake_math import divide as fake_divide
from true_math import divide as true_divide
result1 = fake_divide(69, 0)
result2 = fake_divide(69, 3)

result3 = true_divide(96, 0)
result4 = true_divide(96, 3)

print(result1)
print(result2)
print(result3)
print(result4)