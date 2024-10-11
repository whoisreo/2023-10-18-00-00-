import fake_math as fake
import true_math as tr


fake.divide(1, 0)
tr.divide(1, 0)


result1 = fake.divide(69, 3)
result2 = fake.divide(3, 0)
result3 = tr.divide(49, 7)
result4 = tr.divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
