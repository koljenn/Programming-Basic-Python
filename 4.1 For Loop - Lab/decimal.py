# a = 0.1
# b = 0.1
# c = 0.1
# result = a + b + c
# print(result)
# Отговора ще е 0.30000000000000004

from decimal import Decimal
a = Decimal("0.1")
b = Decimal("0.1")
c = Decimal("0.1")
result = a + b + c
print(result)
# Отговора ще е 0.3

# 0.1 задължително в кавички!!!